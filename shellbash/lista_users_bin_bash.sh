#!/bin/bash
# lista_users_bin_bash
# vai listar os usuários que tem o shell padrão em /bin/bash

declare listagem
# utilizando a crase para usar comandos do terminal
# um cat para ler o arquivo, um grep para filtrar o shell
# e um awk para exibir apenas a primeira coluna que contem os usuários
listagem=`cat /etc/passwd | grep /bin/bash | awk -F':' '{print $1}'`

echo $listagem

