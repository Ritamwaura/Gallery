gallery
A personal gallery application that you display your photos for others to see.

Description
The application allows users to view images according to their categories and location. 

##screenshots

BDD Specifications Table
User Requirements	Input	Output
View all images	Go to the home page	All images will be displayed
Search for an image	Input the category name in the search bar	All images in that category will display
View the image details	Click on the image	All the image details will be displayed
Copy image	Click on the copy link button	The image link is copied
Setup/Installation Requirements
Ensure you have Python3.6 installed
Clone the Pixels directory
Create your own virtual environment and activate it using these respective commands:python3.6 -m venv --without-pip virtual && source virtual/bin/activate
Install all the necessary dependencies necessarry for running the application using this command: pip install-r requirements.txt
Create a database: psql then create the databse using this command: CREATE DATABASE gallery
Run migrations using these respective commmands: python3.6 manage.py makemigrations images then: python3.6 manage.py migrate
Run the app using this command: python3.6 manage.py runserver on the terminal.You can then open the app on your browser
Technologies Used
Python 3.6
Django
Bootstrap
HTML
Support and Contact Details
Email : mwaurarita@gmail.com

Licence
Copyrightmwaurarita@gmail.com