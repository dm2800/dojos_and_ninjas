from flask_app.config.mysqlconnection import connectToMySQL
# model the class after the dojo table from our database

from flask_app.models.ninja import Ninja

class Dojo:
    db = 'dojos_and_ninjas_schema'
    def __init__( self , data ):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.ninjas = []

    # Now we use class methods to query our database
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM dojos;"
        # make sure to call the connectToMySQL function with the schema you are targeting.
        results = connectToMySQL(cls.db).query_db(query)
        # Create an empty list to append our instances of dojos
        dojos = []
        # Iterate over the db results and create instances of dojos with cls.
        print(f'printing dojos{dojos}')
        for dojo in results:
            dojos.append( cls(dojo) )
            print(f'printing dojos{dojos}')
        return dojos
    
    @classmethod
    def get_one(cls, data):
        query = "SELECT * FROM dojos WHERE id = %(id)s;"
        results = connectToMySQL(cls.db).query_db(query, data)
        if len(results) < 1: 
            return False
        return cls(results[0])

    @classmethod
    def save(cls, data ):
        query = "INSERT INTO dojos (name, created_at, updated_at ) VALUES ( %(name)s , NOW() , NOW());"
        # data is a dictionary that will be passed into the save method from server.py
        return connectToMySQL(cls.db).query_db(query, data )    

    @classmethod
    def update (cls, data):  
        query = "UPDATE dojos SET name = %(name)s, updated_at=NOW() WHERE id = %(id)s;"
        return connectToMySQL(cls.db).query_db(query, data)

    @classmethod
    def delete (cls, data):  
        query = 'DELETE FROM dojos WHERE id = %(id)s;' #the blue text after the % is where DATA comes in. information that is being passed into DB, via DATA. 
        return connectToMySQL(cls.db).query_db(query, data)

    @classmethod
    def allNinjas(cls,data):
        #leftjoin statement will go here to get 1 Dojo and All of its Ninjas. 
        query = 'SELECT * FROM dojos LEFT JOIN ninjas ON dojos.id = ninjas.dojo_id WHERE dojos.id = %(id)s;'
        results = connectToMySQL(cls.db).query_db(query,data)
        print('Getting model allNinjas results: ', results)
        dojo = cls(results[0])
        ninjas = []
        for row in results:
            ninjaData = {
                'id': row['ninjas.id'],
                'dojo_id': row['dojo_id'],
                'first_name': row['first_name'],
                'last_name': row['last_name'],
                'age': row['age'],
                'created_at': row['ninjas.created_at'],
                'updated_at': row['ninjas.updated_at']
            }
            print('each row of ninjaData from Model: ', row)
            dojo.ninjas.append(Ninja(ninjaData))
            print('Printing the list from models: ', dojo)
        return dojo