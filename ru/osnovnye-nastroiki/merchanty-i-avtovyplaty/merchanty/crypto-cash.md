# Crypto-Cash

{% hint style="info" %}
Если вам необходимо обновить модуль на сервере — воспользуйтесь [инструкцией](https://premium.gitbook.io/main/osnovnye-nastroiki/faq/obnovlenie-failov-skripta-na-servere/kak-obnovit-faily-na-servere#moduli-merchantov-i-avtovyplat)
{% endhint %}

## Настройки в личном кабинете мерчанта

{% hint style="warning" %}
Для обсуждения условий работы свяжитесь с [представителем сервиса](https://t.me/CCW_Admin).

**Дисклеймер**: при подключении вашего сайта к тому или иному сервису, пожалуйста, самостоятельно оценивайте возможные риски сотрудничества.
{% endhint %}

[Зарегистрируйтесь на сервисе Crypto-Cash](https://account.crypto-cash.world/registration) и авторизуйтесь в личном кабинете.

{% tabs %}
{% tab title="Crypto-Cash (фиатные валюты)" %}
Перейдите в [раздел с настройками мерчанта](https://account.crypto-cash.world/overview). Выпустите API-ключи по кнопке "**Сгенерировать API ключ**".

<figure><img src="../../../.gitbook/assets/image (450).png" alt=""><figcaption></figcaption></figure>

Выберите подходящие методы для приема средств и скопируйте секретный и публичный ключи в буфер обмена или текстовый файл.

<figure><img src="../../../.gitbook/assets/image (480).png" alt=""><figcaption></figcaption></figure>

Установите ограничения доступа (при использовании мерчанта на прием отметьте "**Пополнение**" и "**История транзакций**"). Укажите в поле "**URL вебхука**" ссылку из настроек модуля на прием средств.

<figure><img src="../../../.gitbook/assets/image (458).png" alt=""><figcaption></figcaption></figure>
{% endtab %}

{% tab title="Crypto-Cash Crypto (криптовалюты)" %}
Перейдите в [раздел с настройками мерчанта](https://account.crypto-cash.world/overview). Выпустите API-ключи по кнопке "**Сгенерировать API ключ**".

<figure><img src="../../../.gitbook/assets/изображение (1) (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt="" width="563"><figcaption></figcaption></figure>

Скопируйте секретный и публичный ключи в буфер обмена или текстовый файл.

<figure><img src="../../../.gitbook/assets/изображение (2) (1) (1) (1) (1) (1) (1).png" alt="" width="563"><figcaption></figcaption></figure>

Установите ограничения доступа (при использовании мерчанта на прием отметьте "**Пополнение**" и "**История транзакций**"). Укажите в поле "**URL вебхука**" ссылку из настроек модуля на прием средств.

<figure><img src="../../../.gitbook/assets/image (444).png" alt=""><figcaption></figcaption></figure>
{% endtab %}
{% endtabs %}

{% hint style="warning" %}
При выпуске API-ключей запомните или запишите тип ключа, который вы выбрали (можно выбрать любой вариант) — вам потребуется выбрать тот же тип ключей в модуле на прием средств при настройке модуля.

![](<../../../.gitbook/assets/image (453).png>)![](<../../../.gitbook/assets/image (454).png>)
{% endhint %}

## Настройки модуля

В панели администратора создайте нового мерчанта в разделе "**Мерчанты**" ➔ "**Добавить мерчант".**

Выберите подходящий модуль в выпадающем списке в поле "**Модуль**", укажите название для модуля и нажмите "**Сохранить**".

{% tabs %}
{% tab title="Crypto-Cash (фиатные валюты)" %}
<figure><img src="../../../.gitbook/assets/image (445).png" alt=""><figcaption></figcaption></figure>
{% endtab %}

{% tab title="Crypto-Cash Crypto (криптовалюты)" %}
<figure><img src="../../../.gitbook/assets/image (447).png" alt=""><figcaption></figcaption></figure>
{% endtab %}
{% endtabs %}

Заполните указанные авторизационные поля.

<figure><img src="../../../.gitbook/assets/image (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt="" width="437"><figcaption></figcaption></figure>

**Домен** — оставьте поле пустым

**Публичный ключ** — публичный ключ, скопированный ранее в ЛК Crypto-Cash

**Секретный ключ** — секретный ключ, скопированный ранее в ЛК Crypto-Cash

## Особые поля

{% tabs %}
{% tab title="Crypto-Cash (фиатные валюты)" %}
<figure><img src="../../../.gitbook/assets/image (449).png" alt=""><figcaption></figcaption></figure>

**API key type** — выберите тип ключей согласно ранее выбранному в ЛК Crypto-Cash при создании ключей

<figure><img src="../../../.gitbook/assets/image (574).png" alt=""><figcaption></figcaption></figure>

**Валюта** — выбор валюты для выдачи адреса кошелька (при выборе пункта "**Автоматически**" будет использоваться код валюты "**Отдаю**")

* **добавить** — добавление своего кода валюты
{% endtab %}

{% tab title="Crypto-Cash Crypto (криптовалюты)" %}
<figure><img src="../../../.gitbook/assets/image (449).png" alt=""><figcaption></figcaption></figure>

**API key type** — выберите тип ключей согласно ранее выбранному в ЛК Crypto-Cash при создании ключей

<figure><img src="../../../.gitbook/assets/image (518).png" alt=""><figcaption></figcaption></figure>

**Валюта** — выбор валюты для выдачи адреса кошелька (при выборе пункта "**Автоматически**" будет использоваться код валюты "**Отдаю**")

* **добавить** — добавление своего кода валюты
{% endtab %}
{% endtabs %}

## Продолжение настройки

Далее произведите настройку мерчанта следуя [общей инструкции по настройке](https://premium.gitbook.io/rukovodstvo-polzovatelya/osnovnye-nastroiki/merchanty-i-avtovyplaty/merchanty/obshie-nastroiki-merchantov).<br>
