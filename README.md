# My Django Blog

### Content:
<ul>
<li>
<a href="#the-purpose-of-the-project">The purpose of the project</a>
</li>
<li>
    <a href="#commands-to-start-app">Commands</a>
</li>
</ul>

<br>

## The purpose of the project
<hr>
This is web application for making posts. It is my own blog. 

<br>

## The map of the project
<hr>
<img href="https://drive.google.com/file/d/1nAIeMgdsZghB_Y5q1EIK03ScvVSImi7b/view?usp=sharing"></img>
<br>

## Commands to start app
<hr>

```
.\venv\Scripts\activate
```

```
cd website
```
```
python manage.py runserver
```
```
python manage.py startapp news
```

```
python manage.py shell

from news.models import News

from django.db import connection
```