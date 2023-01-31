---
marp: true
theme: default
_class: lead
paginate: true
backgroundColor: #fff
backgroundImage: url('https://marp.app/assets/hero-background.svg')
style: |
  .columns {
    display: grid;
    grid-template-columns: repeat(2, minmax(0, 1fr));
    gap: 1rem;
  }
  .columns-left {
    background: yellow;
  }
  .columns-right {
    background: beige;
  }
---

# **Зачем Python разработчику нужно посмотреть на спецификацию asgi**

---

# Что такое asgi

- WSGI - Web Server Gateway Interface, PEP 333/3333: django, flask, falcon... , gunicorn, uwsgi, …
- ASGI - Asynchronous Server Gateway Interface, кастомная спека созданная разработчиками django: django3.1+, django-ninja, starlette, fastapi, falcon,..., uvicorn, hypercorn, daphne


Главная проблема WSGI - cпека 2003, 2010 года, http 2+, websocket, async py
По ASGI спецификации можно запускать wsgi приложения

---

# Как работать с asgi без фреймворка
<div class="columns">
<div class="columns-left">

## Column 1

Content 1

</div>
<div class="columns-right">

```python
async def app(scope, receive, send):
    """
    Echo the request body back in an HTTP response.
    """
    body = await read_body(receive)
    await send({
        'type': 'http.response.start',
        'status': 200,
        'headers': [
            [b'content-type', b'text/plain'],
        ]
    })
    await send({
        'type': 'http.response.body',
        'body': body,
    })
```

</div>
</div>


