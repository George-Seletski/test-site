# My Django Blog

<ul>
<li>[Commands](#commands-to-start-app)</li>
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