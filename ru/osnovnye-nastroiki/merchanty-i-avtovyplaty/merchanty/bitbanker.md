# Bitbanker

{% hint style="info" %}
Если вам необходимо обновить модуль на сервере — воспользуйтесь [инструкцией](https://premium.gitbook.io/main/osnovnye-nastroiki/faq/obnovlenie-failov-skripta-na-servere/kak-obnovit-faily-na-servere#moduli-merchantov-i-avtovyplat)
{% endhint %}

{% hint style="success" %}
По всем вопросам, связанным с работой сервиса, просим обращаться в чат поддержки на сайте [Bitbanker](https://bitbanker.org)
{% endhint %}

## Настройки в личном кабинете мерчанта

[Зарегистрируйтесь](https://app.bitbanker.org/auth/register) на сервисе и авторизуйтесь в личном кабинете. Перейдите в раздел API.

<figure><img src="../../../.gitbook/assets/image (2007).png" alt="" width="222"><figcaption></figcaption></figure>

Скопируйте указанный API Key в буфер обмена или текстовый файл.

<figure><img src="../../../.gitbook/assets/image (2006).png" alt="" width="549"><figcaption></figcaption></figure>

Для работы коллбэка для изменения статуса заявки укажите URL из настроек модуля мерчанта в разделе "**API**" и добавьте в вайтлист вашего файрвола все IP-адреса мерчанта, с которых они отправляют коллбэки (список адресов запрашивайте напрямую у мерчанта).

<figure><img src="../../../.gitbook/assets/image (203).png" alt="" width="563"><figcaption></figcaption></figure>

<figure><img src="../../../.gitbook/assets/image (202).png" alt="" width="563"><figcaption></figcaption></figure>

## Настройки модуля

В панели администратора создайте нового мерчанта в разделе "**Мерчанты**" -> "**Добавить мерчант".**

Выберите Bitbanker в выпадающем списке в поле "**Модуль**", укажите название для модуля и нажмите "**Сохранить**".

<figure><img src="../../../.gitbook/assets/image (232).png" alt="" width="417"><figcaption></figcaption></figure>

Заполните указанные авторизационные поля.

<figure><img src="../../../.gitbook/assets/image (233).png" alt="" width="464"><figcaption></figcaption></figure>

**API ключ** — API Key, скопированный ранее в ЛК мерчанта

## Особые поля

<figure><img src="../../../.gitbook/assets/image (234).png" alt="" width="563"><figcaption></figcaption></figure>

**Сеть** — выберите подходящую сеть для приема средств от клиента

{% hint style="warning" %}
Для каждого используемого способа оплаты необходимо создать отдельную копию модуля мерчанта, в которой выбрать соответствующую сеть, а затем подключить эту копию на вкладке "**Мерчанты и выплаты**" в настройках направления обмена, где в валюте "**Отдаю**" будет подходящая валюта
{% endhint %}

## Продолжение настройки

Далее произведите настройку мерчанта следуя [общей инструкции по настройке](https://premium.gitbook.io/rukovodstvo-polzovatelya/osnovnye-nastroiki/merchanty-i-avtovyplaty/merchanty/obshie-nastroiki-merchantov).\
