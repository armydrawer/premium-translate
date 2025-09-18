# Card Type Identification

{% embed url="https://www.youtube.com/watch?v=UnIjF_islXw" %}

1. To enable card type identification, navigate to the "**Modules" -> "Modules"** section and ensure that the "**Card Information**" module is active. If it is not active, please activate it.

<figure><img src="../../.gitbook/assets/Screenshot_1 (1).png" alt=""><figcaption></figcaption></figure>

2. Go to the "**Modules" -> "Card Type Identification"** section and make the following settings:

<figure><img src="../../.gitbook/assets/Screenshot_2 (1).png" alt=""><figcaption></figcaption></figure>

* **Remember already verified cards:**\
  • **Yes** - do not re-identify the card if its type has already been determined once.
* **Source for card type identification:**\
  • **By the first digits of the card number** - a verification method that uses existing information within the system about the corresponding digits for various payment systems, such as Visa, Mastercard, American Express, etc.\
  • **Bincodes.com and Binlist.net** - services that automate this process by identifying not only the type of payment system but also the bank that issued the card. These services are paid and require you to enter an API key in the field labeled "**API key for services**," which can be obtained from the chosen service's website.
* **Timeout** - when using an automated service, specify the time the system will wait for a response from the API. The recommended time is 15-30 seconds. If no response is received within this period, the check will be skipped.
* **Currencies** - the currencies for which the verification will be conducted.

3. Navigate to the "**Applications" -> "Applications"** section.

<figure><img src="../../.gitbook/assets/Screenshot_3.png" alt=""><figcaption></figcaption></figure>

When an application involving a card is created, information about the card will be displayed in the application information block. In the case of an internal check, the card type (Visa, Mastercard, etc.) will be shown, and if using the automated service, the name of the bank will also be provided.