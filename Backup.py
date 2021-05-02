import configparser
import os
from os.path import isfile, join
from os import listdir, system
import sys
from datetime import datetime
os.system("clear")

"""

ways            : caminhos configurados em [ways] no config.ini
fileFlag        : captura os arquivos configurados em config.ini
FolderFlag      : captura os diretórios configurados em config.ini
NumArguments    : captura o numero de argumentos que o usuario insere
option          : opções de entrada
fileOrFolder    : captura o arquivo
changeForOption : opções de entrada do usuario

"""

ways = []
fileFlag = []
folderFlag = []
numArguments = len(sys.argv)
option = ""
fileOrFolder = ""
changeForOption = ['-a', '-d', '-f', '--help']
    
# função responsável por ler as configurações do config.ini
def ReadIni():
    readLocalBackup = configparser.ConfigParser()
    readFoldersFromBackup = configparser.ConfigParser()
    readLocalBackup.read('config.ini')
    global backupFolder
    backupFolder = readLocalBackup.get('backupDir', 'dir')

    i = 1
    
    while True:
        
        try:
            readFoldersFromBackup.read('config.ini')
            dir = readFoldersFromBackup.get('ways', 'way'+str(i))
        
        except:
            break
        
        ways.append(dir)
        i = i + 1

#função responsável por listar os diretórios e arquivos
def ShowFolders(directories):
    
    print("Você dispõe dos seguintes arquivos e pastas:\n")
    
    for dir in directories:
        
        if os.path.exists(dir):  
            
            try:
                files = [f for f in listdir(dir) if isfile(join(dir,f))]
                print("\033[1;31mEm " + dir + ":\033[0;0m")
                
                for f in files:
                    print("\t↳ " + str(f))
                    fileFlag.append(str(dir) + "/" + str(f))

                print("")
                folderFlag.append(dir)  
            
            except:
                print("\033[1;36m»»»» *FILE* " + dir + "\033[0;0m")
                fileFlag.append(dir)

# função que recebe a pasta ou arquivo que o backup será realizado
def Backup(directories):
    
    for d in directories:
        os.system("cp -r " + d + " " + str(backupFolder))

def VerifyParamsForBackup(option, fileBackupOrFolderBackup):
    
    if fileBackupOrFolderBackup == "":
        
        if option not in changeForOption:
            print("\nISSO É APENAS UMA VISUALIZAÇÃO DOS ARQUIVOS E PASTAS.\n")
        
        elif option == "-a":
            Backup(ways)
            Log("-a", ways)
            print("\nO backup de todos os arquivos e diretórios foram realizados, você pode visualizar esses elementos em : " + "\033[1;33m" + str(backupFolder) + "\033[0;0m\n")
        
        elif option == "-d":
            Backup(folderFlag)
            Log("-d", "")
            print("\nO backup de todos os diretórios foram realizados, você pode visualizar esses elementos em : " + "\033[1;33m" + str(backupFolder) + "\033[0;0m\n")
        
        elif option == "-f":
            Backup(fileFlag)
            Log("-f", "")
            print("\nO backup de todos os arquivos foram realizados, você pode visualizar esses elementos em : " + "\033[1;33m" + str(backupFolder) + "\033[0;0m\n")
        
        elif option == "--help":
            Manual()
    if(option != "" and fileBackupOrFolderBackup != ""):
        
        if option in changeForOption:
            
            if fileBackupOrFolderBackup in fileFlag:
                fileTemp = []
                fileTemp.append(fileBackupOrFolderBackup)
                Backup(fileTemp)
                Log("-f", fileBackupOrFolderBackup)
                print("\nO backup de " + "\033[1;33m" + str(fileBackupOrFolderBackup) + "\033[0;0m" + " foi realizado, você pode visualizar esse arquivo em : " + "\033[1;33m" + str(backupFolder) + "\033[0;0m\n")
            
            elif fileBackupOrFolderBackup in folderFlag:
                folderTemp = []
                folderTemp.append(fileBackupOrFolderBackup)
                Backup(folderTemp)
                Log("-d", fileBackupOrFolderBackup)
                print("\nO backup de " + "\033[1;33m" + str(fileBackupOrFolderBackup) + "\033[0;0m" + " foi realizado, você pode visualizar essa pasta em : " + "\033[1;33m" + str(backupFolder) + "\033[0;0m\n")
        
        else:
            print("\nO parâmetro escolhido para opção não é válido.\n")

def Log(action, fileOrFolder):
    
    now = datetime.now()
    dateTime = now.strftime("%d/%m/%Y, %H:%M:%S")

    logFile = open('log.txt', 'r')
    contentLog = logFile.readlines()

    if action == "-a":
        contentLog.append("\nFoi realizado o Backup do(s) seguinte(s) elemento(s):\n" + str(ways) + "\nEm: " + str(backupFolder) + "\nData: " + dateTime + "\n")
        logFile = open('log.txt', 'w')
        logFile.writelines(contentLog)
        logFile.close()
    
    if action == "-d":
        
        if fileOrFolder != "":
            contentLog.append("\nFoi realizado o Backup do(s) seguinte(s) elemento(s):\n" + str(fileOrFolder) + "\nEm: " + str(backupFolder) + "\nData: " + dateTime + "\n")
            logFile = open('log.txt', 'w')
            logFile.writelines(contentLog)
            logFile.close()
        
        else:
            contentLog.append("\nFoi realizado o Backup do(s) seguinte(s) elemento(s):\n" + str(folderFlag) + "\nEm: " + str(backupFolder) + "\nData: " + dateTime + "\n")
            logFile = open('log.txt', 'w')
            logFile.writelines(contentLog)
            logFile.close()
    
    if action == "-f":
        
        if fileOrFolder != "":
            contentLog.append("\nFoi realizado o Backup do(s) seguinte(s) elemento(s):\n" + str(fileOrFolder) + "\nEm: " + str(backupFolder) + "\nData: " + dateTime + "\n")
            logFile = open('log.txt', 'w')
            logFile.writelines(contentLog)
            logFile.close()
        
        else:
            contentLog.append("\nFoi realizado o Backup do(s) seguinte(s) elemento(s):\n" + str(fileFlag) + "\nEm: " + str(backupFolder) + "\nData: " + dateTime + "\n")
            logFile = open('log.txt', 'w')
            logFile.writelines(contentLog)
            logFile.close()

def Manual():
    print("\n\t\tInstruções para utilizar os comandos do Backup.py\n")
    print("1º - para visualizar os arquivos e diretórios configurados para backup digite: \033[1;33mBackup.py\033[0;0m")
    print("2º - para realizar o backup de todos os diretórios configurados digite: \033[1;33mBackup.py -d\033[0;0m")
    print("3º - para realizar o backup de todos os arquivos configurados digite: \033[1;33mBackup.py -f\033[0;0m")
    print("4º - para realizar o backup de um diretório específico que foi configurado digite: \033[1;33mBackup.py -d [NOME DO DIRETÓRIO]\033[0;0m")
    print("5º - para realizar o backup de um arquivo específico que foi configurado digite: \033[1;33mBackup.py -f [NOME DO ARQUIVO]\033[0;0m")
    print("6º - para realizar backup de tudo que foi configurado para backup digite: \033[1;33mBackup.py -a\033[0;0m")
    print("6º - para obter ajuda de como utilizar os comandos digite: \033[1;33mBackup.py --help\033[0;0m\n")

ReadIni()
ShowFolders(ways)

if (numArguments > 1):
    
    option = sys.argv[1]
    
    if(option not in changeForOption):
        print("\nO comando escolhido não é valido! digitel Backup.py --help para mais instruções\n")
        exit()
    
    if(numArguments > 2):
        fileOrFolder = sys.argv[2]
    
    if(numArguments > 3):
        print("\nA quantidade de entradas não é válida! digitel Backup.py --help para mais instruções\n")
        sys.exit(1)
    
    if '-' not in option:
        print("\nÉ necessário escolher uma entrada válida\n")
        sys.exit(1)

if str(fileOrFolder) == "":
    VerifyParamsForBackup(option ,"")

else:
    
    if(option == "-a" and fileOrFolder == ""):
        VerifyParamsForBackup(option, fileOrFolder)
    
    elif(option == "-a" and fileOrFolder != ""):
        print("\nNão é possível passar parâmetros para o comando '-a'\n")
    
    elif(option == "-f" and fileOrFolder not in fileFlag):
        
        if(fileOrFolder in folderFlag):
            print("\nO parâmetro escolhido trata-se de um diretório, utilize o comando Backup.py -d " + str(fileOrFolder) + "\n")
        
        else:
            print("\nEsse arquivo não foi configurado para backup ou não existe...\n")
    
    elif(option == "-f" and fileOrFolder in fileFlag):
        VerifyParamsForBackup(option, fileOrFolder)
    
    elif(option == "-d" and fileOrFolder not in folderFlag):
        
        if(fileOrFolder in fileFlag):
            print("\nO parâmetro escolhido trata-se de um arquivo, utilize o comando Backup.py -f " + str(fileOrFolder) + "\n")
        
        else:
            print("\nEsse diretório não foi configurado para backup ou não existe...\n")

    elif(option == "-d" and fileOrFolder in folderFlag):
        VerifyParamsForBackup(option, fileOrFolder)