# Bot Settings

{% hint style="warning" %}
Exchanges in categories that require user registration or card/account verification can only be done through the website.

In the settings for these exchange categories, you must disable their access via the API (under the "**Restrictions and Checks**" tab, select "**Website Only**"). Otherwise, these categories will be available for exchange through the bot and will display an error.

![](<../../../ru/.gitbook/assets/image (556) (1).png>)\\
{% endhint %}

### Dialog Message and Additional Options Settings

{% hint style="info" %}
By default, the bot already has all the necessary dialog messages set up for communicating with users. If you want to replace them with your own personalized messages, please fill in the provided fields.

You can set the texts in all available languages. The corresponding text will be displayed to the user based on the selected language in the "**Type**" field when creating the bot.
{% endhint %}

*   **Text of the first message from the bot:**

    <figure><img src="../../.gitbook/assets/image (1157)_eng.png" alt=""><figcaption></figcaption></figure>
*   **API Error Message:**

    <figure><img src="../../../ru/.gitbook/assets/image (922) (1).png" alt=""><figcaption></figcaption></figure>
* **Menu Button Titles 1-6** - titles for selecting menu items (see below).

{% hint style="info" %}
Menus are used to create messages with static text (for example, sections like "**Working Hours**," "**Contact Information**," etc.)
{% endhint %}

*   **Menu Text 1-6:**

    <figure><img src="../../.gitbook/assets/image (1229)_eng.png" alt="" width="427"><figcaption></figcaption></figure>
*   **Text for the "Exchange" Button:**

    <figure><img src="../../.gitbook/assets/image (1206)_eng.png" alt=""><figcaption></figcaption></figure>
*   **Display a list of currencies for selection?** - whether to show a list of available currencies\
    • **No** - in this case, the user must manually enter the name of the currency for exchange\
    • **Yes**

    <figure><img src="../../../ru/.gitbook/assets/image (999) (1).png" alt="" width="396"><figcaption></figcaption></figure>

{% hint style="info" %}
Just like in the templates for application statuses, you can use \[shortcodes] in the bot's message templates to insert values from the exchange category, but only those values that are available above the input field.

<img src="../../.gitbook/assets/image (1165)_eng.png" alt="" data-size="original">
{% endhint %}

*   **Text when selecting the currency "I Give":**

    <figure><img src="../../.gitbook/assets/image (1230)_eng.png" alt=""><figcaption></figcaption></figure>
*   **Text when selecting the currency "I Receive":**

    <figure><img src="../../.gitbook/assets/image (1195)_eng.png" alt=""><figcaption></figcaption></figure>
*   **Text for selecting the exchange side:**

    <figure><img src="../../../ru/.gitbook/assets/image (824) (1).png" alt=""><figcaption></figcaption></figure>
*   **Text when selecting the currency "I Give":**

    <figure><img src="../../../ru/.gitbook/assets/image (988).png" alt=""><figcaption></figcaption></figure>
*   **Text when selecting the currency "I Receive":**

    <figure><img src="../../../ru/.gitbook/assets/image (829) (1).png" alt=""><figcaption></figcaption></figure>
* **Remember entered data?** - whether to remember the data entered by the client for quick creation of future requests\
  • **No**\
  • **Yes**
*   **Text for the button to delete user data:**

    <figure><img src="../../.gitbook/assets/image (1209)_eng.png" alt=""><figcaption></figcaption></figure>
*   **Text for successful data deletion:**

    <figure><img src="../../.gitbook/assets/image (1079)_eng.png" alt=""><figcaption></figcaption></figure>
*   **Text for application information:**

    <figure><img src="../../.gitbook/assets/image (1005)_eng.png" alt=""><figcaption></figcaption></figure>

{% hint style="info" %}
After successfully creating a request, buttons for taking actions will be available to the client:\
![](<../../.gitbook/assets/image (1154)_eng.png>)
{% endhint %}

* **QR Code** - display a QR code for quick payment in the request for crypto payments.\
  • **No**\
  • **Yes**

### "Words" Section

In this section, you can add words that users type in their dialogue with the bot, which will be automatically replaced with words from this section.

If there are many exchange categories in the exchange service and the display of currencies is turned off (selected "**No**" for the option "**Display a list of currencies for selection**") - when the client types, for example, "биток," the word can be replaced with "bitcoin," and the currency BTC will be selected.

{% hint style="info" %}
There is no need to enter words from a different keyboard layout (not "**bitcoin**," but "**ишесщшт**," for example) in the replacements - the bot will automatically recognize such input errors.
{% endhint %}

<figure><img src="../../../ru/.gitbook/assets/image (991) (1).png" alt="" width="473"><figcaption></figcaption></figure>
