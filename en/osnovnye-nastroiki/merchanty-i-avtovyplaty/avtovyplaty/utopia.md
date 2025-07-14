# Utopia

{% hint style="danger" %}
<mark style="color:red;">Before setting up auto payouts, be sure to read</mark> [<mark style="color:blue;">the risk warning</mark>](https://premiumexchanger.com/wiki/preduprezhdenie-auto/)<mark style="color:blue;">!</mark>
{% endhint %}

{% hint style="info" %}
If you need to update the module on your server, please follow this [guide](https://premium.gitbook.io/rukovodstvo-polzovatelya/osnovnye-nastroiki/faq/kak-obnovit-faily-na-servere#moduli-avtovyplat).
{% endhint %}

## Merchant-Side Setup

{% hint style="info" %}
The merchant support team can assist you with the initial setup of the service on your server:

* Utopia Messenger: UNKNOWN1\
  ![](<../../../.gitbook/assets/image (248).png>)
* Telegram: [@utp1984](https://t.me/utp1984)
* Email: [1984@u.is](mailto:1984@u.is)
{% endhint %}

Download the [Utopia app](https://u.is/en/download.html) for your operating system and install it. Complete the registration process and create a new wallet.

<figure><img src="../../../.gitbook/assets/image (1995).png" alt="" width="375"><figcaption><p>Creating an account</p></figcaption></figure>

<figure><img src="../../../.gitbook/assets/image (1996).png" alt=""><figcaption><p>Fill in the required fields</p></figcaption></figure>

<figure><img src="../../../.gitbook/assets/image (1998).png" alt=""><figcaption><p>Specify the folder path where your private key will be stored and create a password for your wallet</p></figcaption></figure>

<figure><img src="../../../.gitbook/assets/image (1999).png" alt=""><figcaption><p>Generating the private key</p></figcaption></figure>

<figure><img src="../../../.gitbook/assets/image (2000).png" alt=""><figcaption><p>Your public key is your wallet address</p></figcaption></figure>

<figure><img src="../../../.gitbook/assets/image (2003).png" alt=""><figcaption><p>Main application screen</p></figcaption></figure>

<figure><img src="../../../.gitbook/assets/image (2001).png" alt="" width="326"><figcaption><p>Available currencies</p></figcaption></figure>

## Module Configuration <a href="#nastroiki-modulya" id="nastroiki-modulya"></a>

In the admin panel, create a new merchant under "**Auto Payouts**" -> "**Add Auto Payout**."

Select "Utopia" from the "**Module**" dropdown, enter a name for the module, and click "**Save**."

<figure><img src="../../../.gitbook/assets/image (1992).png" alt="" width="390"><figcaption></figcaption></figure>

Fill in the required authorization fields.

<figure><img src="../../../.gitbook/assets/image (1993).png" alt="" width="428"><figcaption></figcaption></figure>

**API Key** — the key copied from the merchant’s personal account

**Domain** — the connection URL (your server’s IP address + port assigned to the application during initial setup)

**Token** — the public key (your wallet address obtained during registration with the service)

Here is a natural, fluent English translation of the provided text:

---

{% hint style="info" %}
To correctly display the payment details, the currency code in the "**Receiving**" field must be set to USD, UUSD, or CRP (Crypton token).

![](<../../../.gitbook/assets/image (2002).png>)
{% endhint %}

## Utopia Voucher Module

Set up a separate module to handle Utopia voucher payouts.

### Module Settings <a href="#module-settings-1" id="module-settings-1"></a>

In the admin panel, create a new merchant under "**Auto Payouts**" -> "**Add Auto Payout**."

Select **Utopia Voucher** from the dropdown menu in the "**Module**" field, enter a name for the module, and click "**Save**."

<figure><img src="../../../.gitbook/assets/image (193).png" alt="" width="453"><figcaption></figcaption></figure>

Fill in the required authorization fields.

<figure><img src="../../../.gitbook/assets/image (1993).png" alt="" width="428"><figcaption></figcaption></figure>

**Domain** — the URL for connection (your server’s IP address + the port assigned to the application during initial setup)

**Token** — the public key (your wallet address obtained when registering with the service)

<figure><img src="../../../.gitbook/assets/image (193).png" alt="" width="453"><figcaption></figcaption></figure>

### Special Fields

<figure><img src="../../../.gitbook/assets/image (194).png" alt="" width="362"><figcaption></figcaption></figure>

**User’s E-mail** — select the field type that the client will fill out in the exchange form; the voucher will be sent to this e-mail automatically upon payout request approval.

{% hint style="info" %}
By default, "**User’s E-mail**" is selected — this is a required field that the client must fill out when creating a request.

![](<../../../.gitbook/assets/image (196).png>)

If you want the client to specify a different e-mail address to receive the voucher, rename the "**To Account**" field in the currency settings to "**E-mail to send the voucher to**" or "**Voucher E-mail**."

![](<../../../.gitbook/assets/image (197).png>)
{% endhint %}

## Continuing Setup

Next, configure the merchant by following the [general setup instructions](https://premium.gitbook.io/rukovodstvo-polzovatelya/osnovnye-nastroiki/merchanty-i-avtovyplaty/avtovyplaty/obshie-nastroiki-merchantov-avtovyplat).

---

If you need the images or links adapted or further refined, just let me know!