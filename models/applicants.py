from config import db 

class Applicants(db.Model):
    __tablename__ = 'applicants'
    id=db.Column(db.Integer,primary_key=True)
    job_id = db.Column(db.String(200),nullable=False)
    applicant_name = db.Column(db.String(200),nullable=False)
    applicantion_id = db.Column(db.String(200),nullable=False)
    applicant_email = db.Column(db.String(200),nullable=False)
    applicant_resume = db.Column(db.String(200),nullable=False)
    user_id=db.Column(db.Integer,db.ForeignKey('user.id'))


# class Educations(db.Model):
#     __tablename__ = 'educations'
#     id = db.Column(db.Integer,primary_key=True)
#     school_name = db.Column(db.String(200),nullable=False)
#     degree_name = db.Column(db.String(200),nullable=False)
#     start_date = db.Column(db.String(200),nullable=False)
#     end_date = db.Column(db.String(200),nullable=False)
#     user_id = db.Column(db.Integer, db.ForeignKey('user.id'))