FROM --platform=linux/amd64 python:3.11

WORKDIR ./url_shortener_api

COPY ./requirements.txt /url_shortener_api/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /url_shortener_api/requirements.txt

COPY ./app /url_shortener_api/app

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "6565"]