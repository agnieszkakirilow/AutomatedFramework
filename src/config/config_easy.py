import os

class Config:
    """Config class is responsible for storing framework's and env's configuration"""
    
    def __init__(self):
        pass
    request_timeout = 20
    user_name = os.environ.get('USERNAME')
    env = os.environ.get('BQA_ENV') # for this in terminal export BQA_ENV=aga, echo $BQA_ENV to see if worked. $env:BQA_ENV="aga" for powershell not bash


config = Config()
print(f'={config.request_timeout}')
print(f'={config.user_name}')
print(f'={config.env}')