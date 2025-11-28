# Creating a Bot

{% embed url="https://youtu.be/TWQolhXH_4U" %}

## Creating a Bot in Telegram

In Telegram, send a message **/newbot** to [@BotFather](https://t.me/BotFather) and follow the instructions to create your bot. Once the bot is successfully created, a token will be displayed—copy it to your clipboard, as you will need it for further setup. You do not need to change any other bot settings.

<figure><img src="../../.gitbook/assets/BotFather @ Premium Exchanger (38886)_230731152938 (1).png" alt="" width="563"><figcaption></figcaption></figure>

## Adding a New Bot in the Admin Panel

1. Activate the "**T-bots**" and "**API**" modules in the "**Modules**" section.

<figure><img src="../../.gitbook/assets/image (1213)_eng.png" alt="" width="563"><figcaption></figcaption></figure>

2. Go to the **T-API-bots -> Add** section and create a new bot by filling out all the options listed below:

* **Title** — the name of the bot for display in the "**T-API bots**" section for your convenience in identifying it.
* **Status** — the status of the bot:\
  • **Published** — the bot will be active for use\
  • **Unpublished** — the bot will be inactive for use
* **Logs** — log recording for the bot's operations (found in **T-API-bots** -> **Logs**)\
  • **No** — logs will not be recorded\
  • **Yes** — logs will be recorded
* **API Server** — the address of your website without specifying the **http(s)** protocol. For example: **obmen.com**

{% hint style="info" %}
Instructions on how to create an "**API login**" and "**API key**" can be found in [this](https://premium.gitbook.io/main/en/api-premium-exchanger/api) guide.
{% endhint %}

* **API Login** — the login from the API section
* **API Key** — the key from the API section

{% hint style="warning" %}
Please note that you **must** enable methods in the "**API**" ➔ "**Settings**" section,

<img src="../../.gitbook/assets/image%20(87)_eng.png" alt="" data-size="original">

in addition to the methods in the settings of the specific API key for the bot.

![](../../.gitbook/assets/image%20\(88\)_eng.png)\\
{% endhint %}

* **Version** — the version of the bot (currently only v1 is available)\
  • **v1**
* **Type** — the language the bot will use to communicate with users. If you want to create a bot in multiple languages, you will need to create several bots and select the appropriate language for each.\
  • **RU**\
  • **EN**
* **API Partner ID** — if an ID is specified, all requests will be considered partner requests, and the specified user will receive a percentage from all exchanges. You can find the user ID in the "**Users**" section.
* **Test Server** — a button to check the bot's connection to the exchange API. A successful test result will indicate a correct connection of the bot to the API.

{% code overflow="wrap" %}
```
Array ( [error] => 0 [error_text] => [data] => Array ( [ip] => 000.000.000.0000 [user_id] => 0 [locale] => ru_RU [partner_id] => 827 ) )
```
{% endcode %}

<figure><img src="../../.gitbook/assets/%D0%94%D0%BE%D0%B1%D0%B0%D0%B2%D0%B8%D1%82%D1%8C%20%E2%80%B9%20Premium%20Exchanger%20%E2%80%94%20WordPress%20-%20Google%20Chrome_230727183928_eng.png" alt="" width="563"><figcaption></figcaption></figure>

3. Click the "**Save**" button.
4. Then fill in the "**Token**" field with the token you copied earlier from the created Telegram bot via [@BotFather](https://t.me/BotFather).

<figure><img src="../../.gitbook/assets/%D0%94%D0%BE%D0%B1%D0%B0%D0%B2%D0%B8%D1%82%D1%8C%20%E2%80%B9%20Premium%20Exchanger%20%E2%80%94%20WordPress%20-%20Google%20Chrome_230727184111_eng.png" alt="" width="563"><figcaption></figcaption></figure>

5. Click the "**Save**" button again.
6. After filling in all the connection details, register the webhook by following the link on the settings page.

<figure><img src="../../.gitbook/assets/%D0%94%D0%BE%D0%B1%D0%B0%D0%B2%D0%B8%D1%82%D1%8C%20%E2%80%B9%20Premium%20Exchanger%20%E2%80%94%20WordPress%20-%20Google%20Chrome_230727184233_eng.png" alt="" width="563"><figcaption></figcaption></figure>

{% hint style="info" %}
If the bot is not functioning correctly or stops responding to commands, re-register the webhook—first delete the existing one and then register a new one.
{% endhint %}

7. Enter **@your\_bot\_username** in Telegram and click the "**Start**" button to begin the exchange.

{% hint style="warning" %}
You may need to reactivate the **Premium Exchanger** plugin in the "**Plugins**" section if the bot does not respond after starting.

<img src="../../.gitbook/assets/image (1249)_eng.png" alt="" data-size="original">
{% endhint %}

8. Optionally, perform additional [bot settings](nastroiki-bota.md).
9. If you are using CloudFlare or a similar service for your website, add the [IP addresses of Telegram](https://core.telegram.org/resources/cidr.txt) to the Whitelist in your service. Instructions for adding to the CloudFlare Whitelist can be found [here](broken-reference/).
