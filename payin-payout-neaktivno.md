# Payin-Payout (Inactive)

{% hint style="info" %}
If you need to update the module on the server, please refer to the [instructions](https://premium.gitbook.io/rukovodstvo-polzovatelya/osnovnye-nastroiki/faq/kak-obnovit-faily-na-servere#moduli-merchantov).
{% endhint %}

## Merchant Account Settings

{% hint style="warning" %}
To discuss terms and connection, please contact a [service representative](https://t.me/Payin_payoutt).

**Disclaimer**: When connecting your website to any service, please assess the potential risks of collaboration on your own.
{% endhint %}

To set up the module, you need to [create a store in the merchant's personal account](https://lk.payin-payout.net/app/#/shops/add). Enter the store name, select "Online Store," and click the "Create Store" button.

<figure><img src="../../../.gitbook/assets/image (519)_eng.png" alt="" width="563"><figcaption></figcaption></figure>

Fill in the store details and save them. Complete the account and store verification process.

<figure><img src="../../../.gitbook/assets/image (520)_eng.png" alt="" width="563"><figcaption></figcaption></figure>

After creating the store, copy the information from the "AgentId" and "Key" fields.

<figure><img src="../../../.gitbook/assets/image (516)_eng.png" alt=""><figcaption></figcaption></figure>

## Module Settings

In the admin panel, create a new merchant in the "Merchants" section by selecting "Add Merchant."

Choose Payin-Payout from the dropdown menu in the "Module" field, enter a name for the module, and click "Save."

<figure><img src="../../../.gitbook/assets/image (1858)_eng.png" alt="" width="426"><figcaption></figcaption></figure>

Fill in the required authorization fields.

<figure><img src="../../../.gitbook/assets/image (1859)_eng.png" alt="" width="425"><figcaption></figcaption></figure>

**Agent ID** — The ID displayed on the store card.

**Key** — The key displayed on the store card.

{% hint style="warning" %}
**Make sure** to specify the URL from the "Callback URL" field in the module settings:

![](<../../../.gitbook/assets/image (518)_eng.png>)

in the store settings in the merchant's personal account:\
![](<../../../.gitbook/assets/image (522)_eng.png>)\
![](<../../../.gitbook/assets/image (523)_eng.png>)\
You also need to add the merchant's IP address to the whitelist in the Cloudflare/DDos-Guard personal account or any other service you are using (the IP address can be obtained directly from the merchant).
{% endhint %}

## Special Fields

**Payment Method** — Select the appropriate payment method from the dropdown list.

<figure><img src="../../../.gitbook/assets/image (1896)_eng.png" alt="" width="468"><figcaption></figcaption></figure>

## Continuing the Setup

Next, proceed with the merchant setup by following the [general setup instructions](https://premium.gitbook.io/rukovodstvo-polzovatelya/osnovnye-nastroiki/merchanty-i-avtovyplaty/merchanty/obshie-nastroiki-merchantov).