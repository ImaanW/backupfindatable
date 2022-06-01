from flask import render_template, request
from application import app, db
from application.models import Reservation, Review
from application.restaurant_page_forms import BasicForm, ReviewsForm


# Restaurant page roots
@app.route('/restaurant_page/', methods=['GET', 'POST'])
def make_reservation():
    form = BasicForm()
    # reviews_form = ReviewsForm

    if request.method == 'POST':
        # fetch and store data
        reservation_date = form.reservation_date.data
        reservation_time = form.reservation_time.data
        party_size = form.party_size.data

        reservation = Reservation(reservation_date=reservation_date, reservation_time=reservation_time,
                                  party_size=party_size)
        db.session.add(reservation)
        db.session.commit()
        return 'Booking Confirmed!'

    return render_template('restaurant_page.html', form=form)


@app.route('/account/', methods=['GET', 'POST'])
def sumbit_review():
    form = ReviewsForm()

    if request.method == 'POST':
        star_rating = form.star_rating.data
        review_comment = form.review_comment.data

        review = Review(star_rating=star_rating, review_comment=review_comment)
        db.session.add(review)
        db.session.commit()
        return 'Review Submitted!'

    return render_template('account.html', form=form)


# ACCOUNT 2
@app.route('/account/', methods=['GET', 'POST'])
def submit_review():
    form = ReviewsForm()

    if request.method == 'POST':
        star_rating = form.star_rating.data
        review_comment = form.review_comment.data
        reviewer = Reviews.reviewer_id

        # reviewer =
        review = Reviews(star_rating=star_rating, reviewer_id=reviewer, review_comment=review_comment)

        # add review to database
        db.session.add(review)
        db.session.commit()

        # clear the form
        form.star_rating.data = " "
        form.review_comment.data = " "

        # return a message
        flash("Review Submitted!")

    return render_template('account.html', form=form)

# showing the reviews query on resturant page
@app.route('/restaurantpage/')
def display_review2():
    form = ReservationForm()
    reviews = Reviews.query.order_by(Reviews.date_posted)
    return render_template('restaurant_page.html', form=form, reviews=reviews)


@app.route('/restaurant_page/')
def display_review2():
    form = ReservationForm()
    reviews = Reviews.query.order_by(Reviews.date_posted)
    return render_template('restaurant_page.html', form=form, reviews=reviews)



# @app.route('/reviewspage/', methods=['GET', 'POST'])
# def display_review():
# form = ReviewsForm()
# reviews = Reviews.query.order_by(Reviews.date_posted)
# return render_template('reviewspage.html', form=form, reviews=reviews)


@app.route('/restaurantpage/')
def display_review2():
    form = ReservationForm()
    reviews = Reviews.query.order_by(Reviews.date_posted)
    return render_template('restaurant_page.html', form=form, reviews=reviews)
