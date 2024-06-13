from config import db 

class Jobappliedbyuser(db.Model):
    __tablename__ = 'jobappliedbyuser'
    id=db.Column(db.Integer,primary_key=True)
    job_id = db.Column(db.String(200),nullable=False)
    company_name = db.Column(db.String(200),nullable=False)
    job_desc = db.Column(db.String(200),nullable=False)
    user_id=db.Column(db.Integer,db.ForeignKey('user.id'))