# What Requirements Do Monitoring Services Have for Exchange Services?

If you own an exchange service listed on Bestchange or another monitoring platform, you may receive emails from them outlining compliance requirements for maintaining your listing.

We’ve compiled answers to some common questions:

<details>

<summary>"When creating or updating an order, send an email to the user at the address they provided. The email should include all key exchange details and the payment information of both parties."</summary>

You can configure sending payment details in the Email Template section ("**Messages**") by adding the shortcode **\[to_account]** in the desired line (or use the shortcode button "**Merchant Account**"). Set up email notifications by following this [guide](https://premium.gitbook.io/rukovodstvo-polzovatelya/osnovnye-nastroiki/uvedomleniya/opovesheniya-po-e-mail).

<mark style="background-color:red;">**For version 2.5:**</mark>  
Choose when to request merchant details under "**Exchange Settings**" → "**General Settings**". Select the option "**When creating an order**".

![](<../../.gitbook/assets/image (1124).png>)

<mark style="background-color:red;">**For version 2.4:**</mark>  
The user will receive two emails — one confirming the order creation and another with payment details (both email templates must be configured).

![](<../../.gitbook/assets/image (1305).png>) ![](<../../.gitbook/assets/image (1306).png>)

</details>

<details>

<summary>"Please disable the rates file when the exchange service is offline."</summary>

Create a mode in the "**Maintenance Mode**" section and configure the XML file display settings within that mode.

![](<../../.gitbook/assets/image (961).png>)

</details>

<details>

<summary>Enabling REST API for Monitoring Services</summary>

## Previous API Version

Activate the "**Affiliate Program API**" module in the "**Modules**" section.

<img src="../../.gitbook/assets/image (1069).png" alt="" data-size="original">

Enable the "**Use REST API (ppapi)**" option in your user profile settings.  
![](<../../.gitbook/assets/image (1243).png>)

## Current API Version

### [API Documentation](https://premium.gitbook.io/main/api-premium-exchanger/api-v1)

Activate the "**API**" module in the "**Modules**" section.

![](<../../.gitbook/assets/image (602).png>)

In the "**API - Settings**" section, configure the options as shown below.

![](<../../.gitbook/assets/image (603).png>)

</details>

Enable the "**Work with REST API**" option in the user profile settings for the user who will be issued the keys.

![](<../../.gitbook/assets/image (601).png>)

After that, the user will be able to [generate API keys themselves](https://premium.gitbook.io/main/api-premium-exchanger/api-v1#poluchenie-api-klyuchei-cherez-lichnyi-kabinet-polzovatelya) to access the exchanger’s API.

</details>

<details>

<summary>"Please add our IP address, from which we scan your exchange rates, to the whitelist of your anti-DDoS system (CloudFlare/Incapsula/StormWall)"</summary>

Here is an example for Cloudflare.

Go to "**Security** ➔ **WAF**" in your Cloudflare dashboard, then open the "**Tools**" tab and add the required IP addresses, selecting the **Allow** action.

![](<../../.gitbook/assets/image (2126).png>)

Save the settings.

![](<../../.gitbook/assets/image (2127).png>)

</details>

<details>

<summary>How to change the protocol for a Telegram account link on your website</summary>

You can only change the protocol by editing the code, replacing **https://t.me/** with **tg://resolve?domain=** in the file `wp-content/themes/your_theme_name/header.php`.

Before the change:  
![](<../../.gitbook/assets/изображение (84).png>)

After the change:  
![](<../../.gitbook/assets/изображение (21).png>)

</details>

<details>

<summary>How to add a city to a cash exchange direction</summary>

### XML File

Add cities in the "**Cities**" section and enable them for the exchange direction.

![](<../../.gitbook/assets/image (867).png>)

In the "**Tags for param parameter**" field, specify parameters according to [Bestchange requirements](https://www.bestchange.ru/wiki/rates.html).

![](<../../.gitbook/assets/image (1114).png>)

After that, the information will appear in your XML file.

![](<../../.gitbook/assets/image (1066).png>)

### Email Notification

In "**Exchange Directions**" → the cash exchange direction, under the "**Exchange Direction Template**" tab, enter the template text using the "**City**" shortcode.

![](<../../.gitbook/assets/image (905).png>)

Then, in "**Messages**" → "**E-mail Templates**", add the "**Exchange Direction Template**" shortcode to the "New Request" status.

![](<../../.gitbook/assets/image (1054).png>)

The text from the "**Exchange Direction Template**" field will be displayed in the email.

</details>

<details>

<summary>Export XML file with exchange rates for Bestchange is unavailable</summary>

If the file is unavailable, add BestChange’s IP address in your Cloudflare control panel.

### Old version of Cloudflare dashboard

1. Find the "**Bot Fight Mode**" option under "**Security**" ➔ "**Bots**" and enable it.

<figure><img src="../../.gitbook/assets/image (61).png" alt=""><figcaption></figcaption></figure>



2. In the "**Security**" ➔ "**WAF**" ➔ "**Tools**" section, create a rule with the IP address <mark style="color:red;">**`162.19.29.225`**</mark> and select the action "**Allow**". Save the rule.

<figure><img src="../../.gitbook/assets/image (62).png" alt=""><figcaption></figcaption></figure>

3. The added rule will appear as shown below:

<figure><img src="../../.gitbook/assets/image (63).png" alt=""><figcaption></figcaption></figure>

### New version of the Cloudflare dashboard

1. Go to "**Security**" ➔ "**Settings**" ➔ "**Bot traffic**".

<figure><img src="../../.gitbook/assets/image (68).png" alt=""><figcaption></figcaption></figure>

2. Enable the "**Bot fight mode**" option.

<figure><img src="../../.gitbook/assets/image (69).png" alt=""><figcaption></figcaption></figure>

3. Add a new rule (IP access rules) under "**Security**" ➔ "**Security rules**".

<figure><img src="../../.gitbook/assets/image (65).png" alt=""><figcaption></figcaption></figure>

4. Enter the IP address <mark style="color:red;">**`162.19.29.225`**</mark> in the new rule and select the action "**Allow**". Save the rule.

<figure><img src="../../.gitbook/assets/image (66).png" alt=""><figcaption></figcaption></figure>

5. The added rule will be displayed as follows:

<figure><img src="../../.gitbook/assets/image (67).png" alt=""><figcaption></figcaption></figure>

After completing these steps, access to the XML file will be allowed.

</details>

<details>

<summary>Admin panel activity alerts for admin login and daily verification that these alerts are working (to detect unauthorized admin access)</summary>

You need to have the template enabled and configured in "**Messages**" → "**E-mail templates**" → "**Notify on user login to dashboard**".

![](<../../.gitbook/assets/image (2108).png>)

Then, in the admin panel under "**Users**" (select the user for whom you want to receive login notifications), set "**Yes**" for the "**Login notification (E-mail)**" option.

![](<../../.gitbook/assets/image (2109).png>)

Similar notifications can also be enabled for sending via [Telegram](https://premium.gitbook.io/main/osnovnye-nastroiki/uvedomleniya-administratoram-i-klientam/uvedomleniya-v-telegram) and SMS.

</details>

<details>

<summary>Provide an example of a working direct link to a specific exchange direction on your exchanger</summary>

Make sure the following are configured:\
• Currency codes in the XML file comply with standards\
• The "**Redirect to exchange direction**" module is enabled\
• Parameters for your exchanger are passed from Bestchange (if not, contact the monitoring support team and ask them to enable data transmission)\
![](<../../.gitbook/assets/image (1494).png>)

</details>

<details>

Here is a natural, fluent English translation of the provided text:

---

**Please install the latest update for the Premium Exchanger direction_xml module as soon as possible**

You need to update the module on your server to ensure the BestChange service works correctly with your exported XML file.

1. [Download](https://premiumexchanger.com/uscripts/) the update package for your script version (the PHP version does not matter — just download the archive for your script version).

<figure><img src="../../.gitbook/assets/image (2161).png" alt=""><figcaption></figcaption></figure>

2. Deactivate the module "**Exchange Directions Output Settings in XML/TXT File**" in the "**Modules**" section.

<figure><img src="../../.gitbook/assets/image (2162).png" alt=""><figcaption></figcaption></figure>

3. Log in to ISP Manager using the user account created for your website. Go to the "**Sites**" section, select your site, and then open "**Site Files**".

<figure><img src="../../.gitbook/assets/image (2159).png" alt=""><figcaption></figcaption></figure>

4. Extract the downloaded update archive. Upload the **`direction_xml`** folder to the server, replacing the existing files.  
   Path to the folder: <mark style="color:orange;">**`wp-content/plugins/premiumbox/moduls/`**</mark>

<figure><img src="../../.gitbook/assets/image (2160).png" alt=""><figcaption></figcaption></figure>

5. Reactivate the module "**Exchange Directions Output Settings in XML/TXT File**" in the "**Modules**" section.

---

<details>

<summary>Adding our banner to the exchanger’s footer. <a href="https://exchangesumo.com/dobavlenie-obmennogo-punkta/">Banner options</a></summary>

In the "**Partners**" section of the admin panel, you can activate a banner:  
![](<../../.gitbook/assets/image (1126).png>)

If the banner you need is not listed, click "**Add**" in the "**Partners**" section:  
![](<../../.gitbook/assets/изображение (188).png>)

Enter the partner’s name, add their link, and upload their banner/image:  
![](<../../.gitbook/assets/изображение (82).png>)

For example, a monitoring service might ask you to place their banner:  
_**"We would appreciate it if you could place our banner \<img src="`https://e-mon.ru/b88x31.png`" alt="Best currency exchange rates" title="Best currency exchange rates" border="0">\</a>"**_

`https://e-mon.ru/b88x31.png` is the partner’s banner image, which you need to download to your computer and then upload in the window described above.

</details>

---

If you need any further assistance, feel free to ask!

<summary>Placing a link/banner to reviews of your exchange service on ExchangeSumo after a successful exchange, as well as notifying users about the possibility of receiving cashback from an ExchangeSumo application (a screenshot must be provided).</summary>

In the "**Currency Exchange Direction Templates**," write the required text and add a link to the reviews page for the "**Completed Application**" status.\
![](<../../.gitbook/assets/image (990).png>)