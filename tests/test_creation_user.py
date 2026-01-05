import pytest
from method.methods import Methods
import allure
from data import Person


class TestCreationUser:

   @allure.title('Успешная регистрация курьера')
   def test_create_user_success(self, generate_user_and_delete):
      response = Methods.register_user(body=generate_user_and_delete[0])
      assert response.status_code == 200
      assert response.json()["success"] == True
      assert type(response.json()["accessToken"]) == str
   
   @allure.title('Нельзя зарегистрировать пользователя повторно')
   def test_create_user_with_repeat_data_unsuccess(self, generate_user_and_delete):
      Methods.register_user(body=generate_user_and_delete[0])
      response = Methods.register_user(body=generate_user_and_delete[0])
      assert response.status_code == 403
      assert  response.json()["success"] == False
 

   @allure.title('Нельзя зарегистрировать пользователя с пустым полем в теле запроса')
   @pytest.mark.parametrize('user', Person.invalid_user)
   def test_create_user_with_invalid_data_unsuccess(self, user):
      response = Methods.register_user(body=user)
      assert response.status_code == 403
      assert  response.json()["success"] == False