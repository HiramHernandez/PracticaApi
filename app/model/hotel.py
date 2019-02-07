from sqlalchemy import Integer, String

from app.extensions import db


class Hotel(db.Model):
	__tablename__ = 'hotel'
	id = db.Column(Integer, primary_key=True)
	name = db.Column(String(100), nullable=False)
	city = db.Column(String, nullable=False)
	address = db.Column(String, nullable=False)

	def __init__(self, name, city, address):
		self.name = name
		self.city = city
		self.address = address

	@staticmethod
	def from_json(json):
		return Hotel(
			name=json.get('name'),
        	city=json.get('city'),
            address=json.get('address')
		)

	def to_json(self):
		return {
			'id': str(self.id),
            'name': self.name,
            'city': self.city,
            'address': self.address
		}
