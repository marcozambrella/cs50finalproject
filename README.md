# TRIVIA PORK
### video url:
### description:

the project is composed by 2 principal areas: ` app.py ` and the ` templates ` folder. In app.py, there is the entire backend of the application.

### APP.PY:
at the top of ` app.py ` we can find the various imports. I imported `flask` to run the app; `random` for the question selection function in `/domanda`;sqlite3 to use and have access to a database where I stored all the questions: question.db. then lastly I imported translation.
translation.py is a python file where a dictionary is stored to make the site bilingual; all the text rendered on screen by the html is dynamic text, so by toggling  the switch button in `\` you can change the `session["lang"]` to english or italian, and the dynamic text is changed to the language you have chosen before.
### question.db: 
the database for the questions has the schema:  *questions (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  question TEXT NOT NULL,
  correct_answer TEXT NOT NULL,
  wrong_answer1 TEXT NOT NULL,
  wrong_answer2 TEXT NOT NULL,
  wrong_answer3 TEXT NOT NULL,
  difficulty INTEGER NOT NULL,
  category TEXT NOT NULL,                                                                         language TEXT NOT NULL*
### home page :
`"/"`  it's the first page of the web app, and it renders `homepage.html `. in homepage there is the button to change the language , a button that redirects to ` /giocatori ` and some decorations, including the mascot of the site uploaded to the static folder.

### /giocatori:
in this second template are rendered various button to change the number of players playing the game. in the script there is a short function to update the number of players seen on the screen by the players to match their input visually. then there is a button to submit the number of players. In the back end are stored the number of players in ` session["players"]`
and initialized the variables ` session["scores"]` for the score of each player; and `session["current_player"]` that is used like a pointer to tell the current player and keep track of the player's turn later in the game.

### /regole:
in /regole is rendered regole.html, which is a static html file where the rules of the game are explained. the rules are shown one by one, making the next visible using the  `advance` function, which is called by an event listener that detects clicks on screen.

### /domande:
`/domande` its the core of the app. here the user can choose the category and the difficulty of the question by clicking on the buttons on screen that are linked to `data-cat` for the category of the question and `data-diff` for the difficulty;  then in the `<script>` in  the `selectCat` and `selectDiff` where the values are passed  to `app.py` to use it for `/domanda` to select the question from the database;those function are used to handle the selected visual effect on the buttons. in the back end there is  a for loop that checks every turn if any player's score is greater than or equal to 25; in that case, the user is redirected to `/vincitore`
ending the game. in the `footer` of domande.html, there is a for loop running for the number of players. in this for loop is declared the variable that stores the current player score, then is calculated the percentage (`pct`) of advancement towards the final goal of 25 points; then is declared `width`, which rounds pct to the nearest integer. widht is used for filling the div, which functions like a progress bar.

### /domanda:
`/domanda` handles the category and difficulty of the question previously chosen in `/domande`;
then using sqlite3, the program fetches all the questions with those specific parameters, and then it picks a random one. in the `render_template` it passes all the variables needed to render on screen the question and the answers (`return render_template("domanda.html",
        domanda           = row["question"],
        risposte          = risposte,
        risposta_corretta = risposte.index(row["correct_answer"]),
        categoria         = category,
        difficolta        = difficulty,
        current_player    = session.get("current_player"),
        players           = session.get("players"),
    )`)
    .in the html file, the answers are rendered using a jinja for loop. in the file there is a hidden form that tells the user if the answer is correct or not, and it becomes visible only after submitting, changing the `type` in the html tag; then after the script is executed, revealing the correct answer,
an overlay appears on screen with a message that tells the next player's turn, using the current player variable + 1.

### /risposta:
in `/risposta` are added or subtracted points to the current player score based on his answer. then it updates the current player to the next one; and finally redirecting the user to `/domande`

### /vincitore:
`/vincitore`, which renders `vincitore.html`, is the victory final screen of the app. the user is automatically redirected to `/vincitore` as soon as they hit the 25 point mark (this is checked in `/domande` at lines 60-62). in the html there is a div that covers the whole page, and its the div used in the script for the confetti falling animation.in the file, the final leaderboard is rendered using jinja.
