-s3://your-bucket-name/prefix/lamba-emr/SparkProfitCalc.jar (Spark jar file)
-s3://your-bucket-name/prefix/fake_sales_data.csv (Input data file in S3)
-s3://your-bucket-name/prefix/outputs/report_1/ (Output location in S3)

import json
import boto3


client = boto3.client('emr')


def lambda_handler(event, context):
    
    response = client.run_job_flow(
        Name= 'spark_job_cluster',
        LogUri= 's3://your-bucket-name/prefix/logs',
        ReleaseLabel= 'emr-6.0.0',
        Instances={
            'MasterInstanceType': 'm5.xlarge',
            'SlaveInstanceType': 'm5.large',
            'InstanceCount': 1,
            'KeepJobFlowAliveWhenNoSteps': False,
            'TerminationProtected': False,
            'Ec2SubnetId': 'subnet-XXXXXXXXXXXXXX'
        },
        Applications = [ {'Name': 'Spark'} ],
        Configurations = [ 
            { 'Classification': 'spark-hive-site',
              'Properties': { 
                  'hive.metastore.client.factory.class': 'com.amazonaws.glue.catalog.metastore.AWSGlueDataCatalogHiveClientFactory'}
            }
        ],
        VisibleToAllUsers=True,
        JobFlowRole = 'EMRLambda-EMREC2InstanceProfile-XXXXXXXXX',
        ServiceRole = 'EMRLambda-EMRRole-XXXXXXXXX',
        Steps=[
            {
                'Name': 'flow-log-analysis',
                'ActionOnFailure': 'TERMINATE_CLUSTER',
                'HadoopJarStep': {
                        'Jar': 'command-runner.jar',
                        'Args': [
                            'spark-submit',
                            '--deploy-mode', 'cluster',
                            '--executor-memory', '6G',
                            '--num-executors', '1',
                            '--executor-cores', '2',
                            '--class', 'com.aws.emr.ProfitCalc',
                            's3://your-bucket-name/prefix/lamba-emr/SparkProfitCalc.jar',
                            's3://your-bucket-name/prefix/fake_sales_data.csv',
                            's3://your-bucket-name/prefix/outputs/report_1/'
                        ]
                }
            }
        ]
    )