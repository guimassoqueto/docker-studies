1. `docker run -it ubuntu bash` baixa e executa o ubuntu em modo interativo  
2. `docker ps -s` mostra todas as aplicacoes em execucao com a coluna adicional de tamanho do container (virtual e real)  
Dentro do terminal do container: `apt-get update`  
3. `docker ps -s` 


### Volumes
1. `docker run -v /home/guilherme/Desktop/pastadocker:/pastadocker -it ubuntu bash`
2. No terminal do container: `cd pastadocker && echo guilherme 1> file.txt`  

Todos os arquivos criados dentro da pastadocker no container serao persistidos no host


### Bind Mount
Faremos a mesma coisa feita em Volumes
1. `docker run -it --mount type=bind,source=/home/guilherme/Desktop/pastadocker,target=/pastadocker ubuntu bash`
2. No terminal do container: `cd pastadocker && echo guilherme 1> file.txt`  

Todos os arquivos criados dentro da pastadocker no container serao persistidos no host


### Volumes Gerenciados pelo Docker
1. `docker volume create meu_volume`
2. `docker run -v meu_volume:/pastadocker -it ubuntu bash` O volume sera criado e administrado pelo docker, em um local seguro livre de eventuais exclusoes do usuario do host  
Para descobrir aonde foi montado o volume:
1. `sudo su`
2. `cd /var/lib/docker/volumes/meu_volume` os arquivos criados no container estarao aqui
Seguindo o padrao de bing mounts e criando um volume automaticamente:
1. `docker run -it --mount type=bind,source=novo_volume,target=/pastadocker ubuntu bash` novo_volume sera criado, confirme no host: `docker volume ls`


### tmpfs
Funciona apenas em linux (host)
1. `docker run -it --tmpfs=/app ubuntu bash`
2. [No terminal do conatiner] `cd /app && echo 123 1> test.txt` os arquivos serao escritos e salvos NA MEMORIA DO CONTAINER e nao serao ligados ao host, e serao perdidos quando pararmos o container  
Seguindo o padrao de bind mounts:
1. `docker run -it --mount type=tmpfs,destination=/app ubuntu bash`