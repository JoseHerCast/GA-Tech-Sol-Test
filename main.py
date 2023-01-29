from fastapi import FastAPI, Depends
from pydantic import BaseModel
from controller.user import User
from model.handle_db import HandleDB
import hashlib
import datetime
#from typing import Optional

#http://127.0.0.1:8000 -> local server

# Creating a connection to the database.
db=HandleDB();

# Creating a FastAPI object.
app = FastAPI();

# Defining the paths for the API.
root_path="/api";
security_path="/Seguridad";
login_path="/login";

# The Auth class is a subclass of BaseModel. It has two attributes: usuario and contrasena
class Auth(BaseModel):
    usuario: str
    contrasena: str



"""
    It checks if the user and password are correct, and if they are, it returns a token
    
    :param authRequest: This is the request that the user sends to the server
    :type authRequest: Auth
    :return: A dictionary with the status of the authentication, the description of the response and the
    token.
"""
@app.post(root_path+security_path+login_path)
def authenticate(authRequest:Auth):
    
    try:
        # Getting the user from the database.
        user_db=db.get_only(authRequest.usuario)
    
        # Getting the password from the database.
        password=user_db[2];
    
        # Creating a hash object.
        hash_object=hashlib.sha256();
        # Encoding the password.
        hash_object.update(authRequest.contrasena.encode());
        # Getting the hash of the password that the user sent.
        req_password=hash_object.hexdigest();
    
        # Checking if the user and password are correct.
        if user_db and req_password==password: 
        
            # Getting the expiration date of the token.
            exp_date=datetime.datetime.strptime(user_db[4],"%Y-%m-%d %H:%M:%S.%f");
            # Getting the current date and time.
            today=datetime.datetime.now();
        
            # Checking if the expiration date of the token is greater than the current date and time.
            if exp_date > today:
                # Just printing a message to the console.
                print("EXPIRATION TIME IS VALID");
            else:
                # Creating a User object with the username that the user sent.
                user_4updating=User({"UserName": authRequest.usuario})
                # Updating the expiration date of the token.
                user_4updating.update_user();
                print("EXPIRATION TIME HAS BEEN UPDATED");
        
            # Getting the updated user from the database.
            user_db=db.get_only(authRequest.usuario)
        
            # Getting the token from the database.
            token=user_db[3];
        
            return {
                "estado": True,
                "descripcionRespuesta":"",
                "token":token
            };
        else:
            return{
                "estado": False,
                "descripcionRespuesta":"Usuario o contraseña incorrectos"
            };
    # Catching the TypeError exception.
    except TypeError:
        return{
                "estado": False,
                "descripcionRespuesta":"Usuario o contraseña incorrectos"
        };
    # Catching any exception that is not a TypeError.
    except Exception as e:
        return{
                "estado": False,
                "descripcionRespuesta":"Error: " + str(e)
        };