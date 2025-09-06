---
hidden: true
noIndex: true
---

# Premium Wallet (в разработке)



{% hint style="info" %}
Если вам необходимо обновить модуль на сервере — воспользуйтесь [инструкцией](https://premium.gitbook.io/rukovodstvo-polzovatelya/osnovnye-nastroiki/faq/kak-obnovit-faily-na-servere#moduli-merchantov)
{% endhint %}

## Настройки в личном кабинете мерчанта

{% hint style="warning" %}
Для обсуждения условий и подключения, свяжитесь с [представителем сервиса](https://t.me/ipichipich).

**Дисклеймер**: при подключении вашего сайта к тому или иному сервису, самостоятельно пожалуйста оценивайте возможные риски сотрудничества.
{% endhint %}

После получения реквизитов для входа от представителя сервиса, авторизуйтесь в [ЛК Premium Wallet](https://pw-api.elastoo.com/login). Перейдите в раздел "**Настройки**".

В личном кабинете заполните поле "**Webhook url**" и скопируйте данные из полей "**Client ID**" и "**API Secret**" в буфер обмена или текстовый файл.

<figure><img src="../../../.gitbook/assets/image (2165).png" alt=""><figcaption></figcaption></figure>

{% hint style="warning" %}
В поле "**Webhook url**" укажите URL из поля "**Status URL"** из настроек модуля мерчанта

![](<../../../.gitbook/assets/image (2164).png>)
{% endhint %}

## Настройки модуля

В панели администратора создайте нового мерчанта в разделе "**Мерчанты**" ➔ "**Добавить мерчант".**

Выберите Premium Wallet в выпадающем списке в поле "**Модуль**", укажите название для модуля и нажмите "**Сохранить**".

<figure><img src="../../../.gitbook/assets/image (2163).png" alt="" width="446"><figcaption></figcaption></figure>

Заполните указанные авторизационные поля.

<figure><img src="../../../.gitbook/assets/image (2162).png" alt="" width="430"><figcaption></figcaption></figure>

**Домен** — ссылка, выданная вам представителем сервиса Premium Wallet

**Client ID** — ID, скопированный ранее в ЛК мерчанта

**Секретный ключ** — ключ, скопированный ранее в ЛК мерчанта

## Продолжение настройки

Далее произведите настройку мерчанта следуя [общей инструкции по настройке](https://premium.gitbook.io/rukovodstvo-polzovatelya/osnovnye-nastroiki/merchanty-i-avtovyplaty/merchanty/obshie-nastroiki-merchantov).\
