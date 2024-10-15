from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:root@localhost:3307/quiz_app'
db = SQLAlchemy(app)

# Define the Question model
class Question(db.Model):
    __tablename__ = 'questions'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    question = db.Column(db.String(500), nullable=False)
    options = db.Column(db.String(500), nullable=False)
    correct = db.Column(db.String(100), nullable=False)
    explanation = db.Column(db.String(500),nullable=False)
    hint = db.Column(db.String(500),nullable=False)
    category = db.Column(db.String(50), nullable=False)
    difficulty = db.Column(db.String(50), nullable=False)

# Create a list of questions (replace with your actual data)
questions_data = [
    {
        "question": "What is the chemical symbol for water?",
        "options": "['H2O', 'CO2', 'NaCl', 'O2']",
        "correct": "H2O",
        "explanation": "The chemical symbol for water is H2O, indicating that it is composed of two hydrogen atoms and one oxygen atom.",
        "hint": "Consider the molecular formula of water.",
        "category": "Science",
        "difficulty": "Easy"
    },
    {
        "question": "Which gas is most abundant in Earth's atmosphere?",
        "options": "['Nitrogen', 'Oxygen', 'Carbon dioxide', 'Argon']",
        "correct": "Nitrogen",
        "explanation": "Nitrogen is the most abundant gas in Earth's atmosphere, constituting about 78% of its volume.",
        "hint": "Consider the gas essential for life but not used in respiration.",
        "category": "Science",
        "difficulty": "Easy"
    },
    {
        "question": "Which organ is responsible for pumping blood throughout the body?",
        "options": "['Liver', 'Brain', 'Heart', 'Lungs']",
        "correct": "Heart",
        "explanation": "The heart is a muscular organ responsible for pumping blood throughout the body, delivering oxygen and nutrients to tissues and organs.",
        "hint": "Consider the organ associated with the cardiovascular system.",
        "category": "Science",
        "difficulty": "Easy"
    },
    {
        "question": "Which of the following is not a mammal?",
        "options": "['Dog', 'Cat', 'Snake', 'Dolphin']",
        "correct": "Snake",
        "explanation": "Snakes are not mammals; they belong to the reptile class. Mammals are characterized by features such as mammary glands and the presence of hair or fur.",
        "hint": "Think about animals that give birth to live young and nurse them with milk.",
        "category": "Science",
        "difficulty": "Easy"
    },
    {
        "question": "The speed of light is faster than the speed of sound.",
        "options": "['True', 'False']",
        "correct": "True",
        "explanation": "Light travels at a much faster speed than sound. The speed of light in a vacuum is approximately 299,792 kilometers per second, while the speed of sound in air is about 343 meters per second.",
        "hint": "Think about the velocities of light and sound.",
        "category": "Science",
        "difficulty": "Easy"
    },
    {
        "question": "Which planet is known as the 'Red Planet'?",
        "options": "['Venus', 'Mars', 'Jupiter', 'Saturn']",
        "correct": "Mars",
        "explanation": "Mars is often referred to as the 'Red Planet' due to its reddish appearance, caused by iron oxide (rust) on its surface.",
        "hint": "Think about a planet named after the Roman god of war.",
        "category": "Science",
        "difficulty": "Easy"
    },
    {
        "question": "Acids have a pH value less than 7.",
        "options": "['True', 'False']",
        "correct": "True",
        "explanation": "Acids have a pH value less than 7, indicating their acidic nature. The lower the pH value, the stronger the acid.",
        "hint": "Think about the pH scale and acidic substances.",
        "category": "Science",
        "difficulty": "Easy"
    },
    {
        "question": "Which gas is essential for respiration in humans?",
        "options": "['Oxygen', 'Carbon dioxide', 'Nitrogen', 'Hydrogen']",
        "correct": "Oxygen",
        "explanation": "Oxygen is essential for respiration in humans. It is used by cells to produce energy through the process of cellular respiration.",
        "hint": "Consider the gas used by organisms to breathe and produce energy.",
        "category": "Science",
        "difficulty": "Easy"
    },
    {
        "question": "Electricity is the flow of what?",
        "options": "['Protons', 'Neutrons', 'Ions', 'Electrons']",
        "correct": "Electrons",
        "explanation": "Electricity is the flow of electrons, which are negatively charged particles, through a conductor such as a wire.",
        "hint": "Think about the subatomic particles involved in electrical conduction.",
        "category": "Science",
        "difficulty": "Easy"
    },
    {
        "question": "Which of the following is not a primary color of light?",
        "options": "['Red', 'Blue', 'Yellow', 'Green']",
        "correct": "Yellow",
        "explanation": "Red, blue, and green are considered primary colors of light, as they can be combined to create other colors. Yellow is a secondary color.",
        "hint": "Consider the colors that can be mixed to produce a wide range of colors.",
        "category": "Science",
        "difficulty": "Easy"
    },
    {
        "question": "The Earth's outer layer is called the mantle.",
        "options": "['True', 'False']",
        "correct": "False",
        "explanation": "The Earth's outer layer is called the crust, which is the thin, solid outermost layer of the Earth. The mantle lies beneath the crust.",
        "hint": "Think about the Earth's layers and their characteristics.",
        "category": "Science",
        "difficulty": "Easy"
    },
    {
        "question": "Which organ is responsible for filtering waste from the blood?",
        "options": "['Liver', 'Pancreas', 'Kidneys', 'Spleen']",
        "correct": "Kidneys",
        "explanation": "The kidneys are responsible for filtering waste products from the blood and producing urine, which is then excreted from the body.",
        "hint": "Consider the organ involved in maintaining fluid balance and removing toxins.",
        "category": "Science",
        "difficulty": "Easy"
    },
    {
        "question": "Sound cannot travel through a vacuum.",
        "options": "['True', 'False']",
        "correct": "True",
        "explanation": "Sound requires a medium, such as air, water, or solids, to travel. It cannot propagate through a vacuum, as there are no particles to transmit the vibrations.",
        "hint": "Think about the requirement for sound transmission.",
        "category": "Science",
        "difficulty": "Easy"
    },
    {
        "question": "Which gas is responsible for the green color of plants?",
        "options": "['Oxygen', 'Carbon dioxide', 'Nitrogen', 'Chlorophyll']",
        "correct": "Chlorophyll",
        "explanation": "Chlorophyll, a pigment found in chloroplasts of plant cells, is responsible for the green color of plants and is crucial for photosynthesis.",
        "hint": "Consider the pigment involved in photosynthesis.",
        "category": "Science",
        "difficulty": "Easy"
    }
]


# Function to add questions to the database
@app.route('/')
def add_questions_to_database():
    db.create_all()
    for question_data in questions_data:
        question = Question(**question_data)
        db.session.add(question)
    db.session.commit()

if __name__ == '__main__':
    # Create all tables


    # Add questions to the database
    add_questions_to_database()
