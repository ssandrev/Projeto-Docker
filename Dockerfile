FROM python:2-slim

LABEL version="2.0.0" description="Aplicacoes de redes para transferencia de arquivos" maintainer="Allpahy Lima <allaphy.lima@dcomp.ufs.br> Andre Souza  <andrevss@dcomp.ufs.br> Paulo Mauricio  <paulo.fernandes@dcomp.ufs.br> Felipe Queiroz Barreto <felipe.barreto@dcomp.ufs.br"


WORKDIR /usr/src

COPY /src .

EXPOSE 12127

CMD [ "python", "./server.py" ]
