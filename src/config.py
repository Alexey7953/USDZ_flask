import os


class Config:
    DB_CONNECTION = os.getenv('DB_CONNECTION', 'USDZ.db')
    SECRET_KEY = os.getenv('SECRET_KEY', 'secret').encode()
    JSON_SORT_KEYS = False

