FROM python:3.9-slim

RUN mkdir -p /usr/src/graph_dir

WORKDIR /usr/src/

COPY requirements.txt serve.py ./

COPY ./graph_dir ./graph_dir

RUN pip install --no-cache-dir -r requirements.txt

CMD ["uvicorn", "serve:app", "--host", "0.0.0.0", "--port", "8000"]