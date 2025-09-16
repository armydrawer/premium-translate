# PayCrown

{% hint style="info" %}
Если вам необходимо обновить модуль на сервере — воспользуйтесь [инструкцией](https://premium.gitbook.io/main/osnovnye-nastroiki/faq/obnovlenie-failov-skripta-na-servere/kak-obnovit-faily-na-servere#moduli-merchantov-i-avtovyplat)
{% endhint %}

## Настройки в личном кабинете мерчанта

{% hint style="warning" %}
Для обсуждения условий работы свяжитесь с [представителем сервиса](https://t.me/paycrown_chief).

**Дисклеймер**: при подключении вашего сайта к тому или иному сервису, пожалуйста, самостоятельно оценивайте возможные риски сотрудничества.
{% endhint %}

Зарегистрируйтесь на сервисе PayCrown с помощью [представителя сервиса](https://t.me/paycrown_chief) и запросите API-ключи для подключения к Premium Exchanger.

## Настройки модуля

В панели администратора создайте нового мерчанта в разделе "**Мерчанты**" ➔ "**Добавить мерчант".**

Выберите PayCrown в выпадающем списке в поле "**Модуль**", укажите название для модуля и нажмите "**Сохранить**".

<figure><img src="../../../.gitbook/assets/image (1) (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt="" width="422"><figcaption></figcaption></figure>

Заполните указанные авторизационные поля.

<figure><img src="../../../.gitbook/assets/image (3) (1) (1) (1) (1).png" alt="" width="439"><figcaption></figcaption></figure>

**Домен** — оставьте поле пустым

**ID мерчанта** — ID, переданный вам представителем PayCrown

**API ключ** — публичный ключ, переданный вам представителем PayCrown

**Секретный ключ** — секретный ключ, переданный вам представителем PayCrown

## Особые поля

<figure><img src="../../../.gitbook/assets/image (2) (1) (1) (1) (1) (1) (1) (1) (1).png" alt="" width="439"><figcaption></figcaption></figure>

**Способ оплаты** — метод выдачи реквизитов:

* **C2C** — метод временно не используется
* **Invoice** — выдача номера карты RUB
* **SBP** — выдача номер телефона для оплаты по СБП

## Продолжение настройки

Далее произведите настройку мерчанта следуя [общей инструкции по настройке](https://premium.gitbook.io/rukovodstvo-polzovatelya/osnovnye-nastroiki/merchanty-i-avtovyplaty/merchanty/obshie-nastroiki-merchantov).\
