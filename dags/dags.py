from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from airflow.operators import EmailOperator
from datetime import datetime, timedelta
default_args = {
        'owner': 'airflow',
        'start_date': datetime(2020, 7, 19),
        'schedule_interval': '@daily',
        }

dag = DAG('edmjnl_crawler11', default_args=default_args, 
schedule_interval='@hourly', catchup=True)

t1 = BashOperator(
    task_id='schedule_edmjnl_crawler',
    bash_command="cd ~/airflow/edmjnl2 && scrapy runspider edmjnl.py -o file.csv -t csv",
    dag=dag) 

#For ^ I prefer: file_'{{ execution_date }}'.csv -t csv"

t2 = BashOperator(
    task_id='schedule_edmjnl_crawler2',
    bash_command="cd ~/airflow/edmjnl2 && scrapy runspider post.py -o file2.csv -t csv",
    dag=dag) 
    
t3 = EmailOperator(
    task_id='schedule_edmjnl_email',
    to='antonysama@gmail.com',
    subject='Edmjnl Email',
    html_content="HTML content",
    files='file.csv',
    dag=dag) 

# For ^ I need something like ["home/antony/airflow/edmjnl/file_'{{ execution_date }}'.csv"] 
    
t1>>t2    
