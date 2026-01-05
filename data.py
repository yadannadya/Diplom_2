class Person:
       
       user_without_email = { "email": "",
              "password": "1234",
              "name": "saske"
              }
       user_without_password = {
              "email": "ninja",
              "password": "",
              "name": "saske"
              }
       user_without_name = {
              "email": "ninja@gmail.com",
              "password": "1234",
              "name": ""}
       
       invalid_user = [user_without_password, user_without_email, user_without_name]

       login_zero_email = { "email": "",
              "password": "1234"
              }
       login_zero_password = {
              "email": "ninja",
              "password": ""
              }
       login_invalid_name = {
              "email": "hjiunja@gmail.com",
              "password": "1234"}

       invalid_login = [login_zero_email, login_zero_password, login_invalid_name]

       igridients =  {"ingredients" : ["61c0c5a71d1f82001bdaaa6c", "61c0c5a71d1f82001bdaaa6c", "61c0c5a71d1f82001bdaaa73"]}
       igridients_invalid  =  {"ingredients" : ["61c0c5a71d1f82001a6d", "61a71d1f82001bdaaa73"]}
       igridients_zero =  {"ingredients" : []}
