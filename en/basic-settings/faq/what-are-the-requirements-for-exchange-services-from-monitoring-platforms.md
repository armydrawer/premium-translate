# What are the requirements for exchangers from monitoring services?

If you are the owner of an exchanger listed on Bestchange or another monitoring service, you may receive emails from them regarding compliance requirements for placement on their platform.

We have tried to answer the most popular questions:

<details>

<summary>The "nofollow" attribute</summary>

If you received an email from a monitoring service with the following content:

`We noticed that the link leading to our resource contains the rel="nofollow" attribute. Because of this, banner clicks are not indexed by search engines, and we cannot fully assess the traffic, plus the link weight itself is lost.`

`We ask you to remove the nofollow attribute from the link. This will allow for:`\ `correct tracking of clicks from your site;`\ `increased significance of the placement for search engines.`

Find the theme file for your site on your server at the path `wp-content/themes/your_theme_name/`**`pn-homepage.php`**

In the file, within the **parther\_item** class, delete only the word **nofollow** and save the changes.

<figure><img src="../../.gitbook/assets/image (3) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

</details>

<details>

<summary>"At the moment of creating or changing an order, send the user an email to the address specified by the user when creating the order. The email must contain all the main exchange parameters and the details of the parties"</summary>

You can set up the sending of payment details in the E-mail template ("**Messages**" section) by adding the shortcode **\[to\_account]** (or via the "**Merchant account**" shortcode button) to the required line. Set up email sending according to the [instructions](https://premium.gitbook.io/rukovodstvo-polzovatelya/osnovnye-nastroiki/uvedomleniya/opovesheniya-po-e-mail).

<mark style="background-color:red;">**For version 2.5:**\ choose when to request details from the merchant in the "**Exchanger Settings**" -> "**General Settings**" section. Select the option "**Upon order creation**"

![](<../../.gitbook/assets/image (1124).png>)

\ <mark style="background-color:red;">**For version 2.4:**\ The user will be sent 2 emails - an order creation email and an email with payment details (both templates must be configured)

![](<../../.gitbook/assets/image (1305).png>) ![](<../../.gitbook/assets/image (1306).png>)

</details>

<details>

<summary>"When the exchanger is not working, please disable the rates file"</summary>

Create a mode in the "**Maintenance Mode**" section and configure the XML file display in the mode settings.

![](<../../.gitbook/assets/image (961).png>)

</details>

<details>

<summary>Enabling REST API for monitoring</summary>

#### Previous API version

Activate the "**Affiliate Program API**" module in the "**Modules**" section.

<img src="../../.gitbook/assets/image (1069).png" alt="" data-size="original">

\ Enable the "**Work with REST API (ppapi)**" option in the user profile settings.\ ![](<../../.gitbook/assets/image (1243).png>)

#### Current API version

[**API Documentation**](https://premium.gitbook.io/main/api-premium-exchanger/api-v1)

Activate the "**API**" module in the "**Modules**" section.

![](<../../.gitbook/assets/image (602).png>)

In the "**API - Settings**" section, set the options according to the screenshot below.

![](<../../.gitbook/assets/image (603).png>)

Enable the "**Work with REST API**" option in the profile settings of the user for whom the keys will be issued.

![](<../../.gitbook/assets/image (601).png>)

After this, the user will be able to [independently issue keys](https://premium.gitbook.io/main/api-premium-exchanger/api-v1#poluchenie-api-klyuchei-cherez-lichnyi-kabinet-polzovatelya) for access to the exchanger API.

</details>

<details>

<summary>"Please add our address from which we scan your exchange rates to the whitelist of your CloudFlare\Incapsula\StormWall anti-DDoS system"</summary>

Here is an example for Cloudflare.\ \ Go to the "**Security** ➔ **WAF**" section in the Cloudflare dashboard, then go to the "**Tools**" tab and specify the required IP addresses (select the **Allow** action).\ ![](<../../.gitbook/assets/image (2126).png>)

Save the settings.

![](<../../.gitbook/assets/image (2127).png>)<br>

</details>

<details>

<summary>How to change the protocol for the Telegram account link on the site</summary>

The protocol can only be changed via code by replacing **https://t.me/** with **tg://resolve?domain=** in the file `wp-content/themes/theme_name/header.php`\ \ Before replacement:\ ![](<../../.gitbook/assets/изображение (84).png>)

After replacement:\ ![](<../../.gitbook/assets/изображение (21).png>)

</details>

<details>

<summary>How to add a city in a cash exchange direction</summary>

**XML file**

Add cities in the "**Cities**" section and use them in the exchange direction.

![](<../../.gitbook/assets/image (867).png>)

In the "**Labels for the param parameter**" field, specify the parameters in accordance with [Bestchange requirements](https://www.bestchange.com/wiki/rates.html).

![](<../../.gitbook/assets/image (1114).png>)

After this, the information will be displayed in your XML file.

![](<../../.gitbook/assets/image (1066).png>)

**E-mail letter**

In the "**Exchange Directions**" section -> cash exchange direction, "**Exchange Direction Template**" tab, specify the text for the template with the "**City**" shortcode.

![](<../../.gitbook/assets/image (905).png>)

Then in the "**Messages**" -> "**E-mail templates**" section for the "New order" status, add the "**Exchange Direction Template**" shortcode.

![](<../../.gitbook/assets/image (1054).png>)

The text from the "**Exchange Direction Template**" field will be displayed in the email.

</details>

<details>

<summary>Export XML file with exchange rates for Bestchange is unavailable</summary>

If the file is unavailable, add the BestChange IP address in the CloudFlare control panel.

**Old version of Cloudflare dashboard**

1. Find the "**Bot Fight Mode**" option in the "**Security**" ➔ "**Bots**" section and activate the option.

<figure><img src="../../.gitbook/assets/image (61).png" alt=""><figcaption></figcaption></figure>

2. In the "**Security**" ➔ "**WAF**" ➔ "**Tools**" section, create a rule with the IP address <mark style="color:red;">**`162.19.29.225`** and select the "**Allow**" action. Save the rule.

<figure><img src="../../.gitbook/assets/image (62).png" alt=""><figcaption></figcaption></figure>

3. The added rule will be displayed as follows:

<figure><img src="../../.gitbook/assets/image (63).png" alt=""><figcaption></figcaption></figure>

**New version of Cloudflare dashboard**

1. Go to the "**Security**" ➔ "**Settings**" ➔ "**Bot traffic**" section.

<figure><img src="../../.gitbook/assets/image (68).png" alt=""><figcaption></figcaption></figure>

2. Activate the "**Bot fight mode**" option.

<figure><img src="../../.gitbook/assets/image (69).png" alt=""><figcaption></figcaption></figure>

3. Add a new rule (IP access rules) in the "**Security**" ➔ "**Security rules**" section.

<figure><img src="../../.gitbook/assets/image (65).png" alt=""><figcaption></figcaption></figure>

4. Specify the IP address <mark style="color:red;">**`162.19.29.225`** in the rule being created and select the "**Allow**" action. Save the rule.

<figure><img src="../../.gitbook/assets/image (66).png" alt=""><figcaption></figcaption></figure>

5. The added rule will be displayed as follows:

<figure><img src="../../.gitbook/assets/image (67).png" alt=""><figcaption></figcaption></figure>

After these settings, access to the xml file will be open.

</details>

<details>

<summary>It is necessary to disable caching of served files for our robot's IP addresses</summary>

To add a pool of IP addresses from monitoring, use the [instructions](https://premium.gitbook.io/main/osnovnye-nastroiki/faq/dobavlenie-ip-adresov-v-whitelist-v-cloudflare) or add the monitoring domain itself to the exceptions.

<figure><img src="../../.gitbook/assets/изображение (202).png" alt=""><figcaption></figcaption></figure>

</details>

<details>

<summary>Activity alerts in the site admin panel upon admin login and daily verification that these alerts work (in case of unauthorized access to the admin panel)</summary>

You must have the template enabled and configured in the "**Messages**" → "**E-mail templates**" → "**Notify about user login to account**" section.

![](<../../.gitbook/assets/image (2108).png>)

Then in the admin panel in the "**Users**" section (select the user whose login you want to receive notifications about) → set "**Yes**" for the "**Notification upon login (E-mail)**" parameter.

![](<../../.gitbook/assets/image (2109).png>)

Similar notifications can be enabled for sending to [Telegram](https://premium.gitbook.io/main/osnovnye-nastroiki/uvedomleniya-administratoram-i-klientam/uvedomleniya-v-telegram) and via SMS.

</details>

<details>

<summary>Response regarding passing a preliminary AML check</summary>

The site user must confirm that they are prepared for the fact that their exchange may be suspended as part of an [AML check](https://www.bestchange.com/report/) (which means a refund minus the network fee).

To comply with this requirement, create a new additional field for the exchange direction (not for the currency!) in the admin panel,\ ![](<../../.gitbook/assets/изображение (208).png>)\ fill it out according to the screenshot below and connect the field to the appropriate cryptocurrency exchange directions:

<figure><img src="../../.gitbook/assets/изображение (3) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

A field will appear in the exchange form, one of the items of which every user will be required to select when creating an order.

<figure><img src="../../.gitbook/assets/изображение (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

Monitoring requirement fulfilled.

</details>

<details>

<summary>Provide an example of a working link that goes directly to a direction on your exchanger</summary>

The following items must be configured:\
• currency codes for the XML file comply with standards\
• the "**Redirect to exchange direction**" module is enabled\
• parameters for your exchanger are passed from Bestchange (if this is not the case, contact the monitoring technical support and ask them to enable data transfer)\
![](<../../.gitbook/assets/image (1494).png>)

</details>

<details>

<summary>"We ask you to install the latest update of the Premium Exchanger direction_xml module in the near future"</summary>

You need to update the module on the server for the BestChange service to work correctly with your export xml file.

1. [Download](https://premiumexchanger.com/uscripts/) the distribution with the script update for your script version (PHP version does not matter — download any archive of your version).

<figure><img src="../../.gitbook/assets/image (2161).png" alt=""><figcaption></figcaption></figure>

2. Deactivate the "**Setting up the output of exchange directions in XML/TXT file**" module in the "**Modules**" section.

<figure><img src="../../.gitbook/assets/image (2162).png" alt=""><figcaption></figcaption></figure>

3. Log in to the ISP Manager panel under the user created for the site, go to the "**Sites**" section, select the desired site, and go to the "**Site files**" section.

<figure><img src="../../.gitbook/assets/image (2159).png" alt=""><figcaption></figcaption></figure>

4. Unzip the previously downloaded archive with the script update. Upload the **`direction_xml`** folder, replacing existing files on the server.\
   Path to the folder: <mark style="color:orange;">**`wp-content/plugins/premiumbox/moduls/`**

<figure><img src="../../.gitbook/assets/image (2160).png" alt=""><figcaption></figcaption></figure>

5. Activate the "**Setting up the output of exchange directions in XML/TXT file**" module in the "**Modules**" section.

</details>

<details>

<summary>Placement of our banner in the exchanger footer. <a href="https://exchangesumo.com/dobavlenie-obmennogo-punkta/">Banner of your choice</a></summary>

In the "**Partners**" section in the admin panel, you can activate a banner.\ ![](<../../.gitbook/assets/image (1126).png>)

If the required banner is not in the list, then in the "**Partners**" section, click "**Add**".​\ ![](<../../.gitbook/assets/изображение (59) (1).png>)

Specify the name and add a link to the partner, and also upload their banner/image.\ ![](<../../.gitbook/assets/изображение (82).png>)

​For example, a monitoring service asks you to place its banner: _**"We would be grateful for the placement of our banner \<img src="****`https://e-mon.ru/b88x31.png`****" alt="Profitable currency exchange rate" title="Profitable currency exchange rate" border="0">\</а>"**_

`https://e-mon.ru/b88x31.png` is the partner's banner, which you need to download to your computer and upload in the window specified above.

</details>

<details>

<summary>Placement of a link/banner to reviews about your exchanger on exchangesumo after a successful exchange, as well as notification of the possibility of receiving cashback from an order on exchangesumo (screenshot must be provided).</summary>

In the "**Exchange Direction Templates**", write the necessary text and add a link to the reviews page for the "**Completed order**" status.\ ![](<../../.gitbook/assets/image (990).png>)

</details>
