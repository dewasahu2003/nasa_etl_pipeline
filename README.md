airflow etl pipeline with postgres and api integration

data from nasa aastronomy picture of da api , 
airflow - scheduling , monitoring , managing workflows

docker to run airflowe and postgres as service, ensuring isolated reproducible environment
we also utilise airflow hooks and operators to handle ETL process efficiently


key compoennts
airflow - 
postgresSQL
nasa api

operations 

Extract - simpleHttpOperator -> make api call to nasa api , json response
Transform - taskflowapi of airflow  using @task decorator-> extract relevant data from json response ,extract relevant data frmo json response like date , title , explanation , url
Load - PostgressHook -> data loaded in db if the table is not present it will be created


to run the project
'start the docker desktop`

install astro cli if not installed 
using winget install -e --id Astronomer.Astro

pip install -r requirements.txt
astro dev start

set connections in airflow UI in admin section
for nasa_api 
and postgres
