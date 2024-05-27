FROM apache/airflow:2.9.1

USER root
RUN apt-get update && \
    apt-get install -y --no-install-recommends gcc && \
    apt-get clean

USER airflow

# Cài đặt các thư viện cần thiết cho việc transform CSV và tải lên S3
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt


