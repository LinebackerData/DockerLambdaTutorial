#!/bin/bash
# aws sts get-caller-identity
# export AWS_ACCOUNT_NUMBER=<insert account number here>
aws ecr create-repository --repository-name hello-pandas || echo "repo already exists"
aws ecr get-login-password --region us-east-1 | docker login --username AWS --password-stdin ${AWS_ACCOUNT_NUMBER}.dkr.ecr.us-east-1.amazonaws.com

docker build -t hello-pandas .
docker tag hello-pandas:latest ${AWS_ACCOUNT_NUMBER}.dkr.ecr.us-east-1.amazonaws.com/hello-pandas:latest

docker push ${AWS_ACCOUNT_NUMBER}.dkr.ecr.us-east-1.amazonaws.com/hello-pandas:latest

# update the lambda

aws lambda update-function-code --function-name hello-pandas --image-uri ${AWS_ACCOUNT_NUMBER}.dkr.ecr.us-east-1.amazonaws.com/hello-pandas:latest

# optional wait (but idea before any invokes)
aws lambda wait function-updated --function-name hello-pandas


echo "Lambda Updated"