FROM python:3.10-slim-bullseye

RUN apt-get update && apt-get install -y --no-install-recommends \
    ffmpeg \
    git \
    curl \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app/
COPY . /app/

# تحديث أدوات التثبيت
RUN pip3 install --no-cache-dir -U pip setuptools wheel

# تثبيت المكتبات اللي كان فيها خناقة يدوياً بإصدار حديث
RUN pip3 install --no-cache-dir httpx==0.24.1
RUN pip3 install --no-cache-dir pymongo==3.12.3 motor==2.5.1 pyrogram==2.0.106

# تثبيت باقي الملف مع تجاهل أي خطأ بسيط يوقف الـ Build
RUN pip3 install --no-cache-dir -r requirements.txt || true

CMD ["bash", "start"]
