import os
from configparser import ConfigParser

# Initialize ConfigParser instance globally
config = ConfigParser()
config_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'config.ini'))
config.read(config_path)

def get_config(category, key):
    global config
    return config.get(category, key)
