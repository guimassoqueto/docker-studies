1. `docker run -d -P dockersamples/static-site`  
`-d` roda a aplicacao em background  
`-P` cria um mapeamento automatico de portas  

2. `docker run -d -p 8000:80 dockersamples/static-site`  
`-p porta_maquina:porta_container` mapeia as portas do container com uma porta externa

3. `docker port` mostra todos os mapeamentos de porta em execucao