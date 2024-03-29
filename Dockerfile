FROM tiangolo/uvicorn-gunicorn-fastapi:python3.7

COPY ./requirements.txt .

RUN pip install -r requirements.txt

COPY . .

ENV PORT=8000

EXPOSE 8000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]