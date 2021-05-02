import configparser
import os
from os.path import isfile, join
from os import listdir, system
import sys
from datetime import datetime
os.system("clear")

"""

ways            : caminhos configurados em [ways] no config.ini
file_flag        : captura os arquivos configurados em config.ini
folder_flag      : captura os diretórios configurados em config.ini
num_arguments    : captura o numero de argumentos que o usuario insere
option          : opções de entrada
file_or_folder    : captura o arquivo
CHANGE_FOR_OPTION : opções de entrada do usuario

"""

ways = []
file_flag = []
folder_flag = []
num_arguments = len(sys.argv)
option = ""
file_or_folder = ""

CHANGE_FOR_OPTION = ["-a", "-d", "-f", "--help"]
LOGS_FILE = "logs.log"
INI_CONFIG_FILE = "config.ini"


def read_ini_file():
    """Função responsável por ler as configurações do config.ini"""

    read_local_backup = configparser.ConfigParser()
    read_folders_from_backup = configparser.ConfigParser()
    read_local_backup.read(INI_CONFIG_FILE)
    global backup_folder
    backup_folder = read_local_backup.get("backupDir", "dir")

    i = 1

    while True:

        try:
            read_folders_from_backup.read(INI_CONFIG_FILE)
            dir = read_folders_from_backup.get("ways", "way"+str(i))

        except:
            break

        ways.append(dir)
        i = i + 1


def show_folders(directories):
    """Função responsável por listar os diretórios e arquivos"""

    print("Você dispõe dos seguintes arquivos e pastas:\n")

    for dir in directories:

        if os.path.exists(dir):

            try:
                files = [f for f in listdir(dir) if isfile(join(dir, f))]
                print("\033[1;31mEm " + dir + ":\033[0;0m")

                for f in files:
                    print("\t↳ " + str(f))
                    file_flag.append(str(dir) + "/" + str(f))

                print("")
                folder_flag.append(dir)

            except:
                print("\033[1;36m»»»» *FILE* " + dir + "\033[0;0m")
                file_flag.append(dir)


def backup(directories):
    """Função que recebe a pasta ou arquivo que o backup será realizado"""

    for d in directories:
        os.system("cp -r " + d + " " + str(backup_folder))


def verify_params_for_backup(option, file_backup_or_folder_backup):

    if file_backup_or_folder_backup == "":

        if option not in CHANGE_FOR_OPTION:
            print("\nISSO É APENAS UMA VISUALIZAÇÃO DOS ARQUIVOS E PASTAS.\n")

        elif option == "-a":
            backup(ways)
            log("-a", ways)
            print("\nO backup de todos os arquivos e diretórios foram realizados, você pode visualizar esses elementos em : " +
                  "\033[1;33m" + str(backup_folder) + "\033[0;0m\n")

        elif option == "-d":
            backup(folder_flag)
            log("-d", "")
            print("\nO backup de todos os diretórios foram realizados, você pode visualizar esses elementos em : " +
                  "\033[1;33m" + str(backup_folder) + "\033[0;0m\n")

        elif option == "-f":
            backup(file_flag)
            log("-f", "")
            print("\nO backup de todos os arquivos foram realizados, você pode visualizar esses elementos em : " +
                  "\033[1;33m" + str(backup_folder) + "\033[0;0m\n")

        elif option == "--help":
            manual()

    if(option != "" and file_backup_or_folder_backup != ""):

        if option in CHANGE_FOR_OPTION:

            if file_backup_or_folder_backup in file_flag:
                fileTemp = []
                fileTemp.append(file_backup_or_folder_backup)
                backup(fileTemp)
                log("-f", file_backup_or_folder_backup)
                print("\nO backup de " + "\033[1;33m" + str(file_backup_or_folder_backup) + "\033[0;0m" +
                      " foi realizado, você pode visualizar esse arquivo em : " + "\033[1;33m" + str(backup_folder) + "\033[0;0m\n")

            elif file_backup_or_folder_backup in folder_flag:
                folder_temp = []
                folder_temp.append(file_backup_or_folder_backup)
                backup(folder_temp)
                log("-d", file_backup_or_folder_backup)
                print("\nO backup de " + "\033[1;33m" + str(file_backup_or_folder_backup) + "\033[0;0m" +
                      " foi realizado, você pode visualizar essa pasta em : " + "\033[1;33m" + str(backup_folder) + "\033[0;0m\n")

        else:
            print("\nO parâmetro escolhido para opção não é válido.\n")


def log(action, file_or_folder):

    now = datetime.now()
    date_time = now.strftime("%d/%m/%Y, %H:%M:%S")

    log_file = open(LOGS_FILE, "r")
    content_log = log_file.readlines()

    if action == "-a":
        content_log.append("\nFoi realizado o backup do(s) seguinte(s) elemento(s):\n" +
                           str(ways) + "\nEm: " + str(backup_folder) + "\nData: " + date_time + "\n")
        log_file = open(LOGS_FILE, "w")
        log_file.writelines(content_log)
        log_file.close()

    if action == "-d":

        if file_or_folder != "":
            content_log.append("\nFoi realizado o backup do(s) seguinte(s) elemento(s):\n" + str(
                file_or_folder) + "\nEm: " + str(backup_folder) + "\nData: " + date_time + "\n")
            log_file = open(LOGS_FILE, "w")
            log_file.writelines(content_log)
            log_file.close()

        else:
            content_log.append("\nFoi realizado o backup do(s) seguinte(s) elemento(s):\n" + str(
                folder_flag) + "\nEm: " + str(backup_folder) + "\nData: " + date_time + "\n")
            log_file = open(LOGS_FILE, "w")
            log_file.writelines(content_log)
            log_file.close()

    if action == "-f":

        if file_or_folder != "":
            content_log.append("\nFoi realizado o backup do(s) seguinte(s) elemento(s):\n" + str(
                file_or_folder) + "\nEm: " + str(backup_folder) + "\nData: " + date_time + "\n")
            log_file = open(LOGS_FILE, "w")
            log_file.writelines(content_log)
            log_file.close()

        else:
            content_log.append("\nFoi realizado o backup do(s) seguinte(s) elemento(s):\n" + str(
                file_flag) + "\nEm: " + str(backup_folder) + "\nData: " + date_time + "\n")
            log_file = open(LOGS_FILE, "w")
            log_file.writelines(content_log)
            log_file.close()


def manual():
    print("\n\t\tInstruções para utilizar os comandos do backup.py\n")
    print(
        "1º - para visualizar os arquivos e diretórios configurados para backup digite: \033[1;33mbackup.py\033[0;0m")
    print(
        "2º - para realizar o backup de todos os diretórios configurados digite: \033[1;33mbackup.py -d\033[0;0m")
    print(
        "3º - para realizar o backup de todos os arquivos configurados digite: \033[1;33mbackup.py -f\033[0;0m")
    print(
        "4º - para realizar o backup de um diretório específico que foi configurado digite: \033[1;33mbackup.py -d [NOME DO DIRETÓRIO]\033[0;0m")
    print(
        "5º - para realizar o backup de um arquivo específico que foi configurado digite: \033[1;33mbackup.py -f [NOME DO ARQUIVO]\033[0;0m")
    print(
        "6º - para realizar backup de tudo que foi configurado para backup digite: \033[1;33mbackup.py -a\033[0;0m")
    print(
        "6º - para obter ajuda de como utilizar os comandos digite: \033[1;33mbackup.py --help\033[0;0m\n")


# start script
if __name__ == "__main__":

    read_ini_file()
    show_folders(ways)

    if (num_arguments > 1):

        option = sys.argv[1]

        if(option not in CHANGE_FOR_OPTION):
            print(
                "\nO comando escolhido não é valido! digitel backup.py --help para mais instruções\n")
            exit()

        if(num_arguments > 2):
            file_or_folder = sys.argv[2]

        if(num_arguments > 3):
            print(
                "\nA quantidade de entradas não é válida! digitel backup.py --help para mais instruções\n")
            sys.exit(1)

        if "-" not in option:
            print("\nÉ necessário escolher uma entrada válida\n")
            sys.exit(1)

    if str(file_or_folder) == "":
        verify_params_for_backup(option, "")

    else:

        if(option == "-a" and file_or_folder == ""):
            verify_params_for_backup(option, file_or_folder)

        elif(option == "-a" and file_or_folder != ""):
            print("\nNão é possível passar parâmetros para o comando '-a'\n")

        elif(option == "-f" and file_or_folder not in file_flag):

            if(file_or_folder in folder_flag):
                print("\nO parâmetro escolhido trata-se de um diretório, utilize o comando backup.py -d " +
                      str(file_or_folder) + "\n")

            else:
                print(
                    "\nEsse arquivo não foi configurado para backup ou não existe...\n")

        elif(option == "-f" and file_or_folder in file_flag):
            verify_params_for_backup(option, file_or_folder)

        elif(option == "-d" and file_or_folder not in folder_flag):

            if(file_or_folder in file_flag):
                print("\nO parâmetro escolhido trata-se de um arquivo, utilize o comando backup.py -f " +
                      str(file_or_folder) + "\n")

            else:
                print(
                    "\nEsse diretório não foi configurado para backup ou não existe...\n")

        elif(option == "-d" and file_or_folder in folder_flag):
            verify_params_for_backup(option, file_or_folder)
