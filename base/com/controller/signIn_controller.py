from flask import render_template,redirect,request, session, flash
from base import app
from base.com.vo.login_vo import LoginVO
from base.com.dao.login_dao import LoginDAO

@app.route('/')
def load_login_page():
    return render_template('logIn.html')

@app.route('/sign_up',methods=['GET','POST'])
def load_signup_page():
    return render_template('signUp.html')

@app.route('/add_user',methods=['GET','POST'])
def add_user_page():
    try:
        user_first_name = request.form.get('firstName')
        user_last_name = request.form.get('lastName')
        user_email = request.form.get('email')
        user_phone_number = request.form.get('phoneNumber')
        user_dob = request.form.get('dob')
        user_username = request.form.get('signupUsername')
        user_password = request.form.get('signupPassword')


        login_vo = LoginVO()
        login_dao = LoginDAO()

        login_vo.first_name = user_first_name
        login_vo.last_name = user_last_name
        login_vo.email = user_email
        login_vo.phone_number = user_phone_number
        login_vo.dob = user_dob
        login_vo.username = user_username
        login_vo.password = user_password

        login_dao.insert_user(login_vo)
        return redirect('/')

    except Exception as ex:
        print("Something went Wrong", ex)

@app.route('/authenticate', methods=['GET','POST'])
def authenticate_user():
    print("Reached authenticate_user route")
    try:
        user_username = request.form.get('username')
        user_password = request.form.get('password')

        login_dao = LoginDAO()
        user = login_dao.get_user_by_username(user_username)

        if user and user.password == user_password:
            session['user_id'] = user.user_id
            flash('Login successful', 'success')
            return render_template("home.html")
        else:
            flash('Invalid username or password', 'danger')
            return redirect('/')

    except Exception as ex:
        print("Something went wrong", ex)
        flash('An error occurred while processing your request', 'danger')
        return redirect('/')
