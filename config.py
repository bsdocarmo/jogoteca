import os

SECRET_KEY = 'bruno'

MYSQL_HOST = "localhost"
MYSQL_USER = "root"
MYSQL_PASSWORD = "br32236687"
MYSQL_DB = "jogoteca"
MYSQL_PORT = 3306

UPLOAD_PATH = os.path.dirname(os.path.abspath(__file__)) + '/uploads'
