# backup-py

script feito em python para automatização de backup de arquivos e diretórios.

# como utilizar o Backup.py?

* 1º - Tenha instalado o Python 3.x, caso não tenha instaldo instale o pacote **python3**
* 2º - Configure o arquivo **config.ini** *instruções de configuração logo abaixo*

# configurando o config.ini

> em **[backupDir]** você irá encontrar o campo **dir=**, na frente dele é só colocar o caminho para onde você deseja que os arquivos de backup sejam direcionados, feito isso você já vai ter configurado o ponto de backup.
> em **[ways]** você irá encontrar o campo **way1=**, nele você irá colocar o caminho do diretório em que o Backup será realizado ou o caminho completo do arquivo, para adicionar mais locais em que você queira realizar backup é śo escrever way+[número em sequência], exemplo = way1, way2, way3, ... , way30 e assim vai.

# comandos de utilização

* 1º - Para fazer backup de *todos os arquivos* e diretórios configurados em [ways] digite: 
ˋˋˋconsole
user@pc:~$ python3 Backup.py -a
ˋˋˋ

* 2º - Para fazer backup apenas do *diretórios* configurados em [ways] digite: 
ˋˋˋconsole
user@pc:~$ python3 Backup.py -d
ˋˋˋ

* 3º - Para fazer backup apenas do *arquivos* configurados sem levar as pastas junto digite: 
ˋˋˋconsole
user@pc:~$ python3 Backup.py -f
ˋˋˋ

* 4º - Para fazer backup apenas de um *diretório específico* digite:
ˋˋˋconsole
user@pc:~$ python3 Backup.py -d [CAMINHO DO DIRETÓRIO CONFIGURADO]
ˋˋˋ

* 5º - Para fazer backup apenas de um *arquivo específico* digite:
ˋˋˋconsole
user@pc:~$ python3 Backup.py -f [CAMINHO DO ARQUIVO CONFIGURADO]
ˋˋˋ

* 6º - Para visualizar os arquivos e diretórios configurados digite:
ˋˋˋconsole
user@pc:~$ python3 Backup.py
ˋˋˋ

* 7º - Para ajuda digite:
ˋˋˋconsole
user@pc:~$ python3 Backup.py --help
ˋˋˋ


