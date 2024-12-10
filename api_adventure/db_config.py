import pathlib
from pathlib import Path
import connexion
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

basedir = pathlib.Path(__file__).parent.resolve()
print('Base directory:'+str(basedir))
connex_app = connexion.App(__name__, specification_dir=basedir)

#create an instance of server
app = connex_app.app


#Define configuration parameters
#app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{basedir / 'books.db'}"
app.config["SQLALCHEMY_DATABASE_URI"] = 'postgresql://postgres:jprb2000@localhost:5432/adventuretime'

app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app) #SQLAlchemy es un kit de herramientas SQL para Python y un ORM (Object Relational Mapper)
ma = Marshmallow(app) #Marshmallow is a Python library that converts complex data types to native Python data types and vicevers
print('Configuration Ok')