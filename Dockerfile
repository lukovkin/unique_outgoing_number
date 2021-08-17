FROM python:3.8

WORKDIR /app

EXPOSE 8080

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . /app
ENV PYTHONPATH="/app"

CMD python unique_outgoing_num_bot.py
