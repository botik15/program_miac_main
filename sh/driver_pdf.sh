#!/bin/bash




# полный путь до скрипта
ABSOLUTE_FILENAME=`readlink -e "$0"`
# каталог в котором лежит скрипт
DIRECTORY=`dirname "$ABSOLUTE_FILENAME"`
DIRECTORY=`dirname "$DIRECTORY"`


dpkg --force-all -i $DIRECTORY/files/cups-pdf_2.6.1-22_amd64.deb  $DIRECTORY/files/libpaper-utils_1.1.24+nmu5_amd64.deb  $DIRECTORY/files/printer-driver-cups-pdf_2.6.1-22_amd64.deb

echo -e "\e[1;32m++++++++++++++++++ Установка драйверов для PDF завершена++++++++++++++++++++++++\e[0m"
