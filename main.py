from flask import Flask, render_template, request, redirect
from wwr import get_wwr_job
from stackover import get_so_job
from remoteok import get_ro_job
from save import save_to_file

app = Flask("Jobhunter")

db = {}


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/result")
def result():
    word = request.args.get('word')
    if word:
        word = word.lower()
        from_db = db.get(word)
        if from_db:
            jobs = from_db
        else:
            jobs = get_so_job(word) + get_ro_job(word) + get_wwr_job(word)
            db[word] = jobs
    else:
        return redirect("/")
    return render_template("result.html", searching_by=word, resultsNumber=len(jobs), jobs=jobs)


@app.route("/save")
def save():
    try:
        word = request.args.get("word")
        if not word:
            raise Exception()
        word = word.lower()
        jobs = db.get(word)
        if not jobs:
            raise Exception()
        save_to_file(jobs, word)
        return f"Download CSV for {word}"
    except:
        return redirect('/')


app.run(host="0.0.0.0")
