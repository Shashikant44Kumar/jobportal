from config import db

class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(200),nullable=False)
    applicants = db.relationship('Applicants',backref='user')
    availablejobs = db.relationship('Availablejobs',backref='user')
    jobappliedbyuser = db.relationship('Jobappliedbyuser',backref='user')
    postedjobs = db.relationship('Postedjobs',backref='user')
    