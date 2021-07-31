import socket
from time import sleep

HOST= '0.0.0.0'
PORT = 33312

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))

cmd = raw_input("'list' para listar o conteudo dos arquivos no servidor ou 'upload' para enviar um arquivo ao servidor.\n")

# Comando para listar o conteudo dos arquivos do host.
if cmd == "list":
  s.send("list".encode()) # Envia ao host o comando "list" para que retorne a lista.
  dados = s.recv(2048) # Recebe os dados de arquivos do Servidor.
  print "Lista de musicas do DMU\n"
  print dados.decode(errors="ignore")

# Comando para transferir um arquivo do Cliente para o Servidor.
if cmd == "upload":
  s.send("upload".encode()) # Envia a flag para informar que sera feito uma transferencia de arquivo.
  fpath = raw_input("Informe o caminho do arquivo:\n")
  encontrado = 1 # Flag para verificar se o arquivo especificado pelo usuario foi encontrado.
  if not fpath.endswith(".txt"): # Se nao estiver na extensao .txt, adiciona o .txt
    fpath = fpath + ".txt"
  try: # Tenta abrir o arquivo como um .txt, caso nao encontre, a transferencia e cancelada.
    arq = open(fpath, 'r')
    encontrado = 1
  except IOError:
    encontrado = 0
    print "Arquivo nao encontrado ou formato nao suportado."
  
  if encontrado == 1: # Caso o arquivo tenha sido encontrado, comeca a transferencia
    dirArr = fpath.split("/")
    fname = dirArr[len(dirArr)-1].split(".txt")[0] # Pegando o nome do arquivo para repassar ao servidor.
    s.send(fname.encode()) # Enviando o nome do arquivo ao servidor.
    sleep(0.002) # Espera para que os pacotes do nome do arquivo e os dados do arquivo nao cheguem na ordem errada.
    for i in arq.readlines(): # Comeca a transferir os dados do arquivo, linha por linha
      s.send(i.encode())

    arq.close()
    
s.close()
