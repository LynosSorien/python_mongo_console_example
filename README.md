# python_mongo_console_example
An example of MongoDB console using Python3 and Docker-compose

To run it activate the virtual environent
```
source ./venv/bin/activate
```

Be sure to run docker-compose first with the MongoDB image (you need to have Docker installed and running on your machine)

```
docker-compose up -d
```


Then run it using

```
python main.py
```

You can add more fillers inside of main.py to be able to query them on "console" mode


