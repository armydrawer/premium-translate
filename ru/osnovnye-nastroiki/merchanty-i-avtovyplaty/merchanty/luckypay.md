# Luckypay

{% hint style="info" %}
Если вам необходимо обновить модуль на сервере — воспользуйтесь [инструкцией](https://premium.gitbook.io/main/osnovnye-nastroiki/faq/obnovlenie-failov-skripta-na-servere/kak-obnovit-faily-na-servere#moduli-merchantov-i-avtovyplat)
{% endhint %}

## Настройки в личном кабинете

Зарегистрируйтесь на сервисе [Luckypay](https://luckypay.io/). Авторизуйтесь в личном кабинете, перейдите в раздел "**Терминалы**", выберите существующий терминал или создайте новый и скопируйте указанный в его настройках API-ключ.

<figure><img src="../../../.gitbook/assets/image (2158).png" alt="" width="563"><figcaption></figcaption></figure>

## Настройки в личном кабинете мерчанта

{% hint style="warning" %}
Для обсуждения условий и подключения, свяжитесь с [представителем сервиса](https://t.me/luckypay_accounting).

**Дисклеймер**: при подключении вашего сайта к тому или иному сервису, самостоятельно пожалуйста оценивайте возможные риски сотрудничества.
{% endhint %}

Авторизуйтесь в личном кабинете мерчанта и обязательно укажите URL из настроек модуля мерчанта (Callback URL) в поле "**Статус заказа купить**" в разделе "**Терминалы**".

<figure><img src="../../../.gitbook/assets/image (2049).png" alt="" width="563"><figcaption></figcaption></figure>

<figure><img src="../../../.gitbook/assets/image (17).png" alt="" width="563"><figcaption></figcaption></figure>

## Настройки модуля

В панели администратора создайте нового мерчанта в разделе "**Мерчанты**" -> "**Добавить мерчант".**

Выберите Luckypay в выпадающем списке в поле "**Модуль**", укажите название для модуля и нажмите "**Сохранить**".

<figure><img src="../../../.gitbook/assets/image (319).png" alt="" width="418"><figcaption></figcaption></figure>

Заполните указанные авторизационные поля.

<figure><img src="../../../.gitbook/assets/Arc_5NJ6WqIhsR (1).png" alt="" width="435"><figcaption></figcaption></figure>

**API ключ** — ключ, ранее скопированный из личного кабинета Luckypay

## Особые поля

<div><figure><img src="../../../.gitbook/assets/image (316).png" alt="" width="217"><figcaption></figcaption></figure> <figure><img src="../../../.gitbook/assets/image (317) (1).png" alt="" width="215"><figcaption></figcaption></figure></div>

**Способ оплаты** — выберите необходимый способ для приема средств от клиента (перечень в ваших настройках можете отличаться от вышеуказанного)

## Продолжение настройки

Далее произведите настройку мерчанта следуя [общей инструкции по настройке](https://premium.gitbook.io/rukovodstvo-polzovatelya/osnovnye-nastroiki/merchanty-i-avtovyplaty/merchanty/obshie-nastroiki-merchantov).<br>
