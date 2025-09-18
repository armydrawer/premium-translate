# Affiliate Program API (Old Version)

{% hint style="info" %}
The Affiliate Program API only works with the "**API**" and "**Affiliate Program API**" modules enabled.
{% endhint %}

### Activating the Modules:

<figure><img src="../.gitbook/assets/изображение (173).png" alt=""><figcaption></figcaption></figure>

After activating the module, go to the "**Users**" section, select the user ("**Edit**") for whom API access will be enabled, and activate the following settings:

<figure><img src="../.gitbook/assets/изображение (151).png" alt=""><figcaption></figcaption></figure>

Next, navigate to the "**Affiliate Program**" - "**Settings**" section and enable the API there:

<figure><img src="../.gitbook/assets/изображение (85).png" alt=""><figcaption></figcaption></figure>

## How to Check if the Module is Active and Where to Get the Key?

If the module is activated, the affiliate dashboard page (usually at `https://your_domain/paccount/`) will display a line for the Rest API key in the information block, where you can find your personal key (**api_key**).

<figure><img src="../.gitbook/assets/image (982).png" alt=""><figcaption></figcaption></figure>

If needed, you can generate a new key by clicking on the "**Change REST API Key**" link. After a few seconds, a new key will appear in the "**REST API Key**" field, and the old key will no longer work.

**Endpoint:** `https://your_domain/api.html`

## Data Passed via GET Parameters:

- **api_action** – pp (this action is used by the ppapi module)
- **api_key** – the issued key
- **method** – the API method of the module

You can also obtain the API link by clicking on the Rest API key link in the affiliate dashboard, which will already contain your key and look like this:

**`https://siteurl/api.html?api_action=pp&api_key={api_key}&method={method}`**

## API Methods:

### <mark style="color:blue;">get_info</mark>

Information about the partner

**Request Parameters:**

```
balance — your account balance
min_payout — minimum payout amount
items — available items
id — payout method ID
title — method name
comission — commission deducted upon payout
amount — amount you receive
```

### <mark style="color:blue;">get_links</mark>

Information about affiliate clicks

**Request Parameters:**

```
start_time - unix time from which to display (filter, optional)
end_time - unix time until which to display (filter, optional)
ip - IP address (filter, optional)
```

**Response:**

```
items — available items
id — link ID
time — unix time
date — date and time
browser — browser used
ip — IP address
referrer — REFERRER of the link click
user_hash — unique visitor hash on the site
query_string — query string in the browser (GET parameters)
```

### <mark style="color:blue;">get_exchanges</mark>

Information about affiliate exchanges

**Request Parameters:**

```
start_time - unix time from which to display requests (filter, optional)
end_time - unix time until which to display requests (filter, optional)
```

**Response:**

```
items — available items
id — payout ID
time — unix time
date — date and time
currency_code_give — currency code given
currency_code_get — currency code received
course_give — exchange rate given
course_get — exchange rate received
amount_give — amount given
amount_get — amount received
exchange_success — request status (0 - not completed, 1 - completed)
accrued — partner reward accrual (0 - not accrued, 1 - accrued)
partner_reward — amount of partner reward
user_hash — unique visitor hash on the site
statuses — history of status changes for the request, if the status logging module is enabled. Displays statuses: new request, marked as paid, paid, completed request.
```

### <mark style="color:blue;">get_payouts</mark>

List of user requests for fund withdrawals

**Request Parameters:**

```
start_time - unix time from which to display (filter, optional)
end_time - unix time until which to display (filter, optional)
```

**Response:**

```
items — available items
id — payout ID
time — unix time
date — date and time
method_id — payout method (can be viewed in get_info)
account — account to which the payout is requested
pay_amount — payout amount
pay_currency_code — currency code of the payout amount
original_amount — original payout amount
original_currency_code — currency code of the original payout amount
status — payout request status (0 - pending, 1 - completed, 2 - canceled, 3 - canceled by user)
```

### <mark style="color:blue;">add_payout</mark>

Creating a payout request

**Request Parameters:**

```
method_id — payout method (can be viewed in get_info)
account — account number for the payout
```

**Response:**

```
payout_id - payout ID
```