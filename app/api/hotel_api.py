from flask import jsonify
from flask_restplus import Resource, Namespace
from app.extensions import db
from app.model.hotel import Hotel 

hotels = Namespace('hotels')

@hotels.route('')
class HotelsHandler(Resource):
    def get(self):
        hotels = Hotel.query.all()
        return jsonify([h.to_json() for h in hotels])

    def post(self):
        data = self.api.payload
        h = Hotel(**data)
       
        db.session.add(h)
        db.session.commit()
        return h.to_json()


@hotels.route('/<int:id>')
class HotelHandler(Resource):
    def get(self, id):
        hotel = Hotel.query.filter(Hotel.id == id).first()
        if not hotel:
            return self.api.abort(404, "Hotal id {} doesn't exist".format(id))
        return jsonify(hotel.to_json())

    def put(self, id):
        data = self.api.payload
        hotel = Hotel.query.filter(Hotel.id == id).first()
        if not hotel:
            return self.api.abort(404, "Hotal id {} doesn't exist".format(id))
        hotel.name = data.get('name', hotel.name)
        hotel.address = data.get('address', hotel.address)
        hotel.city = data.get('city', hotel.city)
        db.session.commit()
        return jsonify(hotel.to_json())
    
    def delete(self, id):
        db.session.query(Hotel).filter(Hotel.id == id).delete()
        db.session.commit()
        return jsonify(True)
