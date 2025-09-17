# API v1

## Enabling the API

To use the API, you need to activate the API module in the "Modules" section.

<figure><img src="../.gitbook/assets/image (1210).png" alt=""><figcaption></figcaption></figure>

### API Settings

Once the module is activated, navigate to the "**API**" -> "**Settings**" section. Configure the desired settings:

<figure><img src="../.gitbook/assets/image (1082).png" alt=""><figcaption></figcaption></figure>

* **API:**  
  • **Disabled** — API access is closed.  
  • **All users** — API access will be available to all users of the exchange.  
  • **Selected users** — API access will only be available to users for whom the "**Work with REST API**" option is enabled in the user settings in the admin panel.

<figure><img src="../.gitbook/assets/image (1111).png" alt=""><figcaption></figcaption></figure>

* **Logs** — Enable logging of API activity in the "**API**" -> "**Logs**" section.  
  • **No**  
  • **Yes**  
* **Methods available to users** — A set of methods that will be available to users when they add a key in their personal exchange account.

<figure><img src="../.gitbook/assets/image (1086).png" alt=""><figcaption></figcaption></figure>

### Obtaining API Keys via the User Account

Users can access the API through their personal account. By default, the link is `https://your_domain/user-api/`.

<figure><img src="../.gitbook/assets/image (1402).png" alt=""><figcaption></figcaption></figure>

After selecting the methods and specifying IP addresses, the user must click the "**Add API Key**" button. A "**Login** — **Key**" pair will then be displayed on the page.

<figure><img src="../.gitbook/assets/image (974).png" alt=""><figcaption></figcaption></figure>

Multiple keys with different sets of methods can be generated for a single user.

### Creating API Keys via the Admin Panel

{% hint style="warning" %}
We recommend creating API keys specifically for individual users, not under the "**System**" user.  
If you issue keys under "**System**," you are granting access as the admin of the exchange. It is better to create API keys for the intended user. Otherwise, users accessing the `get_exchanges` method (if enabled) will see all requests created via the API, not just those associated with their account.
{% endhint %}

In the "**API**" -> "**Add**" section, add a new API user.

<figure><img src="../.gitbook/assets/image (1180).png" alt=""><figcaption></figcaption></figure>

* **User** — The ID of the exchange user or 0 (for the "**System**" user).  
* **Allowed IP addresses** — The IP addresses from which API access will be permitted.  
* **Available methods** — The set of methods the user can access.

After saving the data, a "**Login** — **Key**" pair will be generated.

<figure><img src="../.gitbook/assets/image (917).png" alt=""><figcaption></figcaption></figure>

---

## Using the API

Entry point: `https://your_domain/api/userapi/v1/ + API method`

For authorization, include the following information in the headers of your API requests, which you obtained earlier in the "**API**" section:

- **API-LOGIN** — API login  
- **API-KEY** — API key  
- **API-LANG** — Force the use of a specific language (optional). Example: `ru_RU`, `en_US`.

{% hint style="warning" %}
All requests must be sent using the **POST** method. Responses are returned in JSON format. **GET requests are not used.** Parameters should be passed in the request body, not in the headers.

Example of a request with parameters sent via Postman and the corresponding response:  
![](<../.gitbook/assets/image (528).png>)
{% endhint %}

### API Methods:

#### <mark style="color:blue;">test</mark>

A test method to verify API functionality.

**Request Parameters:**

```
---
```

**Response:**

```
ip — Your IP address  
user_id — User ID (if the system is making the request, ID = 0)  
locale — Site language  
partner_id — Partner ID  
```

---

#### <mark style="color:blue;">get_direction_currencies</mark>

Retrieve a list of currencies available for exchange.

**Request Parameters:**

```
currency_id_give — ID of the "Give" currency (filter, optional)  
currency_id_get — ID of the "Receive" currency (filter, optional)  
```

**Response:**

```
Two lists are returned:

give — List of "Give" currencies  
get — List of "Receive" currencies  

Each list contains the following data:  
id — Currency ID in the exchange  
title — Currency name in the exchange  
logo — Link to the currency logo  
```

---

#### <mark style="color:blue;">get_directions</mark>

Retrieve a list of exchange directions available for trading.

**Request Parameters:**

```
currency_id_give — ID of the "Give" currency (filter, optional)  
currency_id_get — ID of the "Receive" currency (filter, optional)  
```

**Response:**

```
A list of exchange directions is returned, containing:

direction_id — Exchange direction ID  
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

**Request Parameters:**

```
direction_id — Exchange direction ID  
```

**Response:**

```
id — Exchange direction ID  
url — Link to the exchange page  
currency_code_give — "Give" currency code  
currency_code_get — "Receive" currency code  
reserve — Reserve amount  
course_give — "Give" currency rate  
course_get — "Receive" currency rate  
sum_give — Amount in "Give" currency  
sum_give_com — Amount in "Give" currency including commission  
sum_get — Amount in "Receive" currency  
sum_get_com — Amount in "Receive" currency including commission  
com_give — Commission text for "Give" currency  
com_get — Commission text for "Receive" currency  
min_give — Minimum "Give" amount (no = not set)  
max_give — Maximum "Give" amount (no = not set)  
min_get — Minimum "Receive" amount (no = not set)  
max_get — Maximum "Receive" amount (no = not set)  

info  
    timeline_text — Exchange description  
    frozen_text — Frozen status text  
    before_button_text — Text displayed before the "Pay" button  

give_fields — List of fields related to the "Give" currency  
get_fields — List of fields related to the "Receive" currency  
dir_fields — List of fields related to the exchange direction  

Field description:  
name — Field name for submission  
type — Field type  
label — Field description  
req — 0 = optional, 1 = required  
tooltip — Tooltip text  
options — Possible options if the field is of type "select"  
cd — Indicator of additional parameters  
```

---

#### <mark style="color:blue;">get_calc</mark>

Calculate amounts for a specific exchange direction.

**Request Parameters:**

```
direction_id — Exchange direction ID  
calc_amount — Amount  
calc_action — Amount type:  
               1 — Amount in "Give" currency  
               2 — Amount in "Receive" currency  
               3 — Amount in "Give" currency including commission  
               4 — Amount in "Receive" currency including commission  
cd — Fields from the exchange direction marked with cd = 1, encoded with URL encode.  
```

**Response:**

```
currency_code_give — "Give" currency code  
currency_code_get — "Receive" currency code  
reserve — Reserve amount for "Receive" currency  
course_give — "Give" currency rate  
course_get — "Receive" currency rate  
sum_give — Amount in "Give" currency  
sum_give_com — Amount in "Give" currency including commission  
sum_get — Amount in "Receive" currency  
sum_get_com — Amount in "Receive" currency including commission  
com_give — Commission text for "Give" currency  
com_get — Commission text for "Receive" currency  
min_give — Minimum "Give" amount (no = not set)  
max_give — Maximum "Give" amount (no = not set)  
min_get — Minimum "Receive" amount (no = not set)  
max_get — Maximum "Receive" amount (no = not set)  
changed — Flag indicating if the input amount needs to be adjusted: 0 = no, 1 = yes  
```

---

#### <mark style="color:blue;">get_exchanges</mark>

Retrieve requests created with the given key.

**Request Parameters:**

```
start_time — Unix timestamp for the start of the request period (filter, optional)  
end_time — Unix timestamp for the end of the request period (filter, optional)  
ip — IP address (filter, optional)  
id — Request ID (filter, optional)  
api_id — ID passed in the API (filter, optional)  
status_history — Include status history: 0 = no, 1 = yes (filter, optional)  
limit — Number of requests to retrieve (filter, optional)  
offset — Number of requests to skip (filter, optional)  
```

**Response:**

```
items — List of requests  

    id — Request ID  
    api_id — ID passed in the API  
    time — Status change time  
    date — Status change date  
    psys_give — Payment system for "Give" currency  
    psys_get — Payment system for "Receive" currency  
    currency_code_give — "Give" currency code  
    currency_code_get — "Receive" currency code  
    course_give — "Give" currency rate  
    course_get — "Receive" currency rate  
    amount_give — Amount in "Give" currency  
    amount_get — Amount in "Receive" currency  
    exchange_success — 0 = request completed, 1 = request not completed  
    user_hash — User hash  
    user_ip — User IP address  
    status — Request status  
    statuses — List of status changes  
        time — Status change time  
        date — Status change date  
        status — Request status  
```

---

#### <mark style="color:blue;">create_bid</mark>

Create a new request.

**Request Parameters:**  
(Details not provided in the original text)

Here’s the provided text translated into naturalistic English:

---

### **Exchange Direction API Documentation**

#### **Parameters for Exchange Request**

- **direction_id** — ID of the exchange direction.
- **partner_id** — Partner ID (optional parameter).
- **api_id** — Application ID in your system (optional parameter).
- **calc_amount** — Exchange amount.
- **calc_action** — Specifies the type of amount:
  - **1** — Amount in the "Give" currency.
  - **2** — Amount in the "Receive" currency.
  - **3** — Amount in the "Give" currency including commission.
  - **4** — Amount in the "Receive" currency including commission.
- **callback_url** — Specify the URL where the API will send a response when the application status changes. The response is sent via the POST method and includes:
  - **bid_id** — Application ID.
  - **account1** — From account.
  - **cfgive8** — Cardholder's name.
  - **account2** — To account.
  - **cf1-99** — Custom fields.

**Examples of custom fields:**
- **cf1** — First Name.
- **cf2** — Middle Name.
- **cf3** — Last Name.
- **cf4** — Phone Number.
- **cf5** — Skype.
- **cf6** — Email.
- **cf8** — Passport Number.
- **cf10** — Region.
- **cf11** — Telegram.

---

#### **Response**

- **url** — Link to the exchange page.
- **id** — Application ID.
- **hash** — Application hash.
- **status** — Application status.
- **status_title** — Status description.
- **psys_give** — Payment system for the "Give" currency.
- **psys_get** — Payment system for the "Receive" currency.
- **currency_code_give** — Code of the "Give" currency.
- **currency_code_get** — Code of the "Receive" currency.
- **amount_give** — Amount in the "Give" currency.
- **amount_get** — Amount in the "Receive" currency.

---

#### **API Actions**

- **type** — Payment type.
- **cancel** — Method for canceling the application:
  - **api** — Via API.
  - **disabled** — Cancellation is disabled.
  - Link for cancellation.
- **pay** — Payment method:
  - **api** — Via API.
  - **disabled** — Payment is disabled.
  - Link for payment.
- **instruction** — Payment instructions.
- **pay_amount** — Amount to be paid.

---

### **cancel_bid**

Cancel an application. This method works **only if** the `create_bid` response includes `api_actions` -> `cancel` = '**api**'.

**Request Parameters:**
- **hash** — Application hash.

**Response:**
- Application status.

---

### **pay_bid**

Mark an application as paid. This method works **only if** the `create_bid` response includes `"api_actions"` -> `"pay": "api"` (when no merchant is used in the exchange direction).

If a merchant was used in the application, the application status will automatically change to "**Paid**" when the merchant confirms receipt of funds.

**Request Parameters:**
- **hash** — Application hash.

**Response:**
- Application status.

---

### **success_bid**

Mark an application as completed.

**Request Parameters:**
- **hash** — Application hash.

**Response:**
- Application status.

---

### **bid_info**

Retrieve payment information for an application.

**Note:** You can only request information for applications created via the API.

**Request Parameters:**
- **id** — Application ID (optional if `hash` is provided).
- **hash** — Application hash (optional if `id` is provided).

**Response:**
- **url** — Link to the exchange page.
- **id** — Application ID.
- **hash** — Application hash.
- **status** — Status.
- **status_title** — Status description.
- **psys_give** — Payment system for the "Give" currency.
- **psys_get** — Payment system for the "Receive" currency.
- **currency_code_give** — Code of the "Give" currency.
- **currency_code_get** — Code of the "Receive" currency.
- **amount_give** — Amount in the "Give" currency.
- **amount_get** — Amount in the "Receive" currency.
- **api_actions** — Options:
  - **type** — Payment type.
  - **cancel** — Method for canceling the application:
    - **api** — Via API.
    - **disabled** — Cancellation link is disabled.
  - **pay** — Payment method:
    - **api** — Via API.
    - **disabled** — Payment is disabled.
    - Link for payment.
  - **instruction** — Payment instructions.
  - **pay_amount** — Amount to be paid.

---

### **get_partner_info**

Retrieve information about the partner.

**Request Parameters:**
- None.

**Response:**
- **partner_id** — Partner ID.
- **balance** — Balance.
- **min_payout** — Minimum payout amount.
- **items** — List of currencies available for payout:
  - **id** — Currency ID.
  - **title** — Currency name.
  - **commission** — Commission.
  - **amount** — Balance in this currency.

---

### **get_partner_links**

Retrieve information about partner referrals.

**Request Parameters:**
- **start_time** — Unix timestamp for the start of the period (optional).
- **end_time** — Unix timestamp for the end of the period (optional).
- **ip** — IP address (optional).
- **limit** — Number of results to return (optional).

**Response:**
- **items** — List of partner referrals:
  - **time** — Time of referral.
  - **date** — Date of referral.
  - **browser** — Browser used.
  - **ip** — IP address of the user.
  - **referrer** — Referring page.
  - **user_hash** — User hash.
  - **query_string** — Query string.

---

### **get_partner_exchanges**

Retrieve information about partner exchanges.

**Request Parameters:**
- **start_time** — Unix timestamp for the start of the period (optional).
- **end_time** — Unix timestamp for the end of the period (optional).
- **ip** — IP address (optional).
- **id** — Application ID (optional).
- **status_history** — Include status history (0 = no, 1 = yes) (optional).
- **limit** — Number of results to return (optional).

**Response:**
- **items** — List of applications:
  - **id** — Application ID.
  - **time** — Time of status change.
  - **date** — Date of status change.
  - **psys_give** — Payment system for the "Give" currency.
  - **psys_get** — Payment system for the "Receive" currency.
  - **currency_code_give** — Code of the "Give" currency.
  - **currency_code_get** — Code of the "Receive" currency.
  - **course_give** — Exchange rate for the "Give" currency.
  - **course_get** — Exchange rate for the "Receive" currency.
  - **amount_give** — Amount in the "Give" currency.
  - **amount_get** — Amount in the "Receive" currency.
  - **exchange_success** — 0 = Not completed, 1 = Completed.
  - **accrued** — 0 = No reward, 1 = Reward accrued.
  - **partner_reward** — Partner reward amount.
  - **user_hash** — User hash.
  - **user_ip** — User IP address.
  - **status** — Application status.
  - **statuses** — List of status changes:
    - **time** — Time of status change.
    - **date** — Date of status change.
    - **status** — Application status.

---

### **get_partner_payouts**

Retrieve a list of user payout requests.

**Request Parameters:**
- **start_time** — Unix timestamp for the start of the period (optional).
- **end_time** — Unix timestamp for the end of the period (optional).
- **limit** — Number of results to return (optional).
- **id** — Application ID (optional).

**Response:**
- **items** — List of payout requests:
  - **id** — Application ID.
  - **time** — Payout time.
  - **date** — Payout date.
  - **method_id** — Payout currency.
  - **account** — Payout account.
  - **pay_amount** — Payout amount.
  - **pay_currency_code** — Payout currency code.
  - **original_amount** — Original payout amount.
  - **original_currency_code** — Original payout currency code.
  - **status** — Application status (0 = Pending, 1 = Paid, 2 = Canceled).

---

### **add_partner_payout**

Create a payout request.

**Request Parameters:**
- **method_id** — Payout currency ID.
- **account** — Payout account number.

**Response:**
- **payout_id** — Payout ID.

---

### **API Error Responses**

1. **Api disabled**  
   Possible reasons:
   - Incorrect authorization details in the **API** section.
   - API access is not enabled in the user settings.

2. **Empty response**  
   - No data found for the provided parameters.

3. **No bid exists**  
   - The requested application does not exist.

4. **Method not supported**  
   - The selected method is not activated in the **API** section.

5. **Direction not found**  
   - Access to the exchange direction is not enabled in the settings.

[^1]: Field numbering may vary; the provided list is an example.

--- 

Let me know if you need further clarification!