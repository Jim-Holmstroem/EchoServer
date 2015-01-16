FROM python:2-onbuild

CMD [ "python", "./main.py", "5000" ]

EXPOSE 80
