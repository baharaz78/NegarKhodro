# Animal
The backend project for **Negar Khodro Technical Assessment**

## How to run?!


### Run
- Open a terminal in root folder of Animal.
- Create a virtual environment with `virtualenv` and activate it:
```
virtualenv venv && source venv/bin/activate
```

- Install requirements:
```
pip install -r requirements.txt
```

- Migrate database:
```
python manage.py migrate
```

- Run project:
```
python manage.py runserver
