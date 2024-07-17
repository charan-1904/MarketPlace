import os
import configparser


class Config:
    def __init__(self, config_path=None):
        self.config = configparser.ConfigParser()
        if config_path:
            self.config.read(config_path)
        else:
            default_path = os.path.join(os.path.dirname(__file__), '..', 'config.ini')
            self.config.read(default_path)

    def get(self, section, option):
        return self.config.get(section, option)