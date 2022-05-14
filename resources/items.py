import sqlite3

from flask_jwt import jwt_required
from flask_restful import Resource, reqparse

from models.item import ItemModel


class Item(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('price',type=float,required=True,help="This field cant be left blank")
    parser.add_argument('store_id',type=int,required=True,help="The storeid field cant be left blank")

    @jwt_required()
    def get(self,name):
        item = ItemModel.find_by_name(name)
        if item:
            return item.json(),200
        return {"message":"item not found"},404

    def post(self,name):
        if ItemModel.find_by_name(name):
            return {"message":f"item with {name} already exists"} ,400

        # data = request.get_json()  # to ignore the header as content-json -- force=True and to give null we need -- silent = True
        data = Item.parser.parse_args()

        item = ItemModel(name ,**data)

        try:
            item.save_to_db()
        except:
            return{"message":"An Error Occured inserting the item"},500    #internal server error

        return item.json(), 201 #this is code is used to tell the data is posted or created ---- 202 is for delaying the creation

    def delete(self,name):
        item = ItemModel.find_by_name(name)
        if item:
            item.delete_from_db()
            return{'message':"item has been deleted sucessfully"},200
        return{'message':"No such item found"}

    def put(self,name):

        data = Item.parser.parse_args()
        item = ItemModel.find_by_name(name)

        if item:
            try:
                item.price= data['price']
                item.store_id=data['store_id']
            except:
                return {"message":"An Error has occured inserting the item."},500
        else:
            try:
                item = ItemModel(name,**data)
            except:
                return {"message":"An Error has occured updating the item."},500
        item.save_to_db()

        return item.json()


class ItemList(Resource):
    def get(self):
        return {'items': [item.json() for item in ItemModel.query.all()]} #this is used to get all the items in json format
        #or we can use {'items': list(map(lambda x: x.json(),ItemModel.query.all()))} using the lambda function
