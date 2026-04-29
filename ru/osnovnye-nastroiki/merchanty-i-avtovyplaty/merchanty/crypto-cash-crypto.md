# Crypto-Cash Crypto

{% hint style="info" %}
Если вам необходимо обновить модуль на сервере — воспользуйтесь [инструкцией](https://premium.gitbook.io/main/osnovnye-nastroiki/faq/obnovlenie-failov-skripta-na-servere/kak-obnovit-faily-na-servere#moduli-merchantov-i-avtovyplat)
{% endhint %}

## Настройки в личном кабинете мерчанта

{% hint style="warning" %}
Для обсуждения условий работы свяжитесь с [представителем сервиса](https://t.me/CCW_Admin).

**Дисклеймер**: при подключении вашего сайта к тому или иному сервису, пожалуйста, самостоятельно оценивайте возможные риски сотрудничества.
{% endhint %}

[Зарегистрируйтесь на сервисе Crypto-Cash](https://account.crypto-cash.world/registration), авторизуйтесь в личном кабинете и перейдите в [раздел настроек мерчанта](https://account.crypto-cash.world/overview). Выпустите API-ключи по кнопке "**Сгенерировать API ключ**".

<figure><img src="../../../.gitbook/assets/изображение (1) (1) (1) (1) (1) (1) (1) (1).png" alt="" width="563"><figcaption></figcaption></figure>

&#x20;Установите ограничения доступа (при использовании мерчанта на прием отметьте "**Пополнение**" и "**История транзакций**"). Укажите в поле "**URL вебхука**" ссылку из настроек модуля на прием средств.

<figure><img src="../../../.gitbook/assets/изображение (2) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

Скопируйте секретный и публичный ключи в буфер обмена или текстовый файл.&#x20;

<figure><img src="../../../.gitbook/assets/изображение (2) (1) (1) (1) (1).png" alt="" width="563"><figcaption></figcaption></figure>

## Настройки модуля

В панели администратора создайте нового мерчанта в разделе "**Мерчанты**" ➔ "**Добавить мерчант".**

Выберите Crypto-Cash Crypto в выпадающем списке в поле "**Модуль**", укажите название для модуля и нажмите "**Сохранить**".

<figure><img src="../../../.gitbook/assets/image (2216).png" alt="" width="482"><figcaption></figcaption></figure>

Заполните указанные авторизационные поля.

<figure><img src="../../../.gitbook/assets/image (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt="" width="437"><figcaption></figcaption></figure>

**Домен** — оставьте поле пустым

**Публичный ключ** — публичный ключ, скопированный ранее в ЛК Crypto-Cash

**Секретный ключ** — секретный ключ, скопированный ранее в ЛК Crypto-Cash

## Особые поля

<figure><img src="../../../.gitbook/assets/image (2217).png" alt="" width="437"><figcaption></figcaption></figure>

**Валюта** — выбор валюты для выдачи адреса кошелька (при выборе пункта "**Автоматически**" будет использоваться код валюты "**Отдаю**")

* **добавить** — добавление своего кода валюты

## Продолжение настройки

Далее произведите настройку мерчанта следуя [общей инструкции по настройке](https://premium.gitbook.io/rukovodstvo-polzovatelya/osnovnye-nastroiki/merchanty-i-avtovyplaty/merchanty/obshie-nastroiki-merchantov).<br>
