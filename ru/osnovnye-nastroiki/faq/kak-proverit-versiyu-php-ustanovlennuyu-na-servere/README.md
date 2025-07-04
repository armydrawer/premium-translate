# Как проверить версию PHP, установленную на сервере?

## При использовании ISP Manager

Зайти в ISP Manager под любым пользователем, имеющим доступ к файлам сайта, и перейдите в раздел "**Сайты**". В столбце "**Обработчик**" вы увидите версию PHP, использующуюся для сайта.

<figure><img src="../../../.gitbook/assets/image (1718).png" alt=""><figcaption></figcaption></figure>

## Просмотр версии PHP в браузере

Подключитесь по FTP или по SSH к серверу и перейдите в корневой каталог вашего сайта. Там создайте файл [`phpversion.php`](#user-content-fn-1)[^1]со следующим содержимым:

`<?php phpinfo(); ?>`

<figure><img src="../../../.gitbook/assets/image (1720).png" alt="" width="488"><figcaption></figcaption></figure>

Затем откройте ваш сайт и допишите в адресной строке адрес этого файла:

<figure><img src="../../../.gitbook/assets/image (1719).png" alt=""><figcaption></figcaption></figure>

Если всё сделано верно, будет выведена большая таблица с информацией про PHP и установленные расширения, а в самом верху страницы будет версия PHP.

Если вы не хотите выводить всю таблицу с информацией о PHP, то можно вывести только версию PHP. Для этого укажите в файле `phpversion.php` следующую строку:

`<?php echo phpversion(); ?>`

<figure><img src="../../../.gitbook/assets/image (1722).png" alt="" width="473"><figcaption></figcaption></figure>

В результате вы получите такую страницу:

<figure><img src="../../../.gitbook/assets/image (1721).png" alt=""><figcaption></figcaption></figure>

[^1]: название файла приведено в качестве примера, вы можете использовать любое название
