## Building a Knowledge Management System using the Django Framework
Tutorial -> [Click](https://github.com/appleaut/kms/wiki)


----

### Quick Install
```
virtualenv venv --python=python3.12.4
cd kms
source ../venv/bin/activate
pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate 
python manage.py runserver localhost:4200
```


### Quick run
```
source ../venv/bin/activate
python manage.py runserver localhost:4200
```

### Migration
```
python manage.py makemigrations
python manage.py migrate 
```

### Collect Static
```
python manage.py collectstatic
```