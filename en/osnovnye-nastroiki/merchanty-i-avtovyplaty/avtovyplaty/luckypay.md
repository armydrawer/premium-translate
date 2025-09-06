# Luckypay

{% hint style="danger" %}
<mark style="color:red;">Перед настройкой автовыплат обязательно прочитайте</mark> [<mark style="color:blue;">предупреждение о рисках</mark>](https://premium.gitbook.io/main/osnovnye-nastroiki/merchanty-i-avtovyplaty/avtovyplaty/preduprezhdenie-o-riskakh)<mark style="color:blue;">!</mark>
{% endhint %}

{% hint style="info" %}
Если вам необходимо обновить модуль на сервере — воспользуйтесь [инструкцией](https://premium.gitbook.io/main/osnovnye-nastroiki/faq/obnovlenie-failov-skripta-na-servere/kak-obnovit-faily-na-servere#moduli-merchantov-i-avtovyplat)
{% endhint %}

## Настройки в личном кабинете мерчанта <a href="#nastroiki-v-lichnom-kabinete-merchanta" id="nastroiki-v-lichnom-kabinete-merchanta"></a>

{% hint style="warning" %}
Для обсуждения условий и подключения, свяжитесь с [представителем сервиса](https://t.me/luckypay_accounting).

**Дисклеймер**: при подключении вашего сайта к тому или иному сервису, самостоятельно пожалуйста оценивайте возможные риски сотрудничества.
{% endhint %}

Авторизуйтесь в [ЛК мерчанта](https://merchant.luckypay.io/). В разделе "**API**" скопируйте API-ключ для авторизации в модуле автовыплаты.

<figure><img src="../../../.gitbook/assets/image (2046).png" alt="" width="563"><figcaption></figcaption></figure>

Также обязательно укажите URL из настроек модуля автовыплаты (Callback URL) в поле "**Статус заказа продать**".

<figure><img src="../../../.gitbook/assets/image (2045).png" alt="" width="563"><figcaption></figcaption></figure>

<figure><img src="../../../.gitbook/assets/image (77).png" alt="" width="563"><figcaption></figcaption></figure>

## Настройки модуля <a href="#nastroiki-modulya" id="nastroiki-modulya"></a>

В панели администратора создайте нового мерчанта в разделе "**Автовыплаты**" -> "**Добавить автовыплату".**

Выберите Luckypay в выпадающем списке в поле "**Модуль**", укажите название для модуля и нажмите "**Сохранить**".

<figure><img src="../../../.gitbook/assets/image (374).png" alt="" width="418"><figcaption></figcaption></figure>

Заполните указанные авторизационные поля.

<figure><img src="../../../.gitbook/assets/Arc_5NJ6WqIhsR.png" alt="" width="435"><figcaption></figcaption></figure>

**API ключ** — ключ, ранее скопированный из личного кабинета Luckypay

## Особые поля

<div><figure><img src="../../../.gitbook/assets/image (375).png" alt="" width="217"><figcaption></figcaption></figure> <figure><img src="../../../.gitbook/assets/image (377).png" alt="" width="215"><figcaption></figcaption></figure></div>

**Способ оплаты** — выберите необходимый способ для выплаты средств

## Продолжение настройки

Далее произведите настройку мерчанта следуя [общей инструкции по настройке](https://premium.gitbook.io/rukovodstvo-polzovatelya/osnovnye-nastroiki/merchanty-i-avtovyplaty/avtovyplaty/obshie-nastroiki-merchantov-avtovyplat).
