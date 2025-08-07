FROM python:3.11-slim

# Установим зависимости: mysql-client и другие системные пакеты
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        default-mysql-client \
        build-essential \
        libpq-dev \
        netcat-openbsd \
        curl \
        pkg-config \
        libmariadb-dev \
    && apt-get clean && rm -rf /var/lib/apt/lists/*

# Установка зависимостей Python
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Копируем проект
COPY . .

# Команда по умолчанию
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
