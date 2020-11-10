# Knjiga receptov

Create a virutal environment and activate it:
```
python -m venv venv3
source venv3/bin/activate
```

Install Django:
```
pip install django
```

Go to the `eBabi/` folder, migrate the DB and run the server:
```
cd eBabi/
python manage.py migrate
python manage.py runserver
```

