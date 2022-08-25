1. Give an image and give it a tag:  
`docker build -t assignment1node:1.0.0 .`
2. Run it:  
`docker run --name nodeserver --rm -p 3000:3000 -d assignment1node:1.0.0`