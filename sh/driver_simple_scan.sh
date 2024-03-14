#!/bin/bash




# полный путь до скрипта
ABSOLUTE_FILENAME=`readlink -e "$0"`
# каталог в котором лежит скрипт
DIRECTORY=`dirname "$ABSOLUTE_FILENAME"`
DIRECTORY=`dirname "$DIRECTORY"`

apt-get install simple-scan -y

echo -e "\e[1;32m++++++++++++++++++Настройка simple-scan завершена++++++++++++++++++++++++\e[0m"
