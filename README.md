# Sayakat

### “Sayakat” means travel in the Kyrgyz language. 
### The purpose of this web application is to make travelling smooth and exciting for people who are interested in travelling to Kyrgyzstan.

Adjust the code below according to your needs in settings.py

`
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'sayakat',
        'USER': 'root',
        'PASSWORD': 'mypassword',
        'HOST': 'mysql',
        'PORT': '3306',
        'OPTIONS': {
            'init_command': "SET sql_mode='STRICT_TRANS_TABLES'"
        }
    }
}
`

## Run as the docker container

`docker-compose up -d`

`docker ps to get` <container_name> to create django admin user

`docker exec -it <container_name> python manage.py createsuperuser`

Open http://localhost:8080

## Run in the local dev environment

Create migrations:

`python manage.py makemigrations
`

Apply migrations:

`python manage.py migrate
`

Run project:

`python manage.py runserver`

Open http://localhost:8000