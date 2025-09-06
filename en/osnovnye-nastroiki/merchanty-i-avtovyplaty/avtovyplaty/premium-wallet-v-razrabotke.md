---
hidden: true
noIndex: true
---

# Premium Wallet (в разработке)

{% hint style="danger" %}
<mark style="color:red;">Перед настройкой автовыплат обязательно прочитайте</mark> [<mark style="color:blue;">предупреждение о рисках</mark>](https://premiumexchanger.com/wiki/preduprezhdenie-auto/)<mark style="color:blue;">!</mark>
{% endhint %}

{% hint style="info" %}
Если вам необходимо обновить модуль на сервере — воспользуйтесь [инструкцией](https://premium.gitbook.io/rukovodstvo-polzovatelya/osnovnye-nastroiki/faq/kak-obnovit-faily-na-servere#moduli-avtovyplat)
{% endhint %}

<figure><img src="../../../.gitbook/assets/image (2160).png" alt=""><figcaption></figcaption></figure>

## Настройки в личном кабинете мерчанта

{% hint style="warning" %}
Для обсуждения условий и подключения, свяжитесь с [представителем сервиса](https://t.me/ipichipich).

**Дисклеймер**: при подключении вашего сайта к тому или иному сервису, самостоятельно пожалуйста оценивайте возможные риски сотрудничества.
{% endhint %}

В личном кабинете заполните поле "**Webhook url**" и скопируйте данные из полей "**Client ID**" и "**API Secret**" в буфер обмена или текстовый файл.

<figure><img src="../../../.gitbook/assets/image (2161).png" alt=""><figcaption></figcaption></figure>

{% hint style="warning" %}
В поле "**Webhook url**" укажите URL из поля "**Callback URL"** из настроек модуля автовыплаты

<img src="../../../.gitbook/assets/image (2160).png" alt="" data-size="original">
{% endhint %}

## Настройки модуля

В панели администратора в разделе "**Мерчанты**" ➔ "**Автовыплаты"** нажмите кнопку "**Добавить**" и выберите Premium Wallet.

<figure><img src="../../../.gitbook/assets/image (175).png" alt="" width="464"><figcaption></figcaption></figure>

Заполните указанные авторизационные поля.

<figure><img src="../../../.gitbook/assets/image (174).png" alt="" width="430"><figcaption></figcaption></figure>

**Домен** —&#x20;

**Client ID** — ID, скопированный ранее в ЛК мерчанта

**Секретный ключ** — ключ, скопированный ранее в ЛК мерчанта

## Продолжение настройки

Далее произведите настройку мерчанта следуя [общей инструкции по настройке](https://premium.gitbook.io/rukovodstvo-polzovatelya/osnovnye-nastroiki/merchanty-i-avtovyplaty/avtovyplaty/obshie-nastroiki-merchantov-avtovyplat).
