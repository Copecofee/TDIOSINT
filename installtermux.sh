#!/bin/bash
#
# install.sh - Install the dependencies for Termux
#
# Made by: Copecofee Lovegood
# Manutention: Copecofee
#
#-----------------------------------------------------------------------------------------------------------------------------------------------------------
# History:
#
#  v1.0 Copecofee:
#    - The Script Was created
#  v1.1  07-18-2022, Copecofee:
#    - Adding comments
#    - Making the script a program
#    - Organazing the code
#
#-----------------------------------------------------------------------------------------------------------------------------------------------------------

pkg update && pkg upgrade
pkg install golang
pip install colorama
chmod -x osintools.py osintoolstermux.py installtermux.sh install.sh
