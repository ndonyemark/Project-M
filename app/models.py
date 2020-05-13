from . import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from .import login_manager
from datetime import datetime

class User(UserMixin, db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(255))
    email = db.Column(db.String(255), unique = True, index = True)
    pass_secure = db.Column(db.String(255))
    bio = db.Column(db.String(255))
    events = db.relationship('Events', backref='user', lazy = 'dynamic')
    bookings=db.relationship("Bookings", backref="user", lazy="dynamic")

    @property
    def password(self):
        raise AttributeError("You cannot read the password attribute")

    @password.setter
    def password(self, password):
        self.pass_secure = generate_password_hash(password)
    
    def verify_password(self, password):
        return check_password_hash(self.pass_secure, password)

    def __repr__(self):
        return f'User {self.username}'

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class Events(db.Model):
    __tablename__ = "events"
    id = db.Column(db.Integer, primary_key = True)
    event_name = db.Column(db.String(255))
    event_venue = db.Column(db.String(255))
    date_of_event = db.Column(db.DateTime)
    Age_restriction = db.Column(db.String(25))
    users_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    tickets=db.relationship("Tickets", backref="events", lazy="dynamic")

    @classmethod
    def get_all_events(cls):
        event = Events.query.all()
        return event
    
    @classmethod
    def get_single_event(cls, event_id):
        event = Events.query.filter_by(id=event_id).first()
        return event

class Tickets(db.Model):
    __tablename__ = "ticket_info"
    id = db.Column(db.Integer, primary_key = True)
    normal_ticket_price = db.Column(db.String)
    VIP_ticket_price = db.Column(db.String)
    VVIP_ticket_price = db.Column(db.String)
    event_id = db.Column(db.Integer, db.ForeignKey("events.id"))
    bookings=db.relationship("Bookings", backref="tickets", lazy="dynamic")

class Bookings(db.Model):
    __tablename__ = "bookings"
    id = db.Column(db.Integer, primary_key = True)
    ticket_id = db.Column(db.Integer, db.ForeignKey("ticket_info.id"))
    users_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    email = db.Column(db.String(255))
    phone_number = db.Column(db.Integer)
    ticket_type = db.Column(db.String(255))
    no_of_tickets = db.Column(db.Integer)