## How to Install it and use it

Install this proyect as a Zip, then unzip it. To run this Django project is neccesary to have installed PostgreSQL. I repit, it's obligatory to use the project. 
<br><br>
Then we dip into settings.py and change the database options, adapting them with our configuration. 
<br>
Now we run the API with the following commands (It's highly recommended to use a virtual environment):

```bash
pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```

Now with this activated and the letters_soup program you'll be able to test the complete experience of this project.
