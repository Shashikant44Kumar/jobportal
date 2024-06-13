from config import db 

class Postedjobs(db.Model):
    __tablename__ = 'postedjobs'
    id=db.Column(db.Integer,primary_key=True)
    job_id = db.Column(db.String(200),nullable=False)
    company_name = db.Column(db.String(200),nullable=False)
    role = db.Column(db.String(200),nullable=False)
    job_desc = db.Column(db.String(200),nullable=False)
    salary = db.Column(db.String(200),nullable=False)
    location = db.Column(db.String(200),nullable=False)
    skills_required = db.Column(db.String(200),nullable=False)
    user_id=db.Column(db.Integer,db.ForeignKey('user.id'))