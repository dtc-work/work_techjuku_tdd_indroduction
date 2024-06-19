FROM python:3.12-slim

WORKDIR /app

COPY src/bff/ ./

RUN set -x \
 && apt update -y \
 && apt upgrade -y \
 && \
 : "package install" \
 && pip install --upgrade pip \
 && pip install --no-cache-dir --upgrade -r requirements.txt \
 && \
 : "end proccess" \
 && apt-get clean \
 && rm -rf /var/lib/apt/lists/*

EXPOSE 8000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
