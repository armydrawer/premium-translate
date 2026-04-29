# Payplay

{% hint style="danger" %}
<mark style="color:red;">Before setting up auto payouts, please read the</mark> [<mark style="color:blue;">risk warning</mark>](https://premium.gitbook.io/main/osnovnye-nastroiki/merchanty-i-avtovyplaty/avtovyplaty/preduprezhdenie-o-riskakh)<mark style="color:blue;">!</mark>
{% endhint %}

{% hint style="info" %}
If you need to update the module on the server, please refer to the [instructions](https://premium.gitbook.io/main/osnovnye-nastroiki/faq/obnovlenie-failov-skripta-na-servere/kak-obnovit-faily-na-servere#moduli-merchantov-i-avtovyplat).
{% endhint %}

## Merchant Account Settings

{% hint style="warning" %}
To discuss terms and setup, please contact a [service representative](https://t.me/only7pay).

**Disclaimer**: When connecting your website to any service, please assess the potential risks of collaboration on your own.
{% endhint %}

Register for the PayPlay service through a service representative and log into your merchant account.

## Module Settings

In the admin panel, create a new merchant in the "**Auto Payouts**" section by clicking "**Add Auto Payout**."

Select PayPlay from the dropdown menu in the "**Module**" field, enter a name for the module, and click "**Save**."

<figure><img src="../../../.gitbook/assets/изображение (217).png" alt=""><figcaption></figcaption></figure>

Fill in the required authorization fields.

<figure><img src="../../../.gitbook/assets/изображение (220).png" alt=""><figcaption></figcaption></figure>

**Domain** — leave this field empty.

**API Key** — the API key displayed in your PayPlay account settings.

<figure><img src="../../../.gitbook/assets/изображение (241).png" alt="" width="563"><figcaption></figcaption></figure>

<figure><img src="../../../.gitbook/assets/изображение (221).png" alt="" width="390"><figcaption></figcaption></figure>

**Slug** — the ID of the payment page displayed in your PayPlay account.

<figure><img src="../../../.gitbook/assets/изображение (247).png" alt=""><figcaption></figcaption></figure>

Please note that for the auto payout module, you need to specify a webhook URL for proper verification of payouts. Copy the URL from the auto payout module settings

<figure><img src="../../../.gitbook/assets/изображение (248).png" alt=""><figcaption></figcaption></figure>

and paste it into the designated field in your PayPlay account settings, as shown in the screenshot below.

<figure><img src="../../../.gitbook/assets/изображение (249).png" alt="" width="563"><figcaption></figcaption></figure>

After saving the webhook, be sure to select the methods for working with it and save the changes.

<figure><img src="../../../.gitbook/assets/изображение (250).png" alt="" width="514"><figcaption></figcaption></figure>

## Special Fields

<figure><img src="../../../.gitbook/assets/изображение (251).png" alt="" width="462"><figcaption></figcaption></figure>

**Currency code** — select the appropriate method for disbursing funds to the client.

* **Additional Fields** — use the currency code specified in the [additional field](https://premium.gitbook.io/main/osnovnye-nastroiki/valyuty-i-napravleniya-obmena/dopolnitelnye-polya#dopolnitelnye-polya-dlya-valyuty) for the currency "**Receiving**" or in the exchange direction, or [additional fields for the exchange direction](https://premium.gitbook.io/main/osnovnye-nastroiki/valyuty-i-napravleniya-obmena/dopolnitelnye-polya#dopolnitelnye-polya-dlya-napravleniya-obmena).
* **Currency Codes** — manually select the currency code (in this case, the module will only work with the specified currency).

<figure><img src="../../../.gitbook/assets/изображение (252).png" alt="" width="461"><figcaption></figcaption></figure>

**Network** — select the appropriate network for the payout currency.

* **Additional Fields** — use the currency code specified in the [additional field](https://premium.gitbook.io/main/osnovnye-nastroiki/valyuty-i-napravleniya-obmena/dopolnitelnye-polya#dopolnitelnye-polya-dlya-valyuty) for the currency "**Receiving**" or in the exchange direction, or [additional fields for the exchange direction](https://premium.gitbook.io/main/osnovnye-nastroiki/valyuty-i-napravleniya-obmena/dopolnitelnye-polya#dopolnitelnye-polya-dlya-napravleniya-obmena).
* **Currency Codes** — manually select the currency code (in this case, the module will only work with the specified currency).

## Continuing the Setup

Next, proceed to configure the merchant by following the [general setup instructions](https://premium.gitbook.io/rukovodstvo-polzovatelya/osnovnye-nastroiki/merchanty-i-avtovyplaty/avtovyplaty/obshie-nastroiki-merchantov-avtovyplat).<br>
