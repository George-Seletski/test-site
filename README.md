# README

# My Django Blog

### Content:

- [The purpose of the project](about:blank#the-purpose-of-the-project)
- [Commands](about:blank#commands-to-start-app)
- [Inspiration](about:blank#inspiration)

## The purpose of the project

This is web application for making posts. It is my own blog.

## The map of the project

![test-site-map.drawio.png](README%2088e271b5363a4aa8be73e3e5d861310c/test-site-map.drawio.png)

## Commands to start app

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

## Inspiration

- [ZenBlog Bootstrap Template Demo](https://bootstrapmade.com/demo/ZenBlog/)



## Plans
* Add to post template:
  *  Author Title
  *  Date Title
  *  comments
  
  