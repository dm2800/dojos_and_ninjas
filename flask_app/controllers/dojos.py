
from flask_app import app # need app for app routes. 

from flask import Flask, render_template, redirect, session, request


from flask_app.models.dojo import Dojo 


#Controller files contain routes. 

@app.route('/')
def index():
    return redirect ('/dojos/')


@app.route('/dojos/')
def dojos():
    return render_template ('dojos.html', dojos = Dojo.get_all()) # displaying the getAll function on the dojo.html page. 


@app.route('/dojos/add/')
def addDojo():
    return render_template('addDojo.html')

@app.route('/dojos/create/', methods = ['POST'])
def createDojo():
    data = {
        'name': request.form['name']
    }
    Dojo.save(data)
    return redirect ('/dojos/')

@app.route('/dojos/<int:id>/')
def viewDojo(id):
    data = {
        'id': id
    }
    # ninjas = Dojo.allNinjas(data)
    # print("all ninjas:", ninjas)
    return render_template('viewdojo.html', dojo=Dojo.allNinjas(data))
    
    
    


@app.route('/dojos/<int:dojo_id>/edit/') #To view the form to actually edit it. 
def editdojo(dojo_id):
    data = {
        'id': dojo_id
    }
    return render_template('editdojo.html', dojo=Dojo.get_one(data))
    



@app.route('/dojos/<int:dojo_id>/update/', methods=['POST']) #ONLY UPDATE ROUTE TAKES POST. 
def updatedojo(dojo_id):
    data = {
        'id': dojo_id,
        'name': request.form['name'],
        'headquarters': request.form['headquarters'],
        'locations': request.form['locations'],
        'workers': request.form['workers'],
        'planes': request.form['planes'],
    }
    Dojo.update(data)
    return redirect(f'/dojos/{dojo_id}/view/') #THIS NEEDS TO BE AN F STRING IN ORDER TO PASS IN THE ID AS A PARAMETER. 
    


@app.route('/dojos/<int:dojo_id>/delete/')
def deletedojo(dojo_id):
    data = {
        'id': dojo_id
    }
    Dojo.delete(data)
    return   redirect('/dojos/')
    






