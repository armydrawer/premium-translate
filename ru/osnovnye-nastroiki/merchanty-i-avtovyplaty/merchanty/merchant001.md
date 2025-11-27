# Merchant001

{% hint style="info" %}
Если вам необходимо обновить модуль на сервере — воспользуйтесь [инструкцией](https://premium.gitbook.io/main/osnovnye-nastroiki/faq/obnovlenie-failov-skripta-na-servere/kak-obnovit-faily-na-servere#moduli-merchantov-i-avtovyplat)
{% endhint %}

{% hint style="info" %}
Для отображения в заявке для клиента **ФИО владельца карты и название банка, выдавшего карту**, добавьте шорткод \[dest\_tag] в инструкции в настройках мерчанта

![](<../../../.gitbook/assets/image (1627).png>)
{% endhint %}

## Настройки в личном кабинете мерчанта

{% hint style="warning" %}
Для обсуждения условий и подключения, свяжитесь с [представителем сервиса](https://t.me/merch001online).

**Дисклеймер**: при подключении вашего сайта к тому или иному сервису, самостоятельно пожалуйста оценивайте возможные риски сотрудничества.
{% endhint %}

<figure><img src="../../../.gitbook/assets/image (1717).png" alt=""><figcaption></figcaption></figure>

## Настройки модуля

В панели администратора создайте нового мерчанта в разделе "**Мерчанты**" -> "**Добавить мерчант".**

Выберите Merchant001 в выпадающем списке в поле "**Модуль**", укажите название для модуля и нажмите "**Сохранить**".

<figure><img src="../../../.gitbook/assets/image (530).png" alt="" width="450"><figcaption></figcaption></figure>

Заполните указанные авторизационные поля.

<figure><img src="../../../.gitbook/assets/image (531).png" alt="" width="461"><figcaption></figcaption></figure>

**Токен** — домен, сгенерированный в ЛК Merchant001 после создания доступа к API

**Код доступа** — техническое поле, его заполнять не требуется

## Особые поля

<figure><img src="../../../.gitbook/assets/image (532).png" alt="" width="409"><figcaption></figcaption></figure>

**Способ оплаты** — доступные варианты выдачи реквизитов для клиентов (валюты — BYN, KZT, RUB, UAH, UZS)

{% hint style="info" %}
Список доступных систем и валют в выпадающем списке определяется по вашему токену, указанному в настройках модуля для авторизации.

Если необходимые вам системы или валюты, указанных на скриншоте выше, не отображаются в списке - обратитесь в техподдержку мерчанта за их включением.
{% endhint %}

## Продолжение настройки

Далее произведите настройку мерчанта следуя [общей инструкции по настройке](https://premium.gitbook.io/rukovodstvo-polzovatelya/osnovnye-nastroiki/merchanty-i-avtovyplaty/merchanty/obshie-nastroiki-merchantov).<br>
