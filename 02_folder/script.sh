#!/bin/bash

# Nome do diretório do ambiente virtual
ENV_NAME="virtualenviroment"

# Verifica se o diretório existe
if [ -d "$ENV_NAME" ]; then
    echo "O ambiente virtual '$ENV_NAME' já existe. Excluindo..."
    rm -rf "$ENV_NAME"
    echo "Ambiente virtual removido com sucesso."
else
    echo "O ambiente virtual '$ENV_NAME' não existe."
fi

# Cria um novo ambiente virtual
echo "Criando novo ambiente virtual '$ENV_NAME'..."
python3 -m venv "$ENV_NAME"
./"$ENV_NAME"/bin/activate

# Instalation
pip install scapy

# Verifica se a criação foi bem-sucedida
if [ $? -eq 0 ]; then
    echo "Ambiente virtual '$ENV_NAME' criado com sucesso!"
else
    echo "Erro ao criar o ambiente virtual '$ENV_NAME'."
    exit 1
fi
