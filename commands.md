Para instalar o django coverage

```pip install django-coverage``` 


####
Rodar os Testes
####

`coverage run manage.py test app_name`

####
Ver os Resultados
####

`coverage report`

`coverage html`

> abrir arquivo index.html no browser

####
Esconder a pasta venv dos resultados
####

`coverage run --omit='*/venv/*' manage.py test`

####
Add a new user to the User Table
####
```py
self.user = User.objects.create_user(username='testuser', password='12345')
login = self.client.login(username='testuser', password='12345')
```


####
Running Tests
####

# Run the specified module
`py manage.py test app1`

# Run the specified module
`py manage.py test app1.tests`

# Run the specified class
`py manage.py test app1.tests.models`

# Run the specified method
`py manage.py test app1.tests.models.TestNew`