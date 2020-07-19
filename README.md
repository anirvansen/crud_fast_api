# REST API with FAST API Framework(Python)

<img width="943" alt="cover" src="https://user-images.githubusercontent.com/20265546/87872807-5044e500-c9d9-11ea-954f-a11c4af7954b.PNG">

### I have created this project to demonstrate how convenient and easy it is to create rest api through FAST API framework. <br/>

<a href="https://fastapi.tiangolo.com/" target="_blank">FAST API </a>
 framework is high performance, easy to learn, fast to code, ready for production 

### This project shows below functionality which can be used as a template for API development

> Common CRUD operations on product API

> Database access with SQLAlchemy, a popular ORM tool.

> OAuth2 with Password (and hashing), Bearer with JWT tokens

> Automatic data model documentation with JSON Schema


## Table of Contents

- [Installation](#installation)
- [Features](#features)
- [Contributing](#contributing)
- [Team](#team)
- [FAQ](#faq)
- [Resources](#resources)
- [License](#license)

## Installation


```bash
$ git clone git@github.com:anirvansen/crud_fast_api.git

$ cd crud_fast_api

#Create a virutal environment
$ python -m venv venv

#Active it
#On windows
$ .\venv\Scripts\activte

#On mac and linux
$ source venv/bin/activate

#Install the dependencies

$ pip install requirements.txt

#Let's run the project

$ uvicorn app.main:app --reload

```
We are using uvicorn server to run the api,
Open http://127.0.0.1:8000 in the browser to see the project.

## Features

##  Register User
![register_user](https://user-images.githubusercontent.com/20265546/87872987-2db3cb80-c9db-11ea-80ec-717cf7103c96.gif)

Here I am using sqllite to store the information, You can always change the database by changing SQLALCHEMY URL in <a href="app/database.py">database.py</a>

> In case if you want to use postgresql

```python
SQLALCHEMY_DATABASE_URL = "postgresql://user:password@postgresserver/db"
```

# Authenticate User

Below routes are protected , to use these route you need to authenticate yourself so that a jwt token will be issued and this token can be used to authenticate in the subsequent request.

<img width="933" alt="protected_route" src="https://user-images.githubusercontent.com/20265546/87873114-483a7480-c9dc-11ea-8708-a95235255537.PNG">

### Let's Authenticate

![authenticate](https://user-images.githubusercontent.com/20265546/87873180-f8a87880-c9dc-11ea-9642-c9c0253e5889.gif)


<br/>

### Once you are authenticated you can use the protected routes , Lets see an example

<br/>

![add_product](https://user-images.githubusercontent.com/20265546/87873285-cba89580-c9dd-11ea-92c7-4910148750a4.gif)

> Behind the scene the client sends Authorization: Bearer in the header which is a jwt token in our case.
You can see the token in developer console ,
Network --> Headers

<img width="767" alt="token" src="https://user-images.githubusercontent.com/20265546/87873334-5d180780-c9de-11ea-871d-e621795a9dea.PNG">


> ### Feel free to play with other endpoints.


## Contributing

> ###  Fork the project and let me know if you find any issue or enhancement in the project.
I will be more than happy to look into your comments.


## FAQ

- **Why did i created this project ?**
    - To give a template which can be used to  get started with fast api with common functionalities.
- **Are you going to add more functionalities ?**
    - Yes, I am planning to add file uploads,Mail functionality and  many more

- **Why so basic crud project ?**
    - I am also in the process of learning the framework, I shall add more complex and advace functionalities in future.



## Resources

* <a href="https://fastapi.tiangolo.com/" target="_blank" >Official Fast api documentation</a>

* <a href="https://fastapi.tiangolo.com/tutorial/security/" target="_blank" >Fast Api Security</a>





## License
- **[MIT license](http://opensource.org/licenses/mit-license.php)**



    







