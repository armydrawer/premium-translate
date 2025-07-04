# Установка и настройка Electrum (2 кошелька)

{% hint style="info" %}
Системные требования к модулю, устанавливаемому на сервере:

* Операционная система **Ubuntu 20.x** или **22.x**. **Другие ОС не поддерживаются**.
* Панель управления **ISP Manager 6 Lite**
* **Premium Exchanger v2.4** и выше

Системные требования к приложению, устанавливаемому на клиентском устройстве:

* Операционная система **Linux/Windows (8.1 and higher)/macOS (10.13 and higher)/Android (5.0 and higher)**
{% endhint %}

## Установка необходимых модулей на сервер через ISP Manager 6 Lite

1. Авторизуйтесь в панели управления ISP Manager с использованием учетных данных <mark style="color:red;">**root-пользователя**</mark>.
2. Перейдите в раздел "**Администрирование" ->"Shell-клиент"**

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

10. Создайте 2 кошелька (или сделайте копию созданного кошелька копированием файла), следуя инструкциям приложения.

{% hint style="danger" %}
Внимание! В пароле для создаваемого кошелька не используйте символ **$** — это приводит к ошибкам в работе скрипта
{% endhint %}

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

11. Создайте второй кошелек по аналогии с первым (или используйте дубликат).
12. Откройте установленное приложение Electrum на вашем компьютере и вызовите пункт меню "**Файл**" -> "**Открыть**".

<figure><img src="../../.gitbook/assets/image (647).png" alt="" width="403"><figcaption></figcaption></figure>

13. Откроется папка с кошельками — найдите кошельки с названиями, которые вы использовали при его установке.\
    \
    Назовите кошелек на прием средств как **default\_wallet\_in**, а кошелек для выплаты средств как **default\_wallet\_out** (если вы не планируете использовать автовыплату, просто не создавайте новую копию модуля в панели администратора в дальнейшем, сам кошелек требуется для корректной установки модуля).

<figure><img src="../../.gitbook/assets/image (1575).png" alt=""><figcaption></figcaption></figure>

## Загрузка файлов на сервер

14. Зайдите в раздел "**Сайты**" в ISP Manager.

<figure><img src="../../.gitbook/assets/изображение (190).png" alt="" width="300"><figcaption></figcaption></figure>

15. Выделите ваш сайт и нажмите на кнопку **"Войти как владелец"**. Вы будете авторизованы как <mark style="color:green;">пользователь, созданный для сайта</mark>.

<figure><img src="../../.gitbook/assets/изображение (71).png" alt=""><figcaption></figcaption></figure>

16. Откройте раздел "**Менеджер файлов**" в боковой панели.

<figure><img src="../../.gitbook/assets/изображение (115).png" alt="" width="330"><figcaption></figcaption></figure>

17. В открывшуюся директорию загрузите файлы из архива **`electrum_installer.zip`**, который вы получили от нас **после** [**оплаты модуля**](https://premiumexchanger.com/masspayments/), и ранее созданные файлы двух кошельков Electrum из папки "**electrum\_data**" на вашем компьютере.

Файлы установщика Electrum:

{% file src="../../.gitbook/assets/start_or_restart_electrum_daemon2.sh" %}

{% file src="../../.gitbook/assets/install_electrum2.sh" %}

<figure><img src="../../.gitbook/assets/image (1576).png" alt="" width="519"><figcaption></figcaption></figure>

{% hint style="danger" %}
Если загружаемые на сервер кошельки имеют названия, отличные от **default\_wallet\_in** и **default\_wallet\_out**, то после загрузки кошельков на сервер обязательно переименуйте их в **default\_wallet\_in** и **default\_wallet\_out** на сервере и компьютере — это необходимо для автоматического переноса файла кошельков в папку Electrum на сервере
{% endhint %}

Список файлов, которые должны быть загружены на сервер:

* `start_or_restart_electrum_daemon2.sh`
* `install_electrum.2sh`
* `default_wallet_in`
* `default_wallet_out`

18. В корневой директории откройте файл **`start_or_restart_electrum_daemon2.sh`** для редактирования двойным кликом. В строках 4 и 8 вместо <mark style="color:purple;">`пароль для кошелька`</mark> укажите соответственно пароли от кошельков на прием и выплату, которые были заданы в процессе их установки на компьютере и сохраните изменения в файле.

<figure><img src="../../.gitbook/assets/image (1578).png" alt=""><figcaption></figcaption></figure>

## Установка Electrum на сервере

19. Перейдите в раздел **"Shell-клиент",** будучи авторизованным под <mark style="color:green;">пользователем, созданным для сайта</mark>.

<figure><img src="../../.gitbook/assets/изображение (52).png" alt="" width="330"><figcaption></figcaption></figure>

20. Нажмите правой клавишей на пустом экране и выберите пункт **"Paste from browser"**, введите команду **`bash install_electrum2.sh`** и нажмите кнопку ОК. Затем нажмите клавишу **Enter** для запуска команды.

<figure><img src="../../.gitbook/assets/image (1579).png" alt=""><figcaption></figcaption></figure>

21. После выполнения скрипта сохраните данные, выделенные красными рамками на скриншоте ниже, для дальнейшей настройки модулей в панели администратора.

<figure><img src="../../.gitbook/assets/image (1580).png" alt=""><figcaption></figcaption></figure>

{% hint style="warning" %}
Если вы устанавливаете модуль Electrum на сервер, отличный от того, где установлен скрипт Premium Exchanger — в настройках модуля мерчанта/автовыплаты в панели администратора позже необходимо будет также заполнить поле "API Server", указав IP-адрес сервера, на котором установлен Electrum.

![](<../../.gitbook/assets/image (1351).png>)
{% endhint %}

## Добавление заданий Cron

22. Скопируйте первую команду для настройки планировщика задач Cron на сервере. Выделите соответствующую строчку левой клавишей мыши, а кликом правой клавиши вызовите меню и нажмите пункт "**Copy**".

<figure><img src="../../.gitbook/assets/image (575).png" alt=""><figcaption></figcaption></figure>

23. Перейдите в раздел **"Планировщик СRON".**

{% hint style="danger" %}
Задания cron добавляются из-под <mark style="color:green;">пользователя, созданного для сайта</mark>, **не** из-под <mark style="color:red;">**root-пользователя**</mark>!
{% endhint %}

<figure><img src="../../.gitbook/assets/изображение (75).png" alt="" width="315"><figcaption></figcaption></figure>

24. Нажмите кнопку **"Создать задание"**, в поле **"Команда"** укажите команду, скопированную в п. 22, а затем выполните настройку формы согласно скриншоту ниже.

<figure><img src="../../.gitbook/assets/image (1582).png" alt="" width="375"><figcaption></figcaption></figure>

Нажмите кнопку "**Создать"**.

25. Создайте задание для второй команды.

<figure><img src="../../.gitbook/assets/image (1327).png" alt="" width="473"><figcaption></figcaption></figure>

## Удаление файлов на сервере

26. В разделе "**Файловый менеджер"** удалите 3 из 4 ранее загруженных файла с сервера:

* `install_electrum2.sh`
* `default_wallet_in`
* `default_wallet_out`

Файл `start_or_restart_electrum_daemon2.sh` — <mark style="color:red;">не удалять!</mark>

<figure><img src="../../.gitbook/assets/image (576).png" alt="" width="563"><figcaption></figcaption></figure>

## **Перезагрузка сервера**

27. **Обязательно** перезагрузите сервер после установки.

{% hint style="danger" %}
После установки Electrum или после смены кошелька/пароля для кошелька **необходимо** перезагружать сервер
{% endhint %}

## Продолжение настройки

После установки Electrum на сервере настройте подключение к кошелькам Electrum в панели администратора:

* [Инструкция для настройки мерчанта на прием BTC](https://premium.gitbook.io/main/osnovnye-nastroiki/merchanty-i-avtovyplaty/merchanty/electrum)
* [Инструкция для настройки мерчанта на выплату BTC](https://premium.gitbook.io/main/osnovnye-nastroiki/merchanty-i-avtovyplaty/avtovyplaty/electrum)
