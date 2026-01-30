# استخدام نسخة أحدث ومستقرة تدعم بايثون ونود
FROM node:18-bullseye

# تثبيت بايثون والأدوات اللازمة
RUN apt-get update && apt-get install -y --no-install-recommends \
    python3 \
    python3-pip \
    ffmpeg \
    git \
    && apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# تحديد مسار العمل
WORKDIR /app/

# نسخ الملفات للمجلد
COPY . /app/

# تثبيت مكتبات بايثون وتحديثها
RUN pip3 install --no-cache-dir -U -r requirements.txt

# أمر التشغيل
CMD ["bash", "start"]
