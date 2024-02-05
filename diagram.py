from diagrams import Diagram, Cluster
from diagrams.aws.compute import EC2
from diagrams.aws.storage import S3
from diagrams.custom import Custom
from diagrams.onprem.workflow import Airflow
from diagrams.programming.language import Python


with Diagram("Data pipeline", show=False):
     api = Custom("API", "api.png")
     python = Python("Python")

     with Cluster("ETL"): 
          pythonETL = [
               EC2("EC2"),Airflow("Airflow")
          ]

     bucket = S3("S3")

     api >> python >> pythonETL >> bucket