## Install Virtual Environment
```As both Flask works with Python Its better to create a Virtual Environment.
- virtualenv <envname> --python=python3
    - type this command to create a virtual environment, where envname can be any name chosen by user.
- To Activate Virtual Environment
    - source envname/bin/activate
- To Deactivate Virtual Environment
    - deactivate
```

## Instal required libraries from requirements.txt
```Libraries required for working of Flask, all libraries are stored in requirements.txt 
To Install type this command.
- pip install -r requirements.txt    
```


## For running Flask Server
```
Go to flask_backend folder.
    - python app.py
```

## For Api
```
    - Goto Browser/postman and type : http://localhost:5000/
```

## For Docker
```
Go to flask_backend folder.
    - docker-compose up
```