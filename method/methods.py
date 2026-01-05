import requests
from curl import Url
import allure

class Methods:
      
   @staticmethod 
   @allure.step('Создать пользователя')
   def register_user(body):
      return requests.post(Url.register_user, json=body)
    
   @staticmethod
   @allure.step('Создать заказ')
   def create_order(body, token):
      headers={'Authorization': token}
      return requests.post(url=Url.order, json=body, headers=headers)
   
   @staticmethod
   @allure.step('Авторизовать пользователя')
   def login_user(body):
      return requests.post(Url.login_user, json=body)

   @staticmethod 
   @allure.step('Удалить пользователя')
   def delete_user(token):
      return requests.delete(f"{Url.delete_user}", headers={'Authorization': token})



   
   
      