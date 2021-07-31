import socket
import glob
import os

HOST= '0.0.0.0'
PORT = 33312

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(1)

# Loop para que o servidor fique sempre escutando clientes.
while 1:
	conn, addr = s.accept()

	cmd = conn.recv(512) # Recebe o comando da operacao
	if cmd.decode(errors="ignore") == "list": # Caso o comando seja "list" envia o conteudo de todos os arquivos do servidor.
	  arqs = glob.glob("/home/ipv6br/host/dmu/*/*.txt") # Pega todos os arquivos .txt de todas as pastas no diretorio /hom/ipv6br/host/dmu
	  res = ""
	  # Organiza a listagem em uma string para ser enviada ao cliente.
	  for f in arqs:
	    arq = open(f, 'r')
	    for line in arq.readlines():
	      res = res + line
	    res = res + '\n'
	  res = res + '\nFim.'
	  conn.sendto(res.encode(), addr) # Envia a lista organizada ao cliente.

	if cmd.decode(errors="ignore") == "upload": # Caso o comando seja "upload", comeca a receber os dados enviados pelo cliente.
	  aname = conn.recv(512) # Recebe o nome do arquivo a ser transferido.
	  if aname:
	    path = '/home/ipv6br/host/dmu/' + addr[0] # Diretorio para salvar o arquivo no servidor, sendo uma pasta nomeada pelo ip do cliente, assim nao tera problemas com nomes de arquivos iguais vindos de diferentes clientes.
	    if not os.path.exists(path): # Caso a pasta do ip do cliente nao exista, essa pasta sera criada.
	      os.makedirs(path)

	    arq = open(path + '/' + aname.decode(errors="ignore") + '.txt', 'w') # Cria o arquivo no servidor.
	    while 1: # Loop para receber linha por linha do arquivo em transferencia.
	      dados = conn.recv(2048)
	      if not dados:
	        break
	      arq.write(dados.decode(errors="ignore")) # Escreve os dados no arquivo do servidor.

	    arq.close()

	conn.close()
