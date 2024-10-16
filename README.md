# QuizQuest

## Overview

**QuizQuest** is a dynamic quiz application where users can sign up, log in via OTP (displayed in the console), and take quizzes across various topics and difficulty levels. The app features a timed quiz, optional hints, progress tracking, and explanations for incorrect answers. Upon completion, users can view and download a certificate. Admins can manage the quiz question bank by adding new questions.

## Features

1. **User Authentication**:
   - Users can sign up with basic details.
   - OTP-based sign-in (OTP is displayed in the console for demo purposes).

2. **Quiz Topics**:
   - Users can choose from 6 topics: 
     - Geography
     - Science
     - History
     - Sports
     - Technology
     - General Knowledge

3. **Difficulty Levels**:
   - After selecting a topic, users choose a difficulty level: Easy, Medium, or Hard.

4. **Instructions and Start**:
   - An instruction page provides quiz guidelines before starting.
   - The quiz starts after the user confirms.

5. **Timed Questions**:
   - Each question has a 10-second timer.
   - A progress bar shows quiz advancement as users answer questions.

6. **Hints**:
   - Users have a limited number of hints to use during the quiz.

7. **Explanations**:
   - On selecting the wrong answer, an explanation for the correct answer is displayed.

8. **Results and Certification**:
   - After completing the quiz, the result is shown.
   - Users can view and download a certificate, which includes:
     - Username
     - Topic and difficulty level
     - Score and total questions
     - Date

9. **Admin Panel**:
   - Admins can add questions to the quiz bank for all topics and difficulty levels.

## System Requirements

- **Java 8 or higher**
- **MySQL 5.7 or higher** (for storing user and quiz data)
- **JDBC Driver for MySQL**
- **Maven** (optional, for managing dependencies)

## Setup Instructions

### 1. Clone the Repository

Clone this repository to your local machine:

```bash
git clone https://github.com/anshulmmodi/QuizQuest.git
cd QuizQuest
