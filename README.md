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

/when user just opened the page

![alt text](https://user-images.githubusercontent.com/74233809/141135318-28e4dfae-ce7f-44a5-a0dd-7ffe3fd42563.png)

/when user entered the name of coin and clicked search

![alt text](https://user-images.githubusercontent.com/74233809/141133433-709bae2b-6700-4a33-b1fc-d3985acbb1e4.png)


/when user enters unknown coin 
![alt text](https://user-images.githubusercontent.com/74233809/141134661-ed535c52-439a-4b20-811d-db892bf81464.png)


## License


[MIT](https://choosealicense.com/licenses/mit/)
