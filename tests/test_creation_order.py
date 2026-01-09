import pytest
from method.methods import Methods
from data import Person
import allure
        
class TestCreationOrder:

    @allure.title('Успешное создание заказа авторизованным пользователем') 
    def test_create_order_auth_user_with_ingredients_success(self, register_user_and_delete):
        
        response = Methods.create_order(body=Person.igridients, token=register_user_and_delete[1])
        assert response.status_code == 200
        assert response.json()["success"] == True

    @allure.title('Ошибка 400 при создании заказа без ингридиентов с авторизацией') 
    def test_create_order_auth_user_without_ingredients_unsuccess(self, register_user_and_delete):
        response = Methods.create_order(body=Person.igridients_zero, token=register_user_and_delete[1])
        assert response.status_code == 400
        assert response.json()["message"] == "Ingredient ids must be provided"

    @allure.title('Ошибка 500 при создании заказа с неверным хешем ингридиентов с авторизацией')
    def test_create_order_auth_user_with_invalid_ingredients_unsuccess(self, register_user_and_delete):
        response = Methods.create_order(body=Person.igridients_invalid, token=register_user_and_delete[1])
        assert response.status_code == 500

    @allure.title('Успешное создание заказа без авторизации') 
    def test_create_order_unauth_user_with_ingredients_success(self):
        response = Methods.create_order(body=Person.igridients, token="")
        assert response.status_code == 200
        assert response.json()["success"] == True

    @allure.title('Ошибка 400 при создании заказа без ингридиентов без авторизации') 
    def test_create_order_unauth_user_without_ingredients_unsuccess(self):
        response = Methods.create_order(body=Person.igridients_zero, token="")
        assert response.status_code == 400
        assert response.json()["message"] == "Ingredient ids must be provided"

    @allure.title('Ошибка 500 при создании заказа с неверным хешем ингридиентов без авторизации') 
    def test_create_order_unauth_user_with_invalid_ingredients_unsuccess(self):
        response = Methods.create_order(body=Person.igridients_invalid, token="")
        assert response.status_code == 500