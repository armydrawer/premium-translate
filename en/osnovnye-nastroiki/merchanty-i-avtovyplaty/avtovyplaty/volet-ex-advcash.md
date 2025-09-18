# Volet (formerly Advcash)

{% hint style="info" %}
If you need to update the module on the server, please refer to the [instructions](https://premium.gitbook.io/main/osnovnye-nastroiki/faq/obnovlenie-failov-skripta-na-servere/kak-obnovit-faily-na-servere#moduli-merchantov-i-avtovyplat).
{% endhint %}

{% hint style="danger" %}
<mark style="color:red;">Before setting up auto payouts, be sure to read the</mark> [<mark style="color:blue;">risk warning</mark>](https://premium.gitbook.io/main/osnovnye-nastroiki/merchanty-i-avtovyplaty/avtovyplaty/preduprezhdenie-o-riskakh)<mark style="color:blue;">!</mark>
{% endhint %}

### Merchant Account Settings <a href="#nastroiki-v-lichnom-kabinete-merchanta" id="nastroiki-v-lichnom-kabinete-merchanta"></a>

Register in the [Volet](https://account.volet.com/register) system and verify your account to work with the API.

{% hint style="warning" %}
To receive funds in your merchant accounts, it is sufficient to create an **SCI (shopping cart interface)** following the instructions provided below. If you also want to withdraw funds from your merchant accounts, you will need to create a new **API (application programming interface)** as well.
{% endhint %}

Create a new API for merchant operations.

Go to the "**For Developers**" section and click the "**Create New API**" button.

<figure><img src="https://2722984412-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2Fm9kqZXsNykrN6VyxxXBO%2Fuploads%2F8psSPCSWSTp1eiIzISZY%2Fimage.png?alt=media&#x26;token=7fcdd5aa-7089-4f80-9182-1d30016517ca" alt="" width="188"><figcaption></figcaption></figure>

<figure><img src="https://2722984412-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2Fm9kqZXsNykrN6VyxxXBO%2Fuploads%2FBcpqskUKVk3ULEZiLhi7%2Fimage.png?alt=media&#x26;token=fcf15fff-1f8a-4914-9cbc-9edb4d625a09" alt=""><figcaption></figcaption></figure>

Fill out the form that appears and click "**Save**."

<figure><img src="https://2722984412-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2Fm9kqZXsNykrN6VyxxXBO%2Fuploads%2FWmhrfWDVi8w3DV4id8XE%2Fimage.png?alt=media&#x26;token=c03423b1-5978-40bc-90bb-6432e2cbb3a3" alt="" width="375"><figcaption></figcaption></figure>

### Module Settings <a href="#nastroiki-modulya" id="nastroiki-modulya"></a>

In the admin panel, create a new merchant in the "**Merchants**" section by selecting "**Add Auto Payout**."

Choose AdvCash from the dropdown menu in the "**Module**" field, enter a name for the module, and click "**Save**."

<figure><img src="../../../.gitbook/assets/image (674).png" alt=""><figcaption></figcaption></figure>

Fill in the required authorization fields.

<figure><img src="../../../.gitbook/assets/image (675).png" alt=""><figcaption></figcaption></figure>

**API Name** — **the name of the API** specified in your AdvCash account

**Account Email** — **the email address** associated with your AdvCash account

**API Password** — **the API password** provided in your AdvCash account

**Wallet Numbers** — specify the desired wallet numbers for fiat currency withdrawals from your AdvCash account

<figure><img src="../../../.gitbook/assets/image (676).png" alt=""><figcaption></figcaption></figure>

### Continuing the Setup <a href="#prodolzhenie-nastroiki" id="prodolzhenie-nastroiki"></a>

Next, configure the merchant by following the [general setup instructions](https://premium.gitbook.io/rukovodstvo-polzovatelya/osnovnye-nastroiki/merchanty-i-avtovyplaty/avtovyplaty/obshie-nastroiki-avtovyplat).