
from flask_app import app # need app for app routes. 

from flask import Flask, render_template, redirect, session, request


from flask_app.models.dojo import Dojo
from flask_app.models.ninja import Ninja 



@app.route('/newninja/')
def newNinja():   
    return render_template('newninja.html', dojos = Dojo.get_all())



@app.route('/ninjas/create/', methods=['POST'])
def createNinja(): 
    Ninja.save(request.form)  
    print(request.form)
    return redirect(f'/dojos/{request.form["dojo_id"]}/')