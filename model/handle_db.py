import sqlite3
#import datetime

# This class is used to handle the database.
class HandleDB():
    """
        This function connects to the database and creates a cursor object that is used to execute
        SQL commands.
    """
    def __init__(self):
        # Connecting to the database.
        self._con=sqlite3.connect("./db/GA-test-database.db", check_same_thread=False);
        # Creating a cursor object that is used to execute SQL commands.
        self._cur=self._con.cursor()
    
    """
        It selects all the data from the table users and returns it
        :return: All the data from the database.
    """
    def get_all(self):
        # Selecting all the data from the table users.
        data = self._cur.execute("SELECT * FROM users");
        # Returning all the data from the database.
        return data.fetchall();
    
    """
        It returns the first row of the table where the UserAccess column is equal to the data_user
        parameter.
        
        :param data_user: The user's access level
        :return: The first row of the table.
    """
    def get_only(self, data_user):
        # A SQL query that is executed on the database.
        data= self._cur.execute("SELECT * FROM users WHERE UserAccess = '{}'".format(data_user));
        # Returning the first row of the table.
        return data.fetchone();
    
    """
        It inserts data into the database.
        
        :param data_user: A dictionary containing the data to be inserted into the database
    """
    def insert(self, data_user):
        # Inserting data into the database.
        self._cur.execute("INSERT INTO users VALUES('{}','{}','{}','{}','{}')".format(
            data_user["Id"],
            data_user["UserName"],
            data_user["Password"],
            data_user["Token"],
            data_user["ExpirationDate"],
            ));
        # Committing the changes to the database.
        self._con.commit();
    """
        It updates the database with the new token and expiration date.
        
        :param data_user: A dictionary containing the following keys:
    """
    def update_token(self, data_user):
        # Updating the database.
        self._cur.execute("UPDATE users SET TokenAccess='{}', ExpirationAccess='{}' WHERE ID='{}'".format(
            data_user["Token"],
            data_user["ExpirationDate"],
            data_user["Id"]
        ))
        # Committing the changes to the database.
        self._con.commit();            
    
    """
        The __del__() function is called when the object is about to be destroyed
    """
    def __del__(self):
        # Closing the connection to the database.
        self._con.close();



#Functionality and connection test
''' db=HandleDB();
data={
    "Id":0,
    "UserName":"Admin",
    "Password":"Admin",
    "Token":"xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
    "ExpirationDate": datetime.datetime.now()
}
db.insert(data);
print(db.get_all()); '''

''' db=HandleDB();
print(db.get_only("Admin"));  '''