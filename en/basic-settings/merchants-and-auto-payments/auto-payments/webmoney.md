# Webmoney

{% hint style="danger" %}
<mark style="color:red;">Before setting up automatic payouts, please read the</mark> [<mark style="color:blue;">risk warning</mark>](https://premium.gitbook.io/main/osnovnye-nastroiki/merchanty-i-avtovyplaty/avtovyplaty/preduprezhdenie-o-riskakh)<mark style="color:blue;">!</mark>
{% endhint %}

{% hint style="info" %}
If you need to update the module on the server, please refer to the [instructions](https://premium.gitbook.io/main/en/basic-settings/faq/updating-script-files-on-the-server/how-to-update-files-on-the-server#merchant-and-auto-payout-modules).
{% endhint %}

## Settings in the Merchant's Personal Account

1. Log in to the [Webmoney](https://merchant.webmoney.ru/conf/default.asp) website using your WMID, or register if you do not have an account yet.
2. Activate the [XML interface X2](https://wiki.webmoney.ru/projects/webmoney/wiki/interfeys_x2). We recommend [restricting the X2 interface](https://security.webmoney.ru/) to the IP address of your server. If you want to receive reserves in your wallets in real-time, you also need to connect the [XML interface X9](https://wiki.webmoney.ru/projects/webmoney/wiki/interfeys_x9).
3. In WebMoney Keeper Classic, go to the menu item "**Tools" → "Program Settings"**, then navigate to the **"Security"** tab and click the **"Save key to file"** button.\
   Follow the procedures prompted by WM Keeper. Specify the path to save the key file and enter the key file password twice.

<figure><img src="../../../.gitbook/assets/Screenshot_36 (2)_eng.png" alt=""><figcaption></figcaption></figure>

4. Upload the saved .kwm key file to the server under the user account created for the website (not root) in the directory:\
   `your_domain/wp-content/plugins/premiumbox/paymerchants/webmoney/dostup/`

## Module Settings

In the admin panel, create a new merchant in the "**Merchants**" -> "**Add Automatic Payout**" section.

Select Webmoney from the dropdown list in the "**Module**" field, enter a name for the module, and click "**Save**".

<figure><img src="../../../.gitbook/assets/image (1551)_eng.png" alt="" width="438"><figcaption></figcaption></figure>

Fill in the required authorization fields.

<figure><img src="../../../.gitbook/assets/image (1552)_eng.png" alt="" width="447"><figcaption></figcaption></figure>

**WMID** — enter your WMID

**Key file name .kwm** — the name of the key file

**Key file password .kwm** — the password for the key file

**WM* wallet** — your wallet number from the Webmoney personal account

## Continuing the Setup

Next, configure the automatic payout merchant by following the [general setup instructions](https://premium.gitbook.io/rukovodstvo-polzovatelya/osnovnye-nastroiki/merchanty-i-avtovyplaty/avtovyplaty/obshie-nastroiki-merchantov-avtovyplat).