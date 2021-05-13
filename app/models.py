from datetime import datetime
from sqlitemodel import Model, Database, SQL

DBFILE = "geo_ip.db"
Database.DB_FILE = DBFILE


class IP(Model):
    def __init__(self, id=None):
        Model.__init__(self, id, dbfile=None, foreign_keys=False, parse_decltypes=False)
        self.request = ""
        self.status = 0
        self.delay = ""
        self.credit = ""
        self.city = ""
        self.region = ""
        self.region_code = ""
        self.region_name = ""
        self.area_code = ""
        self.dma_code = ""
        self.country_code = ""
        self.country_name = ""
        self.in_eu = ""
        self.eu_vat_rate = ""
        self.continent_code = ""
        self.continent_name = ""
        self.latitude = ""
        self.longitude = ""
        self.location_accuracy_radius = ""
        self.timezone = ""
        self.currency_code = ""
        self.currency_symbol = ""
        self.currency_converter = ""
        self.time_stamp = 0

        # Tries to fetch the object by its rowid from the database
        self.getModel()

    def tablename(self):
        return "geoip"

    def columns(self):
        return [
            {"name": "request", "type": "CHAR(15)"},
            {"name": "status", "type": "INTEGER"},
            {"name": "delay", "type": "CHAR(32)"},
            {"name": "credit", "type": "TEXT"},
            {"name": "city", "type": "TEXT"},
            {"name": "region", "type": "TEXT"},
            {"name": "region_code", "type": "TEXT"},
            {"name": "region_name", "type": "TEXT"},
            {"name": "area_code", "type": "TEXT"},
            {"name": "dma_code", "type": "TEXT"},
            {"name": "country_code", "type": "TEXT"},
            {"name": "country_name", "type": "TEXT"},
            {"name": "in_eu", "type": "TEXT"},
            {"name": "eu_vat_rate", "type": "TEXT"},
            {"name": "continent_code", "type": "TEXT"},
            {"name": "continent_name", "type": "TEXT"},
            {"name": "latitude", "type": "TEXT"},
            {"name": "longitude", "type": "TEXT"},
            {"name": "location_accuracy_radius", "type": "TEXT"},
            {"name": "timezone", "type": "TEXT"},
            {"name": "currency_code", "type": "TEXT"},
            {"name": "currency_symbol", "type": "TEXT"},
            {"name": "currency_converter", "type": "TEXT"},
            {"name": "time_stamp", "type": "INTERGET"},
        ]

    def insert_raw(self, data):
        self.request = data.get("geoplugin_request")
        self.status = data.get("geoplugin_status")
        self.delay = data.get("geoplugin_delay")
        self.credit = data.get("geoplugin_credit")
        self.city = data.get("geoplugin_city")
        self.region = data.get("geoplugin_region")
        self.region_code = data.get("geoplugin_regionCode")
        self.region_name = data.get("geoplugin_regionName")
        self.area_code = data.get("geoplugin_areaCode")
        self.dma_code = data.get("geoplugin_dmaCode")
        self.country_code = data.get("geoplugin_countryCode")
        self.country_name = data.get("geoplugin_countryName")
        self.in_eu = data.get("geoplugin_inEU")
        self.eu_vat_rate = data.get("geoplugin_euVATrate")
        self.continent_code = data.get("geoplugin_continentCode")
        self.continent_name = data.get("geoplugin_continentName")
        self.latitude = data.get("geoplugin_latitude")
        self.longitude = data.get("geoplugin_longitude")
        self.location_accuracy_radius = data.get("geoplugin_locationAccuracyRadius")
        self.timezone = data.get("geoplugin_timezone")
        self.currency_code = data.get("geoplugin_currencyCode")
        self.currency_symbol = data.get("geoplugin_currencySymbol")
        self.currency_converter = data.get("geoplugin_currencyConverter")
        self.time_stamp = datetime.now().timestamp()

    def find_by_ip(self, ip_addr):
        return self.select(SQL().WHERE("request", "=", ip_addr).LIMIT(0, 1))

    def list_all(self):
        return self.select(SQL())

    def data(self):
        return {
            "request": self.request,
            "status": self.status,
            "delay": self.delay,
            "credit": self.credit,
            "city": self.city,
            "region": self.region,
            "region_code": self.region_code,
            "region_name": self.region_name,
            "area_code": self.area_code,
            "dma_code": self.dma_code,
            "country_code": self.country_code,
            "country_name": self.country_name,
            "in_eu": self.in_eu,
            "eu_vat_rate": self.eu_vat_rate,
            "continent_code": self.continent_code,
            "continent_name": self.continent_name,
            "latitude": self.latitude,
            "longitude": self.longitude,
            "location_accuracy_radius": self.location_accuracy_radius,
            "timezone": self.timezone,
            "currency_code": self.currency_code,
            "currency_symbol": self.currency_symbol,
            "currency_converter": self.currency_converter,
            "time_stamp": self.time_stamp,
        }
