# Crypto-Cash Crypto

{% hint style="info" %}
Если вам необходимо обновить модуль на сервере — воспользуйтесь [инструкцией](https://premium.gitbook.io/main/osnovnye-nastroiki/faq/obnovlenie-failov-skripta-na-servere/kak-obnovit-faily-na-servere#moduli-merchantov-i-avtovyplat)
{% endhint %}

## Настройки в личном кабинете мерчанта

{% hint style="warning" %}
Для обсуждения условий работы свяжитесь с [представителем сервиса](https://t.me/CEO_CryptoCash).

**Дисклеймер**: при подключении вашего сайта к тому или иному сервису, пожалуйста, самостоятельно оценивайте возможные риски сотрудничества.
{% endhint %}

[Зарегистрируйтесь на сервисе Crypto-Cash](https://account.crypto-cash.world/registration) и авторизуйтесь в личном кабинете.

Перейдите в [раздел с настройками мерчанта](https://account.crypto-cash.world/overview). Выпустите API-ключи по кнопке "**Сгенерировать API ключ**".

<figure><img src="../../../.gitbook/assets/изображение (1) (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt="" width="563"><figcaption></figcaption></figure>

{% hint style="warning" %}
При генерации API ключей выбирайте метод **ED25519**.&#x20;

Legacy ключи сейчас также будут работать, но перестанут поддерживаться в будущем.

<p align="center"><img src="https://premium.gitbook.io/main/~gitbook/image?url=https%3A%2F%2F2574066779-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252Fm9kqZXsNykrN6VyxxXBO%252Fuploads%252Fyvqc3y1hbCB4h5v1YY3u%252Fbj9Gte0IOW.png%3Falt%3Dmedia%26token%3D2860c3d4-9e8e-4f1b-8256-4bbbda74cc88&#x26;width=300&#x26;dpr=3&#x26;quality=100&#x26;sign=8e78b61f&#x26;sv=2" alt="" data-size="original"></p>
{% endhint %}

Скопируйте секретный и публичный ключи в буфер обмена или текстовый файл.

<figure><img src="../../../.gitbook/assets/изображение (2) (1) (1) (1) (1) (1) (1).png" alt="" width="563"><figcaption></figcaption></figure>

Установите ограничения доступа (при использовании мерчанта на прием отметьте "**Пополнение**" и "**История транзакций**").&#x20;

Укажите в поле "**URL вебхука**" ссылку "**Webhook"** из настроек модуля на прием средств.

## Настройки модуля

В панели администратора создайте нового мерчанта в разделе "**Мерчанты**" ➔ "**Добавить мерчант".**

Выберите подходящий модуль в выпадающем списке в поле "**Модуль**", укажите название для модуля и нажмите "**Сохранить**".

<figure><img src="../../../.gitbook/assets/NSUKH57WpO.png" alt=""><figcaption></figcaption></figure>

Заполните указанные авторизационные поля.

<figure><img src="../../../.gitbook/assets/image (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

**Домен** — оставьте поле пустым

**Публичный ключ** — публичный ключ, скопированный ранее в ЛК Crypto-Cash

**Секретный ключ** — секретный ключ, скопированный ранее в ЛК Crypto-Cash

## Особые поля

<figure><img src="../../../.gitbook/assets/image (449).png" alt=""><figcaption></figcaption></figure>

**API key type** — выберите тип ключей согласно ранее выбранному в ЛК Crypto-Cash при создании ключей

<figure><img src="../../../.gitbook/assets/image (518).png" alt=""><figcaption></figcaption></figure>

**Валюта** — выбор валюты для выдачи адреса кошелька (при выборе пункта "**Автоматически**" будет использоваться код валюты "**Отдаю**")

* **добавить** — добавление своего кода валюты

## Продолжение настройки

**Cron-файл -** [создайте задание](https://premium.gitbook.io/main/osnovnye-nastroiki/faq/kak-sozdat-zadanie-cron-na-servere) с такой ссылкой на сервер&#x435;**.**

Дополнительные настройки модуля выполняются согласно [общей инструкции по настройке](https://premium.gitbook.io/rukovodstvo-polzovatelya/osnovnye-nastroiki/merchanty-i-avtovyplaty/merchanty/obshie-nastroiki-merchantov).
