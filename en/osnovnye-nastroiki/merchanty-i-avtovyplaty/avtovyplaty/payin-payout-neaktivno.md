# Payin-Payout (Inactive)

{% hint style="danger" %}
<mark style="color:red;">Before setting up auto payouts, please read the</mark> [<mark style="color:blue;">risk warning</mark>](https://premiumexchanger.com/wiki/preduprezhdenie-auto/)<mark style="color:blue;">!</mark>
{% endhint %}

{% hint style="info" %}
If you need to update the module on the server, please refer to the [instructions](https://premium.gitbook.io/rukovodstvo-polzovatelya/osnovnye-nastroiki/faq/kak-obnovit-faily-na-servere#moduli-avtovyplat).
{% endhint %}

## Merchant Account Settings

{% hint style="warning" %}
To discuss terms and connection, please contact a [service representative](https://t.me/Payin_payoutt).

**Disclaimer**: When connecting your website to any service, please assess the potential risks of collaboration on your own.
{% endhint %}

## **Module Settings**

In the admin panel, create a new merchant in the "**Auto Payouts**" section by selecting "**Add Auto Payout**."

Choose Payin-Payout from the dropdown menu in the "**Module**" field, enter a name for the module, and click "**Save**."

<figure><img src="../../../.gitbook/assets/image (1568).png" alt="" width="496"><figcaption></figcaption></figure>

Fill in the required authorization fields.

<figure><img src="../../../.gitbook/assets/image (1569).png" alt="" width="455"><figcaption></figcaption></figure>

**Identifier** — This is the account ID from your Payin-Payout personal account.

{% hint style="warning" %}
Request the **Account Identifier** (not the store ID!) in the chat with Payin-Payout.\
![](<../../../.gitbook/assets/image (525).png>)
{% endhint %}

**Private Key** — This is the content from the secret key **`secret.key.pem`**, generated when creating the key pair (see instructions below).

{% hint style="warning" %}
The key content should be viewed in base64 encoding and inserted into the field **along with the lines**:

**`-----BEGIN PRIVATE KEY-----`**&#x20;

**`-----END PRIVATE KEY-----`**
{% endhint %}

{% hint style="warning" %}
[Official documentation for generating an RSA key for auto payouts](https://github.com/payin-payout/payout-api/blob/2.0/docs/README.md#%D0%B3%D0%B5%D0%BD%D0%B5%D1%80%D0%B0%D1%86%D0%B8%D1%8F-%D0%BF%D1%80%D0%B8%D0%B2%D0%B0%D1%82%D0%BD%D0%BE%D0%B3%D0%BE-%D0%BA%D0%BB%D1%8E%D1%87%D0%B0) (Windows only).

You can also contact the merchant for key generation assistance at — [https://t.me/payinpayoutbot](https://t.me/payinpayoutbot).
{% endhint %}

<details>

<summary>Instructions for MacOS:</summary>

On MacOS, you need to:

* Install [OpenSSL](https://macappstore.org/openssl/)
* Use the key generation script:\
  `#!/bin/bash`\
  `openssl rand -out random 1048576`\
  `openssl genrsa -out secret.key.pem -rand random 1024`\
  `openssl rsa -in secret.key.pem -pubout -outform DER -out public.key`\
  `openssl rsa -inform pem -in secret.key.pem -outform der -out secret.key`
* Open Terminal and enter the command:\
  `bash /Users/`**`your_login`**`/Desktop/openssl_gen_key.sh`
* After generation, the keys will be located in the user folder.

    <figure><img src="../../../.gitbook/assets/image (524).png" alt="" width="317"><figcaption></figcaption></figure>
* Send the **`public.key`** to the Payin-Payout chat so they can add it to their server.
* Download and open the **TextEdit** application.
* Open the **`secret.key.pem`** file in the application.\
  ![](<../../../.gitbook/assets/image (526).png>)

- Copy the entire text content of the file, including\
  &#xNAN;**`-----BEGIN PRIVATE KEY-----`**` ``and`` `**`-----END PRIVATE KEY-----`**\
  ![](<../../../.gitbook/assets/image (527).png>)
- [Set up a cron job](https://premium.gitbook.io/main/osnovnye-nastroiki/faq/kak-sozdat-zadanie-cron-na-servere) for the auto payout module to function.

</details>

## Special Fields

<figure><img src="../../../.gitbook/assets/image (1570).png" alt="" width="431"><figcaption></figcaption></figure>

**Payment Method** — Select "**Bank Card Top-Up**" (the module only pays out in rubles, with a minimum payout amount of 1000 RUB) (this method will only appear after entering the correct identifier and authorization key for the module).

{% hint style="warning" %}
Options in the dropdown list of the module will only be available after authorization in the module!
{% endhint %}

## Continuing the Setup

Next, proceed to configure the merchant by following the [general setup instructions](https://premium.gitbook.io/rukovodstvo-polzovatelya/osnovnye-nastroiki/merchanty-i-avtovyplaty/avtovyplaty/obshie-nastroiki-merchantov-avtovyplat).