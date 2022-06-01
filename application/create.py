from application import db
from application.models import Reservation
db.drop_all()
db.create_all()