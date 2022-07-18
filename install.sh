#!/bin/bash
#
# install.sh - Install the dependencies
#
# Made by: Copecofee Lovegood
# Manutention: Copecofee
#
#-----------------------------------------------------------------------------------------------------------------------------------------------------------
# History:
#
#  v1.0 Copecofee:
#    - The Script Was created
#  v1.1  
#    - Adding comments
#    - Making the script a program
#    - Organazing the code
#-----------------------------------------------------------------------------------------------------------------------------------------------------------

apt update
apt install git
pip install colorama
apt install golang-go
chmod -x osintools.py osintoolstermux.py installtermux.sh install.sh
