# TRIVIA PORK
### video url:
### description:

the project is composed by 2 principal areas ` app.py ` and the ` templates ` folder. in the app.py there is all the back end of the application.

### APP.PY:
at the top of ` app.py ` we can find the various import. I imported `flask` tu run the app; `random` for the question selection function in `/domanda`;sqlite3 to use and have access to a database where i stored all the question: question.db and the i imported for last translation.
translation.py is a python file where is stored a dictionary to make the site bilingual; all the text rendered on screen by the html is dynamic text, so by toggling  the switch button in `\` you can change the `session["lang"]` to english or italian, and the dynmic test is changed to the langueage you have chosen before.
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
`"/"`  its the first page of the web app and it renders ` hompegae.html `. in homepage there is the button to change the language , a button that redirects to ` /giocatori ` and some decoretions including the mascotte of the site uploaded to the static folder.

### /giocatori:
in this second template are rendered various button to change the number of players playng the game. in the script there is a short function to update the number of players seen on the screen by the players to match their input visually. then there is a button to submit the number of players. in the back end are stored the number of players in ` session["players"]`
and initialized the variables ` session["scores"]` for the score of each player; and `session["current_player"]` that is used like a pointer to tell the current player and keep track on the players turn later in the game.

### /regole:
in /regole is rendered regole.html, which is a static html file where are explained the rules of the game. the rules are shown one by one, making the next visible using the  `advance` function, that is called by an event listener that detects click.

### /domande:
`/domande` its the core of the app. here the user can choose the category and the difficulty of the question by clicking on the buttons on screen that are linked to `data-cat` for the category of the question and `data-diff` for the difficulty;  then in the `<script>` in  the `selectCat` and `selectDiff` where the values are passed  to `app.py` to use it for `/domanda` to select the question from the database;those function are used to handle the selected visual effect on the buttons. in the back end there is  a for loop that checks every turn if any player score is grater or equal to 25, in that case the user is redirected to `/vincitore`
ending the game. int the `footer` of domande.html there is a for loop running for the number of players. in this for loop is declared the variable that stores the current player score, then is calculated the percentage (`pct`) of advancement towards the final goal of 25 points; then is declared `width`, wich round pct to the nearest integer. widht i used for filling the the div, that functions like a progres bar.
