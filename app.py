from flask import Flask
from flask_jwt import JWT
from flask_restful import Api

from resources.items import Item, ItemList
from resources.store import Store , Storelist
from resources.user import UserRegister
from security import authenticate, identity


app = Flask(__name__) #this is used to invoke the flask app
#this piece of code is very important
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///data.db' #this is used to create the coloumn and also connect to the database
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
app.secret_key='Varun'
api = Api(app)

jwt = JWT(app,authenticate,identity) # /auth

api.add_resource(Store,'/store/<string:name>')
api.add_resource(Item,'/item/<string:name>')
api.add_resource(ItemList,'/items')
api.add_resource(Storelist,'/stores')


api.add_resource(UserRegister,'/register')


if __name__=='__main__':
    from database import db  # we are importing this as a part of circular imports
    db.init_app(app)
    app.run(port=8080,debug=True)
