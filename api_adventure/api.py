import flask
from flask import request,jsonify
from flask_cors import CORS
from db_config import db, app
from model import SalesPerson, salespersons_schema, salesperson_schema

import model

#Run server
#app = flask.Flask(__name__)
#app.config["DEBUG"] = True
app.config["DEBUG"] = True
CORS(app)

    # CORS Headers 
@app.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization,true')
    response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,OPTIONS')
    return response

#Create API
@app.route('/', methods=['GET'])
def home():
    return "<h1>API Web with Database</h1><p> This is a test.</p>"

# A route to return all of the available entries in our catalog.
@app.route("/api/resources/salesperson/all", methods=["GET"])
def salesperson_all():
    all_salesperson = SalesPerson.query.all()
    return salespersons_schema.dump(all_salesperson)


@app.route("/api/resources/salesperson/new", methods=["POST"])
def create_salesperson():
    salesperson = request.get_json(force=True)
    id = salesperson.get("businessentityid")
    existing_salesperson = SalesPerson.query.filter(SalesPerson.businessentityid == id).one_or_none()

    if existing_salesperson is None:
        new_salesperson = salesperson_schema.load(salesperson, session=db.session)
        db.session.add(new_salesperson)
        db.session.commit()
        return salesperson_schema.dump(new_salesperson), 201
    else:
        return jsonify({ 'error': 'Missing input' }), 400


@app.route("/api/resources/salesperson/update", methods=["PUT"])
def update_salesperson():
    salesperson = request.get_json(force=True)
    id = salesperson.get("businessentityid")
    existing_salesperson = SalesPerson.query.filter(SalesPerson.businessentityid == id).one_or_none()

    if existing_salesperson:
        update_salesperson=salesperson_schema.load(salesperson, session=db.session)
        existing_salesperson.businessentityid = update_salesperson.businessentityid
        existing_salesperson.territoryid = update_salesperson.territoryid
        existing_salesperson.salesquota = update_salesperson.salesquota
        existing_salesperson.bonus = update_salesperson.bonus
        existing_salesperson.commissionpct = update_salesperson.commissionpct
        existing_salesperson.salesytd = update_salesperson.salesytd
        existing_salesperson.saleslastyear = update_salesperson.saleslastyear
        existing_salesperson.rowguid = update_salesperson.rowguid
        existing_salesperson.modifieddate = update_salesperson.modifieddate
        db.session.merge(existing_salesperson)
        db.session.commit()
        return salesperson_schema.dump(existing_salesperson), 201
    else:
        return jsonify({ 'error': 'Missing object to be updated' }), 400

@app.route("/api/resources/salesperson/remove", methods=["DELETE"])
def remove_salesperson():
    salesperson = request.get_json(force=True)
    id = salesperson.get("businessentityid")
    existing_salesperson = SalesPerson.query.filter(SalesPerson.businessentityid == id).one_or_none()
    if existing_salesperson:
        db.session.delete(existing_salesperson)
        db.session.commit()
        return jsonify({ 'Ok': 'Object was successfully removed ' }), 200 
    else:
        return jsonify({ 'error': 'Missing object to be deleted' }), 400
    
app.run()
