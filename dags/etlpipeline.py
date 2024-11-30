import json

from airflow import DAG
from airflow.decorators import task
from airflow.providers.http.operators.http import SimpleHttpOperator
from airflow.providers.postgres.hooks.postgres import PostgresHook
from airflow.utils.dates import days_ago

with DAG(dag_id="nasa_apod_dag",start_date=days_ago(1),schedule_interval="@daily",catchup=False) as dag:
    
    #step1: create table if it does not exist
    @task
    def create_table():
        #create table if it does not exist
        postgres_hook = PostgresHook(postgres_connn_id="postgres_default")
        
        #sql query to create the table
        
        table_create_query = """
        CREATE TABLE IF NOT EXISTS nasa_apod (
            id SERIAL PRIMARY KEY,
            title VARCHAR(255),
            date DATE,
            explanation TEXT,
            url TEXT,
            media_type VARCHAR(50)
        );
        """
        #execute the query
        postgres_hook.run(table_create_query)
        
    #step2: extract nasa astronomy picture of the day
    #https://api.nasa.gov/planetary/apod?api_key=uFNfVWn5gPGh1GcMQ8u5diJGBI3h5KdzG9PfUdAe
    extrach_apod= SimpleHttpOperator(
        task_id="extract_apod",
        http_conn_id="nasa_api",  #connection id defined in airflow for nasa api
        endpoint="planetary/apod", #nasa api endpoint for astronomy picture of the day
        method="GET",
        data = {"api_key":"{{conn.nasa_api.extra_dejson.api_key}}"}, #api key from the connection
        response_filter=lambda response: response.json(), ##convert response to json
    )
    
    
    #step3: transform data
    @task
    def transform_data(response):
        apod_data = {
            "title": response.get("title",""),
            "date": response.get("date",""),
            "explanation": response.get("explanation",""),
            "url": response.get("url",""),
            "media_type": response.get("media_type","")
        }
        return apod_data
    
    
    #step4: load data into postgres
    @task
    def load_data(apod_data):
        #connect to postgres
        postgres_hook = PostgresHook(postgres_conn_id="postgres_default")

        #query to insert data into postgres
        insert_query = """
        INSERT INTO nasa_apod (title, date, explanation, url, media_type)
        VALUES (%s, %s, %s, %s, %s)
        """
        #insert data into postgres
        postgres_hook.run(insert_query,parameters=(
            apod_data["title"],
            apod_data["date"],
            apod_data["explanation"],
            apod_data["url"],
            apod_data["media_type"]
        ))
        
    
    
    #step5: verify data via DBviewer
    
    
    #step6: defined task dependencies
    create_table() >> extrach_apod #ensuring table is created before extracting data
    #Extract
    api_response = extrach_apod.output
    #Transform
    transformed_data = transform_data(api_response)
    #Load
    load_data(transformed_data)
    
        
        
        