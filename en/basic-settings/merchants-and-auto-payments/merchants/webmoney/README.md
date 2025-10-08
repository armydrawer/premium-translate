# WebMoney

{% hint style="info" %}
If you need to update the module on your server, please refer to the [instructions](https://premium.gitbook.io/main/en/en/basic-settings/faq/updating-script-files-on-the-server/how-to-update-files-on-the-server#merchant-and-auto-payout-modules).
{% endhint %}

{% hint style="warning" %}
To ensure the security of your funds in the WebMoney system, we strongly recommend enabling the following settings in the "[Transaction Confirmation](https://security.webmoney.ru/asp/transconfirm.asp)" section: E-NUM confirmation and SMS confirmation.

![](<../../../../.gitbook/assets/image (1550)_eng.png>)

**Note:** By default, the WebMoney payment merchant does not automatically verify the client's personal data through the XML interface X19.

To enable automatic verification of personal data via the XML interface X19, you will need to configure the X19 module. For more information on how this module works, please refer to the [relevant section](https://premium.gitbook.io/main/en/basic-settings/merchants-and-auto-payments/merchants/webmoney/x19).

For more details about the XML interface X19 and the requirements for WebMoney exchange operations, please read [this link](https://wiki.webmoney.ru/projects/webmoney/wiki/%D0%98%D0%BD%D1%82%D0%B5%D1%80%D1%84%D0%B5%D0%B9%D1%81_X19).

To manually verify client personal data, use the [official X19 web interface](https://verification.webmoney.ru/XTest/X19.aspx).

For the requirements for exchange points that work with WebMoney, please refer to [this link](https://www.megastock.ru/exchange_rules.aspx?lang=ru).
{% endhint %}

## Merchant Account Settings

1. Log in to the [WebMoney](https://merchant.webmoney.ru/conf/default.asp) site with your WMID or register if you don’t have an account yet.
2. Go to the "[**Wallet List**](https://merchant.webmoney.ru/conf/purses.asp)" section and click on the "**Configure**" link next to each wallet you are using.

<figure><img src="../../../../.gitbook/assets/image (1543)_eng.png" alt=""><figcaption></figcaption></figure>

3. Configure and save the following parameters:

* Select the operating mode.
* Enter a custom "**Trade Name**," such as your website address.
* Provide the "**Secret Key**," which will be needed for further configuration.
* Specify your website address for the "**Result/Success/Fail URL**" parameters.
* Check the boxes for "**Send parameters in the preliminary request**" and "**Allow the use of URLs passed in the form**," and "**Send error notifications to the keeper**."
* For the "**Signature Generation Method**" option, select "**SHA256**."

<figure><img src="../../../../.gitbook/assets/image (1547)_eng.png" alt=""><figcaption></figcaption></figure>

## Module Settings

In the admin panel, create a new merchant in the "**Merchants**" -> "**Add Merchant**" section.

Select WebMoney from the dropdown list in the "**Module**" field, enter a name for the module, and click "**Save**."

<figure><img src="../../../../.gitbook/assets/image (1549)_eng.png" alt="" width="442"><figcaption></figcaption></figure>

Fill in the required authorization fields.

<figure><img src="../../../../.gitbook/assets/image (1548)_eng.png" alt="" width="454"><figcaption></figcaption></figure>

**WM\* Wallet** — your wallet number from the WebMoney personal account.

**Secret Key for WM\* Wallet** — the secret key you specified in the wallet settings.

## Continuing Configuration

Next, proceed to configure the merchant by following the [general setup instructions](https://premium.gitbook.io/main/en/en/basic-settings/merchants-and-auto-payments/merchants/general-merchant-settings).