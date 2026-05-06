import json
import os


class DictConfigProvider():

    def __init__(self, input_values):
        super().__init__()
        self.values = input_values

    def get(self, item_name):
        return self.values[item_name]
    

class OSConfigProvider():
    @staticmethod
    def get(item_name):
        value = os.getenv(item_name)
        return value


class JSONConfigProvider():
    @staticmethod
    def _read_config(config_path):
        with open(config_path) as json_file:
            return json.load(json_file)
    
    @staticmethod 
    def get(item_name):
        value = JSONConfigProvider._read_config(".\\src\\config\\envs\\config.json")
        return value.get(item_name)




class ConfigHard:
    """ConfigHard class is responsible for storing framework's and env's configuration"""
    
    def __init__(self, config_providers):
        self.config_providers = config_providers # stores order of providers

        self.config_dictionary = {} # store values of parameters
        
        # parameters registry
        self._register("USERNAME")
        self._register("USER")
        self._register("URLTEST")
        self._register("BROWSER")
        self._register("URL")
        self._register("response_ok")
        
    
    def __getattr__(self, item_name):
        if item_name not in self.config_dictionary:
            raise AttributeError(f"Please register item:{item_name} before usage")
        return self.config_dictionary[item_name]
    
    def _register(self, item_name):
        """Retrieve values of parameter with item_name from the sconfig providers and stores it in config class for later use"""
        for provider in self.config_providers: # iterate over list of configproviders
            value = provider.get(item_name)
            if value is not None:
                self.config_dictionary[item_name] = value # save value to config class
                return # STOP further search

        # error if value for config parameter not found, stop TEST FRAMEWORK EXECUTION   
        raise ValueError (f"item {item_name} is missing in config providers") 
    
dict_confprovider = DictConfigProvider({'USERNAME': 'bla', 'USER': 'ble', 'BROWSER': 'chrome', 'URL': 'https://api.github.com/search/repositories', 
                                        'LALA': 'pala', 'URLTEST': 'http://www.google.pl', 'response_ok': 200})
# here priority is defined OS first because it enables changing on the run
config = ConfigHard([OSConfigProvider, JSONConfigProvider, dict_confprovider]) 

print('....config_all....')
config_all = ConfigHard([OSConfigProvider, JSONConfigProvider, dict_confprovider])
print('....config_two....')
config_two = ConfigHard([JSONConfigProvider, dict_confprovider])
print('....config_one....')
config_one = ConfigHard([dict_confprovider])

print(f'get parameter "USER": {config_all.__getattr__("USER")}')
print(f'get parameter "BROWSER": {config_all.__getattr__("BROWSER")}')
print(f'get parameter "URL": {config_all.__getattr__("URL")}')
        