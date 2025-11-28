# Currency Exchange Rates from a File

The script allows you to obtain exchange rate values from a text file. You can create a file that will store the exchange rates, which will then be displayed on the website as the exchange rate for a specific direction. Please follow these steps:

1. In the website control panel, go to the "**Modules" → "Modules"** section and activate the "**Exchange Rate Parser from File**" module.
2. Create a TXT file and specify the exchange rates in it. List each exchange rate on a new line. Upload the TXT file to the server. Here’s an example of how the file should look:

| <p><code>USDRUB : 1 = 55.7</code></p><p><code>RUBUSD : 57.5 = 1</code></p><p><code>BTCUSD : 1 = 15777</code></p> |
| ---------------------------------------------------------------------------------------------------------------- |

3. In the website control panel, navigate to "**Modules"** → **"Exchange Rate from File**" and enter the URL of the uploaded TXT file.

<figure><img src="../../../.gitbook/assets/image (1168)_eng.png" alt="" width="563"><figcaption></figcaption></figure>

4. In the website control panel, go to the "**Exchange Directions**" section. In the settings for the exchange direction, under the "**Rate**" tab, select the corresponding line number from the file for the "**Exchange Rate from File**" parameter and save the changes.

<figure><img src="../../../.gitbook/assets/image (1064)_eng.png" alt="" width="563"><figcaption></figcaption></figure>

5. Set up a [cron job](https://premium.gitbook.io/main/en/basic-settings/faq/kak-sozdat-zadanie-cron-na-servere) that will retrieve the exchange rate from the file and update it on the website. The script can be run every minute. Here’s an example command for a cron job in Unix format for the ISP Manager control panel:

`/usr/bin/wget -t 1 -O - --no-check-certificate "https://premiumexchanger.com/cron-fcourse_request_cron.html"`

<figure><img src="../../../.gitbook/assets/image (1052)_eng.png" alt="" width="563"><figcaption></figcaption></figure>

{% hint style="info" %}
The command provided in the example may vary for each server. The changes pertain to this part of the command: **`/usr/bin/wget -t 1 -O - --no-check-certificate "your_URL"`**. You can confirm the correct command with your hosting provider's technical support.
{% endhint %}

Now, the exchange rate for the specified direction on the website will be continuously sourced from the TXT file.
