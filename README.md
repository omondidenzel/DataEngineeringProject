# Data Pipeline Setup - Apache Airflow, EC2, S3

## Table of Contents
* [Introduction](#Introduction)
* [Technologies](#technologies)
* [Setup](#setup)

## Introduction
My idea about this project is amaizing, To be a good Data Scientist it is important to also know how to fetch your data, before building be it classification, regression e.t.c models

## Technologies
This project is built using 
*Python 3.*+
*Apache Airflow
*AWS (EC2, S3)

## Setup
## Install dependencies refer to file requirement.txt
```
pip3 install -r requirements.txt for mac users 
pip3 install -r requirements.txt for windows users 
```

## Install Apache Airflow 
```
AIRFLOW_VERSION=2.8.1
PYTHON_VERSION="$(python --version | cut -d " " -f 2 | cut -d "." -f 1-2)"
CONSTRAINT_URL="https://raw.githubusercontent.com/apache/airflow/constraints-${AIRFLOW_VERSION}/constraints-${PYTHON_VERSION}.txt"
pip3 install "apache-airflow[postgres,google]==${AIRFLOW_VERSION}" --constraint "${CONSTRAINT_URL}"
```

## Reference 
https://airflow.apache.org/docs/apache-airflow/stable/installation/installing-from-pypi.html