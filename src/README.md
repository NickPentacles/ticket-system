# Прототип системы обработки и распределения заявок

В ходе разработки был использован Django Framework 4.2 https://www.djangoproject.com/ 

## Установка
1. Склонировать репозиторий
``` git
git clone 
```

2. Установить библиотеки
``` BASH
pip install -r ./requirements.txt
```

3. Провести миграции
``` BASH
python manage.py makemigrations
python manage.py makemigrations core
python manage.py migrate
```
4. Создать супер-пользователя
``` BASH
python manage.py createsuperuser
```

## Запуск
``` BASH
python manage.py runserver
```
### Структура папок
```
│   .gitignore
│   manage.py
│   README.md
│   requirements.txt
│
├───authentication
│   │   apps.py
│   │   forms.py
│   │   urls.py
│   │   views.py
│   │   __init__.py
│   │
│   └───__pycache__
│
├───core
│   │   apps.py
│   │   models.py
│   │   views.py
│   │   __init__.py
│   │
│   ├───middleware
│   │   │   authrequiredmiddleware.py
│   │   │
│   │   └───__pycache__
│   │
│   └───__pycache__
│
├───html
│   ├───static
│   │   └───css
│   │           bootstrap-grid.css
│   │           bootstrap-grid.css.map
│   │           bootstrap-grid.min.css
│   │           bootstrap-grid.min.css.map
│   │           bootstrap-reboot.css
│   │           bootstrap-reboot.css.map
│   │           bootstrap-reboot.min.css
│   │           bootstrap-reboot.min.css.map
│   │           bootstrap.css
│   │           bootstrap.css.map
│   │           bootstrap.min.css
│   │           bootstrap.min.css.map
│   │
│   └───templates
│       │   base.html
│       │
│       ├───core
│       │       request_confirm_delete.html
│       │
│       ├───error
│       │       page_not_found.html
│       │
│       ├───includes
│       │       auth.html
│       │       forms_submit.html
│       │       header.html
│       │       list.html
│       │       thead.html
│       │       tr_color.html
│       │
│       ├───login
│       │       login.html
│       │       register.html
│       │
│       ├───requests
│       │       create.html
│       │       edit.html
│       │       list.html
│       │       pending_requests.html
│       │       requests.html
│       │       
│       └───users
│               edit.html
│               list.html
│
├───requests
│   │   apps.py
│   │   forms.py
│   │   urls.py
│   │   views.py
│   │   __init__.py
│   │
│   └───__pycache__
│
├───src
│   │   asgi.py
│   │   settings.py
│   │   urls.py
│   │   views.py
│   │   wsgi.py
│   │   __init__.py
│   │
│   └───__pycache__                           
│
└───users
    │   apps.py
    │   forms.py
    │   urls.py
    │   views.py
    │   __init__.py
    │
    └───__pycache__
```