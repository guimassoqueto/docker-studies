1. `docker build -t volumes:1.0 .`  
2. `docker run --name nodeserver -p 3000:3000 -d --rm volumes:1.0`
3. `docker stop nodeserver`
4. `docker volume ls`

5. Bind Mounts (execute em lugar do comando 2): `docker run --name nodeserver -p 3000:80 -v feedback:/app/feedback -v "/home/guilherme/Desktop/my_repos/docker_u1:/app" -d --rm volumes:1.0.0`

`-v` name volumes
`--rm` the container is removed whenever it is stopped