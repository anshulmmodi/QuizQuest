from flask import Flask, render_template, request, redirect, url_for, session, jsonify
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
import ast
from datetime import datetime


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:root@localhost:3307/quiz_app'
db = SQLAlchemy(app)
app.config['SECRET_KEY'] = 'anshul'


class User(db.Model):
    __tablename__ = 'user_details'
    user_id = db.Column('user_id', db.Integer, primary_key=True, autoincrement=True)
    user_name = db.Column('user_name', db.String(255), nullable=False)
    user_email = db.Column('user_email', db.String(255), nullable=False)
    user_password = db.Column('user_password', db.String(255), nullable=False)

    def __repr__(self):
        return '<User %r>' % self.user_name

class Question(db.Model):
    __tablename__ = 'questions'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    question = db.Column(db.String(500), nullable=False)
    options = db.Column(db.String(500), nullable=False)
    correct = db.Column(db.String(100), nullable=False)
    explanation = db.Column(db.String(500), nullable=False)
    hint = db.Column(db.String(500), nullable=False)
    category = db.Column(db.String(50), nullable=False)
    difficulty = db.Column(db.String(50), nullable=False)

    def serialize(self):
        options_list = ast.literal_eval(self.options)
        print(options_list)
        return {
            'id': self.id,
            'question': self.question,
            'options': options_list,
            'correct': self.correct,
            'explanation': self.explanation,
            'hint': self.hint
            #'category': self.category,
            #'difficulty': self.difficulty
        }
@app.route('/')
def signin():
    return render_template("signIn.html")


@app.route('/signup', methods=['POST'])
def signup():
    if request.method == 'POST':
        user_name = request.form['name']
        user_email = request.form['email']
        user_password = request.form['password']

        # Check if user already exists
        existing_user = User.query.filter_by(user_email=user_email).first()
        if existing_user:
            return "User already exists!"

        # Create a new user
        new_user = User(user_name=user_name, user_email=user_email, user_password=generate_password_hash(user_password))
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for('signin'))


@app.route('/signin', methods=['POST'])
def login():
    if request.method == 'POST':
        user_email = request.form['email']
        user_password = request.form['password']
        user = User.query.filter_by(user_email=user_email).first()

        if user_email == "admin" and user_password == "admin":
            return render_template("admin.html")
        if user and check_password_hash(user.user_password, user_password):
            # Store user data in session
            session['user_id'] = user.user_id
            session['user_name'] = user.user_name
            return redirect(url_for('home'))
        else:
            error_message = "Invalid email or password. Please try again."
            return render_template("signIn.html", error_message=error_message)

@app.route('/submit_question', methods=['GET', 'POST'])
def submit_question():
    if request.method == 'POST':
        question_text = request.form['questionText']
        question_type = request.form['questionType']
        hint_text = request.form['hintText']
        explanation_text = request.form['explanationText']
        category = request.form['category']
        difficulty = request.form['difficulty']

        if question_type == 'True/False':
            option = ['True', 'False']
            correct_answer = request.form['correctAnswerTrueFalse']
        else:
            option = [request.form['option1'], request.form['option2'], request.form['option3'], request.form['option4']]
            correct_answer = request.form['correctAnswerMCQ']

        options = str(option)

        # Create a new Question object with the received data
        new_question = Question(
            question=question_text,
            options = options,
            correct = correct_answer,
            explanation=explanation_text,
            hint=hint_text,
            category=category,
            difficulty=difficulty,
        )

        # Add the new_question to the database session
        db.session.add(new_question)

        # Commit the changes to the database
        db.session.commit()

        return redirect(url_for('submission_success'))
    else:
        # Render the form to submit a question
        return render_template('admin.html')

@app.route('/submission_success')

def submission_success():
    return render_template('submission_success.html')
@app.route('/home')
def home():
    # Retrieve user data from session
    user_id = session.get('user_id')
    user_name = session.get('user_name')
    return render_template("home.html", user_id=user_id, user_name=user_name)

@app.route('/process_topic')
def process_topic():
    topic = request.args.get('topic')
    session['topic'] = topic
    return render_template("category.html", topic=topic)

@app.route('/process_quiz')
def process_quiz():
    topic = request.args.get('topic')
    difficulty = request.args.get('difficulty')
    session['difficulty'] = difficulty
    return redirect(url_for('quiz', topic=topic, difficulty=difficulty))

@app.route('/quiz')
def quiz():
    topic = request.args.get('topic')
    difficulty = request.args.get('difficulty')

    questions = Question.query.filter_by(category=topic, difficulty=difficulty).all()
    questions_json = []
    for question in questions:
        # Infer question type based on the number of options
        options_list = ast.literal_eval(question.options)
        question_type = 'MCQ' if len(options_list) > 2 else 'TF'
        # Serialize question data including the inferred type
        question_data = question.serialize()
        # Add the inferred type to the serialized data
        question_data['type'] = question_type
        questions_json.append(question_data)
    return render_template('quiz.html', quiz_data=questions_json)

@app.route('/view_certificate')
def view_certificate():
    score = request.args.get('score') # Retrieve the score from query parameters
    total = request.args.get('total')
    user_name = session.get('user_name')
    quiz_name = session.get('topic') + "-" + session.get('difficulty')
    current_date = datetime.now().strftime("%d-%m-%Y")
    return render_template("certificate.html", score=score, user_name=user_name, quiz_name=quiz_name,total=total, current_date=current_date)


if __name__ == "__main__":
    app.run(debug=True)
