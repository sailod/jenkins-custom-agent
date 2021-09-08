In order for the pipeline in this project to run, 

you first need to build the docker image:
docker build -t docker-registry-1630870070.default:30000/custom_python:v1

push to a private registry, I used https://artifacthub.io/packages/helm/twuni/docker-registry:
docker push docker-registry-1630870070.default:30000/custom_python:v1
