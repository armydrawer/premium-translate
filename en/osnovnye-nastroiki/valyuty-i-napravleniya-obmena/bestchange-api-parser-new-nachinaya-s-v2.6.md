Here is a natural, fluent English translation of the provided text:

---

description: The module is available starting from version 2.6!

---

# BestChange API Parser (new, starting from v2.6)

{% hint style="warning" %}
It is technically impossible to transfer settings from the old BestChange parser module, so you will need to configure all exchange rates from scratch to use the new module.
{% endhint %}

{% hint style="danger" %}
To enable automatic currency rate updates, you **must** create a [Cron job](https://premium.gitbook.io/user-guide/basic-settings/faq/how-to-create-a-cron-job-on-the-server) on your server using the link found under "**BestChange API parser**" -> "**Settings**".

![](<../../../.gitbook/assets/image (415).png>)

The hash for the Cron job URL is set in the file **`wp-content/plugins/premiumbox/userdata.php`**

![](<../../../.gitbook/assets/image (416).png>)

![](<../../../.gitbook/assets/image (1520).png>)
{% endhint %}

{% hint style="warning" %}
Please note that using the BestChange API parser does **not** guarantee your exchanger’s position on the BestChange listing as specified in the parser settings.

This module is available to all exchangers using the Premium Exchanger script — your competitors can configure the parser just like you. Therefore, all exchangers using the parser will be competing for the specified position (usually the 1st place) in the chosen exchange direction.

The only way to guarantee the top spot is **constant undercutting** (price dumping).

You can also set minimum and maximum rates following this guide to avoid accidentally going into a loss if another exchanger starts dumping prices as well (this will pull you down too if you have chosen to tie your rate to the first place and haven’t set min/max rate limits).
{% endhint %}

{% hint style="danger" %}
The BestChange API parser will only work for active exchange directions — be sure to activate the exchange direction before configuring the parser.

<img src="../../../.gitbook/assets/image (733).png" alt="" data-size="original">
{% endhint %}

## General Module Settings

<figure><img src="../../../.gitbook/assets/image (2148).png" alt=""><figcaption></figcaption></figure>

**Domain** — enter one of the domains from the list below the field. Use this if the parser does not work (i.e., currencies and cities do not appear in the lists below on this page) when the field is left empty (which means the parser uses the main BestChange domain).

**API Key** — your API key from your [BestChange partner account](https://www.bestchange.ru/partner/profile.html)

---

If you need any further help or adjustments, just let me know!

**Timeout (sec.)** — the waiting time for a response from Bestchange (recommended value is 20 seconds. If set to 0, the value of 20 seconds will also be applied)

**Site version** — the language version of the Bestchange website (en or ru)

**Position:**  
• **Rate** — the base exchange rate (calculation formula: rate = from_amount / to_amount)  
• **Rankrate** — the rate including additional fees, calculated for an exchange amount of $300. This rate is displayed by default on Bestchange. If you want to get the exchanger rankings sorted by exchange rate as on Bestchange, it’s better to use rankrate.

**Blacklist of exchanger IDs (comma-separated)** — IDs of exchangers whose rates will be ignored during parsing

<details>

<summary>How to find an exchanger’s ID?</summary>

Click the image below to see how to find an exchanger’s ID on the Bestchange website.

<img src="../../../.gitbook/assets/Clip2net_230726151417.png" alt="" data-size="original">

</details>

**Whitelist of exchanger IDs (comma-separated)** — IDs of exchangers whose rates will be used during parsing (if at least one ID is specified, the parser will use only the rates from these sources, ignoring all other exchangers)

**Delete old data:**  
• **Yes** — data obtained from the parser will be deleted before each new rate update (if for some reason the rate is not updated, it will be displayed as 0 = 0 until the next successful update)  
• **No** — data obtained from the parser will not be deleted before each new rate update (if for some reason the rate is not updated, the previously obtained value will be displayed until the next successful update)

**Disable protection:**  
• **Yes** — protection against rate spikes is disabled  
• **No** — protection against rate spikes is enabled. The protection uses data from the top 5 exchangers listed on Bestchange to calculate the difference between rates — the rate cannot exceed this difference

{% hint style="info" %}
**Description of the protection mechanism**

To prevent abnormal spikes, we use data obtained from five exchangers (these are underlined in the table that opens by clicking the "**Show rating**" button in the Bestchange parser settings for the exchange direction). We analyze the differences between these rates and set a limit: the rate cannot exceed the maximum difference determined based on this data.

**Key terms:**

<img src="../../../.gitbook/assets/image (323).png" alt="" data-size="original">

The screenshot shows the email sent to the administrator if protection is enabled and the "**Bestchange Security Error**" email template is activated.

• **First rate** — the rate of the top position among the five sources

• **Your rate** — your current rate

• **Min security rate** — the minimum rate considered safe according to our calculations

![](<../../../.gitbook/assets/image (324).png>)

**Reasons for implementing protection**

In the past, we encountered situations where Bestchange experienced sharp rate spikes due to changes in the rate format (for example, switching from 1 to XXX to XXX to 1). This protection was developed to monitor such anomalies.

**Protection operation conditions**

This protection works effectively if you add small increments to the step, for example, 0.0001. However, if you add larger increments, such as 0.5% or more, the rate will already be considered abnormal.
{% endhint %}

**Select currencies** — a list of available currencies from Bestchange for parsing (the list will only appear after entering a valid API key in the parser settings)

<figure><img src="../../../.gitbook/assets/image (420).png" alt="" width="395"><figcaption></figcaption></figure>

**Select cities** — a list of cities from Bestchange for parsing (the list will only appear after entering a valid API key in the parser settings)

<figure><img src="../../../.gitbook/assets/image (421).png" alt="" width="363"><figcaption></figcaption></figure>

## Parser settings for exchange directions

In the control panel, go to "**Exchange Directions → Exchange Directions**" and proceed to edit the exchange direction.

On the "**Exchange Rate Auto-Correction**" and "**BestChange Parser**" tabs, before configuring the BestChange API parser, make sure to disable any active exchange rate auto-corrections if such settings are in use.

<div><figure><img src="../../../.gitbook/assets/image (423).png" alt="" width="359"><figcaption></figcaption></figure> <figure><img src="../../../.gitbook/assets/image (422).png" alt="" width="443"><figcaption></figcaption></figure></div>

On the "**BestChange API Parser**" tab, you will find the settings section. Please configure the options as needed:

<figure><img src="../../../.gitbook/assets/image (424).png" alt="" width="563"><figcaption></figcaption></figure>

**Enable parser:**  
• **Yes** — the parser is enabled for this exchange direction  
• **No** — the parser is not used

{% hint style="warning" %}
To activate the parser, you must select two currencies in the "**Currencies (Give)**" and "**Currencies (Receive)**" fields.
{% endhint %}

**Blacklist of exchanger IDs (comma-separated)** — IDs of exchangers whose rates will be ignored during parsing.

**Whitelist of exchanger IDs (comma-separated)** — IDs of exchangers whose rates will be used during parsing (if at least one ID is specified, the parser will use only the rates from these sources and ignore all others).

{% hint style="warning" %}
If the same fields are filled in the general parser settings, they will be ignored for this exchange direction — settings for the exchange direction take priority.

If these fields are left empty in the exchange direction settings but filled in the general settings, the general settings will apply to this exchange direction.
{% endhint %}

**City** — list of cities checked in the general parser settings (select a city for cash exchange directions).

**Currencies (Give)** — select the currency you are giving.

**Currencies (Receive)** — select the currency you are receiving.

**Rate side:**  
• **Auto** — automatically select the rate side for the values in the "**Min. rate**" and "**Max. rate**" fields  
• **1 = XXX** — force the rate to be 1 to XXX  
• **XXX = 1** — force the rate to be XXX to 1

**Position** — the position in the BestChange rating for the selected exchange direction (if left empty, the 1st position is used).

**Step** — adjustment to the rate received from the parser (for example, 0.001). By default, the system always sets your rate to be more favorable than the rate specified in the "**Position**" field. The step can also be set as a percentage (for example, 3%).

A step value with a "**-**" sign will make your rate less favorable than the rate of the specified position (e.g., -0.001 or -3%). You can also use multiplication and division (\*2 or /2, \*3% or /3%).

**Min. reserve for position** — the minimum reserve amount required for the position (for the currency "**You receive**"). Exchange services with reserves below this value will be ignored by the module.

**Show rating** — a page displaying currency rates from Bestchange along with the recommended step.

<figure><img src="../../../.gitbook/assets/image (1763).png" alt="" width="563"><figcaption></figcaption></figure>

**Min. rate** — the lower limit of the rate at which the position binding will operate. If a competitor for the specified position goes below this minimum rate, the module will reset your rate to the standard rate (if this option is enabled).

{% hint style="warning" %}
If rates for one or all of the options ("**Minimum rate**", "**Maximum rate**", "**Standard rate**") are set both manually and selected in the "**Auto rate adjustment**" option,  
![](<../../../.gitbook/assets/image (1785).png>)  
then the rate from the "**Auto rate adjustment**" field will always take priority and will be used by the parser.
{% endhint %}

**Auto adjustment of min. rate** — links the minimum rate to the selected source from the "**Parsers 2.0**" -> "**Rates**" section.  
• **Add to rate** — adjustment applied to the minimum rate obtained from the source (for example, adding 3% or subtracting 3%).

**Max. rate** — the upper limit of the rate at which the position binding will operate. If a competitor for the specified position exceeds this maximum rate, the module will reset your rate to the standard rate (if this option is enabled).

**Auto-Adjustment of Maximum Rate** — links the maximum exchange rate to a selected source from the "**Parsers 2.0**" -> "**Rates**" section.  
• **Add to rate** — adjusts the maximum rate obtained from the source (for example, adding 3% or subtracting 3%).

**Reset to Standard Rate:**  
• **Yes** — enables resetting to the standard rate if the rate goes outside the minimum/maximum range.  
• **No** — this option is not used.

**Standard Rate (You Give)** — manually specify the standard rate for the "**You Give**" side.

**Standard Rate (You Receive)** — manually specify the standard rate for the "**You Receive**" side.

**Auto-Adjustment of Rate** — links the standard rate to a selected source from the "**Parsers 2.0**" -> "**Rates**" section.  
• **Add to rate (You Give)** — adjusts the rate obtained from the source (for example, adding 3% or subtracting 3%) for the "**You Give**" side.  
• **Add to rate (You Receive)** — adjusts the rate obtained from the source (for example, adding 3% or subtracting 3%) for the "**You Receive**" side.

**Convert Rate:**  
• **Yes** — forces the exchange rate to be converted into the format 1 to XXX.  
• **No** — this option is not used.