# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

import os, random, string
import getpass
import urllib.parse
import sshtunnel
import MySQLdb
from urllib.parse import quote_plus

class Config(object):


    sshtunnel.SSH_TIMEOUT = 5.0
    sshtunnel.TUNNEL_TIMEOUT = 5.0


    usr = getpass.getuser()
    PROJECT_ID = 'matchealo'

    if usr == 'jhon':
        SECRET_KEY = os.environ.get('agenda_crm_key')
        SITE_KEY = os.environ["site_key"]
        # VERIFY_URL= 'https://www.google.com/recaptcha/api/siteverify'
        MYSQL_HOST = '127.0.0.1' #'db'
        # MYSQL_USER = 'permutas'  #'root'
        # MYSQL_PASSWORD = os.environ.get('cloudSQL_passwordN')
        DOMAIN ='http://localhost:5000'
        PASSWORD_LOGIN_PYTHON = os.environ['PASSWORD_LOGIN_PYTHON']
        PASSWORD_DB_PYTHON = os.environ['PASSWORD_DB_PYTHON']

        tunnel= sshtunnel.SSHTunnelForwarder(
            ('ssh.pythonanywhere.com'),
            ssh_username='jhonpg',
            ssh_password=PASSWORD_LOGIN_PYTHON,
            remote_bind_address=('jhonpg.mysql.pythonanywhere-services.com', 3306)
        ) 
        tunnel.start()
        SQLALCHEMY_DATABASE_URI = "mysql+pymysql://jhonpg:"+PASSWORD_DB_PYTHON+"@127.0.0.1:{}/jhonpg$papeleria".format(tunnel.local_bind_port)

            

        SQLALCHEMY_TRACK_MODIFICATIONS = False
        MAIL_SERVER = 'smtp.gmail.com'
        MAIL_PORT = 465
        # MAIL_USERNAME = 'admin@matchealo.com'
        # MAIL_PASSWORD = os.environ['mail_password']
        MAIL_USE_TLS = False
        MAIL_USE_SSL = True
    else:
        print('ERROR: No valid value for PROJECT_ENV')
    SQLALCHEMY_TRACK_MODIFICATIONS = False 

    basedir = os.path.abspath(os.path.dirname(__file__))
    GITHUB_ID      = os.getenv('GITHUB_ID'    , None)
    GITHUB_SECRET  = os.getenv('GITHUB_SECRET', None)
    # Assets Management
    ASSETS_ROOT = os.getenv('ASSETS_ROOT', '/static/assets')  
    
    # # Set up the App SECRET_KEY
    # SECRET_KEY  = os.getenv('SECRET_KEY', None)
    # if not SECRET_KEY:
    #     SECRET_KEY = ''.join(random.choice( string.ascii_lowercase  ) for i in range( 32 ))

    # # Social AUTH context
    # SOCIAL_AUTH_GITHUB  = False

    # GITHUB_ID      = os.getenv('GITHUB_ID'    , None)
    # GITHUB_SECRET  = os.getenv('GITHUB_SECRET', None)

    # # Enable/Disable Github Social Login    
    # if GITHUB_ID and GITHUB_SECRET:
    #      SOCIAL_AUTH_GITHUB  = True        

    # SQLALCHEMY_TRACK_MODIFICATIONS = False

    # DB_ENGINE   = os.getenv('DB_ENGINE'   , None)
    # DB_USERNAME = os.getenv('DB_USERNAME' , None)
    # DB_PASS     = os.getenv('DB_PASS'     , None)
    # DB_HOST     = os.getenv('DB_HOST'     , None)
    # DB_PORT     = os.getenv('DB_PORT'     , None)
    # DB_NAME     = os.getenv('DB_NAME'     , None)

    # USE_SQLITE  = True 

    # # try to set up a Relational DBMS
    # if DB_ENGINE and DB_NAME and DB_USERNAME:

    #     try:
            
    #         # Relational DBMS: PSQL, MySql
    #         SQLALCHEMY_DATABASE_URI = '{}://{}:{}@{}:{}/{}'.format(
    #             DB_ENGINE,
    #             DB_USERNAME,
    #             DB_PASS,
    #             DB_HOST,
    #             DB_PORT,
    #             DB_NAME
    #         ) 

    #         USE_SQLITE  = False

    #     except Exception as e:

    #         print('> Error: DBMS Exception: ' + str(e) )
    #         print('> Fallback to SQLite ')    

    # if USE_SQLITE:

    #     # This will create a file in <app> FOLDER
    #     SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'db.sqlite3')
    
class ProductionConfig(Config):
    DEBUG = False

    # Security
    SESSION_COOKIE_HTTPONLY = True
    REMEMBER_COOKIE_HTTPONLY = True
    REMEMBER_COOKIE_DURATION = 3600

class DebugConfig(Config):
    DEBUG = True

# Load all possible configurations
config_dict = {
    'Production': ProductionConfig,
    'Debug'     : DebugConfig
}
