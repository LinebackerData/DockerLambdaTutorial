For 02_hellopandas, we will need BUCKET_NAME to be defined:
```
export BUCKET_NAME=<your_bucket_here>

# create sample data and publish to s3
./create_sample.sh
```

Build your Docker image with the docker build command. Enter a name for the image. The following example names the image hello-pandas.

```
# Build a docker image locally and tag (-t) with "hello-pandas"
docker build -t hello-pandas .   
```
Start the Docker image with the docker run command. For this example, enter hello-pandas as the image name.

```
# Run the "hello-pandas" container as a service and use port 9000 locally to connect to port 8080 on the server
docker run -p 9000:8080 hello-pandas 
```

(Optional) Test your application locally using the runtime interface emulator. From a new terminal window, post an event to the following endpoint using a curl command:

```
# Send a test to post 9000 (it is fowarded on to 8080 inside docker)

export BUCKET_NAME=<your_bucket_here> # if you are in separate terminal

curl -XPOST "http://localhost:9000/2015-03-31/functions/function/invocations" -d "{\"url\": \"s3://${BUCKET_NAME}/test.csv\"}"

# view the output
aws s3 ls $BUCKET_NAME
aws s3 cp s3://$BUCKET_NAME/test_output.csv.gz - | gunzip -c
```

## Publish to ECR
```
# Create repository
aws ecr create-repository --repository-name hello-pandas 

# view account
aws sts get-caller-identity

# steps in the ECR 
https://us-east-1.console.aws.amazon.com/ecr/repositories/private/<AWS ACCOUNT>/hello-pandas?region=us-east-1

# Tag it
export AWS_ACCOUNT_NUMBER=<insert number above>
docker tag hello-pandas:latest ${AWS_ACCOUNT_NUMBER}.dkr.ecr.eu-west-1.amazonaws.com/lambda-container-demo:latest

# Login
aws --region eu-west-1 ecr get-login-password | docker login --username AWS --password-stdin 123412341234.dkr.ecr.eu-west-1.amazonaws.com

# Push the image
docker push 123412341234.dkr.ecr.eu-west-1.amazonaws.com/lambda-container-demo:latest
```