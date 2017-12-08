# CloudFormation exercises

A bunch of stacks created to test various cfn functionalities, in particular:

## 1.Autoscaling

In this folder you can find a cfn stack that creates an auto scaling group with 2 instances. Each instance is configure with:
- A PHP page
- One item is added to a DynamoDB table
- The Cloudwatch Agent is installed and configured.
These configuration doesn't make any sense in a real scenario but it's useful for training purposes.
An Application Load Balancer and a DynamoDB table are configured too. Finally, an instance profile is created to allow the autoscaling group instance to get access to Dynamo and CW.

## 2. Customres

In this folder you can find a cfn stack with a custom resource backed by a Lambda function. 
This function gets the parameters from the EC2 Parameter Store and return them to the stack.
The Lambda function is deployed with the Zappa framework.

## 3. lamp_stack

In this folder you can find a cfn stack which deploys a WordPress website on a single EC2 Instance.

## 4. nestedcf

In this folder you can find a nested cfn stacks which deployes a resilient WordPress website in an auto scaling configuration, backed by a RDS MySql database.
The main stack is the **app.yml**

## 5. s3bucket

In this folder you can find a very simple cfn stack that creates a S3 bucket.