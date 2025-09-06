# Rapira

{% hint style="info" %}
Если вам необходимо обновить модуль на сервере - воспользуйтесь [инструкцией](https://premium.gitbook.io/main/osnovnye-nastroiki/faq/obnovlenie-failov-skripta-na-servere/kak-obnovit-faily-na-servere#moduli-merchantov-i-avtovyplat)
{% endhint %}

## Настройки в личном кабинете мерчанта

Пройдите регистрацию в системе [Rapira](https://rapira.net/).

Зайдите в личный кабинет, пройдите верификацию на сервисе и подключите двухфакторную аутентификацию (GoogleAuth).

<figure><img src="../../../.gitbook/assets/image (1406).png" alt=""><figcaption></figcaption></figure>

После успешного прохождения верификации и подключения GoogleAuth перейдите в раздел "**Настройки - API-ключи**" и нажмите кнопку "**Создать API-ключ**".

<figure><img src="../../../.gitbook/assets/image (1404).png" alt=""><figcaption></figcaption></figure>

Сохраните данные сгенерированного API-ключа.

<figure><img src="../../../.gitbook/assets/image (1405).png" alt="" width="490"><figcaption></figcaption></figure>

## Настройки модуля

В панели администратора в разделе "**Мерчанты**" -> "**Мерчанты"** нажмите кнопку "**Добавить**" и выберите Rapira Crypto.

<figure><img src="../../../.gitbook/assets/image (1407).png" alt=""><figcaption></figcaption></figure>

Заполните указанные авторизационные поля.

<figure><img src="../../../.gitbook/assets/image (1408).png" alt=""><figcaption></figcaption></figure>

**Privatу Key** - приватный ключ, сгенерированный Rapira при создании API-ключа

**UID** - уникальный идентификатор пользователя (UID), сгенерированный Rapira при создании API-ключа

## Особые поля

<figure><img src="../../../.gitbook/assets/image (1409).png" alt=""><figcaption></figcaption></figure>

**Требуемое количество подтверждений транзакции** - подтвержденная транзакция означает то, что она включена в блок и, следовательно, в цепочку блоков. Она проверена и зарегистрирована, платеж обработан, его нельзя изменить или отменить. Чтобы стать законной, операция должна получить определенное количество подтверждений. Каждое новое подтверждение в геометрической прогрессии снижает риск отмены самой транзакции.

{% hint style="info" %}
* <mark style="color:green;">Рекомендуется!</mark> Установите значение 0, чтобы заявка считалась оплаченной только после получения требуемого количество подтверждений на бирже
* <mark style="color:red;">Не рекомендуется!</mark> Если установить значение отличное от 0, то обменник будет менять статус заявки на "Оплаченная" согласно этой настройке, несмотря на статус транзакции, который отображается в истории платежей биржи. При установке подобной опции, вы принимаете возможные риски на себя.
{% endhint %}

## Продолжение настройки

Далее произведите настройку мерчанта следуя [общей инструкции по настройке](https://premium.gitbook.io/rukovodstvo-polzovatelya/osnovnye-nastroiki/merchanty-i-avtovyplaty/merchanty/obshie-nastroiki-merchantov).
