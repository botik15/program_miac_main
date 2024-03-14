#!/bin/bash



# полный путь до скрипта
ABSOLUTE_FILENAME=`readlink -e "$0"`
# каталог в котором лежит скрипт
DIRECTORY=`dirname "$ABSOLUTE_FILENAME"`
DIRECTORY=`dirname "$DIRECTORY"`



sudo apt-get install conky conky-all -y

         cat /dev/null > /etc/xdg/autostart/conky.desktop
    echo "
[Desktop Entry]
Encoding=UTF-8
Version=0.9.4
Type=Application
Name=conky
Comment=Системный монитор
Exec=conky -p 15
#OnlyShowIn=XFCE;
StartupNotify=false
Terminal=false
Hidden=false"> /etc/xdg/autostart/conky.desktop

    #////

#     #cat /dev/null > /etc/xdg/autostart/conky-settings-miac.desktop
#     echo "
#     [Desktop Entry]
#     Name[ru]=conky-settings-miac.desktop
#     Type=Application
#     NoDisplay=false
#     Exec=/usr/bin/conky-settings-miac.sh
#     Hidden=false
#     Terminal=false
#     StartupNotify=false"> /etc/xdg/autostart/conky-settings-miac.desktop
#
#     cp $DIRECTORY/files/conkyrc /usr/bin/.conkyrc

    cp $DIRECTORY/files/conkyrc /etc/skel/.conkyrc

#     i=`echo $DIRECTORY/files/conkyrc /etc/skel/.conkyrc`
#     find /home/ -maxdepth 1 -type d -exec sh -c "cp $DIRECTORY/files/conkyrc $0/.conkyrc" '{}' \; && rm /home/.conkyrc
   find /home/ -maxdepth 1 -type d -exec sh -c "cp $DIRECTORY/files/conkyrc \$0/.conkyrc" "{}" \; && rm /home/.conkyrc
    #cat /dev/null > /usr/bin/conky-settings-miac.sh
#     echo "
# #!/bin/bash
#
# cp /usr/bin/.conkyrc \$HOME/.conkyrc
# chmod 777 \$HOME/.conkyrc
# "> /usr/bin/conky-settings-miac.sh
# chmod +x /usr/bin/conky-settings-miac.sh
#
# chmod 777 /usr/bin/.conkyrc


echo -e "\e[1;32m++++++++++++++++++ Настройка conky завершена++++++++++++++++++++++++\e[0m"
