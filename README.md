# flask_sql_scrapper

### Akbarov Damir, Orujova Elmira SE-2008

Flask application that allows to search new about cryptocurrency and output it

 

## Installation

To do this project following libraries required: ```Flask```, ```Flask SQLAlchemy```, ```beautifulsoup```, ```Psycopg2```. Below shown the installation



```

pip install beautifulsoup4
pip install Flask
pip install Flask-SQLAlchemy
pip install requests
pip install psycopg2

```

## Install script





```

git clone https://github.com/M0nero/flask_sql_scrapper.git

cd flask_sql_scrapper

#create venv

```

## Usage 



User needs to change password and enter his/her password from DBMS, in my case it is '123'



```python

app = Flask(__name__, template_folder='../templates', static_url_path='', static_folder='../static')

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:123@localhost:5432/jwt_flask'

app.config['SECRET_KEY'] = 'thisismyflasksecretkey'

```

![alt text](https://user-images.githubusercontent.com/74233809/141132628-ea94f216-a908-48ef-815f-bba18c3283ee.png)






## Examples



/login - at first user asked to enter the login and a password



![alt text](https://user-images.githubusercontent.com/74233809/139107074-7c6427fa-e40a-4a28-9e49-b8de55ea6456.png)



If user entered correct login and password this page will open



![alt text](https://user-images.githubusercontent.com/74233809/139108084-0da1fd32-84ce-4ee2-88c4-1cb5fb53adb3.png)



If user entered wrong login or password

![alt text](https://user-images.githubusercontent.com/74233809/139115984-6ff11a6f-8ad2-4665-bf66-8c04ca10ea33.png)



/protected 



![alt text](https://user-images.githubusercontent.com/74233809/139108822-d4ccedf7-eae5-4c8a-8212-798e26600900.png)



![alt text](https://user-images.githubusercontent.com/74233809/139109550-2ca4701a-6876-4679-92f8-d616603ceaf9.png)





## License


[MIT](https://choosealicense.com/licenses/mit/)
