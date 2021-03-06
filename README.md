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

## Publish to ECR
```
# Build the image
docker build -t hello-pandas .

# Create repository
aws ecr create-repository --repository-name lambda-container-demo --image-scanning-configuration scanOnPush=true

# Tag it
docker tag lambda-container-demo:latest 123412341234.dkr.ecr.eu-west-1.amazonaws.com/lambda-container-demo:latest

# Login
aws --region eu-west-1 ecr get-login-password | docker login --username AWS --password-stdin 123412341234.dkr.ecr.eu-west-1.amazonaws.com

# Push the image
docker push 123412341234.dkr.ecr.eu-west-1.amazonaws.com/lambda-container-demo:latest
```
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

## FAQ

### Cleanup disk space for docker images
https://docs.docker.com/config/pruning/

## Resources
https://aripalo.com/blog/2020/aws-lambda-container-image-support/