# What are the monitoring requirements for exchangers?

If you are the owner of an exchanger that is hosted on Bestchange or other monitoring — you can receive letters from them about compliance requirements for placement on the site.

We tried to answer some popular questions:

<details>

<summary>Nofollow attribute</summary>

If you receive a monitoring email with the following content:

`We noticed that the link to our resource contains the rel="nofollow" attribute. Because of this, banner hops are not indexed by search engines, and we cannot fully estimate traffic, and the weight of the link itself is lost.`

`Please remove the nofollow attribute from the link. This will allow:`\
`correctly take into account transitions from your site;`\
`increase the importance of placement for search engines.`

Find the site theme file on your server along the path `wp-content/themes/name_your_theme/`**`pn-homepage.php`**

In a file in the **parther\_item** class, delete only the word **nofollow** and save the changes.

<figure><img src="./../.gitbook/assets/image (3) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

</details>

<details>

<summary>"At the time of creating or changing an application, send a letter to the user to the email address specified by the user when creating the application. The email must contain all the main exchange parameters and details of the parties"</summary>

You can configure the sending of details in the E-mail template (section "**Messages**") by adding the shortcode **\[to\_account]** to the desired line (or using the shortcode button "** Merchant account**"). Configure sending emails with [instructions](https://premium.gitbook.io/rukovodstvo-polzovatelya/osnovnye-nastroiki/uvedomleniya/opovesheniya-po-e-mail).

<mark style="background-color:red;">**For version 2.5:**</mark>\
select when to request details from the merchant in the "**Exchanger Settings**" -> "**Basic Settings**" section. Select the option "**When creating an application**"

![](<../../.gitbook/assets/image (1124).png>)

\
<mark style="background-color:red;">**For version 2.4:**</mark>\
The user will be sent 2 letters - a letter about creating an application and a letter with payment details (both templates must be configured)

![](<../../.gitbook/assets/image (1305).png>) ![](<../../.gitbook/assets/image (1306).png>)

</details>

<details>

<summary>"At a time when the exchanger is not working, please disable the rate file"</summary>

Create a mode in the "**Service Mode**" section and configure the display of the XML file in the mode settings

![](<../../.gitbook/assets/image (961).png>)

</details>

<details>

<summary>Enable REST API for monitoring</summary>

#### Previous version of API

Activate the module "**API Affiliate Program**" in the "**Modules**" section

<img src="./../.gitbook/assets/image (1069).png" alt="" data-size="original">

\
Enable the option "**Work with REST API (ppapi)**" in the user profile settings\
![](<../../.gitbook/assets/image (1243).png>)

#### Current version of API

[**API Documentation**](https://premium.gitbook.io/main/api-premium-exchanger/api-v1)

Activate the "**API**" module in the "**Modules**" section

![](<../../.gitbook/assets/image (602).png>)

Under "**API - Settings**", set the options according to the screenshot below

![](<../../.gitbook/assets/image (603).png>)

Enable the option "**Work with REST API**" in the profile settings of the user for whom the keys will be issued

![](<../../.gitbook/assets/image (601).png>)

After this, the user will be able to [self-release keys](https://premium.gitbook.io/main/api-premium-exchanger/api-v1#poluchenie-api-klyuchei-cherez-lichnyi-kabinet-polzovatelya) to access the exchanger API.

</details>

<details>

<summary>"Please add our address from which we scan your exchange rates in the whitelist of your anti-DDOS system CloudFlare\Incapsula\StormWall"</summary>
