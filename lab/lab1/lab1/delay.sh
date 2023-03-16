#!/usr/bin/env bash 

# Tells OS that the script is in bash

echo -n "Min delay: "
cut -d ',' -f 16 $1|sort -n|head -1 ## haed passes as input

echo -n "Max delay: "
cut -d ',' -f 16 $1|sort -n|tail -2

