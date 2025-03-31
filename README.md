# Inventory Management System

## Описание
Это система управления запасами, разработанная с использованием Django. Она позволяет:
- Управлять продуктами и их запасами.
- Автоматически проверять уровень запасов и создавать задачи на пополнение.

## Установка и запуск

1. Установите зависимости:
   ```bash
   pip install -r requirements.txt
   
   Настройте базу данных в settings.py.

   Выполните миграции:
   python manage.py makemigrations
python manage.py migrate

Создайте суперпользователя: 
python manage.py createsuperuser

Запустите сервер:
python manage.py runserver

Запустите Celery:
celery -A inventory_management worker -B --loglevel=info
   
