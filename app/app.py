import argparse
import logging
import time
import requests
from app.models import IP


class App:
    log = None

    def __init__(self):
        # Setup Arg parser
        parser = argparse.ArgumentParser()
        parser.add_argument("--debug", action="store_true")
        parser.add_argument("-ip")
        parser.add_argument("-find")
        parser.add_argument("-list", action="store_true")
        parser.add_argument(
            "-run", nargs="?", default=0, const="endless", action="store"
        )
        args = parser.parse_args()

        # Set debug flags
        log_level = logging.INFO
        if args.debug:
            log_level = logging.DEBUG

        logging.basicConfig(
            format="%(asctime)s %(filename)s:%(lineno)s %(levelname)-8s %(message)s",
            level=log_level,
            datefmt="%Y-%m-%d %H:%M:%S",
        )

        if args.ip:
            lookup(args.ip)

        if args.find:
            find(args.find)

        if args.list:
            list_entries()

        if args.run:
            log_current_ip(args.run)


def lookup(ip_addr):
    url = f"http://www.geoplugin.net/json.gp?ip={ip_addr}"
    try:
        response = requests.get(url)
        if response.status_code != 200:
            logging.error("%s replyed with a not ok status code", url)
            return ""

        new_ip = IP()
        new_ip.insert_raw(response.json())
        new_ip.save()
        return new_ip
    except ConnectionError:
        logging.error("failed to fetch api details for %s", url)
        return ""


def find(ip_addr):
    new_ip = IP()
    row = new_ip.find_by_ip(ip_addr)
    if not row:
        logging.info("no entry found for %s", ip_addr)
        new_ip = lookup(ip_addr)
        logging.info(new_ip.data())
        return

    logging.info(row[0].data())


def list_entries():
    new_ip = IP()
    rows = new_ip.list_all()
    print(rows)
    for row in rows:
        logging.info(row.data())


def log_current_ip(repeat):
    repeat = 0 if repeat == "endless" else repeat
    count = 0
    while True:
        logging.debug("running current ip lookup")
        if repeat:
            count += 1
        try:
            current_ip = requests.get("https://api.ipify.org")
            if current_ip.status_code == 200:
                lookup(current_ip)
        except ConnectionError:
            continue

        if repeat and int(repeat) == int(count):
            break

        time.sleep(60)
