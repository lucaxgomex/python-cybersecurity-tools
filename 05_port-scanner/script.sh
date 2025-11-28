#!/bin/bash

ENV_NAME="virtualenviroment"

if [ -d "$ENV_NAME" ]; then
    echo "The virtual environment '$ENV_NAME' already exists. Deleting..."
    rm -rfv "$ENV_NAME"
    echo "Virtual environment sucessfully removed."
else
    echo "The virtual environment '$ENV_NAME' does not exist."
fi

echo "Setting up a new virtual environment '$ENV_NAME'..."
python3 -m venv "$ENV_NAME"

source ./$ENV_NAME/bin/activate

# Instalating libraries
pip install scapy
pip install netaddr

if [ $? -eq 0 ]; then
    echo "The virtual environment '$ENV_NAME' were sucessfully created!"
else
    echo "Error during the creation of '$ENV_NAME'."
    exit 1
fi