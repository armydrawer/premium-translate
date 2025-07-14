# Nicepay

{% hint style="danger" %}
<mark style="color:red;">Before setting up auto payouts, be sure to read</mark> [<mark style="color:blue;">the risk warning</mark>](https://premiumexchanger.com/wiki/preduprezhdenie-auto/)<mark style="color:blue;">!</mark>
{% endhint %}

{% hint style="info" %}
If you need to update the module on your server, please follow this [instruction](https://premium.gitbook.io/rukovodstvo-polzovatelya/osnovnye-nastroiki/faq/kak-obnovit-faily-na-servere#moduli-avtovyplat).
{% endhint %}

## Merchant Account Settings

{% hint style="warning" %}
To discuss terms and get connected, please contact the [service representative](https://t.me/nice_sup).

**Disclaimer:** When integrating your website with any service, please carefully assess the potential risks of cooperation on your own.
{% endhint %}

Register with the Nicepay service through the [service representative](https://t.me/nice_sup) and log in to your [merchant account](https://nicepay.io/ru/app).

<figure><img src="../../../.gitbook/assets/image (41).png" alt="" width="506"><figcaption></figcaption></figure>

In your merchant account, create a new project under the "**Payment Solutions**" section.

<figure><img src="../../../.gitbook/assets/image (36).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../../../.gitbook/assets/image (37).png" alt="" width="563"><figcaption></figcaption></figure>

<figure><img src="../../../.gitbook/assets/image (38).png" alt="" width="563"><figcaption></figcaption></figure>

Go to the settings of the project you just created.

<figure><img src="../../../.gitbook/assets/image (40).png" alt="" width="563"><figcaption></figcaption></figure>

Copy the Merchant ID and Secret Key to your clipboard or save them in a text file.

<figure><img src="../../../.gitbook/assets/image (39).png" alt="" width="563"><figcaption></figcaption></figure>

## Module Settings <a href="#nastroiki-modulya" id="nastroiki-modulya"></a>

In the admin panel, create a new merchant under "**Auto Payouts**" ➔ "**Add Auto Payout**."

<figure><img src="../../../.gitbook/assets/image (31).png" alt="" width="427"><figcaption></figcaption></figure>

Select Nicepay from the dropdown menu in the "**Module**" field, enter a name for the module, and click "**Save**."

Fill in the required authorization fields.

<figure><img src="../../../.gitbook/assets/image (32).png" alt="" width="422"><figcaption></figcaption></figure>

- **Domain** — leave this field empty  
- **Merchant ID** — the Merchant ID you copied earlier from your merchant account  
- **Secret Key** — the Secret Key you copied earlier from your merchant account  

## Special Fields

- **Payment Method** — select the appropriate payout method

<figure><img src="../../../.gitbook/assets/image (33).png" alt=""><figcaption></figcaption></figure>

## Continuing Setup

[The document continues here...]

Next, configure the merchant by following the [general setup instructions](https://premium.gitbook.io/rukovodstvo-polzovatelya/osnovnye-nastroiki/merchanty-i-avtovyplaty/avtovyplaty/obshie-nastroiki-merchantov-avtovyplat).