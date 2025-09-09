import configparser
import os

class ConfigReader:
    def __init__(self, file_path=None):
        if not file_path:
            file_path = os.path.join("config", "config.ini")
        self.config = configparser.ConfigParser()
        self.config.read(file_path)

    def get_url(self, key):
        return self.config["URLS"][key]

    def get_browser(self):
        return self.config["BROWSER"]["default"]

    def get_timeout(self, key):
        return int(self.config["TIMEOUTS"][key])

    def get_credential(self, key):
        return self.config["LOGIN_CREDENTIALS"][key]

# Usage:
# config = ConfigReader()
# url = config.get_url("home_page")
# browser = config.get_browser()
# implicit_wait = config.get_timeout("implicit_wait")
