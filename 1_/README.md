1. Build the container:  
`docker build -t nodeapp:1.0 .`  
2. Run the container:  
`docker run --name nodeapp -d -p 3000:80`

  
`--rm` remove image after stop it
`--name` name of the image
`-d` run in detach mode
`-p` machineport:containerp