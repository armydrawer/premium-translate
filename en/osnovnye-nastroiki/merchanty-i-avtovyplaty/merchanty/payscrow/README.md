# Payscrow

{% hint style="info" %}
Если вам необходимо обновить модуль на сервере — воспользуйтесь [инструкцией](https://premium.gitbook.io/main/osnovnye-nastroiki/faq/obnovlenie-failov-skripta-na-servere/kak-obnovit-faily-na-servere#moduli-merchantov-i-avtovyplat)
{% endhint %}

{% hint style="info" %}
Для отображения в заявке для клиента ФИО владельца карты, выданной мерчантом, добавьте шорткод \[dest\_tag] в инструкции в настройках мерчанта

![](<../../../../.gitbook/assets/image (1686).png>)
{% endhint %}

## Настройки в личном кабинете мерчанта

Пройдите регистрацию в системе [Payscrow](https://payscrow.io/). Авторизуйтесь в личном кабинете мерчанта и перейдите в раздел "**Настройки API**".

<figure><img src="../../../../.gitbook/assets/image (598).png" alt=""><figcaption></figcaption></figure>

В разделе будут указаны ключи для доступа к API. Сохраните их в txt-файл.

<figure><img src="../../../../.gitbook/assets/image (599).png" alt="" width="563"><figcaption></figcaption></figure>

{% hint style="warning" %}
Для этого мерчанта проверка платежей для смену статуса заявок доступна как по колбэку, так и по заданию cron.

![](<../../../../.gitbook/assets/image (1682).png>)

При использовании cron — создайте задание на сервере по [инструкции](https://premium.gitbook.io/main/osnovnye-nastroiki/faq/kak-sozdat-zadanie-cron-na-servere)

При использовании колбэка — добавьте URL из строки "**STATUS URL**" в поле "**Статус покупки**" в ЛК мерчанта (раздел "**Настройки API"**)

![](<../../../../.gitbook/assets/image (1685).png>)
{% endhint %}

## Настройки модуля

В панели администратора создайте нового мерчанта в разделе "**Мерчанты**" -> "**Добавить мерчант".**

Выберите Payscrow в выпадающем списке в поле "**Модуль**", укажите название для модуля и нажмите "**Сохранить**".

<figure><img src="../../../../.gitbook/assets/image (596).png" alt="" width="461"><figcaption></figcaption></figure>

Заполните указанные авторизационные поля.

<figure><img src="../../../../.gitbook/assets/image (597).png" alt="" width="449"><figcaption></figcaption></figure>

**Домен** — домен, выданный Payscrow после создания доступа к API (для каждого клиента выделяется отдельный домен вида `ec69bb31.merchant.payscrow.io`)

**Публичный ключ** — API ключ, сгенерированный в ЛК Payscrow

**Секретный ключ** — ключ подписи, сгенерированный в ЛК Payscrow

## Особые поля

<div><figure><img src="../../../../.gitbook/assets/image (600).png" alt="" width="482"><figcaption></figcaption></figure> <figure><img src="../../../../.gitbook/assets/image (593).png" alt="" width="476"><figcaption></figcaption></figure></div>

<div><figure><img src="../../../../.gitbook/assets/image (593).png" alt="" width="476"><figcaption></figcaption></figure> <figure><img src="../../../../.gitbook/assets/image (594).png" alt="" width="479"><figcaption></figcaption></figure></div>

**Способ оплаты** — доступные типы выдачи реквизитов для клиентов (минимальная сумма для заявки - 500 RUB)

* **\[BankCard] Smart order** — автоматический выбор банка, определеямый по номеру карты клиента (для этого способа в настройках принимаемой валюты для должен быть активирован параметр **"Выводить поле "Со счета"**" )

<figure><img src="../../../../.gitbook/assets/image (592).png" alt="" width="563"><figcaption></figcaption></figure>

* **\[BankCard, RUB] {название\_банка}** — выдача номера карты указанного банка
* **\[BankCard, RUB] Любой банк РФ** — выдача номера карты любого банка
* **\[SBP,RUB] СБП** — выдача номера телефона для оплаты по нему
* **\[SBP,RUB] СБП {название\_банка}** — выдача номера телефона для оплаты по нему, к которому привязана карта выбранного банка

## Продолжение настройки

Далее произведите настройку мерчанта следуя [общей инструкции по настройке](https://premium.gitbook.io/rukovodstvo-polzovatelya/osnovnye-nastroiki/merchanty-i-avtovyplaty/merchanty/obshie-nastroiki-merchantov).\
