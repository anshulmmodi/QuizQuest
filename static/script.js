let timeLeft = document.querySelector(".time-left");
let quizContainer = document.getElementById("container");
let nextBtn = document.getElementById("next-button");
let countOfQuestion = document.querySelector(".number-of-question");
let displayContainer = document.getElementById("display-container");
let scoreContainer = document.querySelector(".score-container");
let restart = document.getElementById("restart");
let viewCertificate = document.getElementById("view-certificate")
let userScore = document.getElementById("user-score");
let startScreen = document.querySelector(".start-screen");
let startButton = document.getElementById("start-button");
let questionCount;
let scoreCount = 0;
let count = 11;
let countdown;
let currentQuestionIndex = 0;
let correctAnswers = 0;
let hintsUsed = 0;
let hintUsedForCurrentQuestion = false;
let circularProgress = document.querySelector(".circular-progress"),
    progressValue = document.querySelector(".progress-value")


//Questions and Options array
const quizArray = quizData

//Restart Quiz
restart.addEventListener("click", () => {
    initial();
    displayContainer.classList.remove("hide");
    scoreContainer.classList.add("hide");
});

viewCertificate.addEventListener("click", () => {
    displayCertificate()
})

function displayCertificate() {
    const score = scoreCount;
    const total = quizArray.length;

    // Opening a new window with the URL including both score and total in the query string
    window.open(`/view_certificate?score=${score}&total=${total}`, '_blank');
}



//Next Button
nextBtn.addEventListener("click", () => displayNext());

function displayNext() {
    // Hide any visible hint when moving to the next question
    hideHint();

    // Handle no selection case: If no option was selected, this is treated as incorrect
    // This can be modified based on how you want to handle unanswered questions
    let questionEl = document.getElementsByClassName("container-mid")[questionCount];
    let options = questionEl.querySelectorAll(".option-div");
    let optionSelected = Array.from(options).some(option => option.classList.contains("correct") || option.classList.contains("incorrect"));
    if (!optionSelected) {
        // Optionally, you can add logic here to mark the question as unanswered
        // For example, showing a specific message or handling the score differently
    }

    //increment questionCount
    questionCount++;

    //if last question
    if (questionCount >= quizArray.length) {
        // End of quiz: hide question container and display score
        displayContainer.classList.add("hide");
        scoreContainer.classList.remove("hide");
        userScore.innerHTML = "Your score is " + scoreCount + " out of " + quizArray.length;
        updateCircularProgressBar(scoreCount, quizArray.length)
    } else {
        // Display next question
        countOfQuestion.innerHTML = questionCount + 1 + " of " + quizArray.length + " Question";
        count = 11; // Reset the count variable to 11 for the next question
        hintUsedForCurrentQuestion = false;
        clearInterval(countdown); // Clear existing interval
        timerDisplay(); // Reset and start the timer for the next question
        quizDisplay(questionCount); // Display the next question
        updateProgressBar(); // Update the progress bar
    }
}

// Make sure timerDisplay function resets and starts the timer correctly for each question
const timerDisplay = () => {
    clearInterval(countdown); // Clear existing interval
    countdown = setInterval(() => {
        count--;
        timeLeft.innerHTML = `${count}s`;
        if (count <= 3) {
            document.querySelector('.timer-div').classList.add('low-time');
        } else {
            document.querySelector('.timer-div').classList.remove('low-time');
        }
        if (count === 0) {
            displayNext(); // Automatically move to the next question
        }
    }, 1000);
};

function showHint() {
    const hintsLeftElement = document.getElementById("hints-left");
    const totalHints = 2;

    // Assuming hintUsedForCurrentQuestion and hintsUsed are declared somewhere in your code
    if (hintUsedForCurrentQuestion) {
        const hintAlertBox = document.getElementById("hint-alert-container");
        hintAlertDescription = document.getElementById("hint-alert-description")
        hintAlertDescription.innerHTML = "Hint used for this question"
        hintAlertBox.style.display = "block"
        document.querySelector('.hint-alert-close').addEventListener('click', function() {
            document.getElementById("hint-alert-box").classList.add("hide");
        });
        setTimeout(() => hintAlertBox.style.display="none", 3000);
        console.log("Hello")
        return;
    }

    if (hintsUsed < totalHints) {
        const hintMessage = document.getElementById("hint-message");
        hintMessage.innerText = quizArray[questionCount].hint; // Assuming quizArray and questionCount are defined elsewhere
        hintMessage.style.display = "block";
        hintsUsed++; // Increment the count of used hints
        hintUsedForCurrentQuestion = true; // Set the flag since a hint is now used for this question

        // Update the hints left display
        hintsLeftElement.innerText = `Hints Left: ${totalHints - hintsUsed}`;
    } else {
        const hintAlertBox = document.getElementById("hint-alert-container");
        hintAlertBox.style.display = "block"
        document.querySelector('.hint-alert-close').addEventListener('click', function() {
            document.getElementById("hint-alert-box").classList.add("hide");
        });
        setTimeout(() => hintAlertBox.style.display="none", 3000);
    }
}


//Display quiz
const quizDisplay = (questionCount) => {
    let quizCards = document.querySelectorAll(".container-mid");
    //Hide other cards
    quizCards.forEach((card) => {
        card.classList.add("hide");
    });
    //display current question card
    quizCards[questionCount].classList.remove("hide");
    // remove explanation element
    let explanation = quizCards[questionCount].querySelector(".explanation");

    //explanation.innerHTML = "";
    // Reset the timer when a new question is displayed
    timerDisplay();
};
//Quiz Creation
function quizCreator() {
    // Iterate over each quiz question to generate its HTML
    quizArray.forEach((question) => {
        // Create the question card
        let div = document.createElement("div");
        div.classList.add("container-mid", "hide");

        // Set the initial question number display
        countOfQuestion.innerHTML = "1 of " + quizArray.length + " Question";

        // Add the question text
        let questionDiv = document.createElement("p");
        questionDiv.classList.add("question");
        questionDiv.innerHTML = question.question;
        div.appendChild(questionDiv);

        // Add the options based on question type
        if (question.type === "MCQ") {
            // MCQ options
            question.options.forEach(option => {
                let button = document.createElement("button");
                button.classList.add("option-div");
                button.setAttribute("onclick", "checker(this)");
                button.textContent = option;
                div.appendChild(button);
            });
        } else if (question.type === "TF") {
            // True/False options
            ["True", "False"].forEach(option => {
                let button = document.createElement("button");
                button.classList.add("option-div");
                button.setAttribute("onclick", "checker(this)");
                button.textContent = option;
                div.appendChild(button);
            });
        }

        // Append the question card to the quiz container
        quizContainer.appendChild(div);
    });
}


function checker(userOption) {
    let userSolution = userOption.innerText.trim(); // Trim to remove extra spaces
    let questionEl = document.getElementsByClassName("container-mid")[questionCount];
    let options = questionEl.querySelectorAll(".option-div");
    let isCorrect = userSolution === quizArray[questionCount].correct;

    // Hide any visible hint when answering a question
    hideHint();

    // Applying classes based on user's choice
    if (isCorrect) {
        userOption.classList.add("correct");
        scoreCount++;
        // Since the answer is correct, we don't show the explanation
    } else {
        userOption.classList.add("incorrect");
        // Highlight the correct option, works for both MCQ and True/False questions
        options.forEach((element) => {
            if (element.innerText.trim() === quizArray[questionCount].correct) { // Trim to remove extra spaces
                element.classList.add("correct");
            }
        });
        // Adding explanation for incorrect answers (optional based on your design)
        let explanationDiv = questionEl.querySelector(".explanation");
        if (!explanationDiv) { // Check if the explanationDiv doesn't already exist
            explanationDiv = document.createElement("div");
            explanationDiv.classList.add("explanation");
            questionEl.appendChild(explanationDiv);
        }
        explanationDiv.innerText = quizArray[questionCount].explanation;
    }

    // Disable all options after selection to prevent changing answers
    options.forEach((element) => {
        element.disabled = true;
    });

    // Stop the timer for the current question
    clearInterval(countdown);
}


// Function to hide the hint for the current question
function hideHint() {
    let hintElement = document.getElementById("hint-message");
    if (hintElement) {
        hintElement.style.display = "none"; // Hide the hint element
        hintElement.innerText = ""; // Reset the hint message
    }
}

// Remember to call hideHint() in the displayNext function or wherever you're setting up the question view


//initial setup
function initial() {
    quizContainer.innerHTML = "";
    questionCount = 0;
    scoreCount = 0;
    count = 11;
    hintsUsed = 0;
    hintUsedForCurrentQuestion = false;
    console.log(quizArray)
    updateProgressBar();
    clearInterval(countdown);
    timerDisplay();
    quizCreator();
    quizDisplay(questionCount);

    document.getElementById("hints-left").innerText = "Hints Left: 2";
}
//when user click on start button
startButton.addEventListener("click", () => {
    startScreen.classList.add("hide");
    displayContainer.classList.remove("hide");
    initial();
});
//hide quiz and display start screen
window.onload = () => {
    startScreen.classList.remove("hide");
    displayContainer.classList.add("hide");
};
function updateProgressBar() {
    const progressBar = document.getElementById("progress-bar");
    const progressPercentage = ((questionCount + 1) / quizArray.length) * 100;
    progressBar.style.width = `${progressPercentage}%`;
}
function updateCircularProgressBar(score, totalQuestions) {
    let progressEndValue = Math.round((score / totalQuestions) * 100);
    let progressStartValue = 0;
    const speed = 50; // How fast the animation progresses

    // Directly handle the case where progress should be 0%
    if (progressEndValue === 0) {
        progressValue.textContent = "0%";
        circularProgress.style.background = `conic-gradient(#21d727 0deg, #ededed 0deg)`;
        return; // Exit the function early
    }

    //clearInterval(progress); // Clear any existing interval to avoid overlaps
    let progress = setInterval(() => {
        progressStartValue++;
        progressValue.textContent = `${progressStartValue}%`;
        circularProgress.style.background = `conic-gradient(#21d727 ${progressStartValue * 3.6}deg, #ededed 0deg)`;

        if (progressStartValue >= progressEndValue) {
            clearInterval(progress);
        }
    }, speed);
}

