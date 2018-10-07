FROM python:3.7
ADD backend /code/backend
ADD dist /code/dist
ADD app.py /code
ADD do_create.py /code
WORKDIR /code
RUN pip install --upgrade pip
RUN pip install Flask sqlalchemy
RUN python do_create.py
CMD python app.py