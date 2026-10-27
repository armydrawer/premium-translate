# Custodex

{% hint style="danger" %}
<mark style="color:red;">Перед настройкой автовыплат обязательно прочитайте</mark> [<mark style="color:blue;">предупреждение о рисках!</mark>](https://premium.gitbook.io/main/osnovnye-nastroiki/merchanty-i-avtovyplaty/avtovyplaty/preduprezhdenie-o-riskakh)
{% endhint %}

{% hint style="info" %}
Если вам необходимо обновить модуль на сервере — воспользуйтесь [инструкцией](https://premium.gitbook.io/main/osnovnye-nastroiki/faq/obnovlenie-failov-skripta-na-servere/kak-obnovit-faily-na-servere#moduli-merchantov-i-avtovyplat)
{% endhint %}

## Настройки в личном кабинете мерчанта

Пройдите регистрацию на сайте [Custodex](https://custodex.sv/). Пройдите KYB и подключите 2FA в личном кабинете в разделе "Настройки" -> "Аккаунт".

<figure><img src="../../../.gitbook/assets/image (1241).png" alt=""><figcaption></figcaption></figure>

## Получение пары ключей

В личном кабинете мерчанта перейдите в раздел "Настройки" -> "Интеграция", скопируйте приватный и публичные ключи в блокнот или в буфер обмена.&#x20;

<figure><img src="../../../.gitbook/assets/image (1244).png" alt=""><figcaption></figcaption></figure>

## Настройки модуля

В панели администратора создайте нового мерчанта в разделе "**Мерчанты**" ➔ "**Добавить автовыплату".**

Выберите Custodex в выпадающем списке в поле "**Модуль**", укажите название для модуля и нажмите "**Сохранить**".

<figure><img src="../../../.gitbook/assets/image (1284).png" alt=""><figcaption></figcaption></figure>

Заполните указанные авторизационные поля.

<figure><img src="../../../.gitbook/assets/image (1280).png" alt=""><figcaption></figcaption></figure>

**Private key** — приватный ключ, скопированный ранее в ЛК Custodex

**Public key** — публичный ключ, скопированный ранее в ЛК Custodex

## Продолжение настройки

Далее произведите настройку мерчанта следуя [общей инструкции по настройке](https://premium.gitbook.io/rukovodstvo-polzovatelya/osnovnye-nastroiki/merchanty-i-avtovyplaty/merchanty/obshie-nastroiki-merchantov).
