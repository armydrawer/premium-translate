# Merchant001

{% hint style="danger" %}
<mark style="color:red;">Перед настройкой автовыплат обязательно прочитайте</mark> [<mark style="color:blue;">предупреждение о рисках</mark>](https://premium.gitbook.io/main/osnovnye-nastroiki/merchanty-i-avtovyplaty/avtovyplaty/preduprezhdenie-o-riskakh)<mark style="color:blue;">!</mark>
{% endhint %}

{% hint style="info" %}
Если вам необходимо обновить модуль на сервере — воспользуйтесь [инструкцией](https://premium.gitbook.io/main/osnovnye-nastroiki/faq/obnovlenie-failov-skripta-na-servere/kak-obnovit-faily-na-servere#moduli-merchantov-i-avtovyplat)
{% endhint %}

## Настройки в личном кабинете мерчанта

{% hint style="warning" %}
Для обсуждения условий и подключения, свяжитесь с [представитлем сервиса](https://t.me/merch001online).

**Дисклеймер**: при подключении вашего сайта к тому или иному сервису, самостоятельно пожалуйста оценивайте возможные риски сотрудничества.
{% endhint %}

В [личном кабинете мерчанта](https://app.merchant001.io/merchant/api) сгенерируйте токен для авторизации к API мерчанта и скопируйте его в буфер обмена или сохраните в текстовый файл.

<figure><img src="../../../.gitbook/assets/image (1717).png" alt=""><figcaption></figcaption></figure>

## **Настройки модуля**

В панели администратора создайте нового мерчанта в разделе "**Автовыплаты**" -> "**Добавить автовыплату".**

Выберите Merchant001 в выпадающем списке в поле "**Модуль**", укажите название для модуля и нажмите "**Сохранить**".

<figure><img src="../../../.gitbook/assets/image (1628).png" alt="" width="449"><figcaption></figcaption></figure>

Заполните указанные авторизационные поля.

<figure><img src="../../../.gitbook/assets/image (1629).png" alt="" width="491"><figcaption></figcaption></figure>

**Токен** — домен, сгенерированный в ЛК Merchant001 после создания доступа к API

## Особые поля

<figure><img src="../../../.gitbook/assets/image (1630).png" alt="" width="430"><figcaption></figcaption></figure>

**Способ оплаты** — доступные варианты выплат (при выплате происходит конвертация с вашего счета у мерчанта из USDT в RUB по рыночному курсу)

При использовании метода "**Перевод по СБП**" необходимо передавать мерчанту название банка, которое будет выбирать клиент в форме обмена.

{% hint style="success" %}
Если вы используете валюту с уже указанным в названии банком (например, **СБП Т-Банк** или **СБП Сбер**) — доп. поле создавать <mark style="color:green;">**не требуется**</mark> (будет передаваться само название валюты). Во всех остальных случаях создание доп. поля необходимо.
{% endhint %}

Для этого создайте новое дополнительное поле в разделе "**Валюты**" -> "**Доп. поля валют**" и настройте его согласно скриншоту ниже:

<figure><img src="https://premium.gitbook.io/~gitbook/image?url=https%3A%2F%2F2574066779-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252Fm9kqZXsNykrN6VyxxXBO%252Fuploads%252FEbpC5wuOdzNjbcWl6uMw%252Fimage.png%3Falt%3Dmedia%26token%3Df492a8b8-4299-4c37-8fb4-281b702e4a07&#x26;width=768&#x26;dpr=4&#x26;quality=100&#x26;sign=cc43be2f&#x26;sv=1" alt="" width="563"><figcaption></figcaption></figure>

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

<figure><img src="https://premium.gitbook.io/~gitbook/image?url=https%3A%2F%2F2574066779-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252Fm9kqZXsNykrN6VyxxXBO%252Fuploads%252FdpeqgjfYafIq473jYRtm%252Fimage.png%3Falt%3Dmedia%26token%3D8a4d7e3a-43ad-41ad-ab33-85685cc48b56&#x26;width=768&#x26;dpr=4&#x26;quality=100&#x26;sign=6b7a4abe&#x26;sv=1" alt="" width="375"><figcaption></figcaption></figure>

Или в настройках валюты на вкладке "**Доп. поля**":

<figure><img src="https://premium.gitbook.io/~gitbook/image?url=https%3A%2F%2F2574066779-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252Fm9kqZXsNykrN6VyxxXBO%252Fuploads%252F95K4xQBIe6IxZomKPUAn%252Fimage.png%3Falt%3Dmedia%26token%3D33e8957f-3ee1-4075-8d13-12897756eacb&#x26;width=768&#x26;dpr=4&#x26;quality=100&#x26;sign=788cd580&#x26;sv=1" alt="" width="375"><figcaption></figcaption></figure>

Cохраните изменения.

После этого поле будет отображаться в форме обмена и клиенту будет необходимо выбрать один из вариантов при создании заявки.

<figure><img src="https://premium.gitbook.io/~gitbook/image?url=https%3A%2F%2F2574066779-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252Fm9kqZXsNykrN6VyxxXBO%252Fuploads%252F7UGhEmtrSnAHov7P8Z89%252Fimage.png%3Falt%3Dmedia%26token%3D6fcc59ea-b292-4803-8b6f-c547a73b4fe5&#x26;width=768&#x26;dpr=4&#x26;quality=100&#x26;sign=5f0e9aa&#x26;sv=1" alt="" width="375"><figcaption></figcaption></figure>

## Продолжение настройки

Далее произведите настройку мерчанта следуя [общей инструкции по настройке](https://premium.gitbook.io/rukovodstvo-polzovatelya/osnovnye-nastroiki/merchanty-i-avtovyplaty/avtovyplaty/obshie-nastroiki-merchantov-avtovyplat).
