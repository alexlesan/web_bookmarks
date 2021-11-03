# TASK ASSIGNEMENT: Web Bookmarks
Installation
------------
1. Create a virtual environment and activate it:
 ```bash
 python3.9 -m venv .venv
.venv\scripts\activate
 ```
2. Install python project dependencies. From this point on the working directory will be: 
 ```bash
 pip install -r requirements.txt
 ```
3. Run database migrations. 
 ```bash
 python manage.py migrate
 ```
4. Now that everything is in place, create an admin user to be able to access the application:
 ```bash
 python manage.py createsuperuser
 ```
5. Start the development server:
 ```bash
 python manage.py runserver 127.0.0.1:8000
 ```