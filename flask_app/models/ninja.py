from flask_app.config.mysqlconnection import connectToMySQL
# model the class after the ninja table from our database
class Ninja:
    db = 'dojos_and_ninjas_schema'
    def __init__( self , data ):
        self.dojo_id = data['dojo_id'] #Connects Dojos to Ninjas with Foreign Key. 
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.age = data['age']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
    # Now we use class methods to query our database
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM ninjas;"
        # make sure to call the connectToMySQL function with the schema you are targeting.
        results = connectToMySQL(cls.db).query_db(query)
        # Create an empty list to append our instances of ninjas
        ninjas = []
        # Iterate over the db results and create instances of ninjas with cls.
        for ninja in results:
            ninjas.append( cls(ninja) )
        return ninjas
    
    @classmethod
    def get_one(cls, data):
        query = "SELECT * FROM ninjas WHERE id = %(id)s;"
        results = connectToMySQL(cls.db).query_db(query, data)
        if len(results) < 1: 
            return False
        return cls(results[0])

    @classmethod
    def save(cls, data ):
        query = "INSERT INTO ninjas ( dojo_id, first_name , last_name , age , created_at, updated_at ) VALUES ( %(dojo_id)s, %(first_name)s , %(last_name)s , %(age)s , NOW() , NOW() );"
        # data is a dictionary that will be passed into the save method from server.py
        return connectToMySQL(cls.db).query_db(query, data )    

    @classmethod
    def update (cls, data):  
        query = "UPDATE ninjas SET first_name = %(first_name)s, last_name = %(last_name)s,email = %(age)s, updated_at=NOW() WHERE id = %(id)s;"
        return connectToMySQL(cls.db).query_db(query, data)

    @classmethod
    def delete (cls, data):  
        query = 'DELETE FROM ninjas WHERE id = %(id)s;' #the blue text after the % is where DATA comes in. information that is being passed into DB, via DATA. 
        return connectToMySQL(cls.db).query_db(query, data)
