from db_config import db, ma

# Create the business entities
# class Book(db.Model):
#     __tablename__ = "book"
#     id = db.Column(db.Integer, primary_key=True)
#     author = db.Column(db.String(32))
#     title = db.Column(db.String(1000), unique=True)
#     first_sentence = db.Column(db.String(2000))
#     year_published = db.Column(db.Integer)

class SalesPerson(db.Model):
    __tablename__ = "salesperson"
    businessentityid = db.Column(db.Integer, primary_key=True)
    territoryid = db.Column(db.Integer)
    salesquota = db.Column(db.Float)
    bonus = db.Column(db.Float)
    commissionpct = db.Column(db.Float)
    salesytd = db.Column(db.Float)
    saleslastyear = db.Column(db.Float)
    rowguid = db.Column(db.String(36))
    modifieddate = db.Column(db.DateTime)

class Product(db.Model):
    __tablename__ = "product"
    productid = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String())
    productnumber = db.Column(db.String())
    makeflag = db.Column(db.String())
    finishedgoodsflag = db.Column(db.String())
    color = db.Column(db.String())
    safetystocklevel = db.Column(db.Integer)
    reorderpoint = db.Column(db.Integer)
    standardcost = db.Column(db.Float)
    listprice = db.Column(db.Float)
    size = db.Column(db.String())
    sizeunitmeasurecode = db.Column(db.String())
    weightunitmeasurecode = db.Column(db.String())
    weight = db.Column(db.Float)
    daystomanufacture = db.Column(db.Integer)
    productline = db.Column(db.String())
    class_ = db.Column(db.String())
    style = db.Column(db.String())
    productsubcategoryid = db.Column(db.Integer)
    productmodelid = db.Column(db.Integer)
    sellstartdate = db.Column(db.DateTime)
    sellenddate = db.Column(db.DateTime)
    discontinueddate = db.Column(db.DateTime)
    rowguid = db.Column(db.String(36))
    modifieddate = db.Column(db.DateTime)


#Create code for serialization
# class BookSchema(ma.SQLAlchemyAutoSchema):
#     class Meta:
#         model = Book
#         load_instance = True
#         sqla_session = db.session

class SalesPersonSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = SalesPerson
        load_instance = True
        sqla_session = db.session

class ProductSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Product
        load_instance = True
        sqla_session = db.session

# book_schema = BookSchema()
# books_schema = BookSchema(many=True)

salesperson_schema = SalesPersonSchema()
salespersons_schema = SalesPersonSchema(many=True)
product_schema = ProductSchema()
products_schema = ProductSchema(many=True)
print ("The model has been successfully created ")