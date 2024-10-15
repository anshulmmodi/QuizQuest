from base import db

class LoginVO(db.Model):
    __tablename__='user_details'
    user_id = db.Column('user_id',db.Integer,primary_key=True,autoincrement=True)
    first_name=db.Column('first_name',db.String(255),nullable=False)
    last_name = db.Column('last_name', db.String(255))
    phone_number = db.Column('phone_number', db.BigInteger(),nullable=False)
    email = db.Column('email', db.String(255),nullable=False)
    dob = db.Column('dob',db.Date(),nullable=False)
    username = db.Column('username',db.String(255),nullable=False)
    password = db.Column('password',db.String(255),nullable=False)

    def as_dict(self):
        return{
            'user_id':self.user_id,
            'first_name':self.first_name,
            'last_name':self.last_name,
            'phone_number':self.phone_number,
            'email':self.email,
            'dob':self.dob,
            'username':self.username,
            'password':self.password
        }
db.create_all()
