# Volet (formerly AdvCash)

{% hint style="info" %}
If you need to update the module on your server, please follow the [update instructions](https://premium.gitbook.io/rukovodstvo-polzovatelya/osnovnye-nastroiki/faq/kak-obnovit-faily-na-servere#moduli-avtovyplat).
{% endhint %}

{% hint style="danger" %}
<mark style="color:red;">Before setting up auto payouts, be sure to read</mark> the [<mark style="color:blue;">risk warning</mark>](https://premiumexchanger.com/wiki/preduprezhdenie-auto/)<mark style="color:blue;">!</mark>
{% endhint %}

### Merchant Account Settings <a href="#merchant-account-settings" id="merchant-account-settings"></a>

Register an account with [Volet](https://account.volet.com/register) and verify it to enable API access.

{% hint style="warning" %}
To receive funds into your merchant account, it’s enough to create an **SCI (Shopping Cart Interface)** following the instructions below. If you also want to make payouts from your merchant account, you will need to create a separate **API (Application Programming Interface)**.
{% endhint %}

Create a new API for your merchant account.

Go to the "**For Developers**" section and click "**Create New API**."

<figure><img src="https://2722984412-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2Fm9kqZXsNykrN6VyxxXBO%2Fuploads%2F8psSPCSWSTp1eiIzISZY%2Fimage.png?alt=media&#x26;token=7fcdd5aa-7089-4f80-9182-1d30016517ca" alt="" width="188"><figcaption></figcaption></figure>

<figure><img src="https://2722984412-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2Fm9kqZXsNykrN6VyxxXBO%2Fuploads%2FBcpqskUKVk3ULEZiLhi7%2Fimage.png?alt=media&#x26;token=fcf15fff-1f8a-4914-9cbc-9edb4d625a09" alt=""><figcaption></figcaption></figure>

Fill out the form that appears and click "**Save**."

<figure><img src="https://2722984412-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2Fm9kqZXsNykrN6VyxxXBO%2Fuploads%2FWmhrfWDVi8w3DV4id8XE%2Fimage.png?alt=media&#x26;token=c03423b1-5978-40bc-90bb-6432e2cbb3a3" alt="" width="375"><figcaption></figcaption></figure>

### Module Settings <a href="#module-settings" id="module-settings"></a>

In the admin panel, create a new merchant under "**Merchants**" -> "**Add Auto Payout**."

Select AdvCash from the "**Module**" dropdown, enter a name for the module, and click "**Save**."

<figure><img src="../../../.gitbook/assets/image (674).png" alt=""><figcaption></figcaption></figure>

Fill in the required authorization fields.

<figure><img src="../../../.gitbook/assets/image (675).png" alt=""><figcaption></figcaption></figure>

- **API Name** — the name of the API you created in your AdvCash account  
- **Account Email** — the email address associated with your AdvCash account  
- **API Password** — the API password you set in your AdvCash account

**Wallet Numbers** — specify the desired wallet numbers for fiat currency withdrawals from your AdvCash personal account.

<figure><img src="../../../.gitbook/assets/image (676).png" alt=""><figcaption></figcaption></figure>

### Continuing the Setup <a href="#prodolzhenie-nastroiki" id="prodolzhenie-nastroiki"></a>

Next, proceed with configuring the merchant by following the [general setup instructions](https://premium.gitbook.io/rukovodstvo-polzovatelya/osnovnye-nastroiki/merchanty-i-avtovyplaty/avtovyplaty/obshie-nastroiki-avtovyplat).