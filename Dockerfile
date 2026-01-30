FROM python:3.10-slim-bullseye

RUN apt-get update && apt-get install -y --no-install-recommends \
    ffmpeg \
    git \
    curl \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app/
COPY . /app/

RUN pip3 install --no-cache-dir -U pip setuptools wheel
RUN pip3 install --no-cache-dir -U pymongo==3.12.3 motor==2.5.1 pyrogram==2.0.106 tgcrypto
RUN pip3 install --no-cache-dir -U -r requirements.txt

CMD ["bash", "start"]
