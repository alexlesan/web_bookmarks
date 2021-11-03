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
3. Run database migrations ( or can be used already existing database db.sqlite3) . 
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

# Structure of the project
    1. 'core' folder contains the Django core code;
    2. 'api' folder contains versions of the api, for example 'v1' is the first version of the api, 
        in this way it's possible to work at the same time to other versions.
    3. 'api/v1/' contians the list of applications used by the project.
    4. 'api/v1/accounts' contains the code regarding authenitication and also can be added more code about accounts profile...
    5. 'api/v1/bookmark' contians functionalities/code used to work with bookmarks.
    6. in the file 'requirements.txt' are listed packages used for this task.
    7. 'curl.txt' file should contain examples of curl requests that could be run to call urls from the project. 

# Git Repository
    - https://github.com/alexlesan/web_bookmarks.git