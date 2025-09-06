---
hidden: true
noIndex: true
---

# Garantex Crypto

{% hint style="info" %}
Если вам необходимо обновить модуль на сервере — воспользуйтесь [инструкцией](https://premium.gitbook.io/rukovodstvo-polzovatelya/osnovnye-nastroiki/faq/kak-obnovit-faily-na-servere#moduli-merchantov)
{% endhint %}

## Настройки в личном кабинете мерчанта

Пройдите регистрацию на сайте [Garantex](https://garantex.org/). После подтверждения регистрации сервисом, авторизуйтесь в личном кабинете. Включите 2FA для вашего аккаунта.

<figure><img src="../../../.gitbook/assets/image (700).png" alt=""><figcaption></figcaption></figure>

После входа в личный кабинет отправьте запрос в техподдержку для включения API для вашего аккаунта.&#x20;

<figure><img src="../../../.gitbook/assets/image (699).png" alt="" width="516"><figcaption></figcaption></figure>

<figure><img src="../../../.gitbook/assets/image (695).png" alt="" width="325"><figcaption></figcaption></figure>

После открытия доступа к API перейдите в раздел "Настройки" и создайте новый доступ.

<figure><img src="../../../.gitbook/assets/image (696).png" alt="" width="563"><figcaption></figcaption></figure>

Сохраните данные, выделенные рамкой в текстовый файл.

<figure><img src="../../../.gitbook/assets/image (702).png" alt=""><figcaption></figcaption></figure>

Перейдите к созданному ключу по кнопке "**Просмотр / Изменение**".

<figure><img src="../../../.gitbook/assets/image (703).png" alt="" width="563"><figcaption></figcaption></figure>

Для работы с мерчантом на прием средств достаточно метода "**Readonly**", не отмечайте другие методы. Желательно указать IP-адрес вашего сервера в поле "IPs" для большей безопасности работы с мерчантом.

<figure><img src="../../../.gitbook/assets/image (704).png" alt=""><figcaption></figcaption></figure>

## Настройки модуля

В панели администратора создайте нового мерчанта в разделе "**Мерчанты**" -> "**Добавить мерчант".**

Выберите модуль Garantex в выпадающем списке в поле "**Модуль**", укажите название для модуля и нажмите "**Сохранить**".\


<figure><img src="../../../.gitbook/assets/image (697).png" alt="" width="494"><figcaption></figcaption></figure>

Заполните указанные авторизационные поля. В качестве хоста можете выбрать любой домен.

<figure><img src="../../../.gitbook/assets/image (698).png" alt="" width="414"><figcaption></figcaption></figure>

**Private Key** — приватный ключ, сгенерированный в Garantex при создании доступа к API (поле "**Приватный ключ**")

**UID** — ID доступа, сгенерированный в Garantex при создании доступа к API (поле "**API UID**")

## Особые поля

<figure><img src="../../../.gitbook/assets/image (705).png" alt=""><figcaption></figcaption></figure>

* "**Требуемое количество подтверждений транзакции**" — подтвержденная транзакция означает то, что она включена в блок и, следовательно, в цепочку блоков. Она проверена и зарегистрирована, платеж обработан, его нельзя изменить или отменить. Чтобы стать законной, операция должна получить определенное количество подтверждений. Каждое новое подтверждение в геометрической прогрессии снижает риск отмены самой транзакции.

{% hint style="info" %}
- <mark style="color:green;">Рекомендуется!</mark> Установите значение 0, чтобы заявка считалась оплаченной только после получения требуемого количество подтверждений на бирже
- <mark style="color:red;">Не рекомендуется!</mark> Если установить значение отличное от 0, то обменник будет менять статус заявки на "Оплаченная" согласно этой настройке, несмотря на статус транзакции, который отображается в истории платежей биржи. При установке подобной опции, вы принимаете возможные риски на себя.
{% endhint %}

## Продолжение настройки

Далее произведите настройку мерчанта следуя [общей инструкции по настройке](https://premium.gitbook.io/rukovodstvo-polzovatelya/osnovnye-nastroiki/merchanty-i-avtovyplaty/merchanty/obshie-nastroiki-merchantov).\
