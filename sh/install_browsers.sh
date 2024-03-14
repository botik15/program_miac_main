#!/bin/bash



# полный путь до скрипта
ABSOLUTE_FILENAME=`readlink -e "$0"`
# каталог в котором лежит скрипт
DIRECTORY=`dirname "$ABSOLUTE_FILENAME"`
DIRECTORY=`dirname "$DIRECTORY"`

echo "Скрипт запустился из папки $DIRECTORY"


apt-get install $DIRECTORY/files/libu2f-udev_1.1.4-1_all.deb -y
#    apt install $DIRECTORY/files/chromium-gost-111.0.5563.64-linux-amd64.deb -y

apt-get install $DIRECTORY/files/YandexBrowser.deb -y

mkdir /etc/skel/.config
cp -r $DIRECTORY/files/yandex-browser/ /etc/skel/.config/


echo '
[Desktop Entry]
Name=Yandex Browser
GenericName=Web Browser
GenericName[ru]=ЯНДЕКС
Type=Application
Comment=Access the Internet
Comment[ru]=Доступ в Интернет
Exec=/usr/bin/yandex-browser-corporate
Actions=new-window;new-private-window;
Icon=yandex-browser
Terminal=false
StartupNotify=true
MimeType=application/pdf;application/rdf+xml;application/rss+xml;application/xhtml+xml;application/xhtml_xml;application/xml;image/gif;image/jpeg;image/png;image/webp;text/html;text/xml;x-scheme-handler/http;x-scheme-handler/https
Categories=Network;WebBrowser
Version=1.0
Comment[ar]=الدخول إلى الإنترنت
Comment[bg]=Достъп до интернет
Comment[bn]=ইন্টারনেটটি অ্যাক্সেস করুন
Comment[ca]=Accedeix a Internet
Comment[cs]=Přístup k internetu
Comment[da]=Få adgang til internettet
Comment[de]=Internetzugriff
Comment[el]=Πρόσβαση στο Διαδίκτυο
Comment[en_GB]=Access the Internet
Comment[es]=Accede a Internet.
Comment[et]=Pääs Internetti
Comment[fi]=Käytä internetiä
Comment[fil]=I-access ang Internet
Comment[fr]=Accéder à Internet
Comment[gu]=ઇંટરનેટ ઍક્સેસ કરો
Comment[he]=גישה אל האינטרנט
Comment[hi]=इंटरनेट तक पहुंच स्थापित करें
Comment[hr]=Pristup Internetu
Comment[hu]=Internetelérés
Comment[id]=Akses Internet
Comment[it]=Accesso a Internet
Comment[ja]=インターネットにアクセス
Comment[kn]=ಇಂಟರ್ನೆಟ್ ಅನ್ನು ಪ್ರವೇಶಿಸಿ
Comment[ko]=인터넷 연결
Comment[lt]=Interneto prieiga
Comment[lv]=Piekļūt internetam
Comment[ml]=ഇന്റര്നെറ്റ് ആക്സസ് ചെയ്യുക
Comment[mr]=इंटरनेटमध्ये प्रवेश करा
Comment[nb]=Gå til Internett
Comment[nl]=Verbinding maken met internet
Comment[or]=ଇଣ୍ଟର୍ନେଟ୍ ପ୍ରବେଶ କରନ୍ତୁ
Comment[pl]=Skorzystaj z internetu
Comment[pt]=Aceder à Internet
Comment[pt_BR]=Acessar a internet
Comment[ro]=Accesaţi Internetul
Comment[sk]=Prístup do siete Internet
Comment[sl]=Dostop do interneta
Comment[sr]=Приступите Интернету
Comment[sv]=Gå ut på Internet
Comment[ta]=இணையத்தை அணுகுதல்
Comment[te]=ఇంటర్నెట్ను ఆక్సెస్ చెయ్యండి
Comment[th]=เข้าถึงอินเทอร์เน็ต
Comment[tr]=İnternete erişin
Comment[uk]=Доступ до Інтернету
Comment[vi]=Truy cập Internet
Comment[zh_CN]=访问互联网
Comment[zh_HK]=連線到網際網路
Comment[zh_TW]=連線到網際網路
GenericName[ar]=متصفح الشبكة
GenericName[bg]=Уеб браузър
GenericName[bn]=ওয়েব ব্রাউজার
GenericName[ca]=Navegador web
GenericName[cs]=WWW prohlížeč
GenericName[da]=Browser
GenericName[de]=Web-Browser
GenericName[el]=Περιηγητής ιστού
GenericName[en_GB]=Web Browser
GenericName[es]=Navegador web
GenericName[et]=Veebibrauser
GenericName[fi]=WWW-selain
GenericName[fil]=Web Browser
GenericName[fr]=Navigateur Web
GenericName[gu]=વેબ બ્રાઉઝર
GenericName[he]=דפדפן אינטרנט
GenericName[hi]=वेब ब्राउज़र
GenericName[hr]=Web preglednik
GenericName[hu]=Webböngésző
GenericName[id]=Browser Web
GenericName[it]=Browser Web
GenericName[ja]=ウェブブラウザ
GenericName[kn]=ಜಾಲ ವೀಕ್ಷಕ
GenericName[ko]=웹 브라우저
GenericName[lt]=Žiniatinklio naršyklė
GenericName[lv]=Tīmekļa pārlūks
GenericName[ml]=വെബ് ബ്രൌസര്
GenericName[mr]=वेब ब्राऊजर
GenericName[nb]=Nettleser
GenericName[nl]=Webbrowser
GenericName[or]=ଓ୍ବେବ ବ୍ରାଉଜର
GenericName[pl]=Przeglądarka WWW
GenericName[pt]=Navegador Web
GenericName[pt_BR]=Navegador da Internet
GenericName[ro]=Navigator de Internet
GenericName[sk]=WWW prehliadač
GenericName[sl]=Spletni brskalnik
GenericName[sr]=Интернет прегледник
GenericName[sv]=Webbläsare
GenericName[ta]=இணைய உலாவி
GenericName[te]=మహాతల అన్వేషి
GenericName[th]=เว็บเบราว์เซอร์
GenericName[tr]=Web Tarayıcı
GenericName[uk]=Навігатор Тенет
GenericName[vi]=Bộ duyệt Web
GenericName[zh_CN]=网页浏览器
GenericName[zh_HK]=網頁瀏覽器
GenericName[zh_TW]=網頁瀏覽器
X-Fly-OriginFile=/usr/share/applications/yandex-browser.desktop


[Desktop Action new-window]
Name=New Window
Name[ru]=Новое окно
Exec=/usr/bin/yandex-browser-corporate


[Desktop Action new-private-window]
Name=New Incognito Window
Name[ru]=Новое окно в режиме инкогнито
Exec=/usr/bin/yandex-browser-corporate --incognito

' > /usr/share/applications/flydesktop/rmis.desktop


#исправляет проблемы с ключем
curl -fsSL https://repo.yandex.ru/yandex-browser/YANDEX-BROWSER-KEY.GPG | gpg --dearmor | sudo tee /etc/apt/trusted.gpg.d/yandex-browser.gpg > /dev/null


echo -e "\e[1;32m++++++++++++++++++ Настройка браузеров завершена++++++++++++++++++++++++\e[0m"
