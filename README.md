# Stepik_Se-Py_Final-project
Проект представляет собой финальное задание курса "Автоматизация тестирования с помощью Selenium и Python", доступный по ссылке:
https://stepik.org/course/575/https://github.com/Alexandra-Squirrel/Stepik_Se_Py_Final_project/blob/main/README.md

Блок 4 - Применение паттерна Page Object Model

## Состав проекта
- Все файлы, где хранятся страницы, лежат в отдельной папке **pages**
- Файл **test_product_page.py** содержит тесты c меткой **need_review**:
   - test_user_can_add_product_to_basket
   - test_guest_can_add_product_to_basket
   - test_guest_cant_see_product_in_basket_opened_from_product_page
   - test_guest_can_go_to_login_page_from_product_page
-  **requirements.txt** содержит нужные версии пакетов

## Запуск
- рекомендуемая команда для запуска:
```
pytest -v --tb=line --language=en -m need_review
```
- тест должен запускаться и проходить успешно с параметром **--language** следующей командой:
 ```
pytest --language=es test_items.py
```
- тест может запускаться и проходить успешно с параметром **--browser_nm** (chrome or firefox)  следующей командой:
```
pytest --browser_nm=firefox test_items.py
```

## Значения по умолчанию
- browser_nm = chrome
- language = en

## Примечание
Если при запуске вы получаете ошибку вроде: 
```
raise ValueError("option names %s already added" % conflict)
ValueError: option names {'--language'} already added
```
Перепроверьте, что у вас нет своего conftest.py в директории выше
