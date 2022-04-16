Build your Docker image with the docker build command. Enter a name for the image. The following example names the image hello-world.

```
docker build -t hello-world .   
```
Start the Docker image with the docker run command. For this example, enter hello-world as the image name.

```
docker run -p 9000:8080 hello-world 
```

(Optional) Test your application locally using the runtime interface emulator. From a new terminal window, post an event to the following endpoint using a curl command:

```
curl -XPOST "http://localhost:9000/2015-03-31/functions/function/invocations" -d '{}'
```