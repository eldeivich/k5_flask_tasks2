from tasks import app
from flask import render_template, request, url_for, redirect

import csv


@app.route("/")
def index():
    if request.method =='GET':
        ldatos = open('./data/tareas.dat', 'r')
        datreader = csv.reader(ldatos, delimiter=',')

        datos = {}
        d = []

        for linea in datreader:
            d.append(linea)

    return render_template("index.html", e=d)

@app.route("/task.html", methods=['GET', 'POST'])
def task():
    if request.method == 'GET':
        return render_template('task.html')


    fdatos = open('./data/tareas.dat', 'a', newline="")
    csvwriter = csv.writer(fdatos, delimiter=",", quotechar='"')

    title = request.values.get('title')
    desc = request.values.get('desc')
    date = request.values.get('date')

    csvwriter.writerow([title, desc, date])

    fdatos.close()
    return redirect(url_for("index"))

