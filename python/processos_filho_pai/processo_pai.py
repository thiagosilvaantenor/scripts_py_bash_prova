#!/usr/bin/python3
# processo_pai.py
# envia um json para outro script python(filho)
import subprocess, json;

filho = subprocess.Popen(["python3", "./python/processos_filho_pai/processo_filho.py"], stdout=subprocess.PIPE, 
            stderr=subprocess.STDOUT, stdin=subprocess.PIPE);
entrada = json.dumps({"aied" : "top",
                       "linux" : "gratuito",
                         "Windows" : "pago"});
output_err = filho.communicate(input=entrada.encode('utf-8'));
print(output_err[0].decode());
