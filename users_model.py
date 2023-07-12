# import the function that will return an instance of a connection
from mysqlconnection import connectToMySQL

DATABASE = 'users-schema'

class User:
    def __init__(self,data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def display_all(cls):
        query = """
            SELECT * FROM users
        """
        results = connectToMySQL(DATABASE).query_db(query)
        print(results)
        all_users = []
        for row_from_db in results:
            user_instance = cls(row_from_db)
            all_users.append(user_instance)
        return all_users
    
    @classmethod
    def create(cls,data):
        query= """
            INSERT INTO users (first_name,last_name, email)
            VALUES (%(fname)s,%(lname)s, %(email)s);
            """
        return connectToMySQL(DATABASE).query_db(query,data)