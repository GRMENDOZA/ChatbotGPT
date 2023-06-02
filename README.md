Comandos para desplegar el contenedor en Local

Listar las imagenes 
docker images

Construir el proyecto a partir de un Dockerfile
docker build -t grmendoza/app-wa .

Deployar el proyecto en Local
docker run -p 3000:3000 grmendoza/app-wa 

Stop the container
docker stop <container_id>

Remove the container
docker rm <container_id>