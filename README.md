# DockerLambdaTutorial

## Installation

### Docker
We will follow the instructions below to get docker on the box
https://docs.docker.com/engine/install/ubuntu/#install-using-the-repository

If you want docker without sudo:
https://docs.docker.com/engine/install/linux-postinstall/

### Create a Lambda
https://docs.aws.amazon.com/lambda/latest/dg/images-create.html

## Creating the base dockerfile
Resources:

- Base Instructions: https://docs.aws.amazon.com/lambda/latest/dg/images-create.html
- This is where we find the images: https://gallery.ecr.aws/lambda/python

Based on this, we will create a Dockerfile

Follow instruction for [Create an image from an AWS base image for Lambda
] at https://docs.aws.amazon.com/lambda/latest/dg/images-create.html

## Deploy
https://docs.aws.amazon.com/lambda/latest/dg/configuration-images.html


## Creating a Function
https://docs.aws.amazon.com/lambda/latest/dg/configuration-images.html

## Command List
```
docker build -t hello-pandas .   
ls -l
docker run -p 9000:8080 hello-world 
curl -XPOST "http://localhost:9000/2015-03-31/functions/function/invocations" -d '{}'
docker run -p 9000:8080 hello-pandas
```

Function Creation
```
aws lambda create-function --region sa-east-1 --function-name my-function \
    --package-type Image  \
    --code ImageUri=<ECR Image URI>   \
    --role arn:aws:iam::123456789012:role/lambda-ex 

aws lambda update-function-code --region sa-east-1 --function-name my-function \
    --image-uri <ECR Image URI>   \

```