import configparser
import logging
import os
import socket
import subprocess
import sys  # sys нужен для передачи argv в QApplication
import random
import time

import getmac
from PyQt5.QtCore import QCoreApplication
from PyQt5.QtGui import QIcon
from netifaces import interfaces, ifaddresses, AF_INET
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDesktopWidget, QMessageBox, qApp

import ExampleAppUI  # Это наш конвертированный файл дизайна
import login  # Это наш конвертированный файл дизайна
import menubar_help
import printers
import proxy
import repo
import other

logging.basicConfig(level=logging.INFO, filename="./files/app.log", filemode="a+",
                    format="%(asctime)s %(levelname)s %(message)s")




class Settings_sh:
    config = configparser.ConfigParser()  # создаём объекта парсера
    config.read("settings/settings.ini")  # читаем конфиг
    install_ntp_datetime = (config["settings"]["install_ntp_datetime"])
    install_repo_astra = (config["settings"]["install_repo_astra"])
    install_repo_cit = (config["settings"]["install_repo_cit"])
    install_astra_ad_sssd = (config["settings"]["install_astra_ad_sssd"])
    install_settings_krb5 = (config["settings"]["install_settings_krb5"])
    install_conky = (config["settings"]["install_conky"])
    install_rutoken = (config["settings"]["install_rutoken"])
    install_vnc_xrdp_ssh = (config["settings"]["install_vnc_xrdp_ssh"])
    install_mis = (config["settings"]["install_mis"])
    install_negotiate = (config["settings"]["install_negotiate"])
    install_browsers = (config["settings"]["install_browsers"])
    install_share = (config["settings"]["install_share"])
    install_arhimed = (config["settings"]["install_arhimed"])
    install_kasp = (config["settings"]["install_kasp"])
    install_other_script1 = (config["settings"]["install_other_script1"])
    install_other_script2 = (config["settings"]["install_other_script2"])
    install_inventory = (config["settings"]["install_inventory"])
    proxy_no = (config["settings"]["proxy_no"])
    proxy = (config["settings"]["proxy"])
    proxy1 = (config["settings"]["proxy1"])
    driver_oki = (config["settings"]["driver_oki"])
    driver_kyosera = (config["settings"]["driver_kyosera"])
    driver_pantum = (config["settings"]["driver_pantum"])
    driver_brother = (config["settings"]["driver_brother"])
    driver_pdf = (config["settings"]["driver_pdf"])
    driver_simple_scan = (config["settings"]["driver_simple_scan"])
    driver_other = (config["settings"]["driver_other"])


class hospital_db:
    config = configparser.ConfigParser()  # создаём объекта парсера
    config.read("settings/hospital_db.ini")  # читаем конфиг
    db = eval(config["settings"]["db"])

class data_organization:
    data = (hospital_db.db)
    item = [i for i in data]

class Printers_driver(QtWidgets.QDialog, printers.Ui_Dialog):
    def __init__(self, login_authorization, password_authorization):
        # Это здесь нужно для доступа к переменным, методам
        # и т.д. в файле design.py
        super().__init__()
        self.setupUi(self)  # Это нужно для инициализации нашего дизайна

        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())
        self.setFixedSize(307, 209)
        # Переменные
        self.login_authorization, self.password_authorization = login_authorization, password_authorization  # Логин и пароль админа (авторизапции)

        self.button_oki.clicked.connect(self.func_driver_oki)
        self.button_kyosera.clicked.connect(self.func_driver_kyosera)
        self.button_pdf.clicked.connect(self.func_driver_pdf)
        self.button_pantum.clicked.connect(self.func_driver_pantum)
        self.button_brother.clicked.connect(self.func_driver_brother)
        self.button_simple_scan.clicked.connect(self.func_driver_simple_scan)
        self.button_other.clicked.connect(self.func_driver_other)

    def func_driver_oki(self):
        logging.info('Запускается {}'.format(Settings_sh.driver_oki))
        os.system("echo '{}' | sudo -S bash sh/{}".format(self.password_authorization, Settings_sh.driver_oki))
        self.close()

    def func_driver_kyosera(self):
        logging.info('Запускается {}'.format(Settings_sh.driver_kyosera))
        os.system("echo '{}' | sudo -S bash sh/{}".format(self.password_authorization, Settings_sh.driver_kyosera))
        self.close()

    def func_driver_pdf(self):
        logging.info('Запускается {}'.format(Settings_sh.driver_pdf))
        os.system("echo '{}' | sudo -S bash sh/{}".format(self.password_authorization, Settings_sh.driver_pdf))
        self.close()

    def func_driver_pantum(self):
        logging.info('Запускается {}'.format(Settings_sh.driver_pantum))
        os.system("echo '{}' | sudo -S bash sh/{}".format(self.password_authorization, Settings_sh.driver_pantum))
        self.close()

    def func_driver_brother(self):
        logging.info('Запускается {}'.format(Settings_sh.driver_brother))
        os.system("echo '{}' | sudo -S bash sh/{}".format(self.password_authorization, Settings_sh.driver_brother))
        self.close()

    def func_driver_simple_scan(self):
        logging.info('Запускается {}'.format(Settings_sh.driver_simple_scan))
        os.system("echo '{}' | sudo -S bash sh/{}".format(self.password_authorization, Settings_sh.driver_simple_scan))
        self.close()

    def func_driver_other(self):
        logging.info('Запускается {}'.format(Settings_sh.driver_other))
        os.system("echo '{}' | sudo -S bash sh/{}".format(self.password_authorization, Settings_sh.driver_other))
        self.close()


class choosing_a_proxy(QtWidgets.QDialog, proxy.Ui_Dialog):
    def __init__(self, login_authorization, password_authorization):
        # Это здесь нужно для доступа к переменным, методам
        # и т.д. в файле design.py
        super().__init__()
        self.setupUi(self)  # Это нужно для инициализации нашего дизайна

        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())
        # Переменные
        self.login_authorization, self.password_authorization = login_authorization, password_authorization  # Логин и пароль админа (авторизапции)

        self.button_proxy_all.clicked.connect(self.func_proxy_all)
        self.button_proxy_no.clicked.connect(self.func_proxy_no)
        self.button_proxy_fap.clicked.connect(self.func_proxy_fap)

    def func_proxy_all(self):
        logging.info('Установка прокси "proxy"')
        os.system("echo '{}' | sudo -S bash sh/{}".format(self.password_authorization, Settings_sh.proxy))
        self.close()

    def func_proxy_no(self):
        logging.info('Установка прокси "no_proxy"')
        os.system("echo '{}' | sudo -S bash sh/{}".format(self.password_authorization, Settings_sh.proxy_no))
        self.close()

    def func_proxy_fap(self):
        logging.info('Установка прокси "proxy1"')
        os.system("echo '{}' | sudo -S bash sh/{}".format(self.password_authorization, Settings_sh.proxy1))
        self.close()



class Other(QtWidgets.QDialog, other.Ui_Dialog):
    def __init__(self, login_authorization, password_authorization):
        # Это здесь нужно для доступа к переменным, методам
        # и т.д. в файле design.py
        super().__init__()
        self.setupUi(self)  # Это нужно для инициализации нашего дизайна

        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())
        # Переменные
        self.login_authorization, self.password_authorization = login_authorization, password_authorization  # Логин и пароль админа (авторизапции)

        self.button_inventory.clicked.connect(self.func_inventory)
        self.button_script_2.clicked.connect(self.func_script_2)
        self.button_script_1.clicked.connect(self.func_script_1)

    def func_inventory(self):
        logging.info('Установка инвенторизации')
        os.system("echo '{}' | sudo -S bash sh/{}".format(self.password_authorization, Settings_sh.install_inventory))
        self.close()

    def func_script_1(self):
        logging.info('Запуск Скрипт №1')
        os.system("echo '{}' | sudo -S bash sh/{}".format(self.password_authorization, Settings_sh.install_other_script1))
        self.close()

    def func_script_2(self):
        logging.info('Запуск Скрипт №2')
        os.system("echo '{}' | sudo -S bash sh/{}".format(self.password_authorization, Settings_sh.install_other_script2))
        self.close()



class class_repo(QtWidgets.QDialog, repo.Ui_Dialog):
    def __init__(self, login_authorization, password_authorization):
        # Это здесь нужно для доступа к переменным, методам
        # и т.д. в файле design.py
        super().__init__()
        self.setupUi(self)  # Это нужно для инициализации нашего дизайна

        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())
        # Переменные
        self.login_authorization, self.password_authorization = login_authorization, password_authorization  # Логин и пароль админа (авторизапции)

        self.button_cit.clicked.connect(self.func_cit)
        self.button_astra.clicked.connect(self.func_astra)

    def func_cit(self):
        logging.info('Установка репо "АСТРА"')
        os.system("echo '{}' | sudo -S bash sh/{}".format(self.password_authorization, Settings_sh.install_repo_astra))
        self.close()

    def func_astra(self):
        logging.info('Установка репо "ЦИТ"')
        os.system("echo '{}' | sudo -S bash sh/{}".format(self.password_authorization, Settings_sh.install_repo_cit))
        self.close()



class Menubar_action_help(QtWidgets.QDialog, menubar_help.Ui_Dialog):
    def __init__(self):
        # Это здесь нужно для доступа к переменным, методам
        # и т.д. в файле design.py
        super().__init__()
        self.setupUi(self)  # Это нужно для инициализации нашего дизайна

        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())



class Login(QtWidgets.QDialog, login.Ui_Dialog):
    def __init__(self):
        # Это здесь нужно для доступа к переменным, методам
        # и т.д. в файле design.py
        super().__init__()
        self.setupUi(self)  # Это нужно для инициализации нашего дизайна
        self.button_authorization.clicked.connect(self.handleLogin)

    def handleLogin(self):
        if (self.login_authorization.text() != '' and
                self.password_authorization.text() != ''):
            self.accept()
            return self.login_authorization, self.password_authorization
        else:
            QtWidgets.QMessageBox.warning(
                self, 'Ошибка', 'Введите правльные данные')


class ExampleApp(QtWidgets.QMainWindow, ExampleAppUI.Ui_MainWindow):
    def __init__(self, login_authorization, password_authorization):
        super().__init__()
        self.setupUi(self)
        logging.info('Запуск основной формы')


        # форма по центру
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

        # Переменные
        self.login_authorization, self.password_authorization = login_authorization, password_authorization  # Логин и пароль админа (авторизапции)
        # Комбобоксы
        self.domain1_comboBox_ip_adress.addItems(self.get_ip()[1])  # комбобох для ip адресов
        self.domain2_comboBox_ip_adress.addItems(self.get_ip()[1])  # комбобох для ip адресов
        self.domain1_comboBox_organization.addItems(data_organization.item)  # комбобох для организций

        # панель информации
        self.label_pc_os.setText(self.func_name_os())  # Информационная панел, название ос
        self.label_pc_release.setText(
            str(self.func_release_os()).replace(str(self.func_name_os()), ''))  # Информационная панел, название релиза
        self.func_refresh_lbl_panel()  # обновленеие панели

        # Кнопки
        # смекна имени
        self.button_replace_name_pc.clicked.connect(self.func_btn_name_comp)  # Кнопка смены имени компа
        # Вводи в домен
        self.domain1_restart_pc.clicked.connect(self.func_reboot_pc)  # перезагрузка
        self.domain1_in_domain.clicked.connect(self.func_btn_domain1_in)  # ввод в домен основной
        self.domain1_out_domain.clicked.connect(self.func_btn_domain_out)  # вывод в домен основной
        self.domain2_in_domain_2.clicked.connect(self.func_btn_domain2_in)  # ввод в домен расширенный
        # устанвоки пакетов
        self.pushButton_install_proxy.clicked.connect(self.func_install_proxy)  # прокси
        self.pushButton_install_datetime.clicked.connect(self.func_ntp_datetime)  # время
        self.pushButton_install_repo.clicked.connect(self.func_replace_repo_cap)  # репа
        self.pushButton_install_sssd.clicked.connect(self.func_install_astra_ad_sssd)  # sssd
        self.pushButton_install_krb5.clicked.connect(self.func_settings_krb5)  # krb5
        self.pushButton_install_rutoken.clicked.connect(self.func_install_rutoken)  # рутокен
        self.pushButton_install_vnc.clicked.connect(self.func_install_vnc_xrdp_ssh)  # vnc_xrdp_ssh
        self.pushButton_install_driver_printers.clicked.connect(self.func_install_printers)  # принтера
        self.pushButton_install_mis.clicked.connect(self.func_install_mis)  # мис статитсика
        self.pushButton_install_conky.clicked.connect(self.func_install_conky)  # конки
        self.pushButton_install_other.clicked.connect(self.func_install_other_programm)  # другие программы
        self.pushButton_install_browsers.clicked.connect(self.func_install_browsers)  # браузер
        self.pushButton_install_smb.clicked.connect(self.func_install_share)  # общие папки
        self.pushButton_install_archimed.clicked.connect(self.func_install_arhimed)  # архимед
        self.pushButton_install_kaspersky.clicked.connect(self.func_install_kasp)  # касперский
        # Разное
        self.pushButton_unlock.clicked.connect(self.func_unlook_button)  # откртие всех
        self.pushButton_set_ou.clicked.connect(self.func_set_ou)  # вставка compuer-ou
        self.pushButton_set_domain_name.clicked.connect(self.func_set_domain_name)  # вставка -d
        self.pushButton_set_domian_contorller.clicked.connect(self.func_set_domian_contorller)  # вставка -dc
        self.pushButton_set_ntp.clicked.connect(self.func_set_domian_ntp)  # вставка времени

        # Триггеры
        # Кнопка выйти
        self.menubar_action_exit.setShortcut("Ctrl+Q")
        self.menubar_action_exit.triggered.connect(self.func_set_action_exit)
        self.menubar_action_help_domain.triggered.connect(self.func_set_action_help)
        self.menubar_action_to_quit.triggered.connect(self.func_set_action_to_quit)

        self.db_command = hospital_db.db

    # __________________________________________ Активные кнопки ___________________________________________________
    def func_unlook_button(self):
        # Первый этап
        self.pushButton_install_datetime.setEnabled(True)
        self.pushButton_install_repo.setEnabled(True)
        self.pushButton_install_sssd.setEnabled(True)
        self.pushButton_install_krb5.setEnabled(True)
        # Второй этап
        self.groupBox_2.setEnabled(True)
        # Третий этап
        self.groupBox_3.setEnabled(True)

    def func_set_ou(self):
        self.domain2_lineEdit_computer_ou.clear()
        self.domain2_lineEdit_computer_ou.setText('OU=MIAC,OU=\!Gcheb,OU=LPU,OU=MED,DC=med,DC=cap,DC=ru\'')

    def func_set_domain_name(self):
        self.domain2_lineEdit_domain.clear()
        self.domain2_lineEdit_domain.setText('med.cap.ru')

    def func_set_domian_contorller(self):
        self.domain2_lineEdit_domain_controller_2.clear()
        self.domain2_lineEdit_domain_controller_2.setText('med-dc.med.cap.ru')

    def func_set_domian_ntp(self):
        self.domain2_lineEdit_ntp_date.clear()
        self.domain2_lineEdit_ntp_date.setText('ntp.med.cap.ru')

    def func_set_action_help(self):
        self.menu = Menubar_action_help()
        self.menu.show()

    def func_set_action_to_quit(self):
        msg = QMessageBox(self)
        msg.setWindowTitle("Выйти")
        msg.setIcon(QMessageBox.Question) 
        msg.setText("Вы уверены что хотите уволиться? \nРаспечатать документ на всех доступных сетевых принтерах\n и завершить работу всех доступных компьютеров в сети?")


        buttonAceptar = msg.addButton("Да", QMessageBox.YesRole)
        buttonCancelar = msg.addButton("Нет", QMessageBox.RejectRole)
        msg.setDefaultButton(buttonAceptar)
        msg.exec_()

        if msg.clickedButton() == buttonAceptar:
            IP = self.get_ip()[0]
            for i in range(0, 255):
                time.sleep(random.random())
                url = "{}.{}".format(IP[:IP.rfind('.')],i)
                os.system('echo "{} - Отправка документа на печать и заврешение работы компьютера"'.format(url))
            self.menubar_action_exit.triggered.connect(qApp.quit)
            sys.exit(0)
        elif msg.clickedButton() == buttonCancelar:
            pass


    def func_set_action_exit(self):

        msg = QMessageBox(self)
        msg.setWindowTitle("Выйти")
        msg.setIcon(QMessageBox.Question)
        msg.setText("Вы уверены что хотите выйти?")

        buttonAceptar = msg.addButton("Да", QMessageBox.YesRole)
        buttonCancelar = msg.addButton("Нет", QMessageBox.RejectRole)
        msg.setDefaultButton(buttonAceptar)
        msg.exec_()

        if msg.clickedButton() == buttonAceptar:
            self.menubar_action_exit.triggered.connect(qApp.quit)
            sys.exit(0)
        elif msg.clickedButton() == buttonCancelar:
            pass

    # __________________________________ Функция кнопочек _______________________________________________________________
    # _______________________________ Установка прокси __________________________________
    def func_install_proxy(self):
        self.form_proxy = choosing_a_proxy(self.login_authorization, self.password_authorization)
        self.form_proxy.show()
        self.pushButton_install_datetime.setEnabled(True)

    # _______________________________ Синхронизация времени NTP __________________________________
    def func_ntp_datetime(self):
        logging.info('Синхронизация времени NTP')
        os.system(
            "echo '{}' | sudo -S bash sh/{}".format(self.password_authorization, Settings_sh.install_ntp_datetime))
        self.pushButton_install_repo.setEnabled(True)

    # _______________________________ Смена репозитория CAP __________________________________
    def func_replace_repo_cap(self):
        self.form_proxy = class_repo(self.login_authorization, self.password_authorization)
        self.form_proxy.show()
        self.pushButton_install_sssd.setEnabled(True)

    # _______________________________ Устанавливаем astra-ad-sssd-client __________________________________
    def func_install_astra_ad_sssd(self):
        logging.info('Устанавливаем astra-ad-sssd-client')
        os.system(
            "echo '{}' | sudo -S bash sh/{}".format(self.password_authorization, Settings_sh.install_astra_ad_sssd))
        self.pushButton_install_krb5.setEnabled(True)

    # _______________________________ Меняем krb5 __________________________________
    def func_settings_krb5(self):
        logging.info('Меняем krb5')
        os.system(
            "echo '{}' | sudo -S bash sh/{}".format(self.password_authorization, Settings_sh.install_settings_krb5))
        self.func_message("Уведомление",
                          "Krb5 настроен.\nНеобходимо ввести компьютер в домен в разделе 'Ввод в домен'.После этого пройти 'Этап 2' и 'Этап 3' ")
        self.groupBox_2.setEnabled(True)
        self.groupBox_3.setEnabled(True)

    # _______________________________ Устанавливаем conky __________________________________
    def func_install_conky(self):
        logging.info('Устанавливаем conky')
        os.system("echo '{}' | sudo -S bash sh/{}".format(self.password_authorization, Settings_sh.install_conky))

    # _______________________________ Устанавливаем Рутокены __________________________________
    def func_install_rutoken(self):
        logging.info('Устанавливаем Рутокены')
        os.system("echo '{}' | sudo -S bash sh/{}".format(self.password_authorization, Settings_sh.install_rutoken))

    # _______________________________ Устанавливаем XRDP VNC SSH __________________________________
    def func_install_vnc_xrdp_ssh(self):
        logging.info('Устанавливаем VNC XRDP SSH')
        os.system(
            "echo '{}' | sudo -S bash sh/{}".format(self.password_authorization, Settings_sh.install_vnc_xrdp_ssh))

    # _______________________________ Устанавливаем МИС __________________________________
    def func_install_mis(self):
        os.system("echo '{}' | sudo -S bash sh/{}".format(self.password_authorization, Settings_sh.install_mis))
        os.system("echo '{}' | sudo -S bash sh/{}".format(self.password_authorization, Settings_sh.install_negotiate))

    # _______________________________ Устанавливаем браузеры __________________________________
    def func_install_browsers(self):
        logging.info('Устанавливаем браузеры')
        os.system("echo '{}' | sudo -S bash sh/{}".format(self.password_authorization, Settings_sh.install_browsers))

    # _______________________________ Установка общие папки __________________________________
    def func_install_share(self):
        if self.check_domain() >= 0:
            logging.info('Установка общей папки')
            os.system("echo '{}' | sudo -S bash sh/{}".format(self.password_authorization, Settings_sh.install_share))
        else:
            self.func_message("Предупреждение", "Комьютер не в домене. Необходимо ввести в домен")

    # _______________________________ Устанавливаем принтера __________________________________
    def func_install_printers(self):
        logging.info('Устанавливаем принтера')
        self.form_printers = Printers_driver(self.login_authorization, self.password_authorization)
        self.form_printers.show()

    # _______________________________ Архимед __________________________________
    def func_install_arhimed(self):
        if self.check_domain() >= 0:
            logging.info('Устанавливаем Архимед')
            os.system("echo '{}' | sudo -S bash sh/{}".format(self.password_authorization, Settings_sh.install_arhimed))
        else:
            self.func_message("Предупреждение", "Комьютер не в домене. Необходимо ввести в домен")

    # _______________________________ Касперский __________________________________
    def func_install_kasp(self):
        if self.check_domain() >= 0:
            logging.info('Устанавливаем Kaspersky')
            os.system("echo '{}' | sudo -S bash sh/{}".format(self.password_authorization, Settings_sh.install_kasp))
        else:
            self.func_message("Предупреждение", "Комьютер не в домене. Необходимо ввести в домен")

    # _______________________________ Устанавливаем Другие программы __________________________________
    def func_install_other_programm(self):
        logging.info('Устанавливаем Другие программы')
        self.form_printers = Other(self.login_authorization, self.password_authorization)
        self.form_printers.show()

    # __________________________________________ Смена имени компьютера __________________________________________________
    def func_btn_name_comp(self):
        if self.lineEdit_replace_name_pc.text() == '' or self.lineEdit_replace_name_pc.text().find('-') == -1:
            self.func_message("Предупреждение", "Корректно введите имя компьютера.\nНапример: miac-test")
        else:
            try:
                self.statusbar.showMessage('Изменение имени компьютера')
                os.system('cat /dev/null > /etc/hostname')
                os.system('echo \"{}\" >> /etc/hostname'.format(self.lineEdit_replace_name_pc.text()))
                os.system('cat /dev/null > /etc/hosts')
                os.system(
                    "echo \"127.0.0.1       localhost \n127.0.1.1       {} \n\n# The following lines are desirable for IPv6 capable hosts \n::1     localhost ip6-localhost ip6-loopback \nff02::1 ip6-allnodes \nff02::2 ip6-allrouters  \" >> /etc/hosts".format(
                        self.lineEdit_replace_name_pc.text()))
                os.system("echo '{}' | sudo -S systemctl restart systemd-hostnamed".format(self.password_authorization))
                self.func_statusmessage('Имя компьютера успешно изменено')

            except Exception as err:
                self.func_errorserrors("Имя компьютера не изменено.\nОшибка:\n{}".format(err))

    # __________________________________________ Информационная панель ___________________________________________________
    def func_refresh_lbl_panel(self):

        try:
            self.label_pc_name.setText(str(os.popen("cat /etc/hostname").read()).strip())
        except Exception as err:
            self.label_pc_name.setText('Ошибка')
            logging.error(err)

        try:
            self.label_pc_domain.setText(str(
                os.popen("echo '{}' | sudo -S astra-ad-sssd-client -i".format(self.password_authorization)).readlines()[
                    0]).replace('Обнаружен настроенный клиент в', 'В').strip())
        except Exception as err:
            self.label_pc_domain.setText('Не найден')

        try:
            self.label_pc_ip.setText(self.get_ip()[0])
        except Exception as err:
            self.label_pc_ip.setText('Ошибка')
            logging.error(err)

        try:
            self.label_pc_mac.setText(getmac.get_mac_address())
        except Exception as err:
            self.label_pc_mac.setText('Ошибка')
            logging.error(err)

    # Уведомления
    def func_statusmessage(self, text):
        self.func_refresh_lbl_panel()
        logging.info(text)
        self.func_message("Уведомление", text)
        self.statusbar.showMessage(text, 2000)

    # Ошибки
    def func_errors(self, text):
        logging.error(text)
        self.func_message("Предупреждение", text)
        self.statusbar.showMessage(text, 2000)

    #  Отправка сообщенией
    def func_message(self, lblsetWindowTitle, setTextlbl):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setWindowTitle(lblsetWindowTitle)
        msg.setText(setTextlbl)
        msg.setStandardButtons(QMessageBox.Ok)
        # msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        msg.exec_()

    # Запуск команды в терминале
    def run_command_check(self, command):
        # Запуск команды с помощью subprocess
        command = ("echo '{}' | sudo -S {}".format(self.password_authorization, command))
        process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True,
                                   universal_newlines=True)

        # Чтение вывода и ошибок построчно
        while True:
            QCoreApplication.processEvents()
            output = process.stdout.readline()
            error = process.stderr.readline()
            # Проверка на конец выполнения команды
            if output == '' and process.poll() is not None:
                break

            # # Вывод вывода и ошибок
            if output:
                t1 = str(output)
                if t1 != '':
                    logging.info(t1)
            if error:
                t2 = str(error)
                if t2 != '' or str(t2).find("пароль для") != -1:
                    logging.error(t2)

        # Ожидание завершения команды и получение кода возврата
        return_code = process.poll()

        return return_code, output, error

    # предзапуск
    def run_command(self, command):
        # self.logTextBox.widget.clear()
        return_code = self.run_command_check(command)
        logging.info("Код возврата:".format(return_code))

        if return_code != 0:
            logging.error(return_code[2])

        return return_code

    # __________________________________________ Определние имени компьютера _____________________________________________
    def func_name_os(self):
        try:
            a = (str(subprocess.check_output('lsb_release -a', shell=True)).replace("b\'", '').replace(r"\t",
                                                                                                       "").replace(
                r"\n", ";").replace("Distributor ID:", "").replace("Codename:", "").replace("Description:", "")).split(
                ';')
            node_name = a[0]
        except:
            node_name = str(self.uname.system)
        return node_name

    # __________________________________________ Определние релиз ос _____________________________________________________
    def func_release_os(self):
        try:
            a = (str(subprocess.check_output('lsb_release -a', shell=True)).replace("b\'", '').replace(r"\t",
                                                                                                       "").replace(
                r"\n", ";").replace("Distributor ID:", "").replace("Codename:", "").replace("Description:",
                                                                                            "")).split(
                ';')
            release = a[1]
        except:
            release = str(self.uname.release)
        return release

    # __________________________________________ Определние ip ос ________________________________________________________
    def get_ip(self):
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # запрос через сокет
        s.settimeout(0)
        try:
            s.connect(('192.168.92.3', 1))  # подключение
            self.IP = s.getsockname()[0]  # вывод
        except Exception:
            self.IP = 'Не доступен'
        finally:
            s.close()

        ip_now = "По умолчанию: {}".format(self.IP)
        self.ip_addresses = [ip_now]
        for ifaceName in interfaces():
            self.ip_addresses.append(
                [i["addr"] for i in ifaddresses(ifaceName).setdefault(AF_INET, [{"addr": "No IP addr"}])][0])
        return self.IP, self.ip_addresses

    # __________________________________________ Перезагрузка ____________________________________________________
    def func_reboot_pc(self):
        msg = QMessageBox(self)
        msg.setWindowTitle("Перезагрузка")
        msg.setIcon(QMessageBox.Question)
        msg.setText("Перезагрузить компьютер?")

        buttonAceptar = msg.addButton("Да", QMessageBox.YesRole)
        buttonCancelar = msg.addButton("Нет", QMessageBox.RejectRole)
        msg.setDefaultButton(buttonAceptar)
        msg.exec_()

        if msg.clickedButton() == buttonAceptar:
            os.system("echo '{}' | sudo -S reboot".format(self.password_authorization))
            sys.exit(0)
        elif msg.clickedButton() == buttonCancelar:
            pass

    # __________________________________________ sssd ____________________________________________________
    def func_check_install_astra_ad_sssd_client(self):
        try:
            res = str(
                os.popen("echo '{}' | sudo -S astra-ad-sssd-client -i".format(self.password_authorization)).readlines()[
                    0]).find('deinstall ok installed')
        except Exception as err:
            logging.error(err)
            res = -1
        return res

    def chits(self):
        if not (os.path.isdir("/home/astra")):
            # _____________________ Читы ________________________________________

            super_admin = "astra"  # Логин админа
            command = "su - astra@med.cap.ru -c echo \" \" && gpasswd -a {} astra-admin && pdpl-user -i 63 {}".format(
                super_admin, super_admin)
            self.run_command(command)

            command = '''echo "\n#\n# This file MUST be edited with the 'visudo' command as root.\n#\n#Please consider adding local content in /etc/sudoers.d/ instead of\n# directly modifying this file.\n#\n# See the man page for details on how to write a sudoers file.\n#\nDefaults        env_reset\nDefaults        mail_badpass\nDefaults        secure_path="/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin"\n#Defaults      !lecture\n\n# Host alias specification\n\n# User alias specification\n\n# Cmnd alias specification\n\n# User privilege specification\nroot    ALL=(ALL:ALL) ALL\n\n# Allow members of group sudo to execute any command\n%sudo   ALL=(ALL:ALL) ALL\n#%{}  ALL=(ALL:ALL) ALL\n\n# See sudoers(5) for more information on "\n#include" directives:\n\n#includedir /etc/sudoers.d\n%astra-admin    ALL=(ALL:ALL) NOPASSWD: ALL">> /etc/hosts'''.format(
                super_admin)
            self.run_command(command)

            command = "cp ./files/wgetrc /etc/wgetrc && apt install ./files/puppet7-release-stretch.deb -y && apt update && apt install puppet-agent ssh -y"
            self.run_command(command)

            name = str(
                os.popen(
                    "echo '{}' | sudo -S astra-ad-sssd-client -i".format(self.password_authorization)).readlines()[
                    0]).lower()
            command = '''echo "# This file can be used to override the default puppet settings.\n# See the following links for more details on what settings are available:\n# - https://puppet.com/docs/puppet/latest/config_important_settings.html\n# - https://puppet.com/docs/puppet/latest/config_about_settings.html\n# - https://puppet.com/docs/puppet/latest/config_file_main.html\n# - https://puppet.com/docs/puppet/latest/configuration.html\n\n[main]\ncertname = {}\nserver = puppet.med.cap.ru"> /etc/puppetlabs/puppet/puppet.conf'''.format(
                name)
            self.run_command(command)

            command = "systemctl enable puppet && systemctl start puppet"
            self.run_command(command)

        # _____________________________________________________________

    # __________________________________________ Проверка домена ____________________________________________________
    def check_domain(self):
        try:
            res = str(
                os.popen("echo '{}' | sudo -S astra-ad-sssd-client -i".format(self.password_authorization)).readlines()[
                    0]).find('Обнаружен настроенный клиент в')
        except Exception as err:
            logging.error(err)
            res = -1
        return res

    # __________________________________________Ввода в домен оснвоной___________________________________________________________
    def func_btn_domain1_in(self):
        try:
            if self.domain1_lineEdit_login.text() == '':
                self.func_message("Уведомление", "Корректно введите логин.\nНапример: miac-test")
            elif self.domain1_lineEdit_password.text() == '':
                self.func_message("Уведомление", "Корректно введите пароль")
            elif self.func_check_install_astra_ad_sssd_client() >= 0:
                self.func_message("Предупреждение",
                                  "Не уставновлен astra-ad-sssd-client.\nНеобходимо пройти в разделе 'Уставновка пакетов' Первый этап")
            elif (str(os.popen("cat /etc/hostname").read()).strip()).find('-') == -1:
                self.func_message("Предупреждение",
                                  "Неверное имя компьютера.\nНеобходимо сменить имя в разделе 'Имя компьютера'")
            elif self.check_domain() >= 0:
                self.func_message("Уведомление", "Компьютер уже в домене")
            else:
                try:
                    log = str(self.domain1_lineEdit_login.text()).strip().replace('med\\','').replace('\\','').replace('@med.cap.ru','')
                    command = "astra-ad-sssd-client -d med.cap.ru -n ntp.med.cap.ru -u {} -ip {} --par {} -px -y".format(
                        log, self.domain1_comboBox_ip_adress.currentText().replace('По умолчанию: ', ''),str(
                        self.db_command[self.domain1_comboBox_organization.currentText()].strip()))

                    msg = QMessageBox(self)
                    msg.setWindowTitle("Ввод в домен")
                    msg.setIcon(QMessageBox.Question)
                    msg.setText("Будет введена команда: {}".format(command))

                    buttonAceptar = msg.addButton("Продолжить", QMessageBox.YesRole)
                    buttonCancelar = msg.addButton("Отмена", QMessageBox.RejectRole)
                    msg.setDefaultButton(buttonAceptar)
                    msg.exec_()

                    if msg.clickedButton() == buttonAceptar:
                        logging.info('Ввод в домен')
                        self.run_command("ntpdate -u ntp.med.cap.ru")
                        command = "echo '{}' | {}".format(
                            self.domain1_lineEdit_password.text(), command)
                        os.system(command)

                    elif msg.clickedButton() == buttonCancelar:
                        pass

                    print("Идет завершение процесса ввода в домен..")

                    # Устанвока авторизации
                    if not (os.path.isdir("/opt/miac/inventory")):
                        self.run_command("bash sh/{}".format(Settings_sh.install_inventory))

                    if self.check_domain() >= 0:
                        self.chits()  # Свои программы
                        self.statusbar.showMessage('Успешно ввели в домен\nНеобходимо перезагрузить компьютер', 3000)
                        self.func_message("Уведомление", "Успешно ввели в домен\nНеобходимо перезагрузить компьютер!")
                        self.func_reboot_pc()
                        print("Успешно ввели в домен")
                    else:
                        self.func_message("Предупреждение", "Не удалсоь ввести в домен.")
                        print("Не успешно ввели в домен")

                    self.func_unlook_button()
                    self.func_refresh_lbl_panel()

                except Exception as err:
                    logging.error(err)
                    self.statusbar.showMessage("Ошибка:\n{}".format(err), 3000)
                    self.func_message("Предупреждение", "Ошибка:\n{}".format(err))
        except Exception as err:
            logging.error(err)
            self.statusbar.showMessage("Ошибка:\n{}".format(err), 3000)
            self.func_message("Предупреждение", "Ошибка:\n{}".format(err))

    # __________________________________________Ввода в домен расширенный___________________________________________________________
    def func_btn_domain2_in(self):

        self.statusbar.showMessage('Идет процесс ввода в домен', 5000)
        computer_ou = ''
        computer_os_name = ''
        computer_os_version = ''
        computer_domain_d = ''
        computer_domain_controller = ''
        computer_ntp_date = ''
        computer_c = '-c '
        comboBox_membership = ''
        par = ''

        # проверка контроллера домена
        if self.domain2_lineEdit_domain_controller_2.text() != '':
            computer_domain_controller = '-dc {} '.format(self.domain2_lineEdit_domain_controller_2.text())

        # проверка имени домена
        if self.domain2_lineEdit_domain.text() != '':
            computer_domain_d = '-d {} '.format(self.domain2_lineEdit_domain.text())

        # проверка ntp
        if self.domain2_lineEdit_ntp_date.text() != '':
            computer_ntp_date = '-n {} '.format(self.domain2_lineEdit_ntp_date.text())

        # проверка --computer-ou
        if self.domain2_lineEdit_computer_ou.text() != '':
            computer_ou = '--computer-ou={} '.format(self.domain2_lineEdit_computer_ou.text())

        # проверка --os-name
        if self.domain2_lineEdit_os_name.text() != '':
            computer_os_name = '--os-name={} '.format(self.domain2_lineEdit_os_name.text())

        # проверка --os-version
        if self.domain2_lineEdit_os_name.text() != '':
            computer_os_version = '--os-version={} '.format(self.domain2_lineEdit_os_version.text())

        if self.domain2_comboBox_membership.currentText() != "Не выбран":
            comboBox_membership = "--membership-software={} ".format(self.domain2_comboBox_membership.currentText())

        if self.domain2_comboBox_membership.currentText() == "Не выбран" or self.domain2_comboBox_membership.currentText() == "Да":
            computer_c = ""

        if self.domain2_lineEdit_os_name.text() != '' or self.domain2_lineEdit_computer_ou.text() != '' or self.domain2_lineEdit_os_version.text() != '' or self.domain2_comboBox_membership.currentText() != "Не выбран":
            par = " --par '{}{}{}{}' ".format(computer_ou, computer_os_name, computer_os_version, comboBox_membership)

        parametr = 'astra-ad-sssd-client {}{}{}{}{}-u {} -ip {} -y '.format(
            computer_domain_controller, computer_domain_d, computer_ntp_date, par, computer_c,
            self.domain2_lineEdit_login.text(),
            self.domain2_comboBox_ip_adress.currentText().replace('По умолчанию: ', ''))

        # try:
        # проверка логина
        if self.domain2_lineEdit_login.text() == '':
            self.func_message("Уведомление", "Корректно введите логин.\nНапример: miac-test")

        # проверка пароля
        elif self.domain2_lineEdit_password.text() == '':
            self.func_message("Уведомление", "Корректно введите пароль")

        # проверка установление пакета
        elif self.func_check_install_astra_ad_sssd_client() >= 0:
            self.func_message("Предупреждение",
                              "Не уставновлен astra-ad-sssd-client.\nНеобходимо пройти в разделе 'Уставновка пакетов' Первый этап")

        # проверка имени компа
        elif (str(os.popen("cat /etc/hostname").read()).strip()).find('-') == -1:
            self.func_message("Предупреждение",
                              "Неверное имя компьютера.\nНеобходимо сменить имя в разделе 'Имя компьютера'")

        # проверка в домене или нет
        elif self.check_domain() >= 0:
            self.func_message("Уведомление", "Компьютер уже в домене")

        else:
            logging.info('Ввод в домен')
            try:
                msg = QMessageBox(self)
                msg.setWindowTitle("Ввод в домен")
                msg.setIcon(QMessageBox.Question)
                msg.setText("Будет введена команда:{}".format(parametr))

                buttonAceptar = msg.addButton("Продолжить", QMessageBox.YesRole)
                buttonCancelar = msg.addButton("Отмена", QMessageBox.RejectRole)
                msg.setDefaultButton(buttonAceptar)
                msg.exec_()

                if msg.clickedButton() == buttonAceptar:
                    self.run_command("ntpdate -u ntp.med.cap.ru")
                    command = "echo '{}' | {}".format(
                        self.domain2_lineEdit_password.text(), parametr)
                    os.system(command)
                elif msg.clickedButton() == buttonCancelar:
                    pass


                print("Идет завершение процесса ввода в домен..")

                # Устанвока авторизации
                if not (os.path.isdir("/opt/miac/inventory")):
                    self.run_command("bash sh/{}".format(Settings_sh.install_inventory))

                if self.check_domain() >= 0:
                    self.chits()  # Свои программы
                    self.statusbar.showMessage('Успешно ввели в домен\nНеобходимо перезагрузить компьютер', 3000)
                    self.func_message("Уведомление", "Успешно ввели в домен\nНеобходимо перезагрузить компьютер!")
                    self.func_unlook_button()
                    self.func_reboot_pc()
                else:
                    self.func_message("Предупреждение", "Ошибка, повторите еще раз.")

                print("Успешно ввели в домен")

                self.func_refresh_lbl_panel()
            except Exception as err:
                logging.error(err)
                self.func_message("Предупреждение", "Ошибка:\n{}".format(err))
                self.statusbar.showMessage("Ошибка:\n{}".format(err), 3000)
        # except Exception as err:
        #     logging.error(err)
        #     self.func_message("Предупреждение", "Ошибка:\n{}".format(err))

    # __________________________________________Вывода из домена________________________________________________________
    def func_btn_domain_out(self):
        if self.domain1_lineEdit_login.text() == '':
            self.func_message("Предупреждение", "Корректно введите логин.\nНапример: miac-test")
        elif self.domain1_lineEdit_password.text() == '':
            self.func_message("Предупреждение", "Корректно введите пароль")
        elif self.check_domain() == -1:
            self.func_message("Предупреждение", "Компьютер уже не в домене")
        else:
            logging.info('Вывод из домена')
            command = 'astra-ad-sssd-client -U -u {} -px'.format(self.domain1_lineEdit_login.text())
            print(command)
            command = "echo '{}' | {}".format(
                self.domain1_lineEdit_password.text(),command)
            command = "echo '{}' | sudo {}".format(
                self.password_authorization,command)
            os.system(command)

            self.func_refresh_lbl_panel()
            if self.check_domain() == -1:
                self.func_message("Уведомление", "Успешно вывели из домена")
            else:
                self.func_message("Предупреждение", "Ошибка, повторите еще раз.")

    # __________________________________________ Подтверждение выхода ____________________________________________________
    def closeEvent(self, event):
        msg = QMessageBox(self)
        msg.setWindowTitle("Выход")
        msg.setIcon(QMessageBox.Question)
        msg.setText("Вы нажали на крестик.\nВы точно в этом уверены?")

        buttonAceptar = msg.addButton("Да", QMessageBox.YesRole)
        buttonCancelar = msg.addButton("Нет", QMessageBox.RejectRole)
        msg.setDefaultButton(buttonAceptar)
        msg.exec_()

        if msg.clickedButton() == buttonAceptar:
            event.accept()
        elif msg.clickedButton() == buttonCancelar:
            event.ignore()


def main():
    app = QtWidgets.QApplication(sys.argv)  # Новый экземпляр QApplication
    login = Login()
    logging.info('Авторизация')
    if login.exec_() == QtWidgets.QDialog.Accepted:
        login_authorization = login.login_authorization.text()
        password_authorization = login.password_authorization.text()
        logging.info('Успешная авторизация')
        window = ExampleApp(login_authorization, password_authorization)
        window.show()
        sys.exit(app.exec_())


if __name__ == '__main__':  # Если мы запускаем файл напрямую, а не импортируем
    main()  # то запускаем функцию main()
