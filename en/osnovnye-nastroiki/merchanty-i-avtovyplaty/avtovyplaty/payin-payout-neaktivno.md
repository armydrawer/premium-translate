Certainly! Here's a natural, fluent English translation of the provided text:

---

hidden: true  
noIndex: true

---

# Payin-Payout (Inactive)

{% hint style="danger" %}
<mark style="color:red;">Before setting up auto payouts, please make sure to read</mark> [<mark style="color:blue;">the risk warning</mark>](https://premiumexchanger.com/wiki/preduprezhdenie-auto/)<mark style="color:blue;">!</mark>
{% endhint %}

{% hint style="info" %}
If you need to update the module on your server, please follow this [instruction](https://premium.gitbook.io/rukovodstvo-polzovatelya/osnovnye-nastroiki/faq/kak-obnovit-faily-na-servere#moduli-avtovyplat).
{% endhint %}

## Merchant Dashboard Settings

{% hint style="warning" %}
To discuss terms and get connected, please contact the [service representative](https://t.me/Payin_payoutt).

**Disclaimer:** When integrating your website with any service, please independently assess the potential risks involved in the partnership.
{% endhint %}

## **Module Setup**

In the admin panel, create a new merchant under "**Auto Payouts**" -> "**Add Auto Payout**."

Select Payin-Payout from the dropdown menu in the "**Module**" field, enter a name for the module, and click "**Save**."

<figure><img src="../../../.gitbook/assets/image (1568).png" alt="" width="496"><figcaption></figcaption></figure>

Fill in the required authorization fields.

<figure><img src="../../../.gitbook/assets/image (1569).png" alt="" width="455"><figcaption></figcaption></figure>

**Identifier** — The account ID from your Payin-Payout dashboard.

{% hint style="warning" %}
Request your **Account Identifier** (not the store ID!) in the Payin-Payout chat.  
![](<../../../.gitbook/assets/image (525).png>)
{% endhint %}

**Private Key** — The contents of the secret key file **`secret.key.pem`**, generated when creating your key pair (see instructions below).

{% hint style="warning" %}
The key content should be viewed in base64 encoding and pasted into the field **including the lines**:

**`-----BEGIN PRIVATE KEY-----`**  
**`-----END PRIVATE KEY-----`**
{% endhint %}

{% hint style="warning" %}
[Official documentation for generating an RSA key for auto payouts](https://github.com/payin-payout/payout-api/blob/2.0/docs/README.md#%D0%B3%D0%B5%D0%BD%D0%B5%D1%80%D0%B0%D1%86%D0%B8%D1%8F-%D0%BF%D1%80%D0%B8%D0%B2%D0%B0%D1%82%D0%BD%D0%BE%D0%B3%D0%BE-%D0%BA%D0%BB%D1%8E%D1%87%D0%B0) (Windows only).

For help generating keys, you can also contact the merchant at — [https://t.me/payinpayoutbot](https://t.me/payinpayoutbot)
{% endhint %}

<details>

<summary>Instructions for MacOS:</summary>

On MacOS, you need to:

---

If you want me to continue with the MacOS instructions or translate any other part, just let me know!

Here is a natural English translation of the provided text:

---

* Install [OpenSSL](https://macappstore.org/openssl/)
* Use the following script to generate the key:  
  ```bash
  #!/bin/bash
  openssl rand -out random 1048576
  openssl genrsa -out secret.key.pem -rand random 1024
  openssl rsa -in secret.key.pem -pubout -outform DER -out public.key
  openssl rsa -inform pem -in secret.key.pem -outform der -out secret.key
  ```
* Open Terminal and run the command:  
  ```bash
  bash /Users/your_username/Desktop/openssl_gen_key.sh
  ```
* After the keys are generated, they will be located in your user folder.

  <figure><img src="../../../.gitbook/assets/image (524).png" alt="" width="317"><figcaption></figcaption></figure>

* Send the **`public.key`** file to the Payin-Payout chat so they can add it to their server.
* Download and open the **TextEdit** application.
* Open the **`secret.key.pem`** file in TextEdit.  
  ![](<../../../.gitbook/assets/image (526).png>)

- Copy the entire text content of the file, including the lines  
  **`-----BEGIN PRIVATE KEY-----`** and **`-----END PRIVATE KEY-----`**  
  ![](<../../../.gitbook/assets/image (527).png>)
- [Set up a cron job](https://premium.gitbook.io/main/osnovnye-nastroiki/faq/kak-sozdat-zadanie-cron-na-servere) to run the autopayout module.

</details>

## Special Fields

<figure><img src="../../../.gitbook/assets/image (1570).png" alt="" width="431"><figcaption></figcaption></figure>

**Payment Method** — select "**Bank Card Top-up**" (the module only pays out in RUB, with a minimum payout amount of 1000 RUB). (This option will only appear after entering a valid identifier and authorization key for the module.)

{% hint style="warning" %}
Dropdown options in the module will only be available after successful authorization!
{% endhint %}

## Continuing Setup

Next, configure the merchant by following the [general setup instructions](https://premium.gitbook.io/rukovodstvo-polzovatelya/osnovnye-nastroiki/merchanty-i-avtovyplaty/avtovyplaty/obshie-nastroiki-merchantov-avtovyplat).

---

If you need the text adapted further or formatted differently, just let me know!