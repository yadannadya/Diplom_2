import pytest
from method.methods import Methods
import helpers
from data import Person


@pytest.fixture
def generate_user_and_delete():
    user = helpers.faker_user()
    user_auth = {"email": user["email"],
                 "password" : user["password"]}
    
    yield [user, user_auth]

    accessToken = Methods.login_user(user_auth).json()["accessToken"]
    Methods.delete_user(accessToken)

@pytest.fixture
def register_user_and_delete():
    user = helpers.faker_user()
    response = Methods.register_user(user)
    accessToken = response.json()["accessToken"]
    user_auth = {"email": user["email"],
                 "password" : user["password"]}

    yield [response, accessToken, user_auth]

    Methods.delete_user(accessToken)
    
    
    