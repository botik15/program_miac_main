#!/bin/bash




# полный путь до скрипта
ABSOLUTE_FILENAME=`readlink -e "$0"`
# каталог в котором лежит скрипт
DIRECTORY=`dirname "$ABSOLUTE_FILENAME"`
DIRECTORY=`dirname "$DIRECTORY"`

dpkg -i $DIRECTORY/files/printers/Pantum/Pantum_Ubuntu_Driver_V1.1.5/pantum-1.1.5-amd64.deb
dpkg -i $DIRECTORY/files/printers/Pantum/Pantum_P3010-P3060-P3300-M6700-M6760-M6800-M6860-M7100-M7200_Series_Ubuntu_Driver_V1.0.19/Pantum-Series-1.0.x86_64.deb
dpkg -i $DIRECTORY/files/printers/Pantum/pantum_1.1.100-1_amd64.deb

echo -e "\e[1;32m++++++++++++++++++ Установка драйверов для Pantum завершена++++++++++++++++++++++++\e[0m"
