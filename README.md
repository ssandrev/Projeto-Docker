# 20202_labt3-duck-container
20202_labt3-duck-container created by GitHub Classroom

## Alunos:
* Allaphy Lima - 201700017143
* André Vitor Santana Souza - 201700099793
* Felipe Queiroz Barreto - 201700017813
* Paulo Mauricio Dourado Fernandes - 201700100482

## Relatório:


### Configuração do Docker:
* Baixar arquivos
  * git clone https://github.com/DCOMP-UFS/20202_labt3-duck-container.git
* Criar a imagem
  * docker build -t  duckContainer `{diretorio do arquivo Dockerfile}`
* Criar Container com a imagem
  * docker run -d -p 33312:33312 -it --rm --name duckduck duckContainer
* Testar o servidor 
  * docker ps (para verificar que o container está ativo)
  * cd src (para entrar no diretório do arquivo client.py)
  * python client.py 

### Modelo de Proposta de Protocolo:

* Descrição:
>Nesta aplicação, diversos clientes podem mandar arquivos de texto com algumas informações relacionadas a suas atividades do DMU para o servidor guarda-las e mostrar esses arquivos caso solicitado.

* Protocolo de transporte: **TCP**

* Número da porta: 33312

* Formato da mensagem:

  * A transferencia é feita do cliente para o servidor
  * Os arquivos a serem transferidos devem estar no formato .txt
  * Cada arquivo deve conter um tamanho máximo de 2048 bytes
  * Só poderá ser enviado um arquivo por vez
  * Os arquivos no servidor são separados pelo endereço de ip do cliente
  * Os arquivos no servidor estão dispostos no diretório "/home/ipv6br/host/dmu"
  * comandos do cliente:
>`list` - Listar o conteúdo dos arquivos que estão no servidor.

>`upload` - Fazer o envio de um arquivo para o servidor. Informe o caminho do arquivo quando solicitado.


`OBS` É preferivel que os arquivos de testes sigam o modelo a seguir:
```
Aluno: Nome do aluno
Musica: Nome da musica
Link: Link da musica
```
 
 ### Verificando a Aplicação:
 
 * retorne ao diretório raiz
 * use cd ./home/ipv6br/host/dmu para acessar o diretório do servidor
 * use dir para verificar as pastas de cada cliente
 * entre na pasta para verificar os arquivos guardados no servidor diretamente
 
 `OBS` caso o mesmo cliente envie arquivos com nomes iguais, o mesmo é sobrescrito
