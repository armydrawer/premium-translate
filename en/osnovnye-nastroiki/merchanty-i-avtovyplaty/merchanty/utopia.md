# Utopia

{% hint style="info" %}
If you need to update the module on your server, please follow the [instructions](https://premium.gitbook.io/rukovodstvo-polzovatelya/osnovnye-nastroiki/faq/kak-obnovit-faily-na-servere#moduli-merchantov).
{% endhint %}

## Merchant-Side Setup

{% hint style="warning" %}
The initial setup of the service on your server can be assisted by the merchant support team:

* Utopia Messenger: UNKNOWN1\
  ![](<../../../.gitbook/assets/image (248).png>)
* Telegram: [@utp1984](https://t.me/utp1984)
* Email: [1984@u.is](mailto:1984@u.is)
{% endhint %}

Download the [Utopia app](https://u.is/en/download.html) for your operating system and install it. Complete the registration process and create a new wallet.

<figure><img src="../../../.gitbook/assets/utopia_GuMWxeYqQj.png" alt="" width="375"><figcaption><p>Creating an account</p></figcaption></figure>

<figure><img src="../../../.gitbook/assets/utopia_6KVpKP7MqV.png" alt=""><figcaption><p>Fill in the required fields</p></figcaption></figure>

<figure><img src="../../../.gitbook/assets/utopia_1dTGinQV89.png" alt=""><figcaption><p>Specify the folder path where your private key will be stored and create a password for your wallet</p></figcaption></figure>

<figure><img src="../../../.gitbook/assets/utopia_HDeIfnYgkC.png" alt=""><figcaption><p>Generating the private key</p></figcaption></figure>

<figure><img src="../../../.gitbook/assets/utopia_G9GdSU4r7V.png" alt=""><figcaption><p>Your public key is the address of your wallet</p></figcaption></figure>

<figure><img src="../../../.gitbook/assets/utopia_mRDQ9jaNO5.png" alt=""><figcaption><p>Main application screen</p></figcaption></figure>

<figure><img src="../../../.gitbook/assets/utopia_N9Et2UDpXJ.png" alt="" width="326"><figcaption><p>Available currencies</p></figcaption></figure>

## Module Configuration

In the admin panel, create a new merchant by going to "**Merchants**" -> "**Add Merchant**."

Select "Utopia" from the dropdown menu in the "**Module**" field, enter a name for the module, and click "**Save**."

<figure><img src="../../../.gitbook/assets/image (1989).png" alt="" width="418"><figcaption></figcaption></figure>

Fill in the required authorization fields.

<figure><img src="../../../.gitbook/assets/image (1990).png" alt="" width="452"><figcaption></figcaption></figure>

**Domain** — The URL for connection (your server’s IP address + the port assigned to the application during initial setup)

**Token** — Your public key (the wallet address you received during registration)

{% hint style="info" %}
To ensure correct processing of payment details, the currency code in the "Giving" field must be set to USD, UUSD, or CRP (Crypton token).

![](<../../../.gitbook/assets/image (199).png>)
{% endhint %}

## Utopia Voucher Module

To accept Utopia vouchers as a payment method, configure a separate module.

### Module Settings



In the admin panel, create a new merchant by going to "**Merchants**" -> "**Add Merchant**."

Select **Utopia Voucher** from the dropdown menu in the "**Module**" field, enter a name for the module, and click "**Save**."

<figure><img src="../../../.gitbook/assets/image (200).png" alt="" width="471"><figcaption></figcaption></figure>

Fill in the required authorization fields.

<figure><img src="../../../.gitbook/assets/image (1990).png" alt="" width="452"><figcaption></figcaption></figure>

- **Domain** — the connection URL (your server’s IP address plus the port assigned to the application during initial setup)
- **Token** — the public key (your wallet address obtained when registering with the service)

{% hint style="warning" %}
To ensure vouchers are accepted correctly, the currency code in the "**Give**" field must be either **UUSD** (US Dollar) or **CRP** (Utopia’s native token).

<img src="../../../.gitbook/assets/image (201).png" alt="" data-size="original">

There is no need to add a "**From Account**" field for the "**Give**" currency in the exchange form — the client’s order will display a "**Proceed to Payment**" button. Clicking this button opens a page where the client can enter the voucher code. After entering a valid code, the client will be redirected back to the order page.
{% endhint %}

## Continuing Setup

Next, continue configuring the merchant by following the [general setup instructions](https://premium.gitbook.io/rukovodstvo-polzovatelya/osnovnye-nastroiki/merchanty-i-avtovyplaty/merchanty/obshie-nastroiki-merchantov).