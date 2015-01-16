FROM python:2-onbuild

ENV PORT 5000

CMD python ./main.py $PORT

EXPOSE 5000
