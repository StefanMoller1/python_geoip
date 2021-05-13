#!/usr/bin/python
import sqlite3
import sys
import os

DBNAME = "geo_ip.db"


def handle(sysarg):
    if sysarg == "new":
        new()
    else:
        print("unknown or invalid command")


def new():
    try:
        os.remove(DBNAME)
    except FileNotFoundError:
        print(f"database {DBNAME} does not exist")
    else:
        print(f"delete database {DBNAME}")
    # pylint: disable=E1101
    conn = sqlite3.connect(DBNAME)
    print(f"Opened database {DBNAME} successfully")
    # 'geoplugin_request':'209.203.39.143',
    # 'geoplugin_status':200,
    # 'geoplugin_delay':'2ms',
    # 'geoplugin_credit':'Some of the returned data includes GeoLite
    #   data created by MaxMind, available from
    #   <a href='http:\/\/www.maxmind.com'>http:\/\/www.maxmind.com<\/a>.',
    # 'geoplugin_city':'Bothasig',
    # 'geoplugin_region':'Western Cape',
    # 'geoplugin_regionCode':'WC',
    # 'geoplugin_regionName':'Western Cape',
    # 'geoplugin_areaCode':'',
    # 'geoplugin_dmaCode':'',
    # 'geoplugin_countryCode':'ZA',
    # 'geoplugin_countryName':'South Africa',
    # 'geoplugin_inEU':0,
    # 'geoplugin_euVATrate':false,
    # 'geoplugin_continentCode':'AF',
    # 'geoplugin_continentName':'Africa',
    # 'geoplugin_latitude':'-33.8604',
    # 'geoplugin_longitude':'18.5446',
    # 'geoplugin_locationAccuracyRadius':'500',
    # 'geoplugin_timezone':'Africa\/Johannesburg',
    # 'geoplugin_currencyCode':'ZAR',
    # 'geoplugin_currencySymbol':'R',
    # 'geoplugin_currencySymbol_UTF8':'R',
    # 'geoplugin_currencyConverter':14.0456
    conn.execute(
        """
    CREATE TABLE geoip
    (
        id INT PRIMARY KEY,
        request                 CHAR(15) NOT NULL,
        status                  INT      NOT NULL,
        delay                   CHAR(32) NOT NULL,
        credit                  TEXT,
        city                    TEXT,
        region                  TEXT,
        region_code              TEXT,
        region_name              TEXT,
        area_code                TEXT,
        dma_code                 TEXT,
        country_code             TEXT,
        country_name             TEXT,
        in_eu                    TEXT,
        eu_vat_rate               TEXT,
        continent_code           TEXT,
        continent_name           TEXT,
        latitude                TEXT,
        longitude               TEXT,
        location_accuracy_radius  TEXT,
        timezone                TEXT,
        currency_code            TEXT,
        currency_symbol          TEXT,
        currency_converter       TEXT,
        time_stamp               INT
    );
    """
    )


if __name__ == "__main__":
    try:
        handle(sys.argv[1])
    except KeyboardInterrupt:
        print("Interrupted")
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)
