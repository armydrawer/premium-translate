# API v1

## Enabling the API

To use the API, you need to activate the API module in the "Modules" section.

<figure><img src="../.gitbook/assets/image (1210).png" alt=""><figcaption></figcaption></figure>

### API Settings

Once the module is activated, go to the "**API**" -> "**Settings**" section. Configure the desired settings:

<figure><img src="../.gitbook/assets/image (1082).png" alt=""><figcaption></figcaption></figure>

* **API:**  
  • **Disabled** — API access is closed.  
  • **All users** — API access will be available to all users of the exchange platform.  
  • **Selected users** — API access will only be available to users for whom the "**Work with REST API**" option is enabled in the user settings within the admin panel.

<figure><img src="../.gitbook/assets/image (1111).png" alt=""><figcaption></figcaption></figure>

* **Logs** — enable logging of API activity in the "**API**" -> "**Logs**" section.  
  • **No**  
  • **Yes**  
* **Methods available to users** — a set of methods that will be accessible to users when adding an API key in their personal account.

<figure><img src="../.gitbook/assets/image (1086).png" alt=""><figcaption></figcaption></figure>

### Obtaining API Keys via the User's Personal Account

Users can access the API through their personal account. By default, the link is `https://your_domain/user-api/`.

<figure><img src="../.gitbook/assets/image (1402).png" alt=""><figcaption></figcaption></figure>

After selecting the methods and specifying IP addresses, the user needs to click the "**Add API Key**" button. A "**Login** — **Key**" pair will then be displayed on the page.

<figure><img src="../.gitbook/assets/image (974).png" alt=""><figcaption></figcaption></figure>

It is possible to generate multiple keys for a single user, each with different sets of methods.

### Creating API Keys via the Admin Panel

{% hint style="warning" %}
We recommend creating API keys specifically for individual users, rather than under the "**System**" user.  
If you issue keys under "**System**," you are granting access as the admin of the exchange platform. It is better to create API keys on behalf of the specific user. Otherwise, the user will gain access to all requests created via the API (using the `get_exchanges` method, if enabled), not just those created from their account.
{% endhint %}

In the "**API**" -> "**Add**" section, add a new API user.

<figure><img src="../.gitbook/assets/image (1180).png" alt=""><figcaption></figcaption></figure>

* **User** — the ID of the exchange platform user or 0 (for the "**System**" user).  
* **Allowed IP addresses** — the IP addresses from which API access will be permitted.  
* **Available methods** — the set of methods the user can utilize.

After saving the data, a "**Login** — **Key**" pair will be generated.

<figure><img src="../.gitbook/assets/image (917).png" alt=""><figcaption></figcaption></figure>

---

## Using the API

Entry point: `https://your_domain/api/userapi/v1/ + API method`

For authorization, you need to include the following information in the headers of your API requests, which you obtained earlier in the "**API**" section:

- **API-LOGIN** — API login.  
- **API-KEY** — API key.  
- **API-LANG** — optional parameter to force the use of a specific language. Example: `ru_RU`, `en_US`.

{% hint style="warning" %}
All requests must be sent using the **POST** method. Responses are returned in JSON format. **GET requests are not used.** Parameters should be passed in the request body, not in the headers.

Example of a request with parameters sent via Postman and the corresponding response:  
![](<../.gitbook/assets/image (528).png>)
{% endhint %}

### API Methods:

#### <mark style="color:blue;">test</mark>

A test method to verify API functionality.

**Request parameters:**

```
---
```

**Response:**

```
ip — your IP address  
user_id — user ID (if the system is making the request, user ID = 0)  
locale — site language  
partner_id — partner ID  
```

---

#### <mark style="color:blue;">get_direction_currencies</mark>

Retrieve a list of currencies available for exchange.

**Request parameters:**

```
currency_id_give — ID of the "Give" currency (optional filter)  
currency_id_get — ID of the "Receive" currency (optional filter)  
```

**Response:**

```
Two lists are returned:  

give — list of "Give" currencies  
get — list of "Receive" currencies  

Each list contains the following data:  
id — currency ID in the exchange platform  
title — currency name in the exchange platform  
logo — link to the currency logo  
```

---

#### <mark style="color:blue;">get_directions</mark>

Retrieve a list of exchange directions available for trading.

**Request parameters:**

```
currency_id_give — ID of the "Give" currency (optional filter)  
currency_id_get — ID of the "Receive" currency (optional filter)  
```

**Response:**

```
A list of exchange directions is returned, with the following details:  

direction_id — exchange direction ID  
currency_give_id — "Give" currency ID  
currency_give_title — "Give" currency name  
currency_give_logo — "Give" currency logo  
currency_get_id — "Receive" currency ID  
currency_get_title — "Receive" currency name  
currency_get_logo — "Receive" currency logo  
```

---

#### <mark style="color:blue;">get_direction</mark>

Retrieve information about a specific exchange direction.

**Request parameters:**

```
direction_id — exchange direction ID  
```

**Response:**

```
id — exchange direction ID  
url — link to the exchange page  
currency_code_give — "Give" currency code  
currency_code_get — "Receive" currency code  
reserve — reserve amount  
course_give — "Give" currency rate  
course_get — "Receive" currency rate  
sum_give — amount in "Give" currency  
sum_give_com — amount in "Give" currency including commission  
sum_get — amount in "Receive" currency  
sum_get_com — amount in "Receive" currency including commission  
com_give — "Give" currency commission text  
com_get — "Receive" currency commission text  
min_give — minimum "Give" currency amount (or "no" if not set)  
max_give — maximum "Give" currency amount (or "no" if not set)  
min_get — minimum "Receive" currency amount (or "no" if not set)  
max_get — maximum "Receive" currency amount (or "no" if not set)  

info:  
    timeline_text — exchange description  
    frozen_text — frozen status text  
    before_button_text — text displayed before the "Pay" button  

give_fields — list of fields related to the "Give" currency  
get_fields — list of fields related to the "Receive" currency  
dir_fields — list of fields related to the exchange direction  

Field description:  
name — field name for submission  
type — field type  
label — field description  
req — 0 (optional), 1 (required)  
tooltip — tooltip text  
options — available options if the field is of type "select"  
cd — indicator of additional parameters  
```

---

#### <mark style="color:blue;">get_calc</mark>

Calculate amounts for a specific exchange direction.

**Request parameters:**

```
direction_id — exchange direction ID  
calc_amount — amount  
calc_action — type of amount:  
               1 — amount in "Give" currency  
               2 — amount in "Receive" currency  
               3 — amount in "Give" currency including commission  
               4 — amount in "Receive" currency including commission  
cd — fields from the exchange direction marked with cd = 1, encoded with URL encode  
```

**Response:**

```
currency_code_give — "Give" currency code  
currency_code_get — "Receive" currency code  
reserve — reserve amount of the "Receive" currency  
course_give — "Give" currency rate  
course_get — "Receive" currency rate  
sum_give — amount in "Give" currency  
sum_give_com — amount in "Give" currency including commission  
sum_get — amount in "Receive" currency  
sum_get_com — amount in "Receive" currency including commission  
com_give — "Give" currency commission text  
com_get — "Receive" currency commission text  
min_give — minimum "Give" currency amount (or "no" if not set)  
max_give — maximum "Give" currency amount (or "no" if not set)  
min_get — minimum "Receive" currency amount (or "no" if not set)  
max_get — maximum "Receive" currency amount (or "no" if not set)  
changed — flag indicating if the input amount needs to be adjusted: 0 (no), 1 (yes)  
```

---

#### <mark style="color:blue;">get_exchanges</mark>

Retrieve requests created with the given API key.

**Request parameters:**

```
start_time — Unix timestamp for the start of the request period (optional filter)  
end_time — Unix timestamp for the end of the request period (optional filter)  
ip — IP address (optional filter)  
id — request ID (optional filter)  
api_id — ID passed in the API (optional filter)  
status_history — include status history: 0 (no), 1 (yes) (optional filter)  
limit — number of requests to retrieve (optional filter)  
offset — number of requests to skip (optional filter)  
```

**Response:**

```
items — list of requests  

    id — request ID  
    api_id — ID passed in the API  
    time — status change time  
    date — status change date  
    psys_give — payment system of the "Give" currency  
    psys_get — payment system of the "Receive" currency  
    currency_code_give — "Give" currency code  
    currency_code_get — "Receive" currency code  
    course_give — "Give" currency rate  
    course_get — "Receive" currency rate  
    amount_give — amount in "Give" currency  
    amount_get — amount in "Receive" currency  
    exchange_success — 0 (request completed), 1 (request not completed)  
    user_hash — user hash  
    user_ip — user IP address  
    status — request status  
    statuses — list of status changes  
        time — status change time  
        date — status change date  
        status — request status  
```

---

#### <mark style="color:blue;">create_bid</mark>

Create a new request.

**Request parameters:**  
... (details not provided in the original text)

Here’s the provided text translated into naturalistic English:

---

### **Parameters for Exchange Requests**

- **direction_id** — Exchange direction ID  
- **partner_id** — Partner ID (optional parameter)  
- **api_id** — Request ID in your system (optional parameter)  
- **calc_amount** — Exchange amount  
- **calc_action** — Amount type:  
  - `1` — Amount in the "Give" currency  
  - `2` — Amount in the "Receive" currency  
  - `3` — Amount in the "Give" currency including commission  
  - `4` — Amount in the "Receive" currency including commission  
- **callback_url** — Specify the URL where the API will send a response when the request status changes. The response is sent via POST and includes:  
  - **bid_id** — Request ID  
  - **account1** — From account  
  - **cfgive8** — Cardholder's name  
  - **account2** — To account  
  - **cf1-99** — Custom fields  

#### **Examples of custom fields**:  
- **cf1** — First name  
- **cf2** — Middle name  
- **cf3** — Last name  
- **cf4** — Phone number  
- **cf5** — Skype  
- **cf6** — Email  
- **cf8** — Passport number  
- **cf10** — Region  
- **cf11** — Telegram  

---

### **Response for Exchange Requests**

- **url** — Link to the exchange page  
- **id** — Request ID  
- **hash** — Request hash  
- **status** — Request status  
- **status_title** — Status description  
- **psys_give** — Payment system for the "Give" currency  
- **psys_get** — Payment system for the "Receive" currency  
- **currency_code_give** — Code of the "Give" currency  
- **currency_code_get** — Code of the "Receive" currency  
- **amount_give** — Amount in the "Give" currency  
- **amount_get** — Amount in the "Receive" currency  

#### **API Actions**  
- **type** — Payment type  
- **cancel** — Request cancellation method:  
  - `api` — Via API  
  - `disabled` — Cancellation disabled  
  - Link for cancellation  
- **pay** — Payment method:  
  - `api` — Via API  
  - `disabled` — Payment disabled  
  - Link for payment  
- **instruction** — Payment instructions  
- **pay_amount** — Amount to be paid  

---

### **cancel_bid**

Cancel a request (this method works **only if** the `create_bid` response includes `api_actions` -> `cancel` = `api`).

#### **Request Parameters**  
- **hash** — Request hash  

#### **Response**  
- Request status  

---

### **pay_bid**

Mark a request as paid (this method works **only if** the `create_bid` response includes `"api_actions"` -> `"pay": "api"` and the exchange direction **does not use** a merchant).

If a merchant is used in the request, the status will automatically change to "**Paid**" when the merchant confirms receipt of funds.

#### **Request Parameters**  
- **hash** — Request hash  

#### **Response**  
- Request status  

---

### **success_bid**

Mark a request as completed.

#### **Request Parameters**  
- **hash** — Request hash  

#### **Response**  
- Request status  

---

### **bid_info**

Retrieve payment information for a request.  

> **Note:** You can only request information for requests created via the API.

#### **Request Parameters**  
- **id** — Request ID (optional if `hash` is provided)  
- **hash** — Request hash (optional if `id` is provided)  

#### **Response**  
- **url** — Link to the exchange page  
- **id** — Request ID  
- **hash** — Request hash  
- **status** — Status  
- **status_title** — Status description  
- **psys_give** — Payment system for the "Give" currency  
- **psys_get** — Payment system for the "Receive" currency  
- **currency_code_give** — Code of the "Give" currency  
- **currency_code_get** — Code of the "Receive" currency  
- **amount_give** — Amount in the "Give" currency  
- **amount_get** — Amount in the "Receive" currency  
- **api_actions** — Options:  
  - **type** — Payment type  
  - **cancel** — Cancellation method:  
    - `api` — Via API  
    - `disabled` — Cancellation disabled  
  - **pay** — Payment method:  
    - `api` — Via API  
    - `disabled` — Payment disabled  
  - **instruction** — Payment instructions  
  - **pay_amount** — Amount to be paid  

---

### **get_partner_info**

Retrieve partner information.

#### **Request Parameters**  
- None  

#### **Response**  
- **partner_id** — Partner ID  
- **balance** — Balance  
- **min_payout** — Minimum payout amount  
- **items** — List of currencies available for payout:  
  - **id** — Currency ID  
  - **title** — Currency name  
  - **commission** — Commission  
  - **amount** — Balance in this currency  

---

### **get_partner_links**

Retrieve information about partner referrals.

#### **Request Parameters**  
- **start_time** — Unix timestamp (optional filter)  
- **end_time** — Unix timestamp (optional filter)  
- **ip** — IP address (optional filter)  
- **limit** — Number of results to return (optional filter)  

#### **Response**  
- **items** — List of partner referrals:  
  - **time** — Time of referral  
  - **date** — Date of referral  
  - **browser** — Browser used  
  - **ip** — User's IP address  
  - **referrer** — Referring page  
  - **user_hash** — User hash  
  - **query_string** — Query string  

---

### **get_partner_exchanges**

Retrieve information about partner exchanges.

#### **Request Parameters**  
- **start_time** — Unix timestamp (optional filter)  
- **end_time** — Unix timestamp (optional filter)  
- **ip** — IP address (optional filter)  
- **id** — Request ID (optional filter)  
- **status_history** — Include status history: `0` (no), `1` (yes) (optional filter)  
- **limit** — Number of results to return (optional filter)  

#### **Response**  
- **items** — List of requests:  
  - **id** — Request ID  
  - **time** — Status change time  
  - **date** — Status change date  
  - **psys_give** — Payment system for the "Give" currency  
  - **psys_get** — Payment system for the "Receive" currency  
  - **currency_code_give** — Code of the "Give" currency  
  - **currency_code_get** — Code of the "Receive" currency  
  - **course_give** — Exchange rate for the "Give" currency  
  - **course_get** — Exchange rate for the "Receive" currency  
  - **amount_give** — Amount in the "Give" currency  
  - **amount_get** — Amount in the "Receive" currency  
  - **exchange_success** — `0` (completed), `1` (not completed)  
  - **accrued** — `0` (reward not credited), `1` (reward credited)  
  - **partner_reward** — Partner reward amount  
  - **user_hash** — User hash  
  - **user_ip** — User's IP address  
  - **status** — Request status  
  - **statuses** — List of status changes:  
    - **time** — Time of status change  
    - **date** — Date of status change  
    - **status** — Request status  

---

### **get_partner_payouts**

Retrieve a list of user payout requests.

#### **Request Parameters**  
- **start_time** — Unix timestamp (optional filter)  
- **end_time** — Unix timestamp (optional filter)  
- **limit** — Number of results to return (optional filter)  
- **id** — Request ID (optional filter)  

#### **Response**  
- **items** — List of payouts:  
  - **id** — Request ID  
  - **time** — Payout time  
  - **date** — Payout date  
  - **method_id** — Payout currency  
  - **account** — Payout account  
  - **pay_amount** — Payout amount  
  - **pay_currency_code** — Payout currency code  
  - **original_amount** — Original payout amount  
  - **original_currency_code** — Original payout currency code  
  - **status** — Request status: `0` (pending), `1` (paid), `2` (canceled)  

---

### **add_partner_payout**

Create a payout request.

#### **Request Parameters**  
- **method_id** — Payout currency ID  
- **account** — Payout account number  

#### **Response**  
- **payout_id** — Payout ID  

---

### **API Error Responses**

#### **Api disabled**  
Possible reasons:  
- Incorrect authorization details in the "**API**" section.  
- API access not enabled in the user settings.  

#### **Empty response**  
- No data found — check the provided parameters.  

#### **No bid exists**  
- The requested request does not exist.  

#### **Method not supported**  
- The selected method is not activated in the "**API**" section.  

#### **Direction not found**  
- Access to the exchange direction is not enabled via API. Update the settings in the exchange direction's "**Restrictions and Checks**" tab.  

---

[^1]: Field numbering may vary; the provided example is illustrative.