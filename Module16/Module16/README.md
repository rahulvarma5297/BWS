1. Download the zip file.
2. Come to the root folder and run these commands.
pipenv shell
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver 0.0.0.0:8000

3. Now open browser and go to http://localhost:8000
