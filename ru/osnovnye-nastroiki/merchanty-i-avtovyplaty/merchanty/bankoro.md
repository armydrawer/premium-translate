# Bankoro

{% hint style="info" %}
Если вам необходимо обновить модуль на сервере — воспользуйтесь [инструкцией](https://premium.gitbook.io/main/osnovnye-nastroiki/faq/obnovlenie-failov-skripta-na-servere/kak-obnovit-faily-na-servere#moduli-merchantov-i-avtovyplat)
{% endhint %}

## Настройки в личном кабинете мерчанта

{% hint style="warning" %}
Для обсуждения условий работы свяжитесь с [представителем сервиса](https://t.me/bankoro_crypto).

**Дисклеймер**: при подключении вашего сайта к тому или иному сервису, пожалуйста, самостоятельно оценивайте возможные риски сотрудничества.
{% endhint %}

[Зарегистрируйтесь на сервисе Bankoro](https://bankoro.io/registration), авторизуйтесь в личном кабинете, перейдите в раздел "**API подключение**" и добавьте новую пару API-ключей.

<figure><img src="../../../.gitbook/assets/image (3) (1).png" alt=""><figcaption></figcaption></figure>

Заполните поля на своё усмотрение (главное предоставьте доступ к приему средств и/или выплате) и выпустите API-ключи по кнопке "**Создать**". Скопируйте оба ключа в буфер обмена или текстовый файл.

<figure><img src="../../../.gitbook/assets/image (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

## Настройки модуля

В панели администратора создайте нового мерчанта в разделе "**Мерчанты**" ➔ "**Добавить мерчант".**

Выберите Bankoro в выпадающем списке в поле "**Модуль**", укажите название для модуля и нажмите "**Сохранить**".

<figure><img src="../../../.gitbook/assets/image (3) (1) (1).png" alt=""><figcaption></figcaption></figure>

Заполните указанные авторизационные поля.

<figure><img src="../../../.gitbook/assets/image (2) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

**Домен** — оставьте поле пустым

**API ключ** — публичный ключ, скопированный ранее в ЛК Bankoro

**Секретный ключ** — секретный ключ, скопированный ранее в ЛК Bankoro

## Особые поля

<figure><img src="../../../.gitbook/assets/image (2221).png" alt=""><figcaption></figcaption></figure>

**Способ оплаты** — выбор валюты для выдачи адреса кошелька (при выборе пункта "**Автоматически**" будет использоваться код валюты "**Отдаю**")

* **добавить** — добавление своего кода валюты

## Продолжение настройки

Далее произведите настройку мерчанта следуя [общей инструкции по настройке](https://premium.gitbook.io/rukovodstvo-polzovatelya/osnovnye-nastroiki/merchanty-i-avtovyplaty/merchanty/obshie-nastroiki-merchantov).\
