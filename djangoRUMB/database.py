import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PROD = False
SQLite = False
AWS = True


def get_database():
    if AWS:
        return {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': 'rumb2',
            'USER': 'rumb',
            'PASSWORD': 'admin12345',
            'HOST': 'rumb2.cxg2mmbm2x4b.us-east-2.rds.amazonaws.com',
            'PORT': '5432',
        }
