#!/bin/bash




# полный путь до скрипта
ABSOLUTE_FILENAME=`readlink -e "$0"`
# каталог в котором лежит скрипт
DIRECTORY=`dirname "$ABSOLUTE_FILENAME"`
DIRECTORY=`dirname "$DIRECTORY"`



#-------------------------------------------- ssh -------------------------------------

apt-get install ssh -y

echo -e "\e[1;32m++++++++++++++++++ Настройка ssh завершена++++++++++++++++++++++++\e[0m"







#-------------------------------------------- xrdp -------------------------------------

apt-get install xrdp -y

echo -e "\e[1;32m++++++++++++++++++ Настройка XRDP завершена ++++++++++++++++++++++++\e[0m"





#-------------------------------------------- vnc -------------------------------------

apt-get install $DIRECTORY/files/libtelepathy-glib0_0.24.1-1.1_amd64.deb -y
apt-get install $DIRECTORY/files/yad_0.38.2-1_amd64.deb -y

----------- Функция ярлык для автозапуска скрипта -----------
function AutoDesktop () {
    cat /dev/null > /etc/xdg/autostart/autoUser-VNCserver-miac.desktop
    echo "
    [Desktop Entry]
    Name[ru]=autoUser-VNCserver-miac.desktop
    Type=Application
    NoDisplay=false
    Exec=/usr/bin/user-VNCserver-autoconfig.sh
    Hidden=false
    Terminal=false
    StartupNotify=false"> /etc/xdg/autostart/autoUser-VNCserver-miac.desktop

    rm /etc/xdg/autostart/autoUser-VNCsettings-miac.desktop
#     cat /dev/null > /etc/xdg/autostart/autoUser-VNCsettings-miac.desktop
#     echo "
#     [Desktop Entry]
#     Name[ru]=autoUser-VNCserver-miac.desktop
#     Type=Application
#     NoDisplay=false
#     Exec=/usr/bin/user-VNCsettings-autoconfig.sh
#     Hidden=false
#     Terminal=false
#     StartupNotify=false"> /etc/xdg/autostart/autoUser-VNCsettings-miac.desktop

    echo "Для входа по VNC на рабочем столе был создан файл: VNC сервер, когда нужна помощь.desktop"
    }

----------- Функция скрипт для создания автоматически ярлыка на рабочем столе пользователей -----------
function VNCesktop () {
    cat /dev/null > /usr/bin/user-VNCserver-autoconfig.sh
    echo "
#!/bin/bash
# проверка существования каталога
if [ -e \$HOME ]
then
echo \"Каталог \$HOME существует. Проверим наличие файла\"
# проверка существования файла
if [ -e \$HOME/.fly/startmenu/МИАЦ/VNC\ сервер,\ когда\ нужна\ помощь.desktop ]
then
# если файл существует, добавить в него данные
echo \"Файл существует. В него не записаны данные.\"
else
        mkdir \$HOME/.fly/startmenu/МИАЦ
        echo \"
            [Desktop Entry]
            Name=VNC сервер, когда нужна помощь
            Name[ru]=VNC сервер, когда нужна помощь
            Type=Application
            NoDisplay=false
            Exec=/usr/bin/user-VNCsettings-autoconfig.sh
            Icon=virtualbox
            Hidden=false
            Terminal=false
            StartupNotify=fals
        \"> \$HOME/.fly/startmenu/МИАЦ/VNC\ сервер,\ когда\ нужна\ помощь.desktop
fi
else
echo \"Простите, но у вас нет Домашнего каталога\"
fi

# проверка существования каталога
if [ -e \$HOME ]
then
echo \"Каталог \$HOME существует. Проверим наличие файла\"
# проверка существования файла
if [ -e \$HOME/Desktop/VNC\ сервер,\ когда\ нужна\ помощь.desktop ]
then
# если файл существует, добавить в него данные
echo \"Файл существует. В него не записаны данные.\"
else
        #mkdir \$HOME/.fly/startmenu/МИАЦ
        echo \"
            [Desktop Entry]
            Name=VNC сервер, когда нужна помощь
            Name[ru]=VNC сервер, когда нужна помощь
            Type=Application
            NoDisplay=false
            Exec=/usr/bin/user-VNCsettings-autoconfig.sh
            Icon=virtualbox
            Hidden=false
            Terminal=fals
            StartupNotify=fals
        \"> \$HOME/Desktop/VNC\ сервер,\ когда\ нужна\ помощь.desktop
fi
else
echo \"Простите, но у вас нет Домашнего каталога\"
fi
"> /usr/bin/user-VNCserver-autoconfig.sh
chmod +x /usr/bin/user-VNCserver-autoconfig.sh

# echo "Введите пароль для VNC сервера"
# read item
cat /dev/null > /usr/bin/user-VNCsettings-autoconfig.sh
echo "
#!/bin/bash

pkill -f vino-server

item=\`echo \$((1000 + (RANDOM * RANDOM * RANDOM) % 1000))\`
ip=\`hostname -I | awk '{print $1}'\`
echo \"\$item\"
echo \"\$ip\"
gsettings set org.gnome.Vino authentication-methods \"['vnc']\"
gsettings set org.gnome.Vino vnc-password \"\$(echo -n \"\$item\" | base64)\"

 yad     --center --borders=20 \
        --command='echo \"123\"' \
        --title \"VNC server\" \
        --text \"VNC server ЗАПУЩЕН\" \
        --columns 1 --form --no-buttons  \
        --field \"Пароль для входа: \$item\":LBL '' \
        --field \"Ваш IP:  \$ip\":LBL '' \
        --field \"Остановить\"!!\"подсказка\":FBTN 'pkill -f vino-server' & /usr/lib/vino/vino-server
"> /usr/bin/user-VNCsettings-autoconfig.sh
chmod +x /usr/bin/user-VNCsettings-autoconfig.sh
chmod 777 /usr/bin/user-VNCsettings-autoconfig.sh
}


apt-get install vino -y
apt-get install libtelepathy-glib0
sudo apt-get install libglib2.0-bin
#gsettings set org.gnome.Vino authentication-methods "['vnc']"
AutoDesktop
VNCesktop
#echo "Введите пароль для VNC сервера"
#read item
#gsettings set org.gnome.Vino vnc-password "$(echo -n "$item" | base64)"


echo -e "\e[1;32m++++++++++++++++++ Настройка VNC завершена++++++++++++++++++++++++\e[0m"
