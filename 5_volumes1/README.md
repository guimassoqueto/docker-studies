1. `docker build -t ubuntu .`
2. `docker run --rm -it -v $(pwd)/files:/files ubuntu bash`

Open the files folder inside the docker and edit the files, the changes will persist in your host machine