### Steps to start the project:
Create virtual environment;
Run commands:
1. pip install -r requirements.txt
2. python manage.py migrate
3. python manage.py runserver

#### Instructions for API:
We have the URL '/ contacts /', and we can send requests to receive all contacts, create new ones and updates.

To get all contacts, you must send a GET request. 
To create a POST with the necessary for our model. 
To update a PUT using the URL in the URL (example: /contact/1/) and the fields in the body you want to change. 