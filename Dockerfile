FROM python:2-onbuild

RUN pip install Flask

CMD [ "python", "./main.py", "5000" ]
EXPOSE 5000
