FROM python:3.10-slim-bullseye

# تثبيت أدوات النظام الأساسية
RUN apt-get update && apt-get install -y --no-install-recommends \
    ffmpeg \
    git \
    curl \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app/
COPY . /app/

# 1. تحديث أدوات التثبيت الأساسية
RUN pip3 install --no-cache-dir -U pip setuptools wheel

# 2. تثبيت المكتبات الحساسة اللي بتسبب أخطاء (إجباري)
RUN pip3 install --no-cache-dir python-dotenv httpx==0.24.1
RUN pip3 install --no-cache-dir pymongo==3.12.3 motor==2.5.1 pyrogram==2.0.106 tgcrypto

# 3. تثبيت باقي المكتبات من الملف
RUN pip3 install --no-cache-dir -r requirements.txt

# أمر التشغيل
CMD ["bash", "start"]
