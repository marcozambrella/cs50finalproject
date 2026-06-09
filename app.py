import sqlite3
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from translations import translations
import random
import os

app = Flask(__name__)

app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
app.config["TEMPLATES_AUTO_RELOAD"] = True
Session(app)

def get_db():
    db = sqlite3.connect(os.path.join(os.path.dirname(__file__), "question.db"))
    db.row_factory = sqlite3.Row
    return db


# app route per il sito bilingue (italiano/inglese)
# le traduzioni sono in translations.py, importate come dizionario "translations"
@app.route("/lang/<code>")
def set_lang(code):
    if code in ("it", "en"):
        session["lang"] = code
    from flask import request
    return redirect(request.referrer or "/")
@app.context_processor
def inject_translations():
    lang = session.get("lang", "it")
    return dict(t=translations[lang], lang=lang)




@app.route("/")
def index():
    return render_template("homepage.html")


@app.route("/giocatori", methods=["GET", "POST"])
def giocatori():
    if request.method == "POST":
        numero_giocatori = int(request.form.get("n"))
        session["players"] = numero_giocatori
        session["scores"] = {}
        session["scores"] = {str(i): 0 for i in range(1, numero_giocatori + 1)}
        session["current_player"] = "1"
        return redirect("/regole") 
    return render_template("giocatori.html")

@app.route("/regole")
def regole():
    return render_template("regole.html")

@app.route("/domande", methods=["GET", "POST"])
def domande():
    if request.method == "POST":
        session["category"] = request.form.get("category")
        session["difficulty"] = request.form.get("difficulty")
        return redirect("/domanda")
    for i in session["scores"]:
        if session["scores"][i] >= 25:
         return redirect("/vincitore")
    
    return render_template("domande.html",
                           current_player = session.get("current_player"),
                           players = session.get("players"),
                           scores = session.get("scores"),)
                          

@app.route("/domanda")
def domanda():
    category = session.get("category")
    difficulty = session.get("difficulty")
    lang = session.get("lang", "en")
    if not category or not difficulty:
        flash("Seleziona categoria e difficoltà.")
        return redirect("/domande")

    row =  get_db().execute(
        "SELECT question, correct_answer, wrong_answer1, wrong_answer2, wrong_answer3 FROM questions WHERE category = ? AND difficulty = ?  AND language = ? ORDER BY RANDOM() LIMIT 1",
        (category, difficulty, lang)
    ).fetchone()

    if row is None:
        flash("Nessuna domanda trovata.")
        return redirect("/domande")

    risposte = [row["correct_answer"], row["wrong_answer1"], row["wrong_answer2"], row["wrong_answer3"]]
    random.shuffle(risposte)

    return render_template("domanda.html",
        domanda           = row["question"],
        risposte          = risposte,
        risposta_corretta = risposte.index(row["correct_answer"]),
        categoria         = category,
        difficolta        = difficulty,
        current_player    = session.get("current_player"),
        players           = session.get("players"),
    )
     

@app.route("/risposta", methods=["POST"])
def risposta():
    if "scores" not in session:
        return redirect("/")
    scelta   = request.form.get("scelta")
    corretta = request.form.get("corretta")

    if not scelta or not corretta:
        flash("Risposta non valida.")

    elif scelta == corretta:
        scores = session["scores"]
        scores[session["current_player"]] += int(session["difficulty"])
        session["scores"] = scores

    else:
        scores = session["scores"]
        scores[session["current_player"]] -= int(session["difficulty"])
        session["scores"] = scores 
    
    session["current_player"] = str(int(session["current_player"]) + 1)
    if int(session["current_player"]) > session["players"]:
        session["current_player"] = "1"
    return redirect("/domande")
 
@app.route("/vincitore")
def vincitore():
    if "scores" not in session:
        return redirect("/")
    return render_template("vincitore.html",
        players = session.get("players", 1),
        scores  = session.get("scores", {})
    )


if __name__ == "__main__":
    app.run(debug=True)