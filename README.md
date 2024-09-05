## Building a Knowledge Management System using the Django Framework
Tutorial -> [Click](https://github.com/appleaut/kms/wiki)


----

### Quick Install
```bash
virtualenv venv --python=python3.12.4
cd kms
source ../venv/bin/activate
pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate 
python manage.py runserver localhost:4200
```


### Quick run
```bash
source ../venv/bin/activate
python manage.py runserver localhost:4200
```

### Migration
```bash
python manage.py makemigrations
python manage.py migrate 
```

### Collect Static
```bash
python manage.py collectstatic
```

### Save Package version
```bash
pip freeze > requirements.txt
```