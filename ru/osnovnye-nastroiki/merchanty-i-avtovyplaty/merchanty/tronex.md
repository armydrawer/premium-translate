# TronEx

{% hint style="info" %}
Если вам необходимо обновить модуль на сервере — воспользуйтесь [инструкцией](https://premium.gitbook.io/main/osnovnye-nastroiki/faq/obnovlenie-failov-skripta-na-servere/kak-obnovit-faily-na-servere#moduli-merchantov-i-avtovyplat)
{% endhint %}

## Настройки в личном кабинете мерчанта

{% hint style="warning" %}
Для обсуждения условий работы свяжитесь с [представителем сервиса](https://t.me/tronexpr).

**Дисклеймер**: при подключении вашего сайта к тому или иному сервису, пожалуйста, самостоятельно оценивайте возможные риски сотрудничества.
{% endhint %}

Свяжитесь с [представителем сервиса](https://t.me/tronexpr) для обсуждения условий работы и получения данных для входа.

{% hint style="warning" %}
На стороне мерчанта работа с разными методами и тарифами реализована отдельными аккаунтами в системе. Под каждый метод - отдельный аккаунт.
{% endhint %}

Вместе с доступами к таким аккаунтам представитель сервиса передает \
API Key и Sign Key.&#x20;

Сохраните полученные данные, они используются для работы модуля мерчанта в системе.

При помощи полученных от представителя мерчанта данных вы можете [авторизоваться в личный кабинет на сервисе](https://tronex.world/).

## Настройки модуля

В панели администратора создайте нового мерчанта в разделе "**Мерчанты**" ➔ "**Добавить мерчант".**

Выберите модуль **TronEx** в выпадающем списке в поле "**Модуль**", укажите название для модуля и нажмите "**Сохранить**".

<figure><img src="../../../.gitbook/assets/Screenshot 2026-08-24 135011.png" alt=""><figcaption></figcaption></figure>

Заполните указанные авторизационные поля.

<figure><img src="../../../.gitbook/assets/Screenshot 2026-08-24 135112.png" alt=""><figcaption></figcaption></figure>

**Домен** — оставьте поле пустым

**API ключ —** API Key полученный от представителя сервиса.

**Ключ подписи** — Sign Key полученный от представителя сервиса.

{% hint style="info" %}
Убедитесь, что оба ключа относятся к одному аккаунту на стороне TronEx.
{% endhint %}

## Типы мерчанта

Каждый из доступных методов работы будет зависеть от указанный в настройках модуля ключей и имеет рекомендованные настройки:

{% tabs %}
{% tab title="   VIETQR   " %}
<figure><img src="../../../.gitbook/assets/image (1032).png" alt=""><figcaption></figcaption></figure>

Тип мерчанта — **Payment Link** - Выдача реквизитов на странице оплаты мерчанта.

<figure><img src="../../../.gitbook/assets/image (1036).png" alt="" width="550"><figcaption></figcaption></figure>

Способ оплаты — **VietQR** - указать явно.
{% endtab %}

{% tab title="    PDF    " %}
<figure><img src="../../../.gitbook/assets/image (1046).png" alt=""><figcaption></figcaption></figure>

Тип мерчанта — **Requisites** - Реквизиты выводятся по шорткодам \[to\_account], \[dest\_tag].

<figure><img src="../../../.gitbook/assets/image (1055).png" alt=""><figcaption></figcaption></figure>

Способ оплаты:

* Автоматический — выбираемый метод зависит от XML обозначения валюты "Отдаю".
* Card2Card — выдается номер карты для оплаты переводом на карту.
* СБП — выдается номер телефона и банк для оплаты по СБП.

{% hint style="info" %}
Перечень соответствия XML кодов валют способам оплаты открывается по плашке "Автоматически".
{% endhint %}
{% endtab %}

{% tab title="   MOBCOM  " %}
<figure><img src="../../../.gitbook/assets/image (1046).png" alt=""><figcaption></figcaption></figure>

Тип мерчанта — **Requisites** - Реквизиты выводятся по шорткодам \[to\_account], \[dest\_tag].

<figure><img src="../../../.gitbook/assets/image (1071).png" alt=""><figcaption></figcaption></figure>

Способ оплаты — **Мобильная комерция** - указать явно.
{% endtab %}

{% tab title="      BT     " %}
<figure><img src="../../../.gitbook/assets/image (1046).png" alt=""><figcaption></figcaption></figure>

Тип мерчанта — **Requisites** - Реквизиты выводятся по шорткодам \[to\_account], \[dest\_tag].

<figure><img src="../../../.gitbook/assets/image (1055).png" alt=""><figcaption></figcaption></figure>

Способ оплаты:

* Автоматический — выбираемый метод зависит от XML обозначения валюты "Отдаю".
* Card2Card — выдается номер карты для оплаты переводом на карту.
* СБП — выдается номер телефона и банк для оплаты по СБП.

{% hint style="info" %}
Перечень соответствия XML кодов валют способам оплаты открывается по плашке "Автоматически".
{% endhint %}
{% endtab %}
{% endtabs %}

## Особые поля

<figure><img src="../../../.gitbook/assets/image (1078).png" alt=""><figcaption></figcaption></figure>

Банк — передача информации о банке с которого клиент будет проводить оплата.&#x20;

Можно выбрать банк явно или выбрать дополнительное поле давая клиенту самостоятельный выбор.

<details>

<summary>Пример создания такого дополнительного поля.</summary>

Такое поле должно быть создано как [дополнительное поле валюты](https://premium.gitbook.io/main/osnovnye-nastroiki/valyuty-i-napravleniya-obmena/dopolnitelnye-polya#dopolnitelnye-polya-dlya-valyuty) с типом "Выбор".&#x20;

Важно указывать значения соответствующие предлагаемым в модуле, например в скобках. Вместе с тем, можно указать любые названия банков на русском.

Не забудьте указать для такого поля уникальный ID, любой. Это нужно для отображения такого поля в селекторе в настройках модуля мерчанта.

<figure><img src="../../../.gitbook/assets/image (1085).png" alt=""><figcaption></figcaption></figure>

</details>

<figure><img src="../../../.gitbook/assets/image (1075).png" alt=""><figcaption></figcaption></figure>

Индивидуальное время удаления неоплаченных заявок — количество минут, через которое неоплаченная заявка будет отменена на стороне мерчанта.&#x20;

{% hint style="info" %}
Проверьте, чтобы такое время не было меньше вашего стандартного времени удаления неоплаченной заявки.
{% endhint %}

**Cron-файл -** [создайте задание](https://premium.gitbook.io/main/osnovnye-nastroiki/faq/kak-sozdat-zadanie-cron-na-servere) с такой ссылкой на сервер&#x435;**.**

## Продолжение настройки

Дополнительные настройки модуля выполняются согласно [общей инструкции по настройке](https://premium.gitbook.io/rukovodstvo-polzovatelya/osnovnye-nastroiki/merchanty-i-avtovyplaty/merchanty/obshie-nastroiki-merchantov).
