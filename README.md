# My Django Blog

<ul>
<li>
<a href="#commands-to-start-app">Commands</a>
</li>
</ul>

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