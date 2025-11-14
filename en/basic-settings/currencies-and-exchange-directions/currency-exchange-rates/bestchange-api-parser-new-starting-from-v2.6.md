---
description: The module is available starting from version 2.6!
---

# Bestchange API Parser (new, starting from v2.6)

{% hint style="warning" %}
Due to technical reasons, it is not possible to transfer settings from the Bestchange parser module. Therefore, you will need to set up all exchange rates from scratch for the new module.
{% endhint %}

{% hint style="danger" %}
To automatically update exchange rates, **it is essential** to create a [Cron job](https://premium.gitbook.io/main/en/basic-settings/faq/kak-sozdat-zadanie-cron-na-servere) on your server using the link from the "**BestChange API Parser**" -> "**Settings**" section.

<img src="../../../.gitbook/assets/image%20(415)_eng.png" alt="" data-size="original">

The hash for the Cron job link is specified in the **`wp-content/plugins/premiumbox/userdata.php`** file.

<img src="../../../.gitbook/assets/image%20(416)_eng.png" alt="" data-size="original"><img src="../../../../ru/.gitbook/assets/image (577) (1).png" alt="" data-size="original">
{% endhint %}

{% hint style="warning" %}
Please note that using the Bestchange API parser does not guarantee you a spot in the list of exchangers on Bestchange, as specified in the parser settings.

The module is available for all exchangers using the Premium Exchanger script—your competitors can set up the parser just like you, so all exchangers using the parser will compete for the specified position (usually the top spot) in the chosen exchange direction.

The only way to guarantee a top position is through **constant undercutting**.

You can also further configure the minimum and maximum rates according to this guide to avoid going into the negative if another exchanger decides to undercut as well (this will pull you along if you have selected the first position binding and have not set the min/max rates).
{% endhint %}

{% hint style="danger" %}
The Bestchange API parser will only work in an active exchange direction—make sure to set the direction to active before starting the configuration of the parser.

<img src="../../../../ru/.gitbook/assets/image (733) (1).png" alt="" data-size="original">
{% endhint %}

## General Module Settings

<figure><img src="../../../../ru/.gitbook/assets/image (2148) (1).png" alt=""><figcaption></figcaption></figure>

**Domain** — Enter one of the domains from the list below the field. If the field is empty (when the parser uses the main BC domain), the parser will not work (currencies and cities will not be displayed in the list below on this page).

**API Key** — The API key from your [personal account on the Bestchange website](https://www.bestchange.ru/partner/profile.html).

<figure><img src="../../../.gitbook/assets/image%20(419)_eng.png" alt="" width="563"><figcaption></figcaption></figure>

**Timeout (sec.)** — The time to wait for a response from Bestchange (recommended value is 20 seconds. If set to 0, it will also default to 20 seconds).

**Site version** — The language version of the Bestchange website (en or ru).

**Position:**\
\&#xNAN;**• Rate** — The base exchange rate (calculation formula: rate = from\_amount / to\_amount)\
\&#xNAN;**• Rankrate** — The rate with additional fees applied, calculated for an exchange amount of $300. This rate is displayed by default on Bestchange. If you want to get a ranking of exchangers sorted by exchange rate as on Bestchange, it is better to use rankrate.

**Blacklist of exchanger IDs (comma-separated)** — IDs of exchangers whose rates will be ignored during parsing.

<details>

<summary>How to find the exchanger ID?</summary>

Click on the image below to see how to find the exchanger ID on the Bestchange website.

<img src="../../../../ru/.gitbook/assets/Clip2net_230726151417 (1).png" alt="" data-size="original">

</details>

**Whitelist of exchanger IDs (comma-separated)** — IDs of exchangers whose rates will be used during parsing (if at least one ID is specified, the parser will only use the rate from this source, ignoring other exchangers).

**Delete old data:**\
\&#xNAN;**• Yes** — Data obtained from the parser will be deleted before each new rate update (if the rate is not updated for any reason, it will display as 0 = 0 until the next successful rate update)\
\&#xNAN;**• No** — Data obtained from the parser will not be deleted before each new rate update (if the rate is not updated for any reason, it will display the previous value until the next successful rate update).

**Disable protection:**\
\&#xNAN;**• Yes** — Protection against rate fluctuations is disabled.\
\&#xNAN;**• No** — Protection against rate fluctuations is enabled. The protection uses data from the top 5 positions in the Bestchange listing to calculate the difference between rates—the rate cannot exceed this difference.

{% hint style="info" %}
**Description of the protection mechanism**

To prevent abnormal fluctuations, we use data obtained from five exchangers (highlighted in the table that opens by clicking the "**Show ranking**" button in the Bestchange parser settings for the exchange direction). We analyze the difference between these rates and set a limit: the rate cannot exceed the maximum difference determined based on this data.

**Key terms:**

<img src="../../../.gitbook/assets/image%20(323)_eng.png" alt="" data-size="original">

In the screenshot, you can see the email sent to the administrator if protection is enabled and the email template "**Bestchange Security Error**" is activated.

• **First rate** — the rate of the first position among the five sources.

• **Your rate** — your current rate.

• **Min security rate** — the minimum rate considered safe according to our calculations.

<img src="../../../.gitbook/assets/image%20(324)_eng.png" alt="" data-size="original">

**Reasons for implementing protection**

In the past, we encountered situations where there were sharp fluctuations in rates on Bestchange due to changes in the format of rate representation (for example, from 1 to XXX to XXX to 1). This protection was developed to track such anomalies.

**Conditions for the protection to work**

This protection will work effectively if you add small values to the step, for example, 0.0001. If you add more significant values, such as 0.5% or higher, the rate will already be considered abnormal.
{% endhint %}

**Select currencies** — A list of available currencies from Bestchange for parsing (the list will only be displayed after entering a valid API key in the parser settings).

<figure><img src="../../../.gitbook/assets/image%20(420)_eng.png" alt="" width="395"><figcaption></figcaption></figure>

**Select cities** — A list of cities from Bestchange for parsing (the list will only be displayed after entering a valid API key in the parser settings).

<figure><img src="../../../.gitbook/assets/image%20(421)_eng.png" alt="" width="363"><figcaption></figcaption></figure>

## Parser Settings for Exchange Direction

In the control panel, go to "**Exchange Directions" → "Exchange Directions"** to edit the exchange direction.

On the "**Auto Rate Adjustment**" and "**Bestchange Parser**" tabs, before starting the configuration of the BestChange API parser, disable any active rate auto-adjustments if such settings are in use.

<div><figure><img src="../../../.gitbook/assets/image%20(423)_eng.png" alt="" width="359"><figcaption></figcaption></figure> <figure><img src="../../../.gitbook/assets/image%20(422)_eng.png" alt="" width="443"><figcaption></figcaption></figure></div>

On the "**BestChange API Parser**" tab, you will see a settings block. Make the necessary configurations:

<figure><img src="../../../.gitbook/assets/image%20(424)_eng.png" alt="" width="563"><figcaption></figcaption></figure>

**Enable parser:**\
\&#xNAN;**• Yes** — The parser is enabled for the exchange direction.\
\&#xNAN;**• No** — The parser is not in use.

{% hint style="warning" %}
To activate the parser, you must select 2 currencies in the "**Currencies (You Give)**" and "**Currencies (You Receive)**" fields.
{% endhint %}

**Blacklist of exchanger IDs (comma-separated)** — IDs of exchangers whose rates will be ignored during parsing.

**Whitelist of exchanger IDs (comma-separated)** — IDs of exchangers whose rates will be used during parsing (if at least one ID is specified, the parser will only use the rate from this source, ignoring other exchangers).

{% hint style="warning" %}
If similar fields are filled in the general parser settings, they will be ignored for the settings of this exchange direction—the settings for the exchange direction take precedence.

If the fields in the exchange direction settings are not filled, but the general settings are, the general settings will apply to the exchange direction.
{% endhint %}

**City** — A list of cities that are checked in the general parser settings (the city is selected for the exchange direction with cash).

**Currencies (You Give)** — Select the currency for the "**You Give**" side.

**Currencies (You Receive)** — Select the currency for the "**You Receive**" side.

**Rate Side:**\
\&#xNAN;**• Auto** — Automatic selection of the rate side for values in the "**Min. Rate**" and "**Max. Rate**" fields.\
\&#xNAN;**• 1 = XXX** — Forced setting of the rate 1 to XXX.\
\&#xNAN;**• XXX = 1** — Forced setting of the rate XXX to 1.

**Position** — The position from the Bestchange ranking for the selected exchange direction (if the field is not filled, the 1st position is used).

**Step** — Adjustment of the rate obtained from the parser (for example, 0.001). The system by default always makes your rate more favorable than the rate specified in the "**Position**" field. The step can also be set as a percentage (for example, 3%).

Here’s a naturalistic English translation of the provided text:

***

The value of a step with a negative sign ("**-**") will decrease your rate compared to the specified position (by -0.001 or -3%). You can also use multiplication and division (e.g., \*2 or /2, \*3% or /3%).

**Minimum Reserve for Position** — the minimum reserve value for the position (for the currency "**You Receive**"). Exchange services with reserves below this specified value will be ignored by the module.

**Show Rating** — a page displaying currency rates from Bestchange along with the recommended step.

<figure><img src="../../../.gitbook/assets/image (1763)_eng.png" alt="" width="563"><figcaption></figcaption></figure>

**Minimum Rate** — the lowest threshold for the rate, below which the binding to the position will not function. If a competitor for the specified position goes below this minimum rate, the module will reset your rate to the standard one (if this option is enabled).

{% hint style="warning" %}
If one or all options ("**Minimum Rate**", "**Maximum Rate**", "**Standard Rate**") are specified both manually and through the "**Auto Rate Adjustment**" option,\
![](<../../../.gitbook/assets/image (1785)_eng.png>)\
the rate from the "**Auto Rate Adjustment**" field will always take precedence and will be used by the parser.
{% endhint %}

**Auto Adjustment of Minimum Rate** — binding the minimum rate to a selected source from the "**Parsers 2.0**" -> "**Rates**" section.\
\&#xNAN;**• Add to Rate** — adjustment of the minimum rate obtained from the source (for example, adding 3% or subtracting -3%).

**Maximum Rate** — the highest threshold for the rate, above which the binding to the position will not function. If a competitor for the specified position exceeds this maximum rate, the module will reset your rate to the standard one (if this option is enabled).

**Auto Adjustment of Maximum Rate** — binding the maximum rate to a selected source from the "**Parsers 2.0**" -> "**Rates**" section.\
\&#xNAN;**• Add to Rate** — adjustment of the maximum rate obtained from the source (for example, adding 3% or subtracting -3%).

**Reset to Standard Rate:**\
\&#xNAN;**• Yes** — enables the option to reset to the standard rate when exceeding the min/max range.\
\&#xNAN;**• No** — the option is not used.

**Standard Rate (You Give)** — manual specification of the standard rate for the "**You Give**" side.

**Standard Rate (You Receive)** — manual specification of the standard rate for the "**You Receive**" side.

**Auto Adjustment of Rate** — binding the standard rate to a selected source from the "**Parsers 2.0**" -> "**Rates**" section.\
\&#xNAN;**• Add to Rate (You Give)** — adjustment of the maximum rate obtained from the source (for example, adding 3% or subtracting -3%) for the "**You Give**" side.\
\&#xNAN;**• Add to Rate (You Receive)** — adjustment of the maximum rate obtained from the source (for example, adding 3% or subtracting -3%) for the "**You Receive**" side.

**Convert Rate:**\
\&#xNAN;**• Yes** — forces the exchange rate to be converted to a format of 1 to XXX.\
\&#xNAN;**• No** — the option is not used.

***

Let me know if you need any further assistance!
