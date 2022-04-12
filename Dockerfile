FROM python:3.10.4-slim

RUN useradd --create-home --shell /bin/bash analytics

WORKDIR /home/analytics

COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

USER analytics

COPY . .

CMD ["bash"]
