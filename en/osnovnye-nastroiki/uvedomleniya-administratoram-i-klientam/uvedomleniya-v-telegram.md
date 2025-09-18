# Telegram Notifications

Telegram notifications are essential for informing administrators and users about changes in application statuses or other requests without the need to keep the exchange page open.

{% hint style="warning" %}
You are currently viewing the guide for creating a Telegram bot to notify clients about their applications. If you need instructions for creating a bot for exchanges, please refer to the [guide](https://premium.gitbook.io/main/osnovnye-nastroiki/telegram-bot-dlya-obmena) in the other section.
{% endhint %}

{% hint style="warning" %}
For the notification bot to function correctly, the following is required:

* The user must have their Telegram username added to their account in your exchange.
* The user must activate your notification bot by sending the command `/start` and receiving a response from it.
{% endhint %}

## Settings

1. In Telegram, send a message **/newbot** to [@BotFather](https://t.me/BotFather) and follow the instructions to create a bot. After successfully creating the bot, a token will be displayed—copy it to your clipboard. No other bot settings need to be changed.
2. In the website control panel (under the "**Telegram**" -> "**Settings**" section), enter the token you received during the bot creation in the "**Token**" field.

<figure><img src="../../.gitbook/assets/image (966).png" alt=""><figcaption><p>Section "<strong>Telegram</strong>" -> "<strong>Settings</strong>"</p></figcaption></figure>

{% hint style="info" %}
If the Telegram section does not appear in the sidebar, enable the module in the "Modules" section:

![](<../../.gitbook/assets/image (863).png>)
{% endhint %}

3. If you need to log the bot's actions and view logs later in the "**Telegram**" -> "**Message Log**" section, activate the following options:

<figure><img src="../../.gitbook/assets/image (886).png" alt=""><figcaption><p>Section "<strong>Telegram</strong>" -> "<strong>Message Log</strong>"</p></figcaption></figure>

4. At the bottom of the "**Telegram**" -> "**Settings**" section, follow the link to register the webhook.

<figure><img src="../../.gitbook/assets/image (865).png" alt=""><figcaption><p>Section "<strong>Telegram</strong>" -> "<strong>Settings</strong>"</p></figcaption></figure>

5. If necessary, write the message texts for the bot users.

<figure><img src="../../.gitbook/assets/image (1234).png" alt=""><figcaption><p>Section "<strong>Telegram</strong>" -> "<strong>Settings</strong>"</p></figcaption></figure>

6. In the "**Users**" section, in your user's profile, specify your Telegram username without the @ symbol (if the username is absent, it must be set in the Telegram settings).

<figure><img src="../../.gitbook/assets/image (1164).png" alt=""><figcaption><p>Section "<strong>Settings</strong>" in Telegram</p></figcaption></figure>

<figure><img src="../../.gitbook/assets/image (1241).png" alt=""><figcaption><p>Section "<strong>Users</strong>" -> "<strong>Edit</strong>"</p></figcaption></figure>

7. Activate the bot by sending it the message **/start** in Telegram.
8. In the "**Messages**" → "**Telegram Templates**" section, configure the necessary templates for various application statuses and other options for sending messages on behalf of the bot to administrators and users:

{% hint style="warning" %}
Please note that the settings for administrators and users in the dropdown list are separate entities and are configured independently of each other.
{% endhint %}

<figure><img src="../../.gitbook/assets/image (1093).png" alt=""><figcaption><p>Section "<strong>Messages**" → "Telegram Templates</strong>"</p></figcaption></figure>

Template settings:

* **Send**: "Yes" — send messages, "No" — do not send.
* **Telegram username of the administrator (without @)** — the administrator's username to which notifications will be sent. You can specify multiple usernames separated by commas if you have several administrators.
* **Text** — the text of the message being sent. Above the text input field, you will find a panel with \[shortcodes]. Use them in the message text and subject line to display data from the applications in the sent messages.

9. To use the bot, you need to add an additional "Telegram" field[^1] to each exchange direction that will use the bot.

<figure><img src="../../.gitbook/assets/image (1242).png" alt=""><figcaption><p>Section "<strong>Exchange Directions</strong>" -> "<strong>Additional Fields</strong>"</p></figcaption></figure>

This is necessary so that the exchange page displays a field for users to input their username.

<figure><img src="../../.gitbook/assets/image (962).png" alt=""><figcaption><p>Exchange page</p></figcaption></figure>

10. To use the bot, the exchange user can specify their Telegram username in their profile settings (it will automatically populate the "Telegram" field if it is present when creating an application—this set of fields is determined by the administrator for each direction individually) or manually enter their username when creating each application.

<figure><img src="../../.gitbook/assets/image (1039).png" alt=""><figcaption><p>User's personal account in the exchange</p></figcaption></figure>

{% hint style="info" %}
By default, messages are not sent to administrators if the administrator changes the application status in the admin panel (in the "**Applications**" section) themselves. If you need messages to always be sent to the administrator, this option must be activated in the "**Exchange Settings**" -> "**General Settings**" -> "**Other Settings**" section, under "Send email to admin if admin changes application status."

<img src="../../.gitbook/assets/image (938).png" alt="" data-size="original">
{% endhint %}

{% hint style="warning" %}
For users to receive notifications in Telegram, each user **must** "start" the bot on their account.
{% endhint %}

## Troubleshooting

**Note for exchange administrators:**\
Clients often forget to start the Telegram bot, which is why they do not receive notifications. To avoid this, it is recommended to add instructions in the Telegram notification template (for example, “**New Application**”):\
<mark style="color:$warning;">“To receive notifications about your application, please first go to our Telegram bot and click</mark> <mark style="color:$warning;"></mark><mark style="color:$warning;">**\Start.**</mark><mark style="color:$warning;">”.</mark> Without activating the bot using this button, Telegram does not allow sending messages from the bot to the client.

If users or administrators are not receiving messages from the bot or have stopped receiving them, check the "**Telegram**" -> "**Message Log**" section, where you can view all logs related to the bot's operation. If necessary, you can use the filter that shows which messages pertain to the bot itself and which are for the bot's users.

<figure><img src="../../.gitbook/assets/image (1158).png" alt=""><figcaption><p>Section "<strong>Telegram</strong>" -> "<strong>Message Log</strong>"</p></figcaption></figure>

If there are issues with sending messages via the bot, you can delete and re-register the webhook (see point 4)—this may help restore the bot's functionality.

If you are using Cloudflare or a similar service for your website, add [Telegram IP addresses](https://core.telegram.org/resources/cidr.txt) to the whitelist in your service:

```
91.108.56.0/22
91.108.4.0/22
91.108.8.0/22
91.108.16.0/22
91.108.12.0/22
149.154.160.0/20
91.105.192.0/23
91.108.20.0/22
185.76.151.0/24
2001:b28:f23d::/48
2001:b28:f23f::/48
2001:67c:4e8::/48
2001:b28:f23c::/48
2a0a:f280::/32
```

An alternative option is to add a pool of IP addresses by ASN (autonomous system number)—the ASN for Telegram and their addition to the whitelist in the Cloudflare account are detailed in the [instructions](https://premium.gitbook.io/main/osnovnye-nastroiki/faq/dobavlenie-ip-adresov-v-whitelist-v-cloudflare).

[^1]: (the name can be changed in the exchange settings)