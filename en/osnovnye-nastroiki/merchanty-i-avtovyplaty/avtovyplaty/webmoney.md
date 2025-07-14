# Webmoney

{% hint style="danger" %}
<mark style="color:red;">Before setting up auto payouts, be sure to read the</mark> [<mark style="color:blue;">risk warning</mark>](https://premiumexchanger.com/wiki/preduprezhdenie-auto/)<mark style="color:blue;">!</mark>
{% endhint %}

{% hint style="info" %}
If you need to update the module on your server, please follow this [instruction](https://premium.gitbook.io/rukovodstvo-polzovatelya/osnovnye-nastroiki/faq/kak-obnovit-faily-na-servere#moduli-avtovyplat).
{% endhint %}

## Settings in the Merchant’s Personal Account

1. Log in to the [Webmoney website](https://merchant.webmoney.ru/conf/default.asp) using your WMID, or register if you don’t have an account yet.
2. Enable the [XML X2 interface](https://wiki.webmoney.ru/projects/webmoney/wiki/interfeys_x2). We recommend [restricting access to the X2 interface](https://security.webmoney.ru/) by your server’s IP address. If you want to receive real-time balance updates on your wallets, you will also need to enable the [XML X9 interface](https://wiki.webmoney.ru/projects/webmoney/wiki/interfeys_x9).
3. In WebMoney Keeper Classic, go to the menu "**Tools → Program Settings**", switch to the **Security** tab, and click **Save key to file**.\
   Follow the steps prompted by WM Keeper. Choose a location to save the key file, and enter the key file password twice.

<figure><img src="../../../.gitbook/assets/Screenshot_36 (2).png" alt=""><figcaption></figcaption></figure>

4. Upload the saved .kwm key file to your server under the user account created for your website (not root) into the directory:\
   `your_domain/wp-content/plugins/premiumbox/paymerchants/webmoney/dostup/`

## Module Settings

In the admin panel, create a new merchant under "**Merchants**" → "**Add Auto Payout**."

Select Webmoney from the "**Module**" dropdown, enter a name for the module, and click "**Save**."

<figure><img src="../../../.gitbook/assets/image (1551).png" alt="" width="438"><figcaption></figcaption></figure>

Fill in the required authorization fields.

<figure><img src="../../../.gitbook/assets/image (1552).png" alt="" width="447"><figcaption></figcaption></figure>

**WMID** — enter your WMID

**Key file name (.kwm)** — enter the name of your key file

**Key file password (.kwm)** — enter the password for your key file

**WM\* wallet** — enter your wallet number from your Webmoney account

## Continuing Setup

Next, complete the merchant auto payout setup by following the [general setup instructions](https://premium.gitbook.io/rukovodstvo-polzovatelya/osnovnye-nastroiki/merchanty-i-avtovyplaty/avtovyplaty/obshie-nastroiki-merchantov-avtovyplat).