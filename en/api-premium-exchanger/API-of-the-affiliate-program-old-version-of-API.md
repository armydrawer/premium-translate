# Affiliate Program API (Old API Version)

{% hint style="info" %}
The Affiliate Program API only works when the "**API**" and "**Affiliate Program API**" modules are enabled.
{% endhint %}

### Activating the Modules:

<figure><img src="../.gitbook/assets/изображение (173).png" alt=""><figcaption></figcaption></figure>

After activating the module, go to the "**Users**" section -> select a user ("**Edit**") for whom API access will be enabled, and activate the following parameters:

<figure><img src="../.gitbook/assets/изображение (151).png" alt=""><figcaption></figcaption></figure>

Next, navigate to the "**Affiliate Program**" -> "**Settings**" section and enable the API there:

<figure><img src="../.gitbook/assets/изображение (85).png" alt=""><figcaption></figcaption></figure>

---

## How to Check if the Module is Active and Where to Find the Key?

If the module is active, the **Rest API Key** field will appear in the information block on the affiliate dashboard page (usually located at `https://your_domain/paccount/`). This field displays your personal key (**api_key**).

<figure><img src="../.gitbook/assets/image (982).png" alt=""><figcaption></figcaption></figure>

If needed, you can generate a new key by clicking the "**Change REST API Key**" link. Within a few seconds, a new key will appear in the "**REST API Key**" field, and the old key will stop working.

**Entry Point:** `https://your_domain/api.html`

---

## Data Passed via GET Parameters:

- **api_action** – `pp` (this action is used by the `ppapi` module)  
- **api_key** – the issued key  
- **method** – the API module method  

You can also get the API link by clicking the **Rest API Key** link in the affiliate dashboard. The link will already include your key and look like this:

**`https://siteurl/api.html?api_action=pp&api_key={api_key}&method={method}`**

---

## API Methods:

### <mark style="color:blue;">get_info</mark>

Provides information about the affiliate.

**Request Parameters:**

```
balance — your account balance
min_payout — minimum payout amount
items — available items
id — payout method ID
title — payout method name
commission — commission deducted during payout
amount — amount you receive
```

---

### <mark style="color:blue;">get_links</mark>

Provides information about affiliate link clicks.

**Request Parameters:**

```
start_time - Unix timestamp from which to display data (optional filter)
end_time - Unix timestamp until which to display data (optional filter)
ip - IP address (optional filter)
```

**Response:**

```
items — available items
id — link ID
time — Unix timestamp
date — date and time
browser — browser used
ip — IP address
referrer — referrer of the link click
user_hash — unique hash of the site visitor
query_string — query string in the browser (GET parameters)
```

---

### <mark style="color:blue;">get_exchanges</mark>

Provides information about affiliate exchanges.

**Request Parameters:**

```
start_time - Unix timestamp from which to display requests (optional filter)
end_time - Unix timestamp until which to display requests (optional filter)
```

**Response:**

```
items — available items
id — exchange ID
time — Unix timestamp
date — date and time
currency_code_give — currency code for the given amount
currency_code_get — currency code for the received amount
course_give — exchange rate for the given amount
course_get — exchange rate for the received amount
amount_give — amount given
amount_get — amount received
exchange_success — exchange status (0 - not completed, 1 - completed)
accrued — affiliate reward status (0 - not accrued, 1 - accrued)
partner_reward — affiliate reward amount
user_hash — unique hash of the site visitor
statuses — status change history of the exchange request (if the status logging module is enabled). Displays statuses such as: new request, marked as paid, paid, completed.
```

---

### <mark style="color:blue;">get_payouts</mark>

Provides a list of user requests for fund withdrawals.

**Request Parameters:**

```
start_time - Unix timestamp from which to display data (optional filter)
end_time - Unix timestamp until which to display data (optional filter)
```

**Response:**

```
items — available items
id — payout ID
time — Unix timestamp
date — date and time
method_id — payout method (can be found in get_info)
account — account to which the payout is requested
pay_amount — payout amount
pay_currency_code — currency code of the payout amount
original_amount — original payout amount
original_currency_code — currency code of the original payout amount
status — payout request status (0 - pending, 1 - completed, 2 - canceled, 3 - canceled by user)
```

---

### <mark style="color:blue;">add_payout</mark>

Creates a payout request.

**Request Parameters:**

```
method_id — payout method (can be found in get_info)
account — account number for the payout
```

**Response:**

```
payout_id - payout ID
```
