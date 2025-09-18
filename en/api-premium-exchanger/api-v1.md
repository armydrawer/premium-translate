# API v1

## Activating the API

To use the API, you need to enable the API module in the "Modules" section.

<figure><img src="../.gitbook/assets/image (1210).png" alt=""><figcaption></figcaption></figure>

### API Settings

After activating the module, go to the "**API**" -> "**Settings**" section. Set your desired configurations:

<figure><img src="../.gitbook/assets/image (1082).png" alt=""><figcaption></figcaption></figure>

* **API:**\
  • **Disabled** — API access is restricted\
  • **All users** — API access will be available to all users of the exchange\
  • **Selected users** — API access will only be granted to users who have the "**Work with REST API**" option enabled in their user settings in the admin panel.

<figure><img src="../.gitbook/assets/image (1111).png" alt=""><figcaption></figcaption></figure>

* **Logs** — Log entries for API usage can be found in the "**API**" -> "**Logs**" section\
  • **No**\
  • **Yes**
* **Methods available to users** — A set of methods that will be accessible to the user when adding a key in their personal account on the exchange.

<figure><img src="../.gitbook/assets/image (1086).png" alt=""><figcaption></figcaption></figure>

### Obtaining API Keys through the User's Personal Account

Users can access the API through their personal account, typically at the link `https://your_domain/user-api/`.

<figure><img src="../.gitbook/assets/image (1402).png" alt=""><figcaption></figcaption></figure>

After selecting the methods and specifying the IP addresses, click the "**Add API Key**" button. The page will then display the generated pair of "**Login** — **Key**".

<figure><img src="../.gitbook/assets/image (974).png" alt=""><figcaption></figcaption></figure>

You can generate multiple keys for a single user with different sets of methods.

### Creating API Keys through the Admin Panel

{% hint style="warning" %}
We recommend creating API keys specifically for individual users, rather than using the "**System**" user.\
When you issue access under "**System**," you are granting access as the admin of the exchange — it's better to create API keys for the intended user. Otherwise, the user may gain access to all requests made via the API through the `get_exchanges` method (if enabled), rather than just those made from their own account.
{% endhint %}

On the "**API**" -> "**Add**" page, add a new API user.

<figure><img src="../.gitbook/assets/image (1180).png" alt=""><figcaption></figcaption></figure>

* **User** — User ID from the exchange or 0 (for the "**System**" user)
* **Allowed IP addresses** — IP addresses from which API access will be permitted
* **Available methods** — A set of methods that the user can utilize

After saving the data, a pair of "**Login** — **Key**" will be generated.

<figure><img src="../.gitbook/assets/image (917).png" alt=""><figcaption></figcaption></figure>

***

## Using the API

Endpoint: `https://your_domain/api/userapi/v1/ + API method`

For authorization, you need to send the following information in the headers of your API requests, which you obtained earlier in the "**API**" section:

**API-LOGIN** — API login

**API-KEY** — API key

**API-LANG** — forced use of the specified language (optional). Example: ru_RU, en_US.

{% hint style="warning" %}
All requests are sent using the **POST** method, and responses are returned in JSON format **(GET requests are not used)**. Parameters are passed in the body of the request (not in the header).

Example of a request with parameter transmission from Postman and the response to the request:\
![](<../.gitbook/assets/image (528).png>)
{% endhint %}

### API Methods:

### <mark style="color:blue;">test</mark>

A test method to check the API functionality.

Request parameters:

```
---
```

Response:

```
ip — your IP address
user_id — User ID (if accessed by the system, ID = 0)
locale — website language
partner_id — Partner ID
```

### <mark style="color:blue;">get_direction_currencies</mark>

Retrieve a list of currencies available for exchange.

Request parameters:

```
currency_id_give — ID of the currency "I give" (filter, optional parameter)
currency_id_get — ID of the currency "I receive" (filter, optional parameter)
```

Response:

```
The response contains 2 lists:

give — list of currencies "I give"
get — list of currencies "I receive"

Each list contains the following data:

id — Currency ID in the exchange
title — Currency name in the exchange
logo — Link to the currency logo
```

### <mark style="color:blue;">get_directions</mark>

Retrieve a list of exchange directions available for exchange.

Request parameters:

```
currency_id_give — ID of the currency "I give" (filter, optional parameter)
currency_id_get — ID of the currency "I receive" (filter, optional parameter)
```

Response:

```
The response contains a list of exchange directions, including:

direction_id — ID of the exchange direction in the exchange
currency_give_id — ID of the currency "I give" in the exchange
currency_give_title — Currency name "I give" in the exchange
currency_give_logo — Logo of the currency "I give" in the exchange
currency_get_id — ID of the currency "I receive" in the exchange
currency_get_title — Currency name "I receive" in the exchange
currency_get_logo — Logo of the currency "I receive" in the exchange
```

### <mark style="color:blue;">get_direction</mark>

Retrieve information about a specific exchange direction.

Request parameters:

```
direction_id — ID of the exchange direction
```

Response:

```
id — ID of the exchange direction in the exchange
url — Link to the exchange page
currency_code_give — Code of the currency "I give"
currency_code_get — Code of the currency "I receive"
reserve — Reserve
course_give — Exchange rate of the currency "I give"
course_get — Exchange rate of the currency "I receive"
sum_give — Amount in the currency "I give"
sum_give_com — Amount in the currency "I give" including commission
sum_get — Amount in the currency "I receive"
sum_get_com — Amount in the currency "I receive" including commission
com_give — Commission text for the currency "I give"
com_get — Commission text for the currency "I receive"
min_give — Minimum amount for the currency "I give", no - not set
max_give — Maximum amount for the currency "I give", no - not set
min_get — Minimum amount for the currency "I receive", no - not set
max_get — Maximum amount for the currency "I receive", no - not set

info
    timeline_text — Description of the exchange
    frozen_text — Text for frozen status
    before_button_text — Text before the "Pay" button
    
give_fields — List of fields related to the currency "I give"
get_fields — List of fields related to the currency "I receive"
dir_fields — List of fields for the exchange direction

Field description:
name — Name for transmission
type — Field type
label — Field description
req — 0 - optional, 1 - required
tooltip — Tooltip text
options — Possible options if the field is of type select
cd — Pointer for additional parameters
```

### <mark style="color:blue;">get_calc</mark>

Calculator for amounts in the exchange direction.

Request parameters:

{% code overflow="wrap" %}
```
direction_id — ID of the exchange direction
calc_amount — Amount
calc_action — Amount type: 1 — amount in the currency "I give",
                                    2 — amount in the currency "I receive",
                                    3 — amount in the currency "I give" including commission,
                                    4 — amount in the currency "I receive" including commission
cd — Fields from the exchange direction, marked with cd = 1, in one field. The field is processed with URL encoding.
```
{% endcode %}

Response:

```
currency_code_give — Code of the currency "I give"
currency_code_get — Code of the currency "I receive"
reserve — Reserve of the currency "I receive"
course_give — Exchange rate of the currency "I give"
course_get — Exchange rate of the currency "I receive"
sum_give — Amount in the currency "I give"
sum_give_com — Amount in the currency "I give" including commission
sum_get — Amount in the currency "I receive"
sum_get_com — Amount in the currency "I receive" including commission
com_give — Commission text for the currency "I give"
com_get — Commission text for the currency "I receive"
min_give — Minimum amount for the currency "I give", no - not set
max_give — Maximum amount for the currency "I give", no - not set
min_get — Minimum amount for the currency "I receive", no - not set
max_get — Maximum amount for the currency "I receive", no - not set
changed — Flag indicating whether the input amount needs to be changed: 0 - no change needed, 1 - change needed
```

### <mark style="color:blue;">get_exchanges</mark>

Retrieve requests created with this key.

Request parameters:

{% code overflow="wrap" %}
```
start_time — Unix time from which to retrieve requests (filter, optional parameter)
end_time — Unix time until which to retrieve requests (filter, optional parameter)
ip — IP address (filter, optional parameter)
id — Request ID (filter, optional parameter)
api_id — ID passed in the API (filter, optional parameter)
status_history — Whether to display status history: 0 - no, 1 - yes (filter, optional parameter)
limit — Number of requests to display (filter, optional parameter)
offset — Number of requests to skip (filter, optional parameter)
```
{% endcode %}

Response:

```
items - List of requests

    id — Request ID
    api_id — ID passed in the API
    time — Status change time
    date — Status change date
    psys_give — Payment system for the currency "I give"
    psys_get — Payment system for the currency "I receive"
    currency_code_give — Code of the currency "I give"
    currency_code_get — Code of the currency "I receive"
    course_give — Exchange rate of the currency "I give"
    course_get — Exchange rate of the currency "I receive"
    amount_give — Amount in the currency "I give"
    amount_get — Amount in the currency "I receive"
    exchange_success — 0 - request completed, 1 - request not completed
    user_hash — User hash
    user_ip — User IP address
    status — Request status
    statuses — List of status changes
	time — Status change time
	date — Status change date
	status — Request status
```

### <mark style="color:blue;">create_bid</mark>

Create a request.

Request parameters:

Here’s a naturalistic English translation of the provided text:

---

**Parameters for Exchange Request:**

- **direction_id** — ID of the exchange direction
- **partner_id** — ID of the partner (optional parameter)
- **api_id** — ID of the request in your system (optional parameter)
- **calc_amount** — amount of the exchange
- **calc_action** — classification of the amount:
  - 1 — amount in the "Giving" currency
  - 2 — amount in the "Receiving" currency
  - 3 — amount in the "Giving" currency with a fee
  - 4 — amount in the "Receiving" currency with a fee
- **callback_url** — specify the URL to which the API will send a response when the status of the request changes. The response will be sent via POST method:

  - **bid_id** — ID of the request
  - **account1** — from account
  - **cfgive8** — name of the cardholder
  - **account2** — to account
  - **cf1-99** — custom fields
    - **Examples of fields**:
      - **cf1** — First Name
      - **cf2** — Middle Name
      - **cf3** — Last Name
      - **cf4** — Phone
      - **cf5** — Skype
      - **cf6** — E-mail
      - **cf8** — Passport Number
      - **cf10** — Region
      - **cf11** — Telegram

---

**Response:**

- **url** — link to the exchange page
- **id** — ID of the request
- **hash** — hash of the request
- **status** — status of the request
- **status_title** — title of the request status
- **psys_give** — payment system for the "Giving" currency
- **psys_get** — payment system for the "Receiving" currency
- **currency_code_give** — currency code for "Giving"
- **currency_code_get** — currency code for "Receiving"
- **amount_give** — amount in the "Giving" currency
- **amount_get** — amount in the "Receiving" currency

**api_actions** — options
- **type** — type of payment
- **cancel** — method for canceling the request
  - **api** — via API
  - **disabled** — disabled
  - **link to cancel**
  
- **pay** — method of payment
  - **api** — via API
  - **disabled** — disabled
  - **link to pay**
  
- **instruction** — payment instructions
- **pay_amount** — amount to be paid

---

### **cancel_bid**

Cancel a request (this method only works if, when creating the request (`create_bid`), the response `api_actions` -> `cancel` = '**api**')

**Request Parameters:**

```
hash — hash of the request
```

**Response:**

```
status of the request
```

---

### **pay_bid**

Mark the request as paid (this method works **only if** when creating the request via `create_bid`, the response contains `"api_actions"`-> `"pay": "api"` (when a merchant is **not used** in the exchange direction)).

![Image](../.gitbook/assets/image (213).png)

If a merchant was used in the request, the request will change its status to "**Paid**" **only automatically** (when the merchant sees the funds received for the request).

**Request Parameters:**

```
hash — hash of the request
```

**Response:**

```
status of the request
```

---

### **success_bid**

Mark the request as completed.

**Request Parameters:**

```
hash — hash of the request
```

**Response:**

![Image](../.gitbook/assets/image (2120).png)

```
status of the request
```

---

### **bid_info**

Payment information about the request.

> **Warning:** You can only request information about the request using this method if the request was created via the API.

**Request Parameters:**

```
id — ID of the request (optional if hash is provided)
hash — hash of the request (optional if ID is provided)
```

**Response:**

```
url — link to the exchange page
id — ID of the request
hash — hash of the request
status — status
status_title — title of the status
psys_give — payment system for the "Giving" currency
psys_get — payment system for the "Receiving" currency
currency_code_give — currency code for "Giving"
currency_code_get — currency code for "Receiving"
amount_give — amount in the "Giving" currency
amount_get — amount in the "Receiving" currency
api_actions — options
    type — type of payment
    cancel — method for canceling the request
        api — via API
        disabled — cancellation link disabled
    pay - method of payment
        api — via API
        disabled — disabled
        link to pay
    instruction — payment instructions
    pay_amount — amount to be paid
```

---

### **get_partner_info**

Information about the partner.

**Request Parameters:**

```
---
```

**Response:**

```
partner_id - ID of the partner
balance - balance
min_payout - minimum payout amount
items - list of currencies available for payout requests
    id - currency ID
    title - currency name
    commission - commission
    amount - balance in this currency
```

---

### **get_partner_links**

Information about partner referrals.

**Request Parameters:**

```
start_time - Unix time from which to display (filter, optional parameter)
end_time - Unix time until which to display (filter, optional parameter)
ip - IP address (filter, optional parameter)
limit - number of entries to display (filter, optional parameter)
```

**Response:**

```
items - list of partner referrals
    time - time of referral
    date - date of referral
    browser - browser used
    ip - IP address of the referring user
    referrer - page from which the referral was made
    user_hash - user hash
    query_string - query string
```

---

### **get_partner_exchanges**

Information about partner exchanges.

**Request Parameters:**

```
start_time - Unix time from which to display requests (filter, optional parameter)
end_time - Unix time until which to display requests (filter, optional parameter)
ip - IP address (filter, optional parameter)
id - ID of the request (filter, optional parameter)
status_history - display status history: 0 - no, 1 - yes (filter, optional parameter)
limit - number of requests to display (filter, optional parameter)
```

**Response:**

```
items - list of requests
    id - ID of the request
    time - time of status change
    date - date of status change
    psys_give - payment system for the "Giving" currency
    psys_get - payment system for the "Receiving" currency
    currency_code_give - currency code for "Giving"
    currency_code_get - currency code for "Receiving"
    course_give - exchange rate for "Giving"
    course_get - exchange rate for "Receiving"
    amount_give - amount in the "Giving" currency
    amount_get - amount in the "Receiving" currency
    exchange_success - 0 - request completed, 1 - request not completed
    accrued - 0 - reward not accrued, 1 - reward accrued
    partner_reward - partner amount
    user_hash - user hash
    user_ip - IP address of the user
    status - status of the request
    statuses - list of status changes
        time - time of status change
        date - date of status change
        status - status of the request
```

---

### **get_partner_payouts**

List of user requests for fund withdrawals.

**Request Parameters:**

```
start_time - Unix time from which to display (filter, optional parameter)
end_time - Unix time until which to display (filter, optional parameter)
limit - number of entries to display (filter, optional parameter)
id - ID of the request (filter, optional parameter)
```

**Response:**

```
items - list
    id - ID of the request
    time - time of payout
    date - date of payout
    method_id - currency of payout
    account - payout account
    pay_amount - payout amount
    pay_currency_code - currency code of payout
    original_amount - original payout amount
    original_currency_code - original currency code of payout
    status - status of the request. 0 - pending, 1 - paid, 2 - canceled
```

---

### **add_partner_payout**

Create a payout request.

**Request Parameters:**

```
method_id - ID of the payout currency
account - account number for the payout
```

**Response:**

```
payout_id - ID of the payout
```

---

## API Error Responses

### **Api disabled**

![Image](../.gitbook/assets/image (1469).png)

Possible reasons for the error and how to resolve them:

- Incorrect authorization details provided in the "**API**" section for the user working with the API.

  ![Image](../.gitbook/assets/image (1472).png)
- API access not enabled in the user settings in the "**Users**" section.

![Image](../.gitbook/assets/image (1466).png)

### Empty Response

![Image](../.gitbook/assets/image (1467).png)

- Requested information is not available — check the parameters being sent.

### No bid exists

![Image](../.gitbook/assets/image (1468).png)

- The requested bid does not exist.

### Method not supported

![Image](../.gitbook/assets/image (1471).png)

- The selected method is not activated in the "**API**" section for the user.

![Image](../.gitbook/assets/image (1473).png)

### Direction not found

![Image](../.gitbook/assets/image (1474).png)

Access to the exchange direction via the API is not allowed (when requesting the exchange direction); access must be enabled in the settings of the exchange direction, under the "**Restrictions and Checks**" tab.

![Image](../.gitbook/assets/image (1470).png)

[^1]: The numbering of fields may vary; the example is provided.

--- 

This translation aims to maintain clarity and readability while accurately conveying the original content's meaning.