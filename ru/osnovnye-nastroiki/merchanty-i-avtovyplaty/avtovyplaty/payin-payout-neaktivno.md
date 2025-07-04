---
hidden: true
noIndex: true
---

# Payin-Payout (неактивно)

{% hint style="danger" %}
<mark style="color:red;">Перед настройкой автовыплат обязательно прочитайте</mark> [<mark style="color:blue;">предупреждение о рисках</mark>](https://premiumexchanger.com/wiki/preduprezhdenie-auto/)<mark style="color:blue;">!</mark>
{% endhint %}

{% hint style="info" %}
Если вам необходимо обновить модуль на сервере — воспользуйтесь [инструкцией](https://premium.gitbook.io/rukovodstvo-polzovatelya/osnovnye-nastroiki/faq/kak-obnovit-faily-na-servere#moduli-avtovyplat)
{% endhint %}

## Настройки в личном кабинете мерчанта

{% hint style="warning" %}
Для обсуждения условий и подключения, свяжитесь с [представитлем сервиса](https://t.me/Payin_payoutt).

**Дисклеймер**: при подключении вашего сайта к тому или иному сервису, самостоятельно пожалуйста оценивайте возможные риски сотрудничества.
{% endhint %}

## **Настройки модуля**

В панели администратора создайте нового мерчанта в разделе "**Автовыплаты**" -> "**Добавить автовыплату".**

Выберите Payin-Payout в выпадающем списке в поле "**Модуль**", укажите название для модуля и нажмите "**Сохранить**".

<figure><img src="../../../.gitbook/assets/image (1568).png" alt="" width="496"><figcaption></figcaption></figure>

Заполните указанные авторизационные поля.

<figure><img src="../../../.gitbook/assets/image (1569).png" alt="" width="455"><figcaption></figcaption></figure>

**Идентификатор** — ID учетной записи от ЛК Payin-Payout

{% hint style="warning" %}
Запросите в чате с Payin-Payout **Идентификатор учетной записи** (не магазина!)\
![](<../../../.gitbook/assets/image (525).png>)
{% endhint %}

**Приватный ключ** — содержимое из секретного ключа **`secret.key.pem`**, сгенерированного при создании пары ключей (см. инструкцию ниже).

{% hint style="warning" %}
Содержимое ключа просматривается в кодировке base64 и вставляется в поле **вместе со строками**:

**`-----BEGIN PRIVATE KEY-----`**&#x20;

**`-----END PRIVATE KEY-----`**
{% endhint %}

{% hint style="warning" %}
[Официальная документация по генерации ключа RSA для автовыплат](https://github.com/payin-payout/payout-api/blob/2.0/docs/README.md#%D0%B3%D0%B5%D0%BD%D0%B5%D1%80%D0%B0%D1%86%D0%B8%D1%8F-%D0%BF%D1%80%D0%B8%D0%B2%D0%B0%D1%82%D0%BD%D0%BE%D0%B3%D0%BE-%D0%BA%D0%BB%D1%8E%D1%87%D0%B0) (только для Windows).

Также по генерации ключей вы можете обращаться к мерчанту — [https://t.me/payinpayoutbot](https://t.me/payinpayoutbot)
{% endhint %}

<details>

<summary>Инструкция для MacOS:</summary>

На MacOS нужно:

* Установить [OpenSSL](https://macappstore.org/openssl/)
* Воспользоваться скриптом по генерации ключа:\
  `#!/bin/bash`\
  `openssl rand -out random 1048576`\
  `openssl genrsa -out secret.key.pem -rand random 1024`\
  `openssl rsa -in secret.key.pem -pubout -outform DER -out public.key`\
  `openssl rsa -inform pem -in secret.key.pem -outform der -out secret.key`
* открыть Терминал, ввести команду:\
  `bash /Users/`**`ваш_логин`**`/Desktop/openssl_gen_key.sh`
*   После генерации ключи будут находиться в папке пользователя

    <figure><img src="../../../.gitbook/assets/image (524).png" alt="" width="317"><figcaption></figcaption></figure>
* Отправьте в чат с Payin-Payout ключ **`public.key`**, чтобы они добавили его на свой сервер
* Скачайте и запустите приложение **TextEdit**
* Откройте в приложении файл **`secret.key.pem`**\
  ![](<../../../.gitbook/assets/image (526).png>)

- Скопируйте полное текстовое содержимое файла, включая\
  &#xNAN;**`-----BEGIN PRIVATE KEY-----`**` ``и`` `**`-----END PRIVATE KEY-----`**\
  ![](<../../../.gitbook/assets/image (527).png>)
- [Настройте cron](https://premium.gitbook.io/main/osnovnye-nastroiki/faq/kak-sozdat-zadanie-cron-na-servere) для работы модуля автовыплаты

</details>

## Особые поля

<figure><img src="../../../.gitbook/assets/image (1570).png" alt="" width="431"><figcaption></figcaption></figure>

**Способ оплаты** — выберите пункт "**Пополнение банковских карт**" (модуль выплачивает только рубли, минимальная сумма выплаты — 1000 RUB) (метод будет отображаться только после указания корректного идентификатора и ключа для авторизации в модуле)

{% hint style="warning" %}
Пункты из выпадающего списка в модуле будут доступны только после авторизации в модуле!
{% endhint %}

## Продолжение настройки

Далее произведите настройку мерчанта следуя [общей инструкции по настройке](https://premium.gitbook.io/rukovodstvo-polzovatelya/osnovnye-nastroiki/merchanty-i-avtovyplaty/avtovyplaty/obshie-nastroiki-merchantov-avtovyplat).
