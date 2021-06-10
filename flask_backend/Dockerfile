FROM python:3.7

WORKDIR /app
COPY . .

RUN python3 -m pip install -r requirements.txt

ENTRYPOINT [ "python3" ]
CMD [ "app.py" ]