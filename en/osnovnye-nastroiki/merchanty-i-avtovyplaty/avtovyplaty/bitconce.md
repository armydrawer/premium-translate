# Bitconce

## Merchant Account Settings

Register or log in to the Bitconce system. Access your Bitconce account by entering your token:

<figure><img src="../../../.gitbook/assets/изображение (116).png" alt="" width="563"><figcaption></figcaption></figure>

Go to the **API** section:

<figure><img src="../../../.gitbook/assets/изображение (92).png" alt="" width="341"><figcaption></figcaption></figure>

To get your token, click the **Create** button in the **API Token** block:

<figure><img src="../../../.gitbook/assets/изображение (100).png" alt=""><figcaption></figcaption></figure>

## Module Settings

In the admin panel, go to **Merchants** -> **Auto Payouts**, click **Add**, and select Bitconce.

<figure><img src="../../../.gitbook/assets/image (1270).png" alt=""><figcaption></figcaption></figure>

Fill in the required authorization fields.

<figure><img src="../../../.gitbook/assets/image (1271).png" alt=""><figcaption></figcaption></figure>

**Token** — the token you obtained from your Bitconce account

## Special Fields

<figure><img src="../../../.gitbook/assets/image (1272).png" alt=""><figcaption></figcaption></figure>

**Direction** — select the bank for the auto payout

* **qiwi** — payout from a Qiwi wallet  
* **yandex** — payout from YooMoney  
* **banks** — user selects the bank  
* **SBP** — payout via the Faster Payments System (SBP)

{% hint style="info" %}
You can offer your client a choice of bank for the payout on the exchange page. To do this, select **banks** in the merchant settings and add an [additional field for the payout currency](https://premium.gitbook.io/rukovodstvo-polzovatelya/osnovnye-nastroiki/valyuty-i-napravleniya/dobavlenie-novoi-valyuty#vkladka-dop.-polya) with the following configuration (the module supports only these banks — **Sberbank, Raiffeisen, Tinkoff**):

![](<../../../.gitbook/assets/image (247).png>)  
Once added, this field will appear on the exchange form, allowing the client to select the bank from which they want to receive funds from the exchanger.
{% endhint %}

## Continuing Setup

Next, complete the auto payout merchant setup by following the [general setup instructions](https://premium.gitbook.io/rukovodstvo-polzovatelya/osnovnye-nastroiki/merchanty-i-avtovyplaty/avtovyplaty/obshie-nastroiki-merchantov-avtovyplat).