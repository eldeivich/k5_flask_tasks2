from tasks import app
from flask import render_template, request, url_for, redirect
from datetime import datetime
import csv, operator


@app.route("/")
def index():
    if request.method =='GET':
        ldatos = open('./data/tareas.dat', 'r')
        datreader = csv.reader(ldatos, delimiter=',')

        d = []

        for linea in datreader:
            d.append(linea)

    do = sorted(d, key=operator.itemgetter(2))
    
    datoFormat = []
    for linea in do:
        anio,mes,dia = linea[2].split("-")
        fechajun = dia,mes,anio
        linea[2] = '-'.join(fechajun)
        datoFormat.append(linea)
    
    return render_template("index.html", e=datoFormat)

@app.route("/task.html", methods=['GET', 'POST'])
def task():
    if request.method == 'GET':
        return render_template('task.html')


    fdatos = open('./data/tareas.dat', 'a', newline="")
    csvwriter = csv.writer(fdatos, delimiter=",", quotechar='"')

    title = request.values.get('title')
    desc = request.values.get('desc')
    fecha = request.values.get('date')
    if title == '' or desc == '' or fecha == '':
        return render_template('500.html')
    '''
    anio, mes, dia = fecha.split("-")
    fechajun = dia,mes,anio
    date = '-'.join(fechajun)
    '''
    csvwriter.writerow([title, desc, date])

    fdatos.close()
    return redirect(url_for("index"))

@app.errorhandler(500)
def base_error_handler(e):
    return render_template('500.html'), 500