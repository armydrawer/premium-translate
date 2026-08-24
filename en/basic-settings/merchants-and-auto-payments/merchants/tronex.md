# TronEx

{% hint style="info" %}
If you need to update the module on the server — use the [instructions](https://premium.gitbook.io/main/en/basic-settings/faq/updating-script-files-on-the-server/how-to-update-files-on-the-server#merchant-and-auto-payout-modules)
{% endhint %}

### Settings in the merchant's personal account

{% hint style="warning" %}
To discuss working conditions, contact the [service representative](https://t.me/tronexpr).

**Disclaimer**: when connecting your site to any service, please independently assess the possible risks of cooperation.
{% endhint %}

Contact the [service representative](https://t.me/tronexpr) to discuss working conditions and obtain login credentials.

{% hint style="warning" %}
On the merchant's side, different methods and tariffs are implemented as separate accounts in the system. Each method requires a separate account.
{% endhint %}

Along with the account credentials, the service representative will provide you with an **API Key** and **Sign Key**.

Save the received data — it is used for the merchant module to operate in the system.

Using the credentials received from the service representative, you can [log in to the service](https://tronex.world/).

### Module settings

In the admin panel, create a new merchant in the **"Merchants"** → **"Add merchant"** section.

Select the **TronEx** module from the dropdown list in the **"Module"** field, enter a name for the module and click **"Save"**.

<figure><img src="../../../.gitbook/assets/image (449).png" alt=""><figcaption></figcaption></figure>

Fill in the authorization fields.

<figure><img src="../../../.gitbook/assets/image (450).png" alt=""><figcaption></figcaption></figure>

**Domain** — leave this field empty.

**API Key** — the API Key received from the service representative.

**Sign Key** — the Sign Key received from the service representative.

{% hint style="info" %}
Make sure that both keys belong to the same account on the TronEx side.
{% endhint %}

### Merchant types

Each available payment method depends on the keys specified in the module settings and has recommended configurations:

{% tabs %}
{% tab title="VIETQR" %}
<figure><img src="../../../.gitbook/assets/image (453).png" alt=""><figcaption></figcaption></figure>

Merchant type — **Payment Link** — payment details are shown on the merchant's payment page.

<figure><img src="../../../.gitbook/assets/image (584).png" alt=""><figcaption></figcaption></figure>

Payment method — **VietQR** — select explicitly.
{% endtab %}

{% tab title="PDF" %}
<figure><img src="../../../.gitbook/assets/image (454).png" alt=""><figcaption></figcaption></figure>

Merchant type — **Requisites** — payment details are displayed via shortcodes \[to\_account], \[dest\_tag].

<figure><img src="../../../.gitbook/assets/image (562).png" alt=""><figcaption></figcaption></figure>

Payment method:

* Automatic — the selected method depends on the XML code of the "Send" currency.
* Card2Card — a card number is provided for payment by card transfer.
* SBP — a phone number and bank are provided for payment via SBP.

{% hint style="info" %}
The list of XML currency code mappings to payment methods can be found under the "Automatic" label.
{% endhint %}
{% endtab %}

{% tab title="MOBCOM" %}
<figure><img src="../../../.gitbook/assets/image (458).png" alt=""><figcaption></figcaption></figure>

Merchant type — **Requisites** — payment details are displayed via shortcodes \[to\_account], \[dest\_tag].

<figure><img src="../../../.gitbook/assets/image (574).png" alt=""><figcaption></figcaption></figure>

Payment method — **Мобильная коммерация** — select explicitly.
{% endtab %}

{% tab title="BT" %}
<figure><img src="../../../.gitbook/assets/image (468).png" alt=""><figcaption></figcaption></figure>

Merchant type — **Requisites** — payment details are displayed via shortcodes \[to\_account], \[dest\_tag].

<figure><img src="../../../.gitbook/assets/image (561).png" alt=""><figcaption></figcaption></figure>

Payment method:

* Automatic — the selected method depends on the XML code of the "Send" currency.
* Card2Card — a card number is provided for payment by card transfer.
* SBP — a phone number and bank are provided for payment via SBP.

{% hint style="info" %}
The list of XML currency code mappings to payment methods can be found under the "Automatic" label.
{% endhint %}
{% endtab %}
{% endtabs %}

### Special fields

<figure><img src="../../../.gitbook/assets/image (480).png" alt=""><figcaption></figcaption></figure>

**Bank** — specifies the bank from which the client will make the payment.

You can select a bank explicitly or add an additional field giving the client the ability to choose independently.

<details>

<summary>Example of creating such an additional field.</summary>

This field must be created as an [additional currency field](../../currencies-and-exchange-directions/additional-fields.md) with the type "Select".

It is important to specify values that match those offered in the module, for example in brackets. At the same time, you can use any bank names in any language.

Don't forget to assign a unique ID to this field. This is required for the field to appear in the selector in the merchant module settings.

<figure><img src="../../../.gitbook/assets/image (518).png" alt=""><figcaption></figcaption></figure>

</details>

<figure><img src="../../../.gitbook/assets/image (560).png" alt=""><figcaption></figcaption></figure>

**Unpaid orders removal time** — the number of minutes after which an unpaid order will be cancelled on the merchant's side.

{% hint style="info" %}
Make sure this value is not less than your standard unpaid order cancellation time.
{% endhint %}

**Cron file** — [create a cron job](../../faq/how-to-create-a-cron-job-on-a-server.md) with the following link on your server.

### Continuing setup

Additional module settings are configured according to the [general setup instructions](general-merchant-settings.md).
