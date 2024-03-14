#!/bin/bash




# полный путь до скрипта
ABSOLUTE_FILENAME=`readlink -e "$0"`
# каталог в котором лежит скрипт
DIRECTORY=`dirname "$ABSOLUTE_FILENAME"`
DIRECTORY=`dirname "$DIRECTORY"`


echo -e "\e[1;32m++++++++++++++++++ Настройка Brother завершена++++++++++++++++++++++++\e[0m"
