---
hidden: true
noIndex: true
noRobotsIndex: true
---

# XPay

{% hint style="info" %}
Если вам необходимо обновить модуль на сервере — воспользуйтесь [инструкцией](https://premium.gitbook.io/main/osnovnye-nastroiki/faq/obnovlenie-failov-skripta-na-servere/kak-obnovit-faily-na-servere#moduli-merchantov-i-avtovyplat)
{% endhint %}

## Настройки в личном кабинете мерчанта

{% hint style="warning" %}
Для подключения к сервису напишите [менеджеру](https://t.me/premiumexchanger_business) — он создаст чат с вами и представителями платежного сервиса для обсуждения условий подключения, тарифов и других вопросов
{% endhint %}

Пройдите регистрацию и верификацию в сервисе Xpay. Перейдите в раздел "**Мерчанты**" и нажмите кнопку "**Создать мерчант**".

<figure><img src="../../../.gitbook/assets/image (1826).png" alt=""><figcaption></figcaption></figure>

Сохраните сгенерированный ключ в текстовый файл и нажмите кнопку "**Готово**".

## Настройки модуля

В панели администратора создайте нового мерчанта в разделе "**Мерчанты**" -> "**Добавить мерчант".**

Выберите XPayPro в выпадающем списке в поле "**Модуль**", укажите название для модуля и нажмите "**Сохранить**".

<figure><img src="../../../.gitbook/assets/image (1822).png" alt="" width="563"><figcaption></figcaption></figure>

Заполните указанные авторизационные поля.

<figure><img src="../../../.gitbook/assets/image (1823).png" alt="" width="421"><figcaption></figcaption></figure>

**API ключ** — ключ, сгенерированный в ЛК XPay

**Host** — выберите домен для работы с мерчантом

## Особые поля

<figure><img src="../../../.gitbook/assets/image (1825).png" alt="" width="278"><figcaption></figcaption></figure>

**Способ оплаты** — выберите тип оплаты для клиента: СБП или банковская карта

<figure><img src="../../../.gitbook/assets/image (1824).png" alt="" width="327"><figcaption></figcaption></figure>

**Банк** — выберите банк, реквизиты которого будут выдаваться клиентам в заявках для оплаты на них

{% hint style="warning" %}
Для **каждого используемого способа оплаты** необходимо создать отдельную копию модуля мерчанта, в которой выбрать соответствующий способ, а затем подключить эту копию на вкладке "**Мерчанты и выплаты**" в настройках направления обмена, где в валюте "**Отдаю**" будет подходящая валюта
{% endhint %}

## Продолжение настройки

Далее произведите настройку мерчанта следуя [общей инструкции по настройке](https://premium.gitbook.io/rukovodstvo-polzovatelya/osnovnye-nastroiki/merchanty-i-avtovyplaty/merchanty/obshie-nastroiki-merchantov).<br>
