# Установка и настройка Electrum (old version)

{% hint style="info" %}
Системные требования к модулю, устанавливаемому на сервере:

* Операционная система **Ubuntu 20.x** или **22.x**. **Другие ОС не поддерживаются**.
* Панель управления **ISP Manager 6 Lite**
* **Premium Exchanger v2.4** и выше

Системные требования к приложению, устанавливаемому на компьютере:

* Операционная система **Linux/Windows (8.1 and higher)/macOS (10.13 and higher)/Android (5.0 and higher)**
{% endhint %}

## Установка необходимых модулей на сервер через ISP Manager 6 Lite

1. Авторизуйтесь в панели управления ISP Manager с использованием учетных данных <mark style="color:red;">**root-пользователя**</mark>.
2. Перейдите в раздел "**Администрирование" -> "Shell-клиент"**

<figure><img src="../../.gitbook/assets/изображение (126).png" alt="" width="330"><figcaption></figcaption></figure>

3. Нажмите правой кнопкой мыши на пустом экране и выберите "**Paste from browser**" в контекстном меню.

<figure><img src="../../.gitbook/assets/изображение (178).png" alt="" width="563"><figcaption></figcaption></figure>

4. Введите команду, указанную ниже, в открывшемся окне и нажмите кнопку "**ОК**". Затем нажмите клавишу **Enter** для выполнения команды.

```
sudo apt-get install libsecp256k1-0 python3-cryptography -y
```

5. Дождитесь завершения выполнения команды.

<figure><img src="../../.gitbook/assets/изображение (38).png" alt=""><figcaption></figcaption></figure>

## Проверка доступа к Shell-клиенту для пользователя, созданного для сайта

6. Перейдите в раздел "**Пользователи**".

<figure><img src="../../.gitbook/assets/изображение (136).png" alt="" width="325"><figcaption></figcaption></figure>

7. Нажмите на логин пользователя, под которым работает сайт.

<figure><img src="../../.gitbook/assets/изображение (183).png" alt=""><figcaption></figcaption></figure>

8. В блоке "**Доступ**" проверьте наличие галочки рядом с **"Доступ к shell"**. Если галочка не установлена, поставьте ее и сохраните настройки пользователя.

<figure><img src="../../.gitbook/assets/изображение (104).png" alt="" width="563"><figcaption></figcaption></figure>

## Установка Electrum на компьютер и создание кошелька

9. [Скачайте](https://download.electrum.org/4.4.6/) и установите Electrum на ваш компьютер:

* [electrum-4.4.6-setup.exe](https://download.electrum.org/4.4.6/electrum-4.4.6-setup.exe) — устанавливаемая версия под Windows
* [electrum-4.4.6-portable.exe](https://download.electrum.org/4.4.6/electrum-4.4.6-portable.exe) — портативная версия под Windows
* [electrum-4.4.6.dmg](https://download.electrum.org/4.4.6/electrum-4.4.6.dmg) — устанавливаемая версия под MacOS
* [electrum-4.4.6.tar.gz](https://download.electrum.org/4.4.6/Electrum-sourceonly-4.4.6.tar.gz) — устанавливаемая версия под Linux

10. Создайте новый кошелек, следуя инструкциям приложения.

<details>

<summary>Создание нового кошелька</summary>

Выберите "Стандартный кошелек"\
![](<../../.gitbook/assets/image (1316).png>)

Создайте новую seed-фразу\
![](<../../.gitbook/assets/image (1317).png>)

Запишите seed-фразу в блокнот и сохраните файл\
![](<../../.gitbook/assets/image (1318).png>)

Введите seed-фразу полностью для проверки\
![](<../../.gitbook/assets/image (1319).png>)

<mark style="color:red;">Обязательно</mark> установите пароль на кошелек (от 16 символов — используйте латинские буквы и цифры) и запишите пароль в блокнот\
![](<../../.gitbook/assets/image (1320).png>)

</details>

11. Откройте установленное приложение Electrum на вашем компьютере и вызовите пункт меню "**Файл**" -> "**Открыть**".

<figure><img src="../../.gitbook/assets/image (647).png" alt="" width="403"><figcaption></figcaption></figure>

12. Откроется папка с кошельком — найдите кошелек с названием, которое вы использовали при его установке.

<figure><img src="../../.gitbook/assets/image (1357).png" alt="" width="482"><figcaption></figcaption></figure>

Обратите внимание, что у вас может быть несколько кошельков, поэтому выберите нужный вам файл кошелька. Этот файл понадобится для его загрузки на сервер на следующем шаге.

{% hint style="warning" %}
По умолчанию кошелек называется **"default\_wallet"**, но вы могли задать ему персонализированное имя во время установки.
{% endhint %}

## Загрузка файлов на сервер

13. Зайдите в раздел "**Сайты**" в ISP Manager.

<figure><img src="../../.gitbook/assets/изображение (190).png" alt="" width="300"><figcaption></figcaption></figure>

14. Выделите нужный сайт и нажмите на кнопку **"Войти как владелец"**. Вы будете авторизованы как <mark style="color:green;">пользователь, созданный для сайта</mark>.

<figure><img src="../../.gitbook/assets/изображение (71).png" alt=""><figcaption></figcaption></figure>

15. Откройте раздел "**Менеджер файлов**" в боковой панели.

<figure><img src="../../.gitbook/assets/изображение (115).png" alt="" width="330"><figcaption></figcaption></figure>

16. В открывшуюся директорию загрузите файлы из архива **`electrum_installer.zip`**, который вы получили от нас, и ранее созданный файл кошелька Electrum из папки "**electrum\_data**" на вашем компьютере.

<figure><img src="../../.gitbook/assets/image (1356).png" alt=""><figcaption></figcaption></figure>

{% hint style="danger" %}
Если загружаемый на сервер кошелек имеет название, отличное от **default\_wallet**, то после загрузки кошелька на сервер обязательно переименуйте его в **default\_wallеt** на сервере и компьютере — это необходимо для автоматического переноса файла кошелька на сервере
{% endhint %}

Список файлов, которые должны быть загружены на сервер:

* `start_or_restart_electrum_daemon.sh`
* `install_electrum.sh`
* `default_wallet` (созданный вами ранее кошелек Electrum)

17. В корневой директории откройте файл **`start_or_restart_electrum_daemon.sh`** для редактирования двойным кликом. В строке<mark style="color:blue;">`4: WALLET_PASSWORD="`</mark><mark style="color:purple;">`пароль от кошелька`</mark><mark style="color:blue;">`"`</mark> вместо <mark style="color:purple;">`пароль для кошелька`</mark> укажите пароль от кошелька, который был задан во время его установки на компьютере и сохраните изменения в файле.

<figure><img src="../../.gitbook/assets/image (1385).png" alt=""><figcaption></figcaption></figure>

## Установка Electrum на сервере

18. Перейдите в раздел **"Shell-клиент",** будучи авторизованным под <mark style="color:green;">пользователем, созданным для сайта</mark>.

<figure><img src="../../.gitbook/assets/изображение (52).png" alt="" width="330"><figcaption></figcaption></figure>

19. Нажмите правой клавишей на пустом экране и выберите пункт **"Paste from browser"**, введите команду **`bash install_electrum.sh`** и нажмите кнопку ОК. Затем нажмите клавишу **Enter** для запуска команды.

<figure><img src="../../.gitbook/assets/изображение (36).png" alt="" width="563"><figcaption></figcaption></figure>

20. После выполнения скрипта сохраните данные, выделенные красной рамкой на скриншоте ниже, для дальнейшей настройки модуля в панели администратора обменника Premium Exchanger.

<figure><img src="../../.gitbook/assets/image (1324).png" alt=""><figcaption></figcaption></figure>

{% hint style="warning" %}
Если вы устанавливаете модуль Electrum на сервер, отличный от того, где установлен скрипт Premium Exchanger — в настройках модуля мерчанта/автовыплаты в панели администратора позже необходимо будет также заполнить поле "API Server", указав IP-адрес сервера, на котором установлен Electrum.

![](<../../.gitbook/assets/image (1351).png>)
{% endhint %}

## Добавление заданий Cron

21. Скопируйте первую команду для настройки планировщика задач Cron на сервере. Выделите соответствующую строчку левой клавишей мыши, а кликом правой клавиши вызовите меню и нажмите пункт "**Copy**".

<figure><img src="../../.gitbook/assets/image (1325).png" alt=""><figcaption></figcaption></figure>

22. Перейдите в раздел **"Планировщик СRON".**

{% hint style="warning" %}
Задания cron добавляются из-под <mark style="color:green;">пользователя, созданного для сайта</mark>, **не** из-под <mark style="color:red;">**root-пользователя**</mark>!
{% endhint %}

<figure><img src="../../.gitbook/assets/изображение (75).png" alt="" width="315"><figcaption></figcaption></figure>

23. Нажмите кнопку **"Создать задание"**, в поле **"Команда"** укажите команду, скопированную в пункте 21, затем выполните настройку формы согласно скриншоту ниже.

<figure><img src="../../.gitbook/assets/image (1326).png" alt="" width="488"><figcaption></figcaption></figure>

Нажмите кнопку "**Создать"**.

24. Создайте задание для второй команды. Скопируйте строку со второй командой.

<figure><img src="../../.gitbook/assets/image (1355).png" alt=""><figcaption></figcaption></figure>

Создайте новое задание и вставьте команду в соответствующее поле, затем выполните настройку формы согласно скриншоту ниже. Нажмите кнопку "**Создать"**.

<figure><img src="../../.gitbook/assets/image (1327).png" alt="" width="473"><figcaption></figcaption></figure>

## Удаление файлов на сервере

25. В разделе "**Файловый менеджер"** удалите загруженные ранее файлы с сервера:

* `start_or_restart_electrum_daemon.sh`
* `install_electrum.sh`
* `default_wallet`

<figure><img src="../../.gitbook/assets/image (1328).png" alt="" width="563"><figcaption></figcaption></figure>

## **Перезагрузка сервера**

26. **Обязательно** перезагрузите сервер после установки.

{% hint style="danger" %}
После установки Electrum или после смены кошелька/пароля **необходимо** перезагружать сервер
{% endhint %}

## Продолжение настройки

После установки Electrum на сервере настройте подключение к кошельку Electrum в панели управления сайтом:

* [Инструкция для настройки мерчанта на прием BTC](https://premium.gitbook.io/rukovodstvo-polzovatelya/osnovnye-nastroiki/merchanty-i-avtovyplaty/merchanty/electrum)
* [Инструкция для настройки мерчанта на выплату BTC](https://premium.gitbook.io/rukovodstvo-polzovatelya/osnovnye-nastroiki/merchanty-i-avtovyplaty/avtovyplaty/electrum)
