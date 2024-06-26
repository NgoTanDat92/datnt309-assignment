# PROJECT: DATA PIPELINES WITH AIRFLOW
1. Download Top Anime Dataset 2024 on Kaggle and save to local folder
2. Transform Data by Python
3. Upload to AWS S3
## About Dataset
This dataset offers a comprehensive overview of the top animes of 2024, and is useful for building recommendation systems, visualizing trends in anime popularity and score, predicting scores and popularity, and such. The dataset is in CSV format and contains 1000 rows corresponding to 1000 anime. The dataset contains 22 columns. Link download: https://www.kaggle.com/datasets/bhavyadhingra00020/top-anime-dataset-2024
## Transform Data by Python
The dataset contains several columns that need to be modified for data analysis and visualization:
  1. Rename "English" column to "Name" column
  2. Split "Aired" column to "Aired_from" column and "Aired_to" column
  3. Convert "Duration" column to minutes and rename to "Duration (min per ep)"
  4. Modify the "Genres" column by extracting the first half of each genre name
# HOW TO RUN THIS PROJECT
1. Clone this project:
```bash
git clone https://github.com/NgoTanDat92/datnt309-assignment
```
2. In this datnt309-assignment folder, run this command:
```bash
mkdir -p ./dags ./logs ./plugins ./config ./input ./output
echo -e "AIRFLOW_UID=$(id -u)" > .env
```
2. Open dag.py, change the name dest_bucket "datnt309" to your dest_bucket name
```py
upload_task = LocalFilesystemToS3Operator(
    task_id='upload_anime_modified_csv',
    filename=r'/opt/airflow/output/Top_Anime_data_output.csv',
    dest_key='Top_Anime_data_output.csv',
    dest_bucket='datnt309',
    aws_conn_id='aws_connection',
    replace=True,
    dag=dag,
)
```
4. Build and start all services of airflow on Docker
```bash
docker compose up
```
5. Navigate to http://localhost:8080/home and login with username: airflow and password: airflow
```bash
_AIRFLOW_WWW_USER_USERNAME: ${_AIRFLOW_WWW_USER_USERNAME:-airflow}
_AIRFLOW_WWW_USER_PASSWORD: ${_AIRFLOW_WWW_USER_PASSWORD:-airflow}
```
6. Set connection to AWS S3
![image alt text](<Connection.PNG>)
- AWS Access Key ID = <your_AWS_Access_Key_ID>
- AWS Secret Access Key = <your_AWS_Secret_Access_Key>
- Extra = <your_AWS_session_token>
7. Run "etl_anime_data" dag name and see the file ouput in your AWS S3






