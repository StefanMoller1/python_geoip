import unittest
import sqlite3
import sys
import os
from os.path import dirname, join, abspath

sys.path.insert(0, abspath(join(dirname(__file__), "..")))

from app.models import IP


TESTDB = "geo_ip.db"
CURRENTIP = "209.203.39.143"

APIRESPONSE = {
    "geoplugin_request": "209.203.39.143",
    "geoplugin_status": 200,
    "geoplugin_delay": "1ms",
    "geoplugin_credit": "Some of the returned data",
    "geoplugin_city": "Bothasig",
    "geoplugin_region": "Western Cape",
    "geoplugin_regionCode": "WC",
    "geoplugin_regionName": "Western Cape",
    "geoplugin_areaCode": "",
    "geoplugin_dmaCode": "",
    "geoplugin_countryCode": "ZA",
    "geoplugin_countryName": "South Africa",
    "geoplugin_inEU": 0,
    "geoplugin_euVATrate": False,
    "geoplugin_continentCode": "AF",
    "geoplugin_continentName": "Africa",
    "geoplugin_latitude": "-33.8604",
    "geoplugin_longitude": "18.5446",
    "geoplugin_locationAccuracyRadius": "500",
    "geoplugin_timezone": "Africa/Johannesburg",
    "geoplugin_currencyCode": "ZAR",
    "geoplugin_currencySymbol": "R",
    "geoplugin_currencySymbol_UTF8": "R",
    "geoplugin_currencyConverter": 14.1204,
}


class TestTwit(unittest.TestCase):
    maxDiff = None

    def setUp(self):
        self.conn = sqlite3.connect(TESTDB)
        cur = self.conn.cursor()
        cur.execute(
            """
            CREATE TABLE IF NOT EXISTS geoip
            (
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

        # cur.execute('''DELETE FROM geoip''')

    def test_insert(self):
        new_ip = IP()
        new_ip.insert_raw(APIRESPONSE)
        new_ip.save()

    def test_row_retrieval(self):
        ip_row = IP()
        result = ip_row.find_by_ip(CURRENTIP)
        result = result[0].data()
        result.pop("time_stamp")
        self.assertEqual(
            result,
            {
                "request": "209.203.39.143",
                "status": 200,
                "delay": "1ms",
                "credit": "Some of the returned data",
                "city": "Bothasig",
                "region": "Western Cape",
                "region_code": "WC",
                "region_name": "Western Cape",
                "area_code": "",
                "dma_code": "",
                "country_code": "ZA",
                "country_name": "South Africa",
                "in_eu": "0",
                "eu_vat_rate": "0",
                "continent_code": "AF",
                "continent_name": "Africa",
                "latitude": "-33.8604",
                "longitude": "18.5446",
                "location_accuracy_radius": "500",
                "timezone": "Africa/Johannesburg",
                "currency_code": "ZAR",
                "currency_symbol": "R",
                "currency_converter": "14.1204",
            },
        )

        self.conn.close()


if __name__ == "__main__":
    try:
        if os.path.exists(TESTDB):
            os.remove(TESTDB)
        unittest.main()
    except Exception as exception:
        print(exception)
        print("Failed to execute")
    finally:
        os.remove(TESTDB)
        print("Done")
