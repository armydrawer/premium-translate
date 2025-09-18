# What are the requirements for exchange services from monitoring platforms?

If you own an exchange service listed on BestChange or another monitoring platform, you may receive emails from them outlining compliance requirements for being featured on their platform.

We’ve compiled answers to some common questions:

***

<details>

<summary>**"When creating or modifying an order, send an email to the user at the address provided during order creation. The email should include all key exchange parameters and account details of the parties involved."**</summary>

You can configure the sending of account details in the email template (under the "**Messages**" section) by adding the shortcode **\[to\_account]** to the appropriate line (or by using the "**Merchant Account**" shortcode button). Follow the [instructions](https://premium.gitbook.io/rukovodstvo-polzovatelya/osnovnye-nastroiki/uvedomleniya/opovesheniya-po-e-mail) to set up email notifications.

**For version 2.5:**\
Go to "**Exchange Settings**" -> "**General Settings**" and select "**Request account details when creating an order**."

![Version 2.5 Screenshot](../../.gitbook/assets/image%20\(1124\).png)

**For version 2.4:**\
The user will receive two emails: one confirming the order creation and another with payment details. You need to configure both templates.

![Version 2.4 Screenshot 1](../../.gitbook/assets/image%20\(1305\).png)\
![Version 2.4 Screenshot 2](../../.gitbook/assets/image%20\(1306\).png)

</details>

***

<details>

<summary>**"Please disable the exchange rate file when your service is offline."**</summary>

Create a maintenance mode in the "**Maintenance Mode**" section and configure the XML file display settings within the mode.

![Maintenance Mode Screenshot](../../.gitbook/assets/image%20\(961\).png)

</details>

***

<details>

<summary>**Enabling REST API for monitoring platforms**</summary>

#### Previous API Version

1. Activate the "**Affiliate Program API**" module in the "**Modules**" section.\
   ![Affiliate Program API Screenshot](../../.gitbook/assets/image%20\(1069\).png)
2. Enable the "**Work with REST API (ppapi)**" option in the user profile settings.\
   ![REST API Option Screenshot](../../.gitbook/assets/image%20\(1243\).png)

#### Current API Version

* Refer to the [API Documentation](https://premium.gitbook.io/main/api-premium-exchanger/api-v1).

1. Activate the "**API**" module in the "**Modules**" section.\
   ![API Module Screenshot](../../.gitbook/assets/image%20\(602\).png)
2. Configure the options in the "**API - Settings**" section as shown below.\
   ![API Settings Screenshot](../../.gitbook/assets/image%20\(603\).png)
3. Enable the "**Work with REST API**" option in the user profile settings for the user who will generate the API keys.\
   ![API Key Option Screenshot](../../.gitbook/assets/image%20\(601\).png)
4. The user can then [generate API keys](https://premium.gitbook.io/main/api-premium-exchanger/api-v1#poluchenie-api-klyuchei-cherez-lichnyi-kabinet-polzovatelya) independently for accessing the exchange service API.

</details>

***

<details>

<summary>**"Please add our IP address used for scanning your exchange rates to the whitelist of your anti-DDoS system (e.g., Cloudflare, Incapsula, StormWall)."**</summary>

**Example for Cloudflare:**

1. Go to the "**Security** ➔ **WAF**" section in your Cloudflare dashboard.
2. Navigate to the "**Tools**" tab and add the required IP addresses, selecting the action "**Allow**."\
   ![Cloudflare WAF Screenshot](../../.gitbook/assets/image%20\(2126\).png)
3. Save the settings.\
   ![Cloudflare Save Settings Screenshot](../../.gitbook/assets/image%20\(2127\).png)

</details>

***

<details>

<summary>**How to replace the protocol for a Telegram account link on your website**</summary>

You can only change the protocol by editing the code. Replace **https://t.me/** with **tg://resolve?domain=** in the file `wp-content/themes/your_theme_name/header.php`.

**Before the change:**\
![Before Change Screenshot](../../.gitbook/assets/%D0%B8%D0%B7%D0%BE%D0%B1%D1%80%D0%B0%D0%B6%D0%B5%D0%BD%D0%B8%D0%B5%20\(84\).png)

**After the change:**\
![After Change Screenshot](../../.gitbook/assets/%D0%B8%D0%B7%D0%BE%D0%B1%D1%80%D0%B0%D0%B6%D0%B5%D0%BD%D0%B8%D0%B5%20\(21\).png)

</details>

***

<details>

<summary>**How to add a city for cash exchange directions**</summary>

#### XML File

1. Add cities in the "**Cities**" section and link them to the exchange direction.\
   ![Cities Section Screenshot](../../.gitbook/assets/image%20\(867\).png)
2. In the "**Labels for param parameter**" field, specify parameters according to [BestChange requirements](https://www.bestchange.ru/wiki/rates.html).\
   ![Labels Screenshot](../../.gitbook/assets/image%20\(1114\).png)
3. The information will then appear in your XML file.\
   ![XML File Screenshot](../../.gitbook/assets/image%20\(1066\).png)

#### Email Notification

1. In the "**Exchange Directions**" section, go to the cash exchange direction and specify the text for the template using the "**City**" shortcode.\
   ![Template Screenshot](../../.gitbook/assets/image%20\(905\).png)
2. In the "**Messages**" -> "**Email Templates**" section, add the "**Exchange Direction Template**" shortcode for the "New Order" status.\
   ![Email Template Screenshot](../../.gitbook/assets/image%20\(1054\).png)

The text from the "**Exchange Direction Template**" field will be displayed in the email.

</details>

***

<details>

<summary>**Export XML file with exchange rates for BestChange is unavailable**</summary>

If the file is unavailable, add BestChange’s IP address in the Cloudflare control panel.

**For the old Cloudflare dashboard:**

1. Enable "**Bot Fight Mode**" in the "**Security** ➔ **Bots**" section.\
   ![Bot Fight Mode Screenshot](../../.gitbook/assets/image%20\(61\).png)
2. In "**Security** ➔ **WAF** ➔ **Tools**," create a rule with the IP address **`162.19.29.225`** and select the action "**Allow**." Save the rule.\
   ![Old Dashboard Rule Screenshot](../../.gitbook/assets/image%20\(62\).png)
3. The added rule will appear as follows:\
   ![Old Dashboard Rule Display Screenshot](../../.gitbook/assets/image%20\(63\).png)

**For the new Cloudflare dashboard:**

1. Go to "**Security** ➔ **Settings** ➔ **Bot Traffic**" and enable "**Bot Fight Mode**."\
   ![New Dashboard Bot Fight Mode Screenshot](../../.gitbook/assets/image%20\(68\).png)
2. Add a new rule (IP access rules) in "**Security** ➔ **Security Rules**."\
   ![New Dashboard Rule Screenshot](../../.gitbook/assets/image%20\(65\).png)
3. Specify the IP address **`162.19.29.225`** in the rule and select the action "**Allow**." Save the rule.\
   ![New Dashboard Rule Save Screenshot](../../.gitbook/assets/image%20\(66\).png)
4. The added rule will appear as follows:\
   ![New Dashboard Rule Display Screenshot](../../.gitbook/assets/image%20\(67\).png)

After these settings, access to the XML file will be restored.

</details>

***

<details>

<summary>**Notifications about admin panel activity upon admin login and daily checks to ensure these notifications are working (to prevent unauthorized access).**</summary>

1. Enable and configure the template in "**Messages**" → "**Email Templates**" → "**Notify about user login to the admin panel**."\
   ![Login Notification Template Screenshot](../../.gitbook/assets/image%20\(2108\).png)
2. In the admin panel, go to "**Users**," select the user for whom you want to receive notifications, and set "**Yes**" for the "**Login Notification (Email)**" parameter.\
   ![User Notification Settings Screenshot](../../.gitbook/assets/image%20\(2109\).png)

You can also enable similar notifications for [Telegram](https://premium.gitbook.io/main/osnovnye-nastroiki/uvedomleniya-administratoram-i-klientam/uvedomleniya-v-telegram) and SMS.

</details>

***

<details>

<summary>**Provide an example of a working link to a specific exchange direction on your platform.**</summary>

Ensure the following are configured:

* Currency codes in the XML file comply with standards.
* The "**Redirect to Exchange Direction**" module is enabled.
* Parameters for your exchange service are being transmitted from BestChange (if not, contact their technical support to enable data transmission).\
  ![Redirect Module Screenshot](../../.gitbook/assets/image%20\(1494\).png)

</details>

***

<details>

<summary>**"Please install the latest update for the Premium Exchanger direction_xml module as soon as possible."**</summary>

To ensure proper functionality of BestChange with your export XML file, update the module on your server.

1. [Download](https://premiumexchanger.com/uscripts/) the update for your script version (PHP version doesn’t matter—download the archive for your script version).\
   ![Download Update Screenshot](../../.gitbook/assets/image%20\(2161\).png)
2. Deactivate the "**Configure Exchange Directions Output in XML/TXT File**" module in the "**Modules**" section.\
   ![Deactivate Module Screenshot](../../.gitbook/assets/image%20\(2162\).png)
3. Log in to ISP Manager under the user created for the site, go to the "**Sites**" section, select the site, and navigate to "**Site Files**."\
   ![ISP Manager Screenshot](../../.gitbook/assets/image%20\(2159\).png)
4. Extract the downloaded archive and upload the **`direction_xml`** folder to the server, replacing existing files.\
   Path: **`wp-content/plugins/premiumbox/moduls/`**\
   ![Upload Files Screenshot](../../.gitbook/assets/image%20\(2160\).png)
5. Reactivate the "**Configure Exchange Directions Output in XML/TXT File**" module in the "**Modules**" section.

</details>

***

<details>

<summary>**Adding our banner to the footer of your exchange service. [Choose a banner](https://exchangesumo.com/dobavlenie-obmennogo-punkta/)**</summary>

1. In the "**Partners**" section of the admin panel, activate the banner.\
   ![Activate Banner Screenshot](../../.gitbook/assets/image%20\(1126\).png)
2. If the desired banner is not listed, click "**Add**" in the "**Partners**" section.\
   ![Add Banner Screenshot](../../.gitbook/assets/%D0%B8%D0%B7%D0%BE%D0%B1%D1%80%D0%B0%D0%B6%D0%B5%D0%BD%D0%B8%D0%B5%20\(188\).png)
3. Enter the name, add the partner’s link, and upload their banner/image.\
   ![Upload Banner Screenshot](../../.gitbook/assets/%D0%B8%D0%B7%D0%BE%D0%B1%D1%80%D0%B0%D0%B6%D0%B5%D0%BD%D0%B8%D0%B5%20\(82\).png)

For example, a monitoring platform may request you to add their banner:\
&#xNAN;_"We would appreciate it if you could place our banner: `<img src="https://e-mon.ru/b88x31.png" alt="Best exchange rates" title="Best exchange rates" border="0">`"_

Download the banner (`https://e-mon.ru/b88x31.png`) to your computer and upload it in the specified section.

</details>

***

<details>

<summary>**Adding a link/banner to reviews about your exchange service on ExchangeSumo after a successful exchange, and notifying users about cashback opportunities for their orders (screenshot required).**</summary>

Follow the instructions provided by ExchangeSumo to integrate the link/banner and set up notifications.

</details>

In the "**Currency Exchange Templates**," write the required text and include a link to the reviews page for the "**Completed Request**" status.\
![](../../.gitbook/assets/image%20\(990\).png)
