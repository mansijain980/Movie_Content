## CONTENT UPLOAD AND REVIEW SYSTEM

**This project is a Django-based API system to upload movie data from CSV files, store it in a MySQL database, and provide API endpoints for retrieving, filtering, and sorting movie data.**

#### Features

**CSV Upload: Upload movie data through a CSV file.**
**MySQL Database: Store movie information in a MySQL database.**
**Pagination: API supports pagination of movie data.**
**Filtering: Filter movies by release year and language.**
**Sorting: Sort movies by release date and rating.**
**Django REST Framework: Powered by Django REST Framework for API management.**
**Django Filters: Support for filtering API queries.**


#### Requirements

~~~
Python 3.8+
Django 4.0+
Django REST Framework
Django Filter
MySQL
~~~

## Installation

1. Clone the repository:

   ~~~
   git clone https://github.com/mansijain980/Movie_Content.git
   cd Movie_Content
   ~~~

2. Create a virtual environment and activate it:

   ~~~
   python3 -m venv env
   source env/bin/activate  On Windows use `env\Scripts\activate`
   ~~~

3. Install the required dependencies:

   ~~~
   pip install -r requirements.txt
   ~~~

4. Configure MySQL Database
   Ensure MySQL is installed and running on your machine. Then, create a new MySQL database:

   ~~~
   CREATE DATABASE movie_db;
   ~~~

   Update the DATABASES section in settings.py to configure MySQL:

   ~~~
   DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'movie_db',
        'USER': 'your_username',
        'PASSWORD': 'your_password',
        'HOST': 'localhost',  # Or your MySQL host
        'PORT': '3306',
    }
   ~~~




5. Run migrations to set up the database schema:
   
   ~~~
   python manage.py makemigrations
   python manage.py migrate
   python manage.py createsuperuser
   python manage.py runserver
   ~~~

6.Access the Django admin panel to manage movies:
Navigate to http://127.0.0.1:8000/admin/ and log in using the superuser credentials.

### API Endpoints

**1. Upload CSV File**
```
URL: http://127.0.0.1:8000/movies/upload
```
Method: POST
Description: Upload a CSV file containing movie data.

**Postman Example:**

Set the method to POST.
In the Body, choose form-data.
Add a key called file, set its type to File, and choose a CSV file to upload.

2. View Movies with Pagination, Filtering, and Sorting

```
URL: http://127.0.0.1:8000/movies/movies
```
Method: GET
Description: Get a paginated list of movies, filter by release year and language, and sort by release date or rating.

## Pagination
The MoviePagination class controls pagination:

page_size: Default is 50 movies per page.<br />
page_size_query_param: Allows the client to customize the page size (maximum of 100).<br />
Filtering and Sorting.
Filter by year of release using the release_date query parameter.
Filter by language using the original_language query parameter.
Sort by release date or vote average using the ordering query parameter.

## Error Handling
Invalid CSV format: If the uploaded file is not in CSV format, the API returns an error message.
Invalid date format: The API expects dates to be in YYYY-MM-DD format.

## Below are some screenshots:
![image](https://github.com/user-attachments/assets/e3a61da2-f193-41fe-b8e8-acc1f99d9972)

![image](https://github.com/user-attachments/assets/09a9391a-b89b-4fc7-b993-c66e356146af)

![image](https://github.com/user-attachments/assets/2fe4f6b3-1842-44e4-8d38-e3cb9e89ddb4)

![image](https://github.com/user-attachments/assets/f8155bcc-4cb7-4ff1-aec7-09dc069772ad)



