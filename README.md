# backup-py

script feito em python para automatização de backup de arquivos e diretórios.

# como utilizar o Backup.py?

>* 1º - É necessário ter uma máquina com um distribuição linux.
>* 2º - Tenha instalado o na versão 3.x, caso não tenha é necessário instalar o pacote **python3** em sua distribuição.
>* 3º - Configure o arquivo **config.ini** *instruções de configuração logo abaixo*.

# configurando o config.ini

> em **[backupDir]** você irá encontrar o campo **dir=**, na frente dele é só colocar o caminho para onde você deseja que os arquivos de backup sejam direcionados, feito isso você já vai ter configurado o ponto de backup.
> 
> em **[ways]** você irá encontrar o campo **way1=**, nele você irá colocar o caminho do diretório em que o Backup será realizado ou o caminho completo do arquivo, para adicionar mais locais em que você queira realizar backup é śo escrever way+[número em sequência], exemplo = way1, way2, way3, ... , way30 e assim vai.

# comandos de utilização

* 1º - Para fazer backup de *todos os arquivos e diretórios* configurados em [ways] digite: 
~~~console
user@pc:~$ python3 Backup.py -a
~~~

* 2º - Para fazer backup apenas dos *diretórios* configurados em [ways] digite: 
~~~console
user@pc:~$ python3 Backup.py -d
~~~

* 3º - Para fazer backup apenas dos *arquivos* configurados sem levar as pastas junto digite: 
~~~console
user@pc:~$ python3 Backup.py -f
~~~

* 4º - Para fazer backup apenas de um *diretório específico* digite:
~~~console
user@pc:~$ python3 Backup.py -d [CAMINHO DO DIRETÓRIO CONFIGURADO]
~~~

* 5º - Para fazer backup apenas de um *arquivo específico* digite:
~~~console
user@pc:~$ python3 Backup.py -f [CAMINHO DO ARQUIVO CONFIGURADO]
~~~

* 6º - Para visualizar os arquivos e diretórios configurados digite:
~~~console
user@pc:~$ python3 Backup.py
~~~

* 7º - Para ajuda digite:
~~~console
user@pc:~$ python3 Backup.py --help
~~~


