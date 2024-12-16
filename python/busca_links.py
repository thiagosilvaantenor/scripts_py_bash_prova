#!/usr/bin/python3
# python_ex1_.py
# função recursiva para entrar em diretorios (até onde conseguir) e buscar links
import os;
# aponta para o diretorio home

    
def buscaLink(diretorio) :

    # busca o local atual e aponta para ele
    os.chdir(diretorio);
    
    arquivos = os.listdir(diretorio);
    for arq in arquivos :
        if os.path.islink(arq) :
                print("Achei um link : " + arq);
                break;
        elif os.path.isdir(arq):
            novoDir = diretorio + '/' + arq;
            print('Agora apontando para: ' + novoDir);
            buscaLink(novoDir);

    print('Diretorio não contem diretórios ou links')

# Pega o diretório inicial
dir = input('Olá, informe o diretorio inicial, ex: /home : ')
# Formata o input e chama a função
if dir.endswith('/') :
    dir = dir.rstrip('/')
    buscaLink(dir)
else :
    buscaLink(dir);
            


