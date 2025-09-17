# Exchange Rates from a File

The script includes functionality to retrieve exchange rate values from a text file. You can create a file to store exchange rate values, which will then be displayed on the website as the exchange rate for a specific direction. To set this up, follow these steps:

---

### 1. Activate the Exchange Rate Parser Module
In the website's admin panel, go to **"Modules" → "Modules"** and activate the module called **"Exchange Rate Parser from File"**.

---

### 2. Create a TXT File with Exchange Rates
Create a TXT file and specify the exchange rates in it. Each exchange rate should be written on a new line. Upload this TXT file to the server. Below is an example of how the file should look:

```
USDRUB : 1 = 55.7
RUBUSD : 57.5 = 1
BTCUSD : 1 = 15777
```

---

### 3. Specify the File URL in the Admin Panel
In the admin panel, navigate to **"Modules" → "Exchange Rate from File"** and enter the URL of the uploaded TXT file.

---

### 4. Configure Exchange Directions
In the admin panel, go to **"Exchange Directions"**. In the settings for a specific exchange direction, open the **"Rate"** tab. For the parameter **"Exchange Rate from File"**, select the corresponding line number from the TXT file and save the changes.

---

### 5. Set Up a Cron Job
Set up a [cron job](https://premium.gitbook.io/main/osnovnye-nastroiki/faq/kak-sozdat-zadanie-cron-na-servere) to regularly fetch the exchange rate value from the file and update it on the website. The script can be scheduled to run every minute. Below is an example of a cron job command in Unix format for the ISP Manager control panel:

```
/usr/bin/wget -t 1 -O - --no-check-certificate "https://premiumexchanger.com/cron-fcourse_request_cron.html"
```

---

### Important Note:
The exact command may vary depending on your server. Specifically, the part of the command **`/usr/bin/wget -t 1 -O - --no-check-certificate "your_URL"`** might differ. Contact your hosting provider's technical support to confirm the correct command for your server.

---

Once everything is set up, the exchange rate for the specified direction on the website will always be retrieved from the TXT file.