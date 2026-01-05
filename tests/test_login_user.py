from method.methods import Methods
import pytest
import allure
import helpers
from data import Person


class TestLoginuser:

   @allure.title('Успешная авторизация зарегистрированного пользователя')
   def test_login_user_success(self, register_user_and_delete):
      response = Methods.login_user(register_user_and_delete[2])
      assert response.status_code == 200
      assert response.json()["success"] == True

   @allure.title('Ошибка авторизации при неверном логине или пароле')
   @pytest.mark.parametrize('user', Person.invalid_login)
   def test_login_user_invalid_body_unsuccess(self, user):
      response = Methods.login_user(user)
      assert response.status_code == 401
      assert response.json()["success"] == False  

