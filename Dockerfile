FROM python:2.7

RUN pip install Flask

CMD [ "python", "./main.py", "5000" ]
