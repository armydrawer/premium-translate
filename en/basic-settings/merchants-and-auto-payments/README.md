# Merchants and Auto-Payments

Initially, the exchange operates in manual mode. You will need to check the receipt of funds from clients yourself and manually process the payments. In manual mode, you can input [your own payment details](https://premium.gitbook.io/main/en/basic-settings/merchants-and-auto-payments/merchants/ispolzovanie-svoikh-kart-koshelkov-schetov) for receiving funds from clients.

For automatic or semi-automatic modes, the following are used:

* **Merchant** — allows you to receive funds from clients into your accounts within the payment system.
* **Auto-Payment** — disburses funds to the client from your accounts in the payment system.

To automate the operation of the exchange, you can connect the receipt and payment of funds using merchants—payment systems that provide their wallets for your funds.

## Module Uploading

* Modules for uploading are available in your [personal account](https://premiumexchanger.com/uscripts/) under the "**Additional Modules**" section.
* Module files should be uploaded to the specified folders:

    * Merchants for receiving funds:

    **`wp-content/plugins/premiumbox/merchants`**

    * Auto-payments:

    **`wp-content/plugins/premiumbox/paymerchants`**

## How Merchants Work

### Receiving Funds into Your Accounts, Payment via Merchant (Semi-Automation)

If you are receiving funds into your own accounts, even with auto-payment enabled, the payment will only be available through the "**Transfer**" button in the application under the "**Requests**" section.

To do this, after receiving funds into your account according to the application, you need to change the application status to one of the following — "**User marked the application as paid**," "**Paid application**," or "**Application under review**" — only after this will the "**Transfer**" button appear in the application.

<figure><img src="../../.gitbook/assets/image (736)_eng.png" alt=""><figcaption></figcaption></figure>

### Receiving Funds into Merchant Accounts, Payment Using Your Accounts (Semi-Automation)

When using only the merchant for receiving funds, only the receipt of funds from the client will be automated. The application will automatically change to the status "**Paid application**" upon receiving funds into the merchant account from your client.

After that, you need to pay the client from your bank account/crypto wallet and manually change the application status to "**Completed application**."

### Receiving Funds into Merchant Accounts, Payment via Merchant (Full Automation)

When using merchants for both receiving and paying, you can automate the exchange process.

Upon receiving funds from your client into the merchant account, the application status will automatically change to "**Paid application**." After that, the auto-payment will disburse the specified amount to the client and change the application status first to "**Waiting for confirmation from the auto-payment module**," then to "**Completed application**."

You can also enable the display of the "**Transfer**" button for the application, even if the exchange direction is automated. In this case, the operator will have the option to manually pay the amount in the application if, for some reason, the auto-payment does not occur.

{% hint style="info" %}
When connecting a merchant for both receiving and paying, you can use modules for different services.
{% endhint %}

## General Recommendations for Connecting to Payment Systems

{% hint style="warning" %}
Please confirm the current working conditions with the technical support of the respective merchant.
{% endhint %}

Crypto Processing:

1. Custodial Services:

* Heleket
* Exnode
* AlfaBit Pay

2. Non-Custodial Services:

* Electrum Wallet (works only with BTC)
* Server Wallet (works with BTC, LTC, ETH, TRON, TON, BSC, USDT, USDC, Monero)

Exchanges: Work with Russian users/rubles

* Rapira (has auto-conversion)
* Yobit
* ABCEX

Fiat: Work with new exchanges

* Merchant001 (RUB) - merchant + auto-payment, requires KYC
* Payscrow (RUB) - merchant + auto-payment, requires KYC
* IvanPay (RUB) - merchant + auto-payment, requires KYC
* SuperMoney (RUB, KZT) - merchant only, requires KYC
* EVO (RUB) - merchant only, does not require KYC
* OTC (RUB, KZT, EUR, USD, AZN, UZS) - auto-payment only
* GoldEX (RUB, USD, EUR, TRY, KZT, BYN, UAH, PAYPAL USD) - auto-payment only
* Firekassa (RUB) - merchant + auto-payment, requires KYC, module only for 2.6

This list includes merchants and auto-payments currently used by a large number of exchanges. You can explore the complete list [here](https://premiumexchanger.com/modules/).

For advanced exchanges, we recommend using the [paid Trading Actions module](https://premiumexchanger.com/tradeapi/).