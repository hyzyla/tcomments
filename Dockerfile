FROM python:3.7.2

# We copy just the requirements.txt first to leverage Docker cache
COPY ./requirements/base.txt /work/requirements/base.txt

WORKDIR /work

RUN pip install -r /work/requirements/base.txt

COPY . /work

