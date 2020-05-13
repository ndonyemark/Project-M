from flask_wtf import FlaskForm
from wtforms import TextAreaField, StringField, SelectField, SubmitField, IntegerField
from wtforms.validators import Required

class UpdateProfile(FlaskForm):

    bio = TextAreaField("Tell us about yourself", validators=[Required()])
    submit = SubmitField("Submit")

class EventsForm(FlaskForm):
    event_name=StringField("Event Name", validators=[Required()])
    event_venue=StringField("Event Venue", validators=[Required()])
    date_of_event=StringField("Date", validators=[Required()])
    age_restriction=SelectField("Age Restriction", choices=[("None", "None"), ("18 and over", "18 and over"), ("Kids", "Kids"), ("Teenagers", "Teenagers")], validate_choice=True, validators=[Required()])
    submit = SubmitField("Post Event")

class TicketsForm(FlaskForm):
    normal_ticket_price=IntegerField("Normal Ticket Price", validators=[Required()])
    VIP_ticket_price = IntegerField("VIP Ticket Price")
    VVIP_ticket_price = IntegerField("VVIP Ticket Price")
    submit = SubmitField("Post Ticket Info")

class Bookings(FlaskForm):
    ticket_type = SelectField("Ticket type", choices=[("Normal", "Normal"),("VIP", "VIP"), ("VVIP", "VVIP")], validators=[Required()])
    phone_number = IntegerField("PhoneNumber", validators=[Required()])
    no_of_tickets = IntegerField("Number of Tickets", validators=[Required()])
    submit = SubmitField("Book a Place")