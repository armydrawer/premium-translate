# Optimoney

{% hint style="info" %}
Если вам необходимо обновить модуль на сервере — воспользуйтесь [инструкцией](https://premium.gitbook.io/main/osnovnye-nastroiki/faq/obnovlenie-failov-skripta-na-servere/kak-obnovit-faily-na-servere#moduli-merchantov-i-avtovyplat)
{% endhint %}

## Настройки в личном кабинете мерчанта

{% hint style="warning" %}
Для обсуждения условий работы свяжитесь с представителем сервиса.

**Дисклеймер**: при подключении вашего сайта к тому или иному сервису, пожалуйста, самостоятельно оценивайте возможные риски сотрудничества.
{% endhint %}

Зарегистрируйтесь на сервисе [Optimoney](https://client.optimoney.com/register). Авторизуйтесь в личном кабинете и создайте новый USD кошелек (имя кошелька укажите на ваше усмотрение).

<figure><img src="../../../.gitbook/assets/image (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../../../.gitbook/assets/image (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

Создайте нового мерчанта в личном кабинете.

<figure><img src="../../../.gitbook/assets/image (2240) (1).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../../../.gitbook/assets/image (2241).png" alt=""><figcaption></figcaption></figure>

После верификации домена в настройках мерчанта укажите его имя (на ваше усмотрение) и выберите созданный кошелек для приема средств на него.

Укажите 3 URL для соответствующих полей (все URL скопируйте из настроек модуля мерчанта в админ-панели Premium Exchanger).

Скопируйте API ключ мерчанта из этих настроек.

<figure><img src="../../../.gitbook/assets/image (3) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../../../.gitbook/assets/image (4) (1) (1).png" alt=""><figcaption></figcaption></figure>

## Настройки модуля

В панели администратора создайте нового мерчанта в разделе "**Мерчанты**" ➔ "**Добавить мерчант".**

Выберите Optimoney в выпадающем списке в поле "**Модуль**", укажите название для модуля и нажмите "**Сохранить**".

<figure><img src="../../../.gitbook/assets/image (2238).png" alt=""><figcaption></figcaption></figure>

Заполните указанные авторизационные поля.

<figure><img src="../../../.gitbook/assets/image (2239).png" alt=""><figcaption></figcaption></figure>

**Домен** — оставьте поле пустым

**API ключ** — API ключ, переданный вам представителем Optimoney

**Секретный ключ** — API ключ, переданный вам представителем Optimoney

**ID мерчанта** — ID из поля "**Мерчант №**" в личном кабинете мерчанта

<figure><img src="../../../.gitbook/assets/image (2243).png" alt=""><figcaption></figcaption></figure>

**API ключ мерчанта** — API ключ, скопированный ранее в настройках созданного мерчанта

<figure><img src="../../../.gitbook/assets/image (2244).png" alt=""><figcaption></figcaption></figure>

## Особые поля

## Продолжение настройки

Далее произведите настройку мерчанта следуя [общей инструкции по настройке](https://premium.gitbook.io/rukovodstvo-polzovatelya/osnovnye-nastroiki/merchanty-i-avtovyplaty/merchanty/obshie-nastroiki-merchantov).<br>
