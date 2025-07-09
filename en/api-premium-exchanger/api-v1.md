# API v1

## Activating the API

To work with the API, you need to activate the API module in the "Modules" section.

![API Module Activation](../.gitbook/assets/image (1210).png)

### API Settings

After activating the module, go to the "**API**" -> "**Settings**" section. Set the desired settings:

![API Settings](../.gitbook/assets/image (1082).png)

* **API:**\
  • **Disabled** — API access is closed\
  • **All Users** — API access will be available to all exchange users\
  • **Selected Users** — API access will only be available to users for whom the "**Work with REST API**" option is enabled in the user settings in the admin panel

![API Settings Continued](../.gitbook/assets/image (1111).png)

* **Logs** — log recording when working with the API in the "**API**" -> "**Logs**" section\
  • **No**\
  • **Yes**
* **Methods Available to Users** — set of methods that will be available to the user when adding a key in the exchange user's account

![API Methods](../.gitbook/assets/image (1086).png)

### Obtaining API Keys through the User Account

Users can access the API through their user account, by default the link is `https://your_domain/user-api/`

![User API Access](../.gitbook/assets/image (1402).png)

After selecting methods and specifying IP addresses, click the "**Add API Key**" button. This will display the generated pair of "**Login** — **Key**" on the page.

![Generated API Key](../.gitbook/assets/image (974).png)

Multiple keys can be issued for one user with different sets of methods.

### Creating API Keys through the Admin Panel

{% hint style="warning" %}
We recommend creating API keys specifically for individual users, not under the user "**System**".\
By using the "**System**" user, you are granting access on behalf of yourself as the exchange admin — it is better to create API keys specifically for the required user. Otherwise, the user will have access to all requests made through the API using the `get_exchanges` method, not just those created from their own account.
{% endhint %}

On the "**API**" -> "**Add**" page, add a new API user.

![Add API User](../.gitbook/assets/image (1180).png)

* **User** - ID of the exchange user or 0 (user "**System**")
* **Allowed IP addresses** - IP addresses from which access to the API will be allowed
* **Available methods** - a set of methods that the user can use

After saving the data, a pair "**Login** - **Key**" will be generated

## Using the API

Entry point: `https://your_domain/api/userapi/v1/ + API method`

To authorize, you need to send the information obtained earlier in the "**API**" section in the headers of the API requests:

**API-LOGIN** - API login

**API-KEY** - API key

**API-LANG** - forced use of the specified language (optional). Example: ru_RU, en_US.

{% hint style="warning" %}
All requests are sent using the **POST** method, the response is returned in json format **(GET requests are not used)**, parameters are passed in the request body (not in the header).

Example of a request with passing a parameter from Postman and the response to the request:\
![](<../.gitbook/assets/image (528).png>)
{% endhint %}

### API Methods:

### <mark style="color:blue;">test</mark>

Test method to check the API functionality.

Request parameters:

```
---
```

Response:

```
ip - your IP address
user_id - user ID (if the system is making the request, ID = 0)
locale - website language
partner_id - partner ID
```

### <mark style="color:blue;">get_direction_currencies</mark>

Get a list of currencies available for exchange.

Request parameters:

```
currency_id_give - ID of the "Give" currency (filter, optional parameter)
currency_id_get - ID of the "Get" currency (filter, optional parameter)
```

Response:

```
There are 2 lists in the response:

give - list of "Give" currencies
get - list of "Get" currencies

Each list contains the following data:

id - currency ID in the exchange
title - currency name in the exchange
logo - currency logo link
```

### <mark style="color:blue;">get_directions</mark>

Get a list of exchange directions available for exchange.

Request parameters:

```
currency_id_give - ID of the "Give" currency (filter, optional parameter)
currency_id_get - ID of the "Get" currency (filter, optional parameter)
```

Response:

```
The response contains a list of exchange directions, in it:



```
direction_id — ID направления обмена
sum_give — сумма в валюте "Отдаю"
sum_get — сумма в валюте "Получаю"
```

Ответ:

```
sum_give_com — сумма в валюте "Отдаю" с комиссией
sum_get_com — сумма "Получаю" с комиссией
```

### Explanation:

The text provided seems to be a technical documentation or specification related to a currency exchange system. It includes information about parameters and responses for certain API requests.

The first part of the text describes the parameters and their meanings for the `get_exchanges` API request. It includes details such as start time, end time, IP address, request ID, API ID, status history, limit, and offset.

The second part of the text outlines the response structure for the `get_exchanges` request, indicating that the response will include a list of items representing exchange requests.

If you need further assistance or clarification, feel free to ask!

Cancel Bid

Request Parameters:

- bid_id: ID of the bid to be canceled

Response:

- status: status of the bid after cancellation
- message: message indicating the result of the cancellation操作
- error: error message if the cancellation was unsuccessful

Cancellation of bid (the method works only if when creating a bid (`create_bid`) the response in `api_actions` -> `cancel`= '**api**')

Request parameters:

```
hash — bid hash
```

Response:

```
bid status
```

### <mark style="color:blue;">pay\_bid</mark>

Marking the bid as paid (the method works **only if** when creating a bid using the `create_bid` method, the response will be `"api_actions"`-> `"pay": "api"` (when **merchant is not used** in the exchange direction)).

If a merchant was used in the bid, the bid status will change to "**Paid**" **automatically** (when the merchant sees the funds received for the bid).

Request parameters:

```
hash — bid hash
```

Response:

```
bid status
```

### <mark style="color:blue;">success\_bid</mark>

Marking the bid as completed.

Request parameters:

```
hash — bid hash
```

Response:

```
bid status
```

### <mark style="color:blue;">bid\_info</mark>

Payment information about the bid

{% hint style="warning" %}
Requesting information about a bid using this method is only possible if the bid itself was created via API.
{% endhint %}

Request parameters:

```
id — bid ID (optional, if hash is provided)
hash — bid hash (optional, if ID is provided)
```

Response:

```
url — exchange page link
id — bid ID
hash — bid hash
status — status
status_title — status title
psys_give — "Sending" payment system
psys_get — "Receiving" payment system
currency_code_give — "Sending" currency code
currency_code_get — "Receiving" currency code
amount_give — amount in "Sending" currency
amount_get — amount in "Receiving" currency
api_actions — options
	type — payment type
	cancel — bid cancellation method
			api — via API
			disabled — cancellation link disabled
	pay - payment method
			api — via API
			disabled — disabled
			payment link
	
		instruction — payment instructions
		pay_amount — amount to be paid
```

### <mark style="color:blue;">get\_partner\_info</mark>

Partner information

Request parameters:

```
---
```

Response:

```
partner_id - partner ID
balance - balance
min_payout - min. payout amount
items - list of currencies for payout order
    id - currency ID
    title - currency name
    comission - commission
    amount - balance in this currency
```

### <mark style="color:blue;">get\_partner\_links</mark>

Information about partner links

Request parameters:

```
start_time - the unix time from which to display requests (filter, optional parameter)
end_time - the unix time until which to display requests (filter, optional parameter)
ip - IP address (filter, optional parameter)
id - request ID (filter, optional parameter)
status_history - whether to display status history: 0 - no, 1 - yes (filter, optional parameter)
limit - the number of requests to display (filter, optional parameter)
```


```
start_time - Unix time to start displaying (filter, optional parameter)
end_time - Unix time to end displaying (filter, optional parameter)
limit - number of items to display (filter, optional parameter)
id - Request ID (filter, optional parameter)
```

Response:

```
items - list
    id - Request ID
    time - payout time
    date - payout date
    method_id - payout currency
    account - payout account
    pay_amount - payout amount
    pay_currency_code - payout currency code
    original_amount - original payout amount
    original_currency_code - original payout currency code
    status - request status. 0 - pending, 1 - paid, 2 - canceled
```

### <mark style="color:blue;">add_partner_payout</mark>

Creating a payout request

Request parameters:

```
method_id - payout currency ID
account - account number for payout
```

Response:

```
payout_id - payout ID
```

## API Error Responses

### **Api disabled**

Possible reasons for the error and methods to resolve them:

* Incorrect authorization data from the "**API**" section for the user working with the API

* API access is not enabled in the user settings in the "**Users**" section

### Empty response

* Requested information is missing - check the parameters being passed

### No bid exists

* Requested bid does not exist

### Method not supported

* Selected method is not activated in the "**API**" section for the user

### Direction not found

Access to the exchange direction through the API is not allowed (when requesting exchange direction), you need to enable access in the exchange direction settings, under the "**Restrictions and Checks**" tab