# Web-Calculator Proxy Calculate
## Live Demo
### Welcome Page
>  http://multiply.40216004.qpc.hal.davecutting.uk/
### Multiplication
> http://143.117.208.65:31860/?x=9&y=3
## Code Buiding
### Maven structure
### Testing the Python program
Make sure you have Python3 installed
Make sure you have Python Packages in requirements.txt installed
Make sure you currect working directory is the same as where this README file is
> python3 server.py

## Docker Buiding
### How to build
Mkes sure you are in the same directory as this README file
> docker build -t proxy-app .
### How to run
> docker run -d --name proxy-app-running -p 10000:5000 proxy-app

### Testing
Go to
> http://localhost:10000/ui

### Stopping application
> docker stop proxy-app-running

### Removing container
> docker rm proxy-app-running

### Removing iamge
> docker rmi proxy-app

## Docker registry
### Login
> docker login registry.hal.davecutting.uk

### Build
> docker build -t registry.hal.davecutting.uk/web-calculator-40216004/proxy .

### Push
> docker push registry.hal.davecutting.uk/web-calculator-40216004/proxy

## Deploying to Rancher
### Deploying a workload
Using the following details

Docker Image
> registry.hal.davecutting.uk/web-calculator-40216004/proxy

Publish the container port
> 5000

Protocol
> TCP (As a NodePort)

On listening port
> Random or User defined

### Load Balancing (Hostname mapping)
Request Host
>  proxy-{{INDEX}}.40216004.qpc.hal.davecutting.uk

Target
> proxy

Port
> 5000



