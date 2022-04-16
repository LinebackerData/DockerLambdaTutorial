Build your Docker image with the docker build command. Enter a name for the image. The following example names the image hello-world.

```
# Build a docker image locally and tag (-t) with "hello-world"
docker build -t hello-world .   
```
Start the Docker image with the docker run command. For this example, enter hello-world as the image name.

```
# Run the "hello-world" container as a service and use port 9000 locally to connect to port 8080 on the server
docker run -p 9000:8080 hello-world 
```

(Optional) Test your application locally using the runtime interface emulator. From a new terminal window, post an event to the following endpoint using a curl command:

```
# Send a test to post 9000 (it is fowarded on to 8080 inside docker)
curl -XPOST "http://localhost:9000/2015-03-31/functions/function/invocations" -d '{}'
```