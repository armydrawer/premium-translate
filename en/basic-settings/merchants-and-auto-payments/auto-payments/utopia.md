# Utopia

{% hint style="danger" %}
<mark style="color:red;">Before setting up auto payouts, please read the</mark> [<mark style="color:blue;">risk warning</mark>](https://premium.gitbook.io/main/en/basic-settings/merchants-and-auto-payments/auto-payments/risk-warning)<mark style="color:blue;">!</mark>
{% endhint %}

{% hint style="info" %}
If you need to update the module on your server, please refer to the [instructions](https://premium.gitbook.io/main/en/en/basic-settings/faq/updating-script-files-on-the-server/how-to-update-files-on-the-server#merchant-and-auto-payout-modules).
{% endhint %}

## Merchant Side Settings

{% hint style="info" %}
For initial setup of the service on your server, you can get assistance from merchant support:

* Utopia Messenger: UNKNOWN1\
  ![](<../../../.gitbook/assets/image (248)_eng.png>)
* Telegram: [@utp1984](https://t.me/utp1984)
* Email: [1984@u.is](mailto:1984@u.is)
{% endhint %}

Download the [Utopia application](https://u.is/en/download.html) for your operating system and install it. Go through the registration process and create a new wallet.

<figure><img src="../../../.gitbook/assets/image (1995)_eng.png" alt="" width="375"><figcaption><p>Creating an Account</p></figcaption></figure>

<figure><img src="../../../.gitbook/assets/image (1996)_eng.png" alt=""><figcaption><p>Fill in the required fields</p></figcaption></figure>

<figure><img src="../../../.gitbook/assets/image (1998)_eng.png" alt=""><figcaption><p>Specify the path to the folder where the private key will be stored and create a password for your wallet</p></figcaption></figure>

<figure><img src="../../../.gitbook/assets/image (1999)_eng.png" alt=""><figcaption><p>Generating the Private Key</p></figcaption></figure>

<figure><img src="../../../.gitbook/assets/image (2000)_eng.png" alt=""><figcaption><p>The public key is your wallet address</p></figcaption></figure>

<figure><img src="../../../.gitbook/assets/image (2003)_eng.png" alt=""><figcaption><p>Main Page of the Application</p></figcaption></figure>

<figure><img src="../../../.gitbook/assets/image (2001)_eng.png" alt="" width="326"><figcaption><p>Available Currencies</p></figcaption></figure>

## Module Settings <a href="#nastroiki-modulya" id="nastroiki-modulya"></a>

In the admin panel, create a new merchant in the "**Auto Payouts**" -> "**Add Auto Payout**" section.

Select Utopia from the dropdown list in the "**Module**" field, provide a name for the module, and click "**Save**".

<figure><img src="../../../.gitbook/assets/image (1992)_eng.png" alt="" width="390"><figcaption></figcaption></figure>

Fill in the required authorization fields.

<figure><img src="../../../.gitbook/assets/image (1993)_eng.png" alt="" width="428"><figcaption></figcaption></figure>

**API Key** — the key copied from the merchant's personal account

**Domain** — URL for connection (IP address of your server + port assigned to the application during initial setup)

**Token** — public key (your wallet address obtained during registration with the service)

{% hint style="info" %}
To ensure correct issuance of details, the currency code in "**Receiving**" should be selected as USD, UUSD, or CRP (Crypton token).

![](<../../../.gitbook/assets/image (2002)_eng.png>)
{% endhint %}

## Utopia Voucher Module

To issue Utopia vouchers, set up a separate module.

### Module Settings <a href="#nastroiki-modulya-1" id="nastroiki-modulya-1"></a>

In the admin panel, create a new merchant in the "**Auto Payouts**" -> "**Add Auto Payout**" section.

Select Utopia Voucher from the dropdown list in the "**Module**" field, provide a name for the module, and click "**Save**".

<figure><img src="../../../.gitbook/assets/image (193)_eng.png" alt="" width="453"><figcaption></figcaption></figure>

Fill in the required authorization fields.

<figure><img src="../../../.gitbook/assets/image (1993)_eng.png" alt="" width="428"><figcaption></figcaption></figure>

**Domain** — URL for connection (IP address of your server + port assigned to the application during initial setup)

**Token** — public key (your wallet address obtained during registration with the service)

<figure><img src="../../../.gitbook/assets/image (193)_eng.png" alt="" width="453"><figcaption></figcaption></figure>

### Special Fields

<figure><img src="../../../.gitbook/assets/image (194)_eng.png" alt="" width="362"><figcaption></figcaption></figure>

**User Email** — choose the type of field that the client will fill out in the exchange form — the voucher will be sent to the specified email upon auto payout request.

{% hint style="info" %}
By default, the "**User Email**" option is selected — a mandatory field that the client fills out when creating a request.

![](<../../../.gitbook/assets/image (196)_eng.png>)

If you want the client to specify a different email for receiving the coupon, rename the "**To Account**" field in the currency settings to "**Email for Voucher**" or "**Email to Send Voucher**".

![](<../../../.gitbook/assets/image (197)_eng.png>)
{% endhint %}

## Continuing the Setup

Next, proceed with the merchant setup by following the [general setup instructions](https://premium.gitbook.io/main/en/basic-settings/merchants-and-auto-payments/auto-payments/obshie-nastroiki-merchantov-avtovyplat).