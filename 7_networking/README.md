`docker network ls` lista as redes disponiveis  

Redes padrao:  
- Bridge: Permite a comunicacao entre containeres multiplos (resolucao de dns automatica)
- Host: O container usa a mesma interface de rede do host, dessa forma, as portas utilizadas pelo container serao as mesmas do host, nao havendo a necessidade de mapeamento das portas
- None: O container nao possui nenhuma interface de rede vinculada a ele (sem acesso a internet e a outros containeres).

1. `docker network create --driver <bridge | host | none> <nome_da_rede_definida_pelo_usuario>`
2. `docker run --name <nome_do_container_definido_pelo_usuario> --network <nome_da_rede_definido_no_passo_anterior> <imagem>`
3. Crie todos os containeres que se comunicarao entre si utilizando o passo 2**
  
**utilize o driver do tipo bridge para comunicacao entre containeres
