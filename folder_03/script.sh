#!/bin/bash

# Nome do diretório do ambiente virtual
ENV_NAME="virtualenviroment"

# Verifica se o diretório existe
if [ -d "$ENV_NAME" ]; then
    echo "The virtual environment '$ENV_NAME' already exists. Deleting..."
    rm -rf "$ENV_NAME"
    echo "Virtual environment sucessfully removed."
else
    echo "The virtual environment '$ENV_NAME' does not exist."
fi

# Cria um novo ambiente virtual
echo "Setting up a new virtual environment '$ENV_NAME'..."
python3 -m venv "$ENV_NAME"
source "$ENV_NAME"/bin/activate

# Instalation
pip install scapy

# Verifica se a criação foi bem-sucedida
if [ $? -eq 0 ]; then
    echo "The virtual environment '$ENV_NAME' were sucessfully created!"
else
    echo "Error during the creation of '$ENV_NAME'."
    exit 1
fi
