FROM python:3
# Set environment varibles
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code
ADD requirements.txt /code/
# Install dependencies
RUN pip install --upgrade pip
RUN pip install pipenv
COPY ./Pipfile /code/Pipfile
RUN pipenv install --deploy --system --skip-lock --dev
RUN pip install -r requirements.txt
# Add the project
ADD . /code/