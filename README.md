# Diplom_2#

## <h>API для Stellar Burgers</h>
Тестирование API для Stellar Burgers. Его документация: qa-scooter.praktikum-services.ru/docs/.


Протестированы ручки:
- Создание пользователя
- Логин пользователя(авторизация)
- Создание заказа


### <h>1. Установите зависимости:</h>

> pip install -r requirements.txt</h>

### <h>2. Запустить все тесты и записать отчет:</h>

> pytest --alluredir=./allure-results

### <h>3. Посмотреть отчет по прогону html</h>

> allure serve ./allure-results