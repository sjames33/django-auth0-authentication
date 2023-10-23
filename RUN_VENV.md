
Run venv for this project: 

In: .../vagrant/django-auth0-authentication/


---------------------------------

In: .../vagrant/django-auth0-authentication/

python3 -m venv venv

source ./venv/bin/activate

pip install -r requirements.txt

deactivate

---------------------------------

git init

git add .

git commit -m "comment here"

git remote add origin https://github.com/sjames33/django-auth0-authentication.git

git branch -M main   (renames default branch to main)

git push -u origin main

---------------------------------

python manage.py migrate

python manage.py runserver 3000
