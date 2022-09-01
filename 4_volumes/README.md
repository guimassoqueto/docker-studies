1. `docker build -t volumes:1.0 .`  
2. `docker run --name nodeserver -d --rm -p 3000:3000 -v nodeserver:/app/feedback volumes:1.0`
2. Bind-Mount: `docker run --name nodeserver -d --rm -p 3000:3000 -v nodeserver:/app/feedback -v "/home/guilherme/Desktop/my_repos/docker_u1/4_volumes:/app" -v /app/node_modules volumes:1.0`
3. `docker stop nodeserver`
4. `docker volume ls`

`-v nodeserver:/app/feedback` folders where you want to persist data
`--rm` the container is removed whenever it is stopped