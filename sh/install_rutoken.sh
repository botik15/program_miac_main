#!/bin/bash



# полный путь до скрипта
ABSOLUTE_FILENAME=`readlink -e "$0"`
# каталог в котором лежит скрипт
DIRECTORY=`dirname "$ABSOLUTE_FILENAME"`
DIRECTORY=`dirname "$DIRECTORY"`

apt-get install libccid pcscd libpcsclite1 pcsc-tools opensc -y
apt-get install $DIRECTORY/files/librtpkcs11ecp_2.7.1.0-1_amd64.deb -y
apt-get install $DIRECTORY/files/libnpRutokenPlugin_4.7.0-1_amd64.deb -y
apt-get install $DIRECTORY/files/IFCPlugin-x86_64.deb

echo -e "\e[1;32m++++++++++++++++++ Настройка Rutoken завершена++++++++++++++++++++++++\e[0m"
