# TRIVIA PORK
### video url:
### description:

the project is composed by 2 principal areas ` app.py ` and the ` templates ` folder. in the app.py there is all the back end of the application.

### APP.PY:
at the top of ` app.py ` we can find the various import. I imported `flask` tu run the app; `random` for the question selection function in `/domanda`;sqlite3 to use and have access to a database where i stored all the question: question.db and the i imported for last translation.
translation.py is a python file where is stored a dictionary to make the site bilingual; all the text rendered on screen by the html is dynamic text, so by toggling  the switch button in `\` you can change the `session["lang"]` to english or italian, and the dynmic test is changed to the langueage you have chosen before.
#### question.db: 
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
in /regole is rendered regole.html

