#!/usr/bin/python3
#identifica_fylesystem_raiz.py
# identifica qual filesystem o disco '/' usa
import subprocess;

# usa do subprocess.run para executar e guardar o resultado do comando df -h, que lista os filesystems e seus locais de montagens
process = subprocess.run(['df', '-h'], stdout=subprocess.PIPE, universal_newlines=True);

saida = process.stdout;
# itera sobre cada linha da saida e separa elas pelos espaços e coloca em uma lista
for linha in saida.splitlines() :
    teste = linha.split(' ')
    # verifica na lista se existe a montagem em /
    if '/' in teste :
        # se sim exibe o filesystem que esta no primeiro indice
        print(teste[0])    


