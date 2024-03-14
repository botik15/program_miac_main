#!/bin/bash
#Установить часовой пояс
sudo timedatectl set-timezone Europe/Moscow
#Переключение аппаратных часов на локальное время:
sudo timedatectl set-local-rtc 1 --adjust-system-clock
#список бинарников, при наличии которых в системе демон systemd-timesyncd не будет работать
cat /lib/systemd/system/systemd-timesyncd.service.d/disable-with-time-daemon.conf
#Служба systemd-timesyncd
#Включить автоматический запуск службы
sudo timedatectl set-ntp true
#Для использования timesyncd в первую очередь необходимо полностью удалить службы ntp и openntpd (если они были установлены):
sudo apt-get purge ntp -y
sudo apt-get purge openntpd -y
cat /dev/null > /etc/ntp.conf
#Если была установлена служба времени chronyd удалить её:
sudo apt-get purge chrony -y
#После чего запустить службу timesyncd:
sudo systemctl start systemd-timesyncd
#Состояние службы можно проверить командой:
#systemctl status systemd-timesyncd
#`Или командой:
sudo timedatectl status

cat /dev/null > /etc/systemd/timesyncd.conf
echo "
[Time]
NTP=192.168.92.3" >> /etc/systemd/timesyncd.conf

#Включаем службу systemd-timesyncd
sudo systemctl enable --now systemd-timesyncd
#Перезапустить службу timesyncd:
sudo systemctl restart systemd-timesyncd
#проверка доступности сервера времени
sudo ntpdate -d ntp.med.cap.ru
#для принудительной коррекции времени
sudo ntpdate -u ntp.med.cap.ru
#Планировщик задач
cat /dev/null > /usr/bin/crontab.sh
echo "
#!/bin/bash
timedatectl set-timezone Europe/Moscow
ntpdate -u ntp.med.cap.ru
" >> /usr/bin/crontab.sh
chmod +x /usr/bin/crontab.sh

cat /dev/null > /etc/crontab
echo "
    # /etc/crontab: system-wide crontab
# Unlike any other crontab you don\'t have to run the \`crontab'
# command to install the new version when you edit this file
# and files in /etc/cron.d. These files also have username fields,
# that none of the other crontabs do.

SHELL=/bin/sh
PATH=/usr/local/sbin:/usr/local/bin:/sbin:/bin:/usr/sbin:/usr/bin

# m h dom mon dow user  command
17 *    * * *   root    cd / && run-parts --report /etc/cron.hourly
25 6    * * *   root    test -x /usr/sbin/anacron || ( cd / && run-parts --report /etc/cron.daily )
47 6    * * 7   root    test -x /usr/sbin/anacron || ( cd / && run-parts --report /etc/cron.weekly )
52 6    1 * *   root    test -x /usr/sbin/anacron || ( cd / && run-parts --report /etc/cron.monthly )
#

@reboot root /usr/bin/crontab.sh
" >> /etc/crontab

