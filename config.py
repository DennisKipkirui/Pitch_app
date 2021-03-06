import os
class Config:
    '''
    General configuration parent class
    '''
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringa:Access@localhost/pitch2'
    
    SECRET_KEY = 'Qwerty'
class ProdConfig(Config):
    '''
    Production  configuration child class
    Args:
        Config: The parent configuration class with General configuration settings
    '''
class DevConfig(Config):
    '''
    Development  configuration child class
    Args:
    Config: The parent configuration class with General configuration settings
    '''

    DEBUG = True
config_options = {
'development':DevConfig,
'production':ProdConfig
}