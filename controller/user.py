from model.handle_db import HandleDB
import uuid
import hashlib
import datetime
#TODO: Añadir un "salt" al cifrado de la contraseña y guardarlo en la base de datos

# It creates a class called User.
class User():
    
    # A class attribute.
    data_user={};
    
    """
        The __init__ function is a constructor that creates a new instance of the HandleDB class and
        assigns the value of the parameter to the attribute.
        
        :param data_user: A list of the user's data
    """
    def __init__(self, data_user):
        # Creating a new instance of the HandleDB class.
        self.db=HandleDB();
        # Assigning the value of the parameter to the attribute.
        self.data_user=data_user;
    
    """
        It creates a user
    """
    def create_user(self):
        # Adding an ID to the user.
        self._add_id();
        # Encrypting the password.
        self._pass_encrypt();
        # Generating a random token for the user.
        self._generate_token();
        # Setting the expiration date for the token.
        self._setExpiration();
        # Inserting the user's data into the database.
        self.db.insert(self.data_user);
        
    def update_user(self):
        
        # Getting the user's data from the database.
        user_db=self.db.get_only(self.data_user["UserName"])
        # Getting the user's ID from the database and assigning it to the dictionary.
        self.data_user["Id"]=user_db[0];
        # Getting the password from the database and assigning it to the dictionary.
        self.data_user["Password"]=user_db[2];
        # It generates a random token for the user.
        self._generate_token();
        # Setting the expiration date for the token.
        self._setExpiration();
        # Updating the token in the database.
        self.db.update_token(self.data_user)
    
    """
        It adds an ID to the user.
    """
    def _add_id(self):
        # Getting all the users from the database.
        users=self.db.get_all();
        if users.__len__()==0:
            id_user=-1;
        else:
            # Getting the last user from the database.
            last_user=users[-1];
            # Getting the last user from the database and converting it into an integer.
            id_user=int(last_user[0]);
        # Adding an ID to the user.
        self.data_user["Id"]=str(id_user+1);
    
    """
        It takes the password, hashes it, and then stores it in the dictionary.
    """
    def _pass_encrypt(self):
        # Creating a hash object.
        hash_object=hashlib.sha256();
        # Taking the password and encoding it into a hash.
        hash_object.update(self.data_user["Password"].encode());
        # Taking the hash object and converting it into a hexadecimal string.
        self.data_user["Password"]=hash_object.hexdigest();
    
    """
        Generating a random token for the user
    """
    def _generate_token(self):
        # Generating a random token for the user.
        self.data_user["Token"]=uuid.uuid4();
    
    """
        It sets the expiration date for the token.
    """
    def _setExpiration(self):
        # Setting the expiration date for the token.
        self.data_user["ExpirationDate"]=datetime.datetime.now() + datetime.timedelta(days=365);
