1. `docker login -u <dockerhub_username>`  
2. [Opcional] `docker tag <container_image>:<app_name>:<tag> <new_image_name>:<new_app_name>:<new_tag>` 
3. `docker push <dockerhub_username>/<docker_app_name>:<version>` verifique a imagem esta listada atraves do comando `docker images` [se o push falhar renomeie o nome da imagem, app e tag seguindo o passo 2]
