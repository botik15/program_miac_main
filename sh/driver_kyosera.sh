#!/bin/bash




# полный путь до скрипта
ABSOLUTE_FILENAME=`readlink -e "$0"`
# каталог в котором лежит скрипт
DIRECTORY=`dirname "$ABSOLUTE_FILENAME"`
DIRECTORY=`dirname "$DIRECTORY"`



if [ ! -d /usr/share/cups/model ]; then
sudo mkdir /usr/share/cups/model
fi
if [ ! -d /usr/share/cups/model/Kyocera ]; then
sudo mkdir /usr/share/cups/model/Kyocera
fi
sudo cp $DIRECTORY/files/printers/Kyosera/* /usr/share/cups/model/Kyocera

sudo cp $DIRECTORY/files/printers/Kyosera/rastertokpsl-fixed /usr/lib/cups/filter/rastertokpsl-fixed
if [ -f /usr/lib/cups/filter/rastertokpsl ] && [ -f /usr/share/cups/model/Kyocera/Kyocera_FS-1040GDI.ppd ] && [ -f /usr/share/cups/model/Kyocera/Kyocera_FS-1060DNGDI.ppd ] && [ -f /usr/share/cups/model/Kyocera/Kyocera_FS-1020MFPGDI.ppd ] && [ -f /usr/share/cups/model/Kyocera/Kyocera_FS-1025MFPGDI.ppd ] && [ -f /usr/share/cups/model/Kyocera/Kyocera_FS-1120MFPGDI.ppd ] && [ -f /usr/share/cups/model/Kyocera/Kyocera_FS-1125MFPGDI.ppd ]; then
echo -e $"Драйвера установились"
break
else
echo -e $"Ошибка уставновки"
fi

echo -e "\e[1;32m++++++++++++++++++ Установка драйверов для Kyocera завершена++++++++++++++++++++++++\e[0m"
