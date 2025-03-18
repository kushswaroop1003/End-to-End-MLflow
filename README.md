#End to End MLops project including MLflow

## Workflows

update config.yaml
update schema.yaml
update paras.yaml
update the entity
update the configuration manager in src config
update the components
update the pipeline
update the main.py
update the app.py


# How to run?
### STEPS:

Clone the repository

https://github.com/kushswaroop1003/End-to-End-MLflow

### STEP 01- Create a conda environment after opening the repository

```bash
conda create -n mlproj python=3.8 -y
```

```bash
conda activate mlproj
```


### STEP 02- install the requirements
```bash
pip install -r requirements.txt
```


```bash
# Finally run the following command
python app.py
```

Now,
```bash
open up you local host and port
```

## MLflow

[Documentation](https://mlflow.org/docs/latest/index.html)


##### cmd
- mlflow ui

### dagshub
[dagshub](https://dagshub.com/)

MLFLOW_TRACKING_URI = https://dagshub.com/kushswaroop1003/End-to-End-MLflow.mlflow
MLFLOW_TRACKING_USERNAME=kushswaroop1003
MLFLOW_TRACKING_PASSWORD=cfe2e1852c4aecb3bac60d18511c62181631b698
python script.py

Run this to export as env variables:

```bash

export/set MLFLOW_TRACKING_URI = https://dagshub.com/kushswaroop1003/End-to-End-MLflow.mlflow
export/set MLFLOW_TRACKING_USERNAME=kushswaroop1003
export/set MLFLOW_TRACKING_PASSWORD=cfe2e1852c4aecb3bac60d18511c62181631b698



# AWS-CICD-Deployment-with-Github-Actions

## 1. Login to AWS console.

## 2. Create IAM user for deployment

	#with specific access

	1. EC2 access : It is virtual machine

	2. ECR: Elastic Container registry to save your docker image in aws


	#Description: About the deployment

	1. Build docker image of the source code

	2. Push your docker image to ECR

	3. Launch Your EC2 

	4. Pull Your image from ECR in EC2
#Policy:

	1. AmazonEC2ContainerRegistryFullAccess

	2. AmazonEC2FullAccess

	
## 3. Create ECR repo to store/save docker image
    - Save the URI: 484907490540.dkr.ecr.us-east-1.amazonaws.com/mlflow

	5. Lauch your docker image in EC2
