from flask_wtf import FlaskForm
from wtforms import IntegerField, SubmitField, DateField, TimeField, TextAreaField, RadioField
from wtforms.validators import DataRequired


# RESTAURANT PAGE
#
class BasicForm(FlaskForm):
    reservation_date = DateField('Date:', validators=[DataRequired()])
    reservation_time = TimeField('Time:', validators=[DataRequired()])
    party_size = IntegerField('Party Size:',validators=[DataRequired()])
    submit1 = SubmitField('Submit Booking!')



#ACCOUNT PAGE
class ReviewsForm(FlaskForm):
    star_rating = RadioField('Rating', choices=[(1, '1 Star'), (2, '2 Stars'), (3, '3 Stars'), (4, '4 Stars'), (5, '5 Stars')], validators=[DataRequired()])
    review_comment = TextAreaField('Tell us what you think:')
    submit2 = SubmitField('Submit Review!')
