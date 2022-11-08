from datetime import datetime
import os
from datetime import datetime
import time

import platform   
import subprocess  

def ping(host):
    # nome txt 
    file = "ping.txt"

    # verifica txt
    arquivo = open(file, 'r')
    conteudo = arquivo.readlines()

    param = '-n' if platform.system().lower()=='windows' else '-c'


    # Building the command. Ex: "ping -c 1 google.com"
    command = ['ping', param, '1', host]
    cmd = subprocess.call(command) == 0
    

    if cmd == True:
        conteudo.append("Conexao ok. " + " | Data: " + datetime.now().strftime("%d/%m/%Y  %H:%M:%S") + '\n')
        arquivo = open(file, 'w')
        arquivo.writelines(conteudo)
        arquivo.close()
        return print("Conexao ok. " + " | Data: " + datetime.now().strftime("%d/%m/%Y %H:%M:%S"))

    else:
        conteudo.append("Conexao desligada. " + " | Data: " + datetime.now().strftime("%d/%m/%Y %H:%M:%S") + '\n')
        arquivo = open(file, 'w')
        arquivo.writelines(conteudo)
        arquivo.close()
        print("Conexao desligada. " + " | Data: " + datetime.now().strftime("%d/%m/%Y %H:%M:%S"))



if __name__ == "__main__":
    while True:
        #coloque o site que  deseja ficar pingando
        ping("www.google.com.br")
        time.sleep(5)