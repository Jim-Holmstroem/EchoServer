FROM python:2-onbuild

CMD [ "python", "./main.py", "80" ]

EXPOSE 80
