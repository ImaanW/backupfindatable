from datetime import datetime

from application import db


class Reservation(db.Model):
    Reservation_ID = db.Column(db.Integer, primary_key=True)
    #Restaurant_ID = db.Column(db.Integer, db.ForeignKey('restaurant.Restaurant_ID'))
    #user_ID = db.Column(db.Integer, db.ForeignKey('users.Userid'))
    reservation_date = db.Column(db.Date, nullable=False)
    reservation_time = db.Column(db.Time, nullable=False)
    party_size = db.Column(db.Integer, nullable=False)


class Review(db.Model):
    review_id = db.Column(db.Integer, primary_key=True)
    #user_ID = db.Column(db.Integer, db.ForeignKey('users.Userid'))
    #restaurant_ID = db.Column(db.Integer, db.ForeignKey('restaurant.Restaurant_ID'))
    star_rating = db.Column(db.Integer, nullable=False)
    review_comment = db.Column(db.String(200), nullable=True)

class Reviews(db.Model):
    review_id = db.Column(db.Integer, primary_key=True)
    # author = db.Column(db.String(255))
    star_rating = db.Column(db.Integer, nullable=False)
    review_comment = db.Column(db.Text, nullable=True)
    date_posted = db.Column(db.DateTime, default=datetime.utcnow)
    # Foriegn Key to link users(refer to the primary key of the user
    reviewer_id = db.Column(db.Integer, db.ForeignKey('user.id'))


