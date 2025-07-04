---
hidden: true
noIndex: true
---

# Paylama (неактивно)

{% hint style="info" %}
Если вам необходимо обновить модуль на сервере - воспользуйтесь [инструкцией](https://premium.gitbook.io/rukovodstvo-polzovatelya/osnovnye-nastroiki/faq/kak-obnovit-faily-na-servere#moduli-merchantov)
{% endhint %}

## Настройки в личном кабинете мерчанта

Пройдите регистрацию на сайте [Paylama](https://paylama.io/) и авторизуйтесь в личном кабинете.

Перейдите в раздел "**Работа с API**" и нажмите кнопку "**Создать API**".

<figure><img src="../../../.gitbook/assets/image (1591).png" alt="" width="563"><figcaption></figcaption></figure>

Укажите произвольное название для создаваемого доступа, IP-адрес вашего сервера (обязательно) и нажмите кнопку "**Создать**".

<figure><img src="../../../.gitbook/assets/image (1585).png" alt="" width="563"><figcaption></figcaption></figure>

Скопируйте сгенерированные ключи и сохраните их в текстовый файл.

<figure><img src="../../../.gitbook/assets/image (1593).png" alt="" width="563"><figcaption></figcaption></figure>

## Настройки модуля

В панели администратора создайте нового мерчанта в разделе "**Мерчанты**" -> "**Добавить мерчант".**

Выберите Paylama Card в выпадающем списке в поле "**Модуль**", укажите название для модуля и нажмите "**Сохранить**".

<figure><img src="../../../.gitbook/assets/image (1586).png" alt="" width="443"><figcaption></figcaption></figure>

Заполните указанные авторизационные поля.

<figure><img src="../../../.gitbook/assets/image (1588).png" alt="" width="422"><figcaption></figcaption></figure>

**API ключ** — APIKey, сгенерированный в ЛК Paylama

## Особые поля

<figure><img src="../../../.gitbook/assets/image (1589).png" alt=""><figcaption></figcaption></figure>

**Тип:**\
• **P2P** — выдача в заявке номера телефона для пополнения по СБП\
• **FPS** — выдача в заявке номера карты выбранного ниже банка

<figure><img src="../../../.gitbook/assets/image (1590).png" alt=""><figcaption></figcaption></figure>

**Тип** — выберите из списка валюту, которую планируете принимать от клиентов и банк, номера карт которого будут выдаваться в заявках

## Продолжение настройки

Далее произведите настройку мерчанта следуя [общей инструкции по настройке](https://premium.gitbook.io/rukovodstvo-polzovatelya/osnovnye-nastroiki/merchanty-i-avtovyplaty/merchanty/obshie-nastroiki-merchantov).\
