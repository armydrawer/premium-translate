# Как обновить PHP

Обновление PHP с версии 8.1 на 8.2 на Ubuntu (пример)


Выполнив следующие шаги, вы сможете перейти на новую версию PHP.

### Шаг 1: [Прежде всего, проверьте версию PHP](https://premium.gitbook.io/main/osnovnye-nastroiki/faq/kak-proverit-versiyu-php-ustanovlennuyu-na-servere)&#xD;

### Шаг 2: Добавьте репозиторий PHP&#xD;

Для обновления до PHP 8.2 необходимо добавить репозиторий PHP в систему. Чтобы добавить репозиторий, введите в консоль следующие инструкции.

{% code overflow="wrap" %}
```nginx
sudo apt install software-properties-common
sudo add-apt-repository ppa:ondrej/php
sudo apt update
```
{% endcode %}

### Шаг 3: Обновите PHP&#xD;

Вы можете обновить PHP до версии 8.2 после добавления репозитория и обновления системы.

{% code overflow="wrap" %}
```nginx
sudo apt install php8.2
```
{% endcode %}

В процессе установки вам может быть предложено подтвердить обновление и ввести пароль. Следуйте указаниям на экране, чтобы продолжить установку.



### Шаг 4: После обновления проверьте наличие обновления PHP&#xD;

Выполните следующую команду, чтобы убедиться, что PHP 8.2 установлен после завершения установки.

```nginx
php -v
```

### Шаг 5: Установка пакетов PHP 8.2&#xD;

Вы можете установить некоторые расширения PHP с помощью управления пакетами apt, если они вам нужны для ваших проектов.

{% code overflow="wrap" %}
```nginx
sudo apt install php8.2
```
{% endcode %}

### Шаг 6: Перезапуск веб-сервера&#xD;

Перезапуск веб-сервера необходим для того, чтобы изменения вступили в силу, если вы используете PHP с веб-сервером Apache или Nginx.

{% code overflow="wrap" %}
```nginx
sudo service apache2 restart # Для Apache
sudo service nginx restart # Для Nginx
```
{% endcode %}

Примечание: Вы можете использовать следующую команду, чтобы выбрать новую версию PHP из списка, если он все еще показывает устаревшую версию PHP.

{% code overflow="wrap" %}
```nginx
sudo update-alternatives --config php
```
{% endcode %}

Проверьте повторно  версию PHP, на которой работает ваш веб-сервер.

### Замена версии PHP для работы скрипта Premium Exchanger

Скачайте и загрузите дистрибутив под **установленную версию скрипта и новую версию PHP.**

**Файлы для установки** — при установке скрипта с нуля

**Файлы для обновления** — при обновлении установленного скрипта

<figure><img src="../../../../.gitbook/assets/image (133).png" alt=""><figcaption></figcaption></figure>

Загрузите архив на сервер в корневую папку и распакуйте его с заменой существующих файлов

<figure><img src="../../../../.gitbook/assets/image (134).png" alt="" width="491"><figcaption></figcaption></figure>

В ISP Manager смените версию PHP для вашего сайта на новую и сохраните изменения.

<figure><img src="../../../../.gitbook/assets/image (135).png" alt="" width="467"><figcaption></figcaption></figure>
