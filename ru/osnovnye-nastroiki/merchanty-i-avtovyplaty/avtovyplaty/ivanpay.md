# Ivanpay



{% hint style="danger" %}
<mark style="color:red;">Перед настройкой автовыплат обязательно прочитайте</mark> [<mark style="color:blue;">предупреждение о рисках</mark>](https://premium.gitbook.io/main/osnovnye-nastroiki/merchanty-i-avtovyplaty/avtovyplaty/preduprezhdenie-o-riskakh)<mark style="color:blue;">!</mark>
{% endhint %}

{% hint style="info" %}
Если вам необходимо обновить модуль на сервере — воспользуйтесь [инструкцией](https://premium.gitbook.io/rukovodstvo-polzovatelya/osnovnye-nastroiki/faq/kak-obnovit-faily-na-servere#moduli-avtovyplat)
{% endhint %}

## Настройки в личном кабинете мерчанта <a href="#nastroiki-v-lichnom-kabinete-merchanta" id="nastroiki-v-lichnom-kabinete-merchanta"></a>

{% hint style="warning" %}
Для обсуждения условий и подключения, свяжитесь с [представителем сервиса](https://t.me/IvanPay_pro).

**Дисклеймер**: при подключении вашего сайта к тому или иному сервису, самостоятельно пожалуйста оценивайте возможные риски сотрудничества.
{% endhint %}

Пройдите регистрацию на сервисе [IvanPay](https://ivanpay.com/).

<figure><img src="../../../.gitbook/assets/image (214).png" alt=""><figcaption></figcaption></figure>

В личном кабинете мерчанта скопируйте данные из поля "**Ваш API-адрес**", а также API-ключ, выданный вам представителем сервиса.

<figure><img src="../../../.gitbook/assets/image (215).png" alt=""><figcaption></figcaption></figure>

## Настройки модуля <a href="#nastroiki-modulya" id="nastroiki-modulya"></a>

В панели администратора создайте нового мерчанта в разделе "**Автовыплаты**" -> "**Добавить автовыплату".**

Выберите Ivanpay в выпадающем списке в поле "**Модуль**", укажите название для модуля и нажмите "**Сохранить**".

<figure><img src="../../../.gitbook/assets/Arc_OcgFEcjunz.png" alt="" width="426"><figcaption></figcaption></figure>

Заполните указанные авторизационные поля.

<figure><img src="../../../.gitbook/assets/image (293).png" alt="" width="421"><figcaption></figcaption></figure>

**Домен** — домен мерчанта, ранее скопированный в ЛК мерчанта из поля "**Ваш API-адрес**"

**API ключ** — **Ключ API**, переданный вам менеджером Ivanpay

## Особые поля

<figure><img src="../../../.gitbook/assets/выплата1.png" alt="" width="398"><figcaption></figcaption></figure>

<figure><img src="../../../.gitbook/assets/выплата2.png" alt="" width="399"><figcaption></figcaption></figure>

**Способ оплаты** — выберите необходимый способ для выплаты средств

{% hint style="warning" %}
Обратите внимание на особенность сервиса Ivanpay — **по возможности** выплата производится с карты банка, выбранного вами в настройках модуля, но при отсутствии карт выбранного банка выплата производится с карты другого банка, которая в данный момент имеется на сервисе (метод при этом не меняется и остается исходным — CARD или SBP)
{% endhint %}

При использовании метода **\[SBP] СБП** (без указания банка) необходимо передавать мерчанту название банка, которое будет выбирать клиент в форме обмена.

Для этого создайте новое дополнительное поле в разделе "**Валюты**" -> "**Доп. поля валют**" и настройте его согласно скриншоту ниже:

<figure><img src="../../../.gitbook/assets/image (1937).png" alt="" width="412"><figcaption></figcaption></figure>

Перечень банков, указываемых в поле "**Варианты**" для разных языковых версий:

{% tabs %}
{% tab title="Для ru-версии" %}
Альфа-Банк

СберБанк

Т-Банк

РНКБ

Открытие

Русский Стандарт

Авангард

Райффайзен

Газпромбанк

Почта банк

Россельхозбанк

РОСБАНК

Промсвязьбанк

МТС Банк

Совкомбанк

Банк Уралсиб

ОТП банк

ВТБ

Ак Барс Банк

Ozon Банк

Банк УБРиР

Экспобанк

Банк ЗЕНИТ

Примсоцбанк

ЮниКредит Банк

АО КБ ЮНИСТРИМ

Яндекс Банк

Банк Левобережный
{% endtab %}

{% tab title="Для en-версии" %}
Alfa-Bank

SberBank

T-Bank Bank

RNCB Bank

Otkritie

Russian Standart

Bank AVANGARD

Raiffeisenbank

Gazprombank

Pochta Bank

Rosselkhozbank

ROSBANK

Promsvyazbank

MTS Bank

Sovcombank

Bank Uralsib OTP

Bank VTB

Bank AK BARS

Bank OZON

Bank UBRD - Ural

Bank Expobank

Bank ZENIT

Primsotsbank

UniCredit Bank

UNISTREAM COMMERCIAL BANK

Yandex Bank

Bank Levoberezhny
{% endtab %}
{% endtabs %}

После этого добавьте доп. поле для валюты, выбранной для выплаты в этом направлении обмена, в настройках самого поля:

<figure><img src="../../../.gitbook/assets/image (289).png" alt="" width="386"><figcaption></figcaption></figure>

Или в настройках валюты на вкладке "**Доп. поля**":

<figure><img src="../../../.gitbook/assets/image (288).png" alt="" width="366"><figcaption></figcaption></figure>

Cохраните изменения.

После этого поле будет отображаться в форме обмена и клиенту будет необходимо выбрать один из вариантов при создании заявки.

<figure><img src="../../../.gitbook/assets/image (290).png" alt="" width="521"><figcaption></figcaption></figure>

## Продолжение настройки

Далее произведите настройку мерчанта следуя [общей инструкции по настройке](https://premium.gitbook.io/rukovodstvo-polzovatelya/osnovnye-nastroiki/merchanty-i-avtovyplaty/avtovyplaty/obshie-nastroiki-merchantov-avtovyplat).
