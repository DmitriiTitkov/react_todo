FROM python:3.7


COPY . /app
WORKDIR /app

RUN python3.7 -m pip install pipenv &&\
    pipenv install --system --dev  --deploy --ignore-pipfile

CMD python3.7 todo_react/manage.py runserver