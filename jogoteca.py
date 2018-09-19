from flask import Flask
from flask_mysqldb import MySQL

app = Flask(__name__)

app.config.from_pyfile('config.py')

db = MySQL(app)

"""--------------------------------------------
            SALVAR SEM ALTERAR NADA
    ---------------------------------------------
"""

from views import *

if __name__ == '__main__':
    app.run(debug=True)
