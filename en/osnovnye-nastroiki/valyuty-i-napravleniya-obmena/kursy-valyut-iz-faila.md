# Exchange Rates from a File

The script allows you to fetch exchange rate values from a file. You can create a text file where you upload the exchange rates, and these rates will be displayed on the website as the exchange rate for a given currency pair. To set this up, follow these steps:

1. In the website control panel, go to **Modules → Modules** and activate the module called **Exchange Rate Parser from File**.

2. Create a TXT file and enter the exchange rates in it. Write each exchange rate on a new line. Upload the TXT file to your server. Here is an example of the file format:

```
USDRUB : 1 = 55.7
RUBUSD : 57.5 = 1
BTCUSD : 1 = 15777
```

3. In the website control panel, navigate to **Modules → Exchange Rate from File** and specify the URL of the uploaded TXT file.

4. In the control panel, go to **Exchange Directions**, open the settings for the desired exchange direction, and on the **Rate** tab, select the appropriate line number from the file for the **Exchange Rate from File** parameter. Save your changes.

5. Set up a scheduled task (cron job) that will fetch the exchange rate from the file and update it on the website. The script can be run every minute. Here is an example of a cron command for a Unix-based system using ISP Manager:

```
/usr/bin/wget -t 1 -O - http(s)://your_domain/request-fcourse.html
```

> **Note:** The exact command may vary depending on your server. The difference usually lies in the `/usr/bin/wget -t 1 -O -` part. Please check with your hosting provider’s technical support to get the correct command for your environment.

After completing these steps, the exchange rate for the selected direction on your website will always be taken from the TXT file.