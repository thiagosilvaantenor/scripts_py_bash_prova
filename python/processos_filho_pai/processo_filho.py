#!/usr/bin/python3
# processo_filho.py
# recebe um json do processo pai e itera todas as keys do json
import json, sys;

dados = sys.stdin.readlines();
processo = json.loads(dados[0].rstrip());

for key in processo.keys() :
    print(key);


