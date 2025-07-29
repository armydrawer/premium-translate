# Как защитить сервер

## Общие рекомендации

Часто обычные хостинги ограничены в возможностях для тонкой настройки безопасности, поэтому мы рекомендуем размещать обменник на виртуальном выделенном сервере (VPS/VDS) и выполнить его настройку, чтобы снизить риски взлома. Как правило, у хостинг-провайдеров есть платные услуги по настройке виртуальных серверов. Привлекать сторонних специалистов для настройки можно, но только тех, кому вы доверяете.

* На хостинге (биллинг для управления услугой), где размещен ваш сайт, включите SMS-авторизацию в личный кабинет. Установите другие способы ограничения на вход, если такие предусмотрены вашим хостингом. Для хостинг-провайдера Reg.ru, как минимум, включите SMS-авторизацию и оповещение на e-mail при авторизации в личном кабинете;
* Обновите модуль **Ioncube Loader** до последней версии;
* Установите и настройте на сервере модуль **fail2ban**;
* Установите на сервере антивирус и сканер портов. Настройте регулярное сканирование файлов сервера и портов;
* Настройте брандмауэр. Заблокируйте порты для FTP, SSH и различных Shell-клиентов;
* Заблокируйте стандартные адреса к форме авторизации сервера. Например, для Ispmanager это: `https://ip_адрес/manager`, `https://ip_адрес/manager/ispmngr`, `https://ip_адрес/ispmngr`;
* Измените стандартный порт к форме авторизации сервера. Для ispmanager обычно используется порт 1500. Установить любое свободное значение порта;
* Заблокируйте адрес доступа к phpmyadmin. Достаточно установить на сервере права 444 на папку с phpmyadmin;
* Заблокируйте адрес доступа к почтовым клиентам. Например, `https://ip_адрес/webmail/`, `https://ip_адрес/roundcube/` и т.п. Достаточно установить на сервере права 444 на папку почтового клиента;
* Для всех пользователей сервера, в том числе **root**, установите пароль длиной не менее 15-25 символов;
* Не храните резервные копии файлов и базы данных на сервере, особенно в корневой папке сайта.

## **Настройка служб и опций**

*   Закройте возможность работы [вебшеллов](https://encyclopedia.kaspersky.ru/glossary/web-shell/) через файл php.ini (отредактируйте существующую или добавьте новую директиву):

    ```ini
    disable_functions = exec,system,passthru,shell_exec,proc_open,show_source
    ```

<details>

<summary>Если вы используете ispmanager, выполните следующие шаги:</summary>

1. Авторизуйтесь в ispmanager под <mark style="color:red;">**root-пользователем**</mark>.

2) Перейдите в раздел "**Сайты**", выберите ваш сайт и нажмите кнопку "Настройки **PHP для сайта**".

<figure><img src="../../.gitbook/assets/image (2181).png" alt=""><figcaption></figcaption></figure>

3. Поиском найдите директиву `disable_functions`, отметьте её галочкой и нажмите кнопку с карандашом ("**Изменить переменную**").

<figure><img src="../../.gitbook/assets/image (2182).png" alt=""><figcaption></figcaption></figure>

4.  Добавьте указанные функции (не удаляйте предыдущие значения — дополните строку указанными функциями): **`exec,system,passthru,shell_exec,proc_open,show_source`** и сохраните изменени&#x44F;**.**

    <figure><img src="../../.gitbook/assets/image (2183).png" alt="" width="544"><figcaption></figcaption></figure>

</details>

*   Запретите загрузку файлов через **`allow_url_include` и `allow_url_fopen`** — это снизит риск удаленного выполнения кода:

    ```ini
    allow_url_fopen = Off
    allow_url_include = Off
    ```

<details>

<summary>Если вы используете ispmanager, выполните следующие шаги:</summary>

1. Авторизуйтесь в ispmanager под <mark style="color:red;">**root-пользователем**</mark>.

2) Перейдите в раздел "**Сайты**", выберите ваш сайт и нажмите кнопку "**Настройки PHP для сайта**".

<figure><img src="../../.gitbook/assets/image (2181).png" alt="" width="563"><figcaption></figcaption></figure>

3. Поиском найдите директивы по тексту `allow_url`, отметьте их галочкой и нажмите кнопку с карандашом ("**Изменить переменную**").

<figure><img src="../../.gitbook/assets/image (2185).png" alt="" width="563"><figcaption></figcaption></figure>

4. Укажите `Off` для переменных и сохраните изменени&#x44F;**.**

<figure><img src="../../.gitbook/assets/image (2184).png" alt="" width="563"><figcaption></figcaption></figure>

</details>

*   Отключите некоторые расширения (если они не нужны). Например:

    ```ini
    extension = phar.so ; // если phar не используется
    ```

<details>

<summary>Если вы используете ispmanager, выполните следующие шаги:</summary>

1. Авторизуйтесь в ispmanager под <mark style="color:red;">**root-пользователем**</mark>.

2) Перейдите в раздел "**PHP**", выберите версию PHP, [которая используется на вашем сайте](https://premium.gitbook.io/main/osnovnye-nastroiki/faq/kak-proverit-versiyu-php-ispolzuyushuyusya-dlya-saita) и нажмите кнопку "Расширения".

<figure><img src="../../.gitbook/assets/image (2186).png" alt="" width="563"><figcaption></figcaption></figure>

3. Поиском найдите расширения по тексту **`phar`** (пример), отметьте их галочкой и нажмите кнопку с карандашом ("**Выключить расширение**").

<figure><img src="../../.gitbook/assets/image (2187).png" alt="" width="531"><figcaption></figcaption></figure>

4. Нажмите кнопку и подтвердите выключение расширения во всплывающем окн&#x435;**.**

</details>

*   Ограничьте доступ к `php.ini` и `wp-config.php` через файл `.htaccess`

    ```ini
    <FilesMatch "^(php\.ini|wp-config\.php)$">
        Order deny,allow
        Deny from all
    </FilesMatch>
    ```



<details>

<summary>Если вы используете ispmanager, выполните следующие шаги:</summary>

1. Авторизуйтесь в ispmanager под <mark style="color:yellow;">**любым пользователем**</mark>.

2) Перейдите в раздел "**Сайты**", выберите ваш сайт и нажмите кнопку "**Файлы сайта**".

<figure><img src="../../.gitbook/assets/image (2188).png" alt=""><figcaption></figcaption></figure>

3. Найдите файл `.htaccess` и перейдите в режим его редактирования двойным кликом.

<figure><img src="../../.gitbook/assets/image (2190).png" alt="" width="479"><figcaption></figcaption></figure>

4. Укажите указанный выше текст в файле и сохраните изменения.

<figure><img src="../../.gitbook/assets/image (2191).png" alt="" width="543"><figcaption></figcaption></figure>

</details>

## Настройка прав на файлы

<figure><img src="../../.gitbook/assets/image (1) (1) (1) (1) (1) (1) (1).png" alt="" width="563"><figcaption></figcaption></figure>

Если в админбаре отображается предупреждение об ошибках в виде анимированного <mark style="color:red;">красного круга</mark>, откройте раздел с ошибками.

Если в разделе отображается ошибка о некорректных правах на файлы, измените права указанных файлов на более безопасные (~~зачеркнутое значение~~ — <mark style="color:red;">текущие права</mark>, после ➔ <mark style="color:green;">рекомендуемые права</mark>).

{% hint style="success" %}
[Официальная инструкция](https://developer.wordpress.org/advanced-administration/security/hardening/#file-permissions) от Wordpress по настройке прав на файлы
{% endhint %}

{% hint style="info" %}
Предупреждения также отображаются в разделе "Консоль", блок "Проверка безопасности"

<img src="../../.gitbook/assets/image (2) (1) (1) (1) (1) (1) (1).png" alt="" data-size="original">
{% endhint %}

\
При использовании ispmanager перейдите в раздел "**Сайты**", выберите ваш сайт и нажмите кнопку "**Файлы сайта**".

<figure><img src="../../.gitbook/assets/image (2188).png" alt=""><figcaption></figcaption></figure>

Выберите файл с некорректными правами и нажмите кнопку "Атрибуты".

<figure><img src="../../.gitbook/assets/image (2193).png" alt=""><figcaption></figcaption></figure>

Укажите рекомендуемые права в строке "Права доступа" и сохраните изменения.

<figure><img src="../../.gitbook/assets/image (2197).png" alt="" width="248"><figcaption></figcaption></figure>

После изменения прав предупреждение пропадёт в админ-панели.
