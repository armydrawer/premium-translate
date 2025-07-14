# Quickex

{% hint style="danger" %}
<mark style="color:red;">Before setting up auto payouts, be sure to read</mark> [<mark style="color:blue;">the risk warning</mark>](https://premiumexchanger.com/wiki/preduprezhdenie-auto/)<mark style="color:blue;">!</mark>
{% endhint %}

{% hint style="info" %}
If you need to update the module on your server, please follow this [instruction](https://premium.gitbook.io/rukovodstvo-polzovatelya/osnovnye-nastroiki/faq/kak-obnovit-faily-na-servere#moduli-avtovyplat).
{% endhint %}

## Merchant Account Settings <a href="#merchant-account-settings" id="merchant-account-settings"></a>

{% hint style="warning" %}
Please note that the auto payout module is a technical tool and **does not perform the actual payout** — the Quickex receiving module processes the payout immediately after receiving funds from the client, while the auto payout module confirms the payout to update the request status to "**Completed**."

The Quickex auto payout module **must always be used together** with the [receiving module](https://premium.gitbook.io/main/osnovnye-nastroiki/merchanty-i-avtovyplaty/merchanty/quickex).

Also, keep in mind that payouts are **always** made at the service’s exchange rate. Therefore, it is highly recommended to use the Quickex [rate parser](https://premium.gitbook.io/main/osnovnye-nastroiki/valyuty-i-napravleniya-obmena/kursy-valyut/parser-kursov-valyut-parsery-2.0) for the exchange direction involving Quickex, and to enable [recalculation of requests based on the exchange rate](https://premium.gitbook.io/main/osnovnye-nastroiki/valyuty-i-napravleniya-obmena/sozdanie-novogo-napravleniya#pereschet-po-kursu-obmena) to ensure the actual payout amount matches the amount in the request.
{% endhint %}

## Module Settings <a href="#module-settings" id="module-settings"></a>

In the admin panel, create a new merchant by going to "**Auto Payouts**" ➔ "**Add Auto Payout**."

Select Quickex from the "**Module**" dropdown, enter a name for the module, and click "**Save**."

<figure><img src="../../../.gitbook/assets/image (29).png" alt="" width="389"><figcaption></figcaption></figure>

There is no need to fill in any authorization fields.

<figure><img src="https://premium.gitbook.io/~gitbook/image?url=https%3A%2F%2F2574066779-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252Fm9kqZXsNykrN6VyxxXBO%252Fuploads%252Fhcpgo0esYP63gs8hEYlt%252Fimage.png%3Falt%3Dmedia%26token%3D601c0074-951c-408a-b11c-7856129e1e3d&#x26;width=768&#x26;dpr=4&#x26;quality=100&#x26;sign=1fde9588&#x26;sv=2" alt="" width="563"><figcaption></figcaption></figure>

**Domain —** This field should be filled in only if a Quickex manager has specifically instructed you to do so (otherwise, leave it blank).

## Continuing the Setup

Next, proceed with configuring the merchant by following the [general setup instructions](https://premium.gitbook.io/rukovodstvo-polzovatelya/osnovnye-nastroiki/merchanty-i-avtovyplaty/avtovyplaty/obshie-nastroiki-merchantov-avtovyplat).