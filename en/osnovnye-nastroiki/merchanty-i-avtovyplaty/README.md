# Merchants and Auto Payouts

Initially, the exchanger operates in manual mode. You verify the receipt of funds from the client yourself and manually make the payouts. In manual mode, you can enter [your own payment details](https://premium.gitbook.io/main/osnovnye-nastroiki/merchanty-i-avtovyplaty/merchanty/ispolzovanie-svoikh-kart-koshelkov-schetov) in the order to receive funds from clients.

For automatic or semi-automatic operation, the following are used:

* **Merchant** — allows you to receive funds from clients into your accounts within the payment system  
* **Auto Payout** — automatically pays out funds to the client from your accounts within the payment system

To automate the exchanger’s workflow, you can enable accepting and paying out funds through merchants — payment systems that provide wallets for your funds.

## Module Installation

* Modules are available for download in your [personal account](https://premiumexchanger.com/uscripts/) under the "**Additional Modules**" section.  
* Module files should be uploaded to the following folders:

    * Merchants for receiving funds:  
    **`wp-content/plugins/premiumbox/merchants`**

    * Auto payouts:  
    **`wp-content/plugins/premiumbox/paymerchants`**

## How Merchants Work

### Receiving Funds to Your Own Accounts, Payouts via Merchant (Semi-Automatic)

If you receive funds into your own accounts, even with auto payout enabled, payouts will only be available via the "**Transfer**" button in the order within the "**Orders**" section.

After receiving funds into your account according to the order, you need to change the order status to one of the following: "**User marked order as paid**", "**Paid order**", or "**Order under review**". Only then will the "**Transfer**" button appear in the order.

<figure><img src="../../.gitbook/assets/image (736).png" alt=""><figcaption></figcaption></figure>

### Receiving Funds to Merchant Accounts, Payouts Using Your Own Accounts (Semi-Automatic)

If you use only a merchant for receiving funds, only the receipt of funds from the client will be automated. The order will automatically change to the status "**Paid order**" once the funds are received in the merchant account from your client.

After this, you need to transfer the funds to the client from your bank account or crypto wallet and manually change the request status to "**Completed Request**."

### Receiving funds into the merchant account and making payouts via the merchant (full automation)

When using merchants for both receiving and payouts, you can fully automate the exchange process.

Once you receive funds from your client into the merchant account, the request status will automatically change to "**Paid Request**." After that, the auto-payout system will send the amount specified in the request to the client and update the request status first to "**Awaiting Confirmation from Auto-Payout Module**," and then to "**Completed Request**."

You can also enable the "**Transfer**" button to appear on the request, even if the exchange direction is automated. This allows the operator to manually process the payout if, for some reason, the auto-payout does not occur.

{% hint style="info" %}
When connecting a merchant for both receiving and payouts, you can use modules for different services.
{% endhint %}

## General Recommendations for Connecting to Payment Systems

{% hint style="warning" %}
Please check the current operating conditions with the technical support of each merchant.
{% endhint %}

Crypto Processing Services:

1. Custodial Services:

* Heleket  
* Exnode  
* AlfaBit Pay  

2. Non-Custodial Services:

* Electrum Wallet (BTC only)  
* Server Wallet (supports BTC, LTC, ETH, TRON, TON, BSC, USDT, USDC, Monero)  

Exchanges: Support users from Russia / Russian ruble

* Rapira (includes auto-conversion)  
* Yobit  
* ABCEX  

Fiat Services: Work with new exchangers

* Merchant001 (RUB) – merchant + auto-payout, KYC required  
* Payscrow (RUB) – merchant + auto-payout, KYC required  
* IvanPay (RUB) – merchant + auto-payout, KYC required  
* SuperMoney (RUB, KZT) – merchant only, KYC required  
* EVO (RUB) – merchant only, no KYC required  
* OTC (RUB, KZT, EUR, USD, AZN, UZS) – auto-payout only  
* GoldEX (RUB, USD, EUR, TRY, KZT, BYN, UAH, PAYPAL USD) – auto-payout only  
* Firekassa (RUB) – merchant + auto-payout, KYC required, module only for version 2.6

This list includes the merchants and automatic payouts currently used by a large number of exchangers. You can view the full list [here](https://premiumexchanger.com/modules/).

For advanced exchangers, we recommend using the [paid Trading Actions module](https://premiumexchanger.com/tradeapi/).