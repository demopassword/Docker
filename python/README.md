## run command
```
gunicorn --bind 0.0.0.0:8080 app:app
```

etc
```
["flask", "run", "host=0.0.0.0", "port=80"]
["python3", "-m", "flask", "run", "--host=0.0.0.0", "--port=80"]
```