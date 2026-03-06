# PayPlay

{% hint style="info" %}
Если вам необходимо обновить модуль на сервере — воспользуйтесь [инструкцией](https://premium.gitbook.io/main/osnovnye-nastroiki/faq/obnovlenie-failov-skripta-na-servere/kak-obnovit-faily-na-servere#moduli-merchantov-i-avtovyplat)
{% endhint %}

## Настройки в личном кабинете мерчанта

{% hint style="warning" %}
Для обсуждения условий работы свяжитесь с [представителем сервиса](https://t.me/am_payplay).

**Дисклеймер**: при подключении вашего сайта к тому или иному сервису, пожалуйста, самостоятельно оценивайте возможные риски сотрудничества.
{% endhint %}

Зарегистрируйтесь на сервисе PayPlay с помощью представителя сервиса и авторизуйтесь в личном кабинете мерчанта.

## Настройки модуля

В панели администратора создайте нового мерчанта в разделе "**Мерчанты**" ➔ "**Добавить мерчант".**

Выберите PayPlay в выпадающем списке в поле "**Модуль**", укажите название для модуля и нажмите "**Сохранить**".

<figure><img src="../../../.gitbook/assets/изображение.png" alt="" width="376"><figcaption></figcaption></figure>

Заполните указанные авторизационные поля.

<figure><img src="../../../.gitbook/assets/изображение (1).png" alt="" width="401"><figcaption></figcaption></figure>

**Домен** — оставьте поле пустым

**API ключ** — API ключ, скопированный из ЛК PayPlay

**Slug** — ID, скопированный из ЛК PayPlay

**WT Token** — ID, скопированный из ЛК PayPlay

## Особые поля

<figure><img src="../../../.gitbook/assets/изображение (3) (1).png" alt=""><figcaption></figcaption></figure>

**Тип мерчанта** (выбранный пункт закрепляется за копией модуля, изменить его в дальнейшем для этой копии не получится):

* **Payment Link** — возвращает в заявке ссылку для оплаты по QR-коду, опция работает совместно с выбранным способом оплаты
* **Requisites** — возвращает карту или телефон для перевода средств в самой заявке через шорткод `[to_account]`

<figure><img src="../../../.gitbook/assets/изображение (2).png" alt="" width="497"><figcaption></figcaption></figure>

**Способ оплаты** — выберите необходимый способ для приема средств от клиента:

**Доп. поля** — использование [доп.поля валюты](https://premium.gitbook.io/main/osnovnye-nastroiki/valyuty-i-napravleniya-obmena/dopolnitelnye-polya#dopolnitelnye-polya-dlya-valyuty) из валюты "**Отдаю**" в направлении обмена для подбора реквизитов

**Способ оплаты** — ручной выбор валюты для подбора реквизитов по ней

## Продолжение настройки

Далее произведите настройку мерчанта следуя [общей инструкции по настройке](https://premium.gitbook.io/rukovodstvo-polzovatelya/osnovnye-nastroiki/merchanty-i-avtovyplaty/merchanty/obshie-nastroiki-merchantov).
