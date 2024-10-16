# QuizQuest

## Overview

**QuizQuest** is a web-based quiz application built using Flask (Python) for the backend and HTML, CSS, and JavaScript for the frontend. The project does not rely on an SQL database; data can be stored directly in files or using in-memory structures like Python dictionaries. Users can sign up, log in via OTP (shown in the console), and take quizzes across various topics and difficulty levels. The quiz features timed questions, optional hints, explanations for incorrect answers, and a downloadable certificate upon completion.

## Features

1. **User Authentication**:
   - Users can sign up and log in using an OTP (OTP is displayed in the console for demo purposes).
  
2. **Quiz Topics**:
   - Six quiz topics available:
     - General Knowledge
     - Geography
     - Science
     - History
     - Sports
     - Technology
     
  
3. **Difficulty Levels**:
   - Each topic has three difficulty levels: Easy, Medium, or Hard.
  
4. **Instructions and Quiz Start**:
   - An instruction page is provided before the quiz begins.
   - Users can start the quiz after reviewing the instructions.
  
5. **Timed Questions**:
   - Each question is timed with a 10-second timer.
   - A progress bar tracks the user's progress through the quiz.

6. **Hints**:
   - Users can use a limited number of hints during the quiz.

7. **Explanations**:
   - After answering incorrectly, an explanation for the correct answer is displayed.

8. **Results and Certification**:
   - After completing the quiz, the result is displayed.
   - Users can view and download a personalized certificate containing:
     - Username
     - Topic and difficulty level
     - Score and total number of questions
     - Date of completion

9. **Admin Features**:
   - Admins can add new questions to the quiz bank by providing the topic, difficulty level, question, options, correct answer, and explanation.

## Technologies Used

- **Backend**: Flask (Python)
- **Frontend**: HTML, CSS, JavaScript

## System Requirements

- **Python 3.7+**
- **Flask** (install via `pip install flask`)

## Setup Instructions

### 1. Clone the Repository

Clone this repository to your local machine:

```bash
git clone https://github.com/anshulmmodi/QuizQuest.git
cd QuizQuest
