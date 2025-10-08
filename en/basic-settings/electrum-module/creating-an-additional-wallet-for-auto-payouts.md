# Creating an Additional Wallet (for Auto-Payouts)

{% hint style="danger" %}
This guide requires updates. Please wait for corrections to be made soon. We apologize for any inconvenience caused.
{% endhint %}

If you are using Electrum to receive and send BTC, we recommend creating two separate wallets to keep receiving and sending transactions on different wallets.

{% hint style="warning" %}
To filter out "tainted" cryptocurrency when sending funds, it is recommended to use separate wallets for receiving and sending. Otherwise, there is a risk of sending out tainted cryptocurrency that may have been received from clients.
{% endhint %}

To ensure the proper functioning of two independent wallets, you need to reinstall the Electrum module in a **different directory** on the server.

Using the file manager in the ISP Manager panel, under the <mark style="color:green;">user account created for the website</mark> (not the <mark style="color:red;">root user</mark>), create a directory for the second module in the root folder of the website.

Install the Electrum module following the same steps as the first installation, as described in [this guide](https://premium.gitbook.io/main/en/basic-settings/modul-electrum/ustanovka-i-nastroika-electrum#zagruzka-failov-na-server).

Create a new wallet and upload the wallet file to the folder designated for the second wallet, following the same process as for the first wallet, starting from [Step 10 in this guide](https://premium.gitbook.io/main/en/basic-settings/modul-electrum/ustanovka-i-nastroika-electrum). Afterward, in the [Electrum Auto-Payout Module](https://premium.gitbook.io/main/en/basic-settings/merchants-and-auto-payments/auto-payments/electrum), specify the password for the payout wallet when entering the authorization details.