# Cryptoway

{% hint style="info" %}
Если вам необходимо обновить модуль на сервере — воспользуйтесь [инструкцией](https://premium.gitbook.io/main/osnovnye-nastroiki/faq/obnovlenie-failov-skripta-na-servere/kak-obnovit-faily-na-servere#moduli-merchantov-i-avtovyplat)
{% endhint %}

## Настройки в личном кабинете мерчанта

{% hint style="warning" %}
**Дисклеймер**: при подключении вашего сайта к тому или иному сервису, пожалуйста, самостоятельно оценивайте возможные риски сотрудничества.
{% endhint %}

Зарегистрируйтесь на [сервисе Cryptoway](https://cryptoway.com/ru) и авторизуйтесь в личном кабинете.

Создайте проект в разделе сервиса ["Проекты"](https://account.cryptoway.com/ru/projects).

<figure><img src="../../../.gitbook/assets/image (1214).png" alt=""><figcaption></figcaption></figure>

Перейдите в ваш проект ➔ "API ключи"&#x20;

<figure><img src="../../../.gitbook/assets/image (1216).png" alt=""><figcaption></figcaption></figure>

Скопируйте Callback-ключ и секретный ключ в буфер обмена или блокнот.&#x20;

<figure><img src="../../../.gitbook/assets/image (1220).png" alt=""><figcaption></figcaption></figure>

## Настройки модуля

В панели администратора создайте нового мерчанта в разделе "**Мерчанты**" ➔ "**Добавить мерчант".**

Выберите модуль **Cryptoway** в выпадающем списке в поле "**Модуль**", укажите название для модуля и нажмите "**Сохранить**".

<figure><img src="../../../.gitbook/assets/image_2026-06-24_182229043.png" alt=""><figcaption></figcaption></figure>

Заполните указанные авторизационные поля.

<figure><img src="../../../.gitbook/assets/image_2026-06-24_182259285.png" alt=""><figcaption></figcaption></figure>

**Домен** — не заполняйте поле, оставьте его пустым.

**API ключ** — Callback-ключ, скопированный ранее в ЛК Cryptoway.

**Секретный ключ** — секретный ключ,скопированный ранее в ЛК Cryptoway.

## Особые поля

Способ оплаты — выбор валюты для выдачи адреса кошелька (при выборе пункта "**Автоматически**" будет использоваться XML код валюты "**Отдаю**")

* **добавить** — добавление своего кода валюты

<figure><img src="../../../.gitbook/assets/image_2026-06-24_182727846.png" alt=""><figcaption></figcaption></figure>

**Cron-файл -** [создайте задание](https://premium.gitbook.io/main/osnovnye-nastroiki/faq/kak-sozdat-zadanie-cron-na-servere) с такой ссылкой на сервер&#x435;**.**

## Продолжение настройки

Дополнительные настройки модуля выполняются согласно [общей инструкции по настройке](https://premium.gitbook.io/rukovodstvo-polzovatelya/osnovnye-nastroiki/merchanty-i-avtovyplaty/merchanty/obshie-nastroiki-merchantov).
