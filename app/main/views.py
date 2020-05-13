from flask import render_template, redirect, request, url_for, abort
from . import main
from flask_login import login_required, current_user
from . import forms
from ..models import User, Events, Bookings, Tickets
from .forms import UpdateProfile, EventsForm, TicketsForm, Bookings
from .. import db

# @main.route("/movie/review/new/<int:id>", methods = ["GET", "POST"])
# @login_required
# def new_review(id):

@main.route("/")
def index():
    events = Events.get_all_events()
    return render_template("index.html", events=events)

@main.route('/user/<uname>')
def profile(uname):

    user = User.query.filter_by(username = uname).first()

    if user is None:
        abort(404)
    
    return render_template("profile/profile.html", user = user)

@main.route("/user/<uname>/update", methods = ["GET", "POST"])
@login_required
def update_profile(uname):
    user = User.query.filter_by(username = uname).first()
    if user is None:
        abort(404)
    
    form = UpdateProfile()

    if form.validate_on_submit():
        user.bio = form.bio.data

        db.session.add(user)
        db.session.commit()

        return redirect(url_for('.profile', uname = user.username))
    
    return render_template('profile/update_profile.html', form = form)

@main.route("/event_registration", methods=["GET", "POST"])
# @login_required
def registration():
    events_form = EventsForm()
    if events_form.validate_on_submit():
        event_name = events_form.event_name.data
        event_venue = events_form.event_venue.data
        date_of_event = events_form.date_of_event.data
        age_restriction = events_form.age_restriction.data

        events = Events(event_name=event_name, event_venue=event_venue, date_of_event=date_of_event, Age_restriction=age_restriction, users_id=current_user.id)    

        db.session.add(events)
        db.session.commit()

        return redirect(url_for("main.ticket_registration", event_id=event_id))

    title="event Registration"
    return render_template("events/event_registration.html", title=title, events_form=events_form)

@main.route("/ticket_registration/event_id")
@login_required
def ticket_registration(event_id):
    tickets_form = TicketsForm()
    if tickets_form.validate_on_submit():
       normal_ticket_price = tickets_form.normal_ticket_price.data
       VIP_ticket_price = tickets_form.normal_ticket_price.data
       VVIP_ticket_price = tickets_form.normal_ticket_price.data
       event_id = event_id

       tickets = Tickets(normal_ticket_price=normal_ticket_price, VIP_ticket_price=VIP_ticket_price, VVIP_ticket_price=VVIP_ticket_price, event_id=event_id)

       db.session.add(tickets)
       db.session.commit()

       return redirect(url_for("main.thankyou"))

    title="Ticket Registration"
    return render_template("events/ticket_registration.html", title=title)

@main.route("/ticket_registration/thankyou")
@login_required
def thankyou():

    title="Confirmation Page"
    return render_template("ticket_registration/thankyou.html")

@main.route("/ticket_bookings/ticket_id")
def bookings(ticket_id):
    bookings_Form = Bookings()
    if bookings_Form.validate_on_submit():
        ticket_type = bookings_Form.ticket_type.data
        phone_number = bookings_Form.phone_number.data
        no_of_tickets = bookings_Form.no_of_tickets.data
        email = current_user.user.email
        users_id = current_user.id
        ticket_id = ticket_id

        tickets = Tickets(ticket_type=ticket_type, phone_number=phone_number, no_of_tickets=no_of_tickets, email=email, users_id=users_id, ticket_id=ticket_id)

        db.session.add(tickets)
        db.session.commit()

        return redirect(url_for("main.bookings", ticket_id=ticket_id))
    
    title="Ticket Booking"
    return render_template("events/ticket_bookings.html", title = title, bookings_Form = bookings_Form)

@main.route("/single_event/<int:event_id>")
def single_event(event_id):

    event = Events.get_single_event(event_id)

    title = "single_event"
    return render_template("events/single_event.html", title=title)











