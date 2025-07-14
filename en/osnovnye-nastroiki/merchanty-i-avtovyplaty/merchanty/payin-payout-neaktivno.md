---
hidden: true
noIndex: true
noRobotsIndex: true
---

# Payin-Payout (Inactive)

{% hint style="info" %}
If you need to update the module on your server, please follow the [instructions](https://premium.gitbook.io/rukovodstvo-polzovatelya/osnovnye-nastroiki/faq/kak-obnovit-faily-na-servere#moduli-merchantov).
{% endhint %}

## Settings in the Merchant Dashboard

{% hint style="warning" %}
To discuss terms and activation, please contact the [service representative](https://t.me/Payin_payoutt).

**Disclaimer:** When connecting your website to any service, please independently assess any potential risks involved in the partnership.
{% endhint %}

To configure the module, you need to [create a shop in the merchant dashboard](https://lk.payin-payout.net/app/#/shops/add). Enter the shop name, select "**Online Store**," and click "**Create Shop**."

<figure><img src="../../../.gitbook/assets/image (519).png" alt="" width="563"><figcaption></figcaption></figure>

Fill in the shop details and save them. Complete the verification process for both your account and the newly created shop.

<figure><img src="../../../.gitbook/assets/image (520).png" alt="" width="563"><figcaption></figcaption></figure>

After creating the shop, copy the values from the "**AgentId**" and "**Key**" fields.

<figure><img src="../../../.gitbook/assets/image (516).png" alt=""><figcaption></figcaption></figure>

## Module Configuration

In the admin panel, create a new merchant under "**Merchants**" -> "**Add Merchant**."

Select Payin-Payout from the "**Module**" dropdown, enter a name for the module, and click "**Save**."

<figure><img src="../../../.gitbook/assets/image (1858).png" alt="" width="426"><figcaption></figcaption></figure>

Fill in the required authorization fields.

<figure src="../../../.gitbook/assets/image (1859).png" alt="" width="425"><figcaption></figcaption></figure>

**Agent ID** — the ID shown on the shop card

**Key** — the key shown on the shop card

{% hint style="warning" %}
**Important:** Be sure to enter the URL from the "**Callback URL**" field found in the module settings:

![](<../../../.gitbook/assets/image (518).png>)

into the shop settings in the merchant dashboard:\
![](<../../../.gitbook/assets/image (522).png>)\
![](<../../../.gitbook/assets/image (523).png>)\
Additionally, you must whitelist the merchant’s IP address in your Cloudflare/DDos-Guard dashboard or any other service you use (the IP address should be requested directly from the merchant).
{% endhint %}

## Special Fields

**Payment Method** — select the appropriate payment method from the dropdown list

<figure><img src="../../../.gitbook/assets/image (1896).png" alt="" width="468"><figcaption></figcaption></figure>

## Next Steps in Configuration



Next, configure the merchant by following the [general setup instructions](https://premium.gitbook.io/rukovodstvo-polzovatelya/osnovnye-nastroiki/merchanty-i-avtovyplaty/merchanty/obshie-nastroiki-merchantov).