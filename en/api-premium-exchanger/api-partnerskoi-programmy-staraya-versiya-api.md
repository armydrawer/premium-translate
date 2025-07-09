# Affiliate Program API (old version API)

{% hint style="info" %}
The Affiliate Program API works only with the enabled modules "**API**" and "**Affiliate Program API**"
{% endhint %}

Activate the modules:

<figure><img src="../.gitbook/assets/изображение (173).png" alt=""><figcaption></figcaption></figure>

After activating the module, go to the "**Users**" section -> select the user ("**Edit**") for whom API access will be enabled and activate the following parameters:

<figure><img src="../.gitbook/assets/изображение (151).png" alt=""><figcaption></figcaption></figure>

Then go to the "**Affiliate Program**" section - "**Settings**" and activate the API in this section:

<figure><img src="../.gitbook/assets/изображение (85).png" alt=""><figcaption></figcaption></figure>

## How to know if the module is active and where to get the key?

If the module is activated, then on the affiliate dashboard page (usually the page `https://your_domain/paccount/`) in the information block, a line with the Rest API key will be displayed, where you can view your personal key (**api_key**).

<figure><img src="../.gitbook/assets/image (982).png" alt=""><figcaption></figcaption></figure>

If necessary, you can generate a new key by clicking on the link "**Change REST API key**" - after a couple of seconds, a new key will be displayed in the "**REST API key**" field, and the old key will stop working.

Entry point: `https://your_domain/api.html`

## Data passed as GET parameters:

**api_action** – pp (this is the action used by the ppapi module)\
**api_key** – issued key\
**method** – API module method

You can also get the API link by clicking on the link in the affiliate dashboard Rest API key, it will already contain your key and will look like this:

**`https://siteurl/api.html?api_action=pp&api_key={api_key}&method={method}`**

## API methods:

### <mark style="color:blue;">get_info</mark>

Information about the partner

Request parameters:

```
---
```

```
balance — your account balance
min_payout — minimum payout amount
items — available items
id — payout method id
title — method name
comission — commission deducted upon payout
amount — amount you receive
```

### <mark style="color:blue;">get_links</mark>

Information about affiliate links

Request parameters:

```
method_id - метод выплаты (посмотреть можно в get_info)
account - счет на который заказана выплата
amount - сумма выплаты
currency_code - код валюты суммы выплаты
```

method_id - payment method (can be viewed in get_info)
account - account number for payment

response:

payout_id - payout id