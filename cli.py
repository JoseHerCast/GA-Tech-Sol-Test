import json
import requests

# Setting the url of the API.
url = "http://127.0.0.1:8000/api/Seguridad/login";

# Setting the variable success to False.
success = False;

# Checking if the variable success is False. If it is False, it will execute the code inside the while
# loop.
while not success:
    # Asking the user to input a username.
    username = input("Ingresa tu nombre de usuario: ");
    # Asking the user to input a password.
    password = input("Ingresa tu contraseña: ");

    # Creating a dictionary with the keys "usuario" and "contrasena" and assigning the values of the
    # variables username and password to them.
    data = {"usuario": username, "contrasena": password};
    # Setting the header of the request to be sent.
    headers = {"Content-type": "application/json"};
    # Converting the response to a JSON object.
    response = requests.post(url, data=json.dumps(data), headers=headers).json();
    
    # Checking if the response is true or false. If it is true, it will print the description and
    # token. If it is false, it will print the error.
    if response["estado"] == True:
        success = True
        #FIXME: Delete all prints after testing completion
        print("DESCRIPCIÓN: ",response["descripcionRespuesta"]);
        print("TOKEN: ",response["token"]);
    else:
        print("ERROR: ",response["descripcionRespuesta"]);
