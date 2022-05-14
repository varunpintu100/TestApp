from flask_restful import Resource

from models.store import StoreModel


class Store(Resource):
    def get(self,name):

        store = StoreModel.find_by_name(name)
        if store:
            return store.json(),200
        return {"message":"Store not found"},404

    def post(self,name):

        store = StoreModel.find_by_name(name)

        if store:
            return {"message":"The store with the '{}' already exists".format(name)},400
        store = StoreModel(name)
        try:
            store.save_to_db()
            return {"message":"New store item is created"},201
        except:
            return {"message":"An error occured while creating the store"},500

    def delete(self,name):
        store = StoreModel.find_by_name(name)

        if store:
            try:
                store.delete_from_db()
                return {"message":"Store '{}' sucessfully deleted".format(name)},200
            except:
                return {"message":"An error occured while deleting the database"},500
        return {"message":"Store with '{}' didnt exists"},400

class Storelist(Resource):

    def get(self):
        return {"stores": [store.json() for store in StoreModel.query.all()]}
