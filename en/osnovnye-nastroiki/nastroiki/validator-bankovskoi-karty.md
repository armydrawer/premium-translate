# Bank Card Validator

The "**Bank Card Information (cardinfo)**" module allows you to determine which bank a client's specified bank card belongs to. This option can be used in transactions involving bank cards to:

• **prevent** the creation of requests with cards from specific banks\
• **allow** the creation of requests only with cards from specific banks

To activate this option, go to the "**Modules**" section and enable the "**Bank Card Information**" module.

<figure><img src="../../.gitbook/assets/image (325)_eng.png" alt=""><figcaption></figcaption></figure>

## Module Settings

After activating the module, navigate to "**Modules**" -> "**Determine Card Type**" and configure the module.

<figure><img src="../../.gitbook/assets/image (1861)_eng.png" alt="" width="563"><figcaption></figcaption></figure>

**Remember previously checked cards:**\
• **Yes** — previously entered card numbers will not be checked again\
• **No** — data for checked cards will not be saved by the module

**If the API does not provide data:**\
• **Nothing** — the request will be created without validation\
• **Error** — the request will not be created, and an error message stating "**account number did not pass validation ()**" will appear below the card number input field in the exchange form.

<figure><img src="../../.gitbook/assets/image (1862)_eng.png" alt="" width="305"><figcaption></figcaption></figure>

**Source for determining card type** — select one of the sources to check the bank card numbers entered by clients:

**Only checks affiliation with the payment system (Visa, MasterCard, Mir), no API key needed:**\
• based on the first digits of the card number\
**Checks affiliation with a specific bank (a separate API key is required for each service):**\
• [bincodes.com](https://www.bincodes.com/users/register/)\
• [binlist.net](https://binlist.net/)\
• [rapidapi.com](https://rapidapi.com/auth/sign-up)

**API key for services** — enter the API key from the selected service in the "**Source for determining card type**" field.

**Timeout (sec.)** — the time the site waits for a response from the external service. If a response is not received within the specified time, the site will continue to operate without an answer. If no time is set or it is set to 0, the standard timeout of 20 seconds will apply. There is no universal timeout value, as it depends on the speed of the specific service.

**Check selected currencies** — select the currencies for which the option will be activated.

## Option in Currency Settings:

<figure><img src="../../.gitbook/assets/image (1860)_eng.png" alt="" width="502"><figcaption></figcaption></figure>

On the "**Field Settings**" tab, in the "**Bank Names**" fields for the currency where the option is enabled, specify the names of the banks for which bank card validation will be conducted.

{% hint style="info" %}
If you want to allow requests with specific banks — list the names of those banks (one name per line). **With this setting, only cards from the specified banks will be allowed for request creation.**

If you want to prohibit requests with cards from specific banks — list the name of that bank with a "**-**"

(example: **-tinkoff bank**)

**With this setting, all cards will be allowed for request creation except for those from the specified banks.**
{% endhint %}

<details>

<summary>Names of some banks for validation (if the source rapidapi.com is selected)</summary>

**RUB:**

tinkoff bank\
sberbank of russia\
joint stock company alfa-bank\
ao raiffeisenbank\
vtb bank (public joint-stock company)\
public joint stock company promsvyazbank\
yoomoney, nbco llc

**UAH:**

jsc universal bank\
jsc cb privatbank

**KZT:**

kaspi bank jsc\
first heartland jusan bank joint stock company\
bank freedom finance kazakhstan joint stock company

</details>

{% hint style="success" %}
The module also supports working with other bank names — if your client reports that their card did not pass validation in the exchange form, ask them for a screenshot of the error message and specify the bank name (as indicated in parentheses) in the currency settings for validation with that bank's cards.
{% endhint %}

{% hint style="danger" %}
Please note that bank names may vary for each service — we recommend using universal bank names according to the service [**Bincheck.io**](https://bincheck.io/ru/bin-list) ([banks in Russia](https://bincheck.io/ru/ru), [banks in Ukraine](https://bincheck.io/ru/ua), [banks in Kazakhstan](https://bincheck.io/ru/kz)).
{% endhint %}

<figure><img src="../../.gitbook/assets/image (327)_eng.png" alt="" width="530"><figcaption></figcaption></figure>