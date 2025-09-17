### Bestchange API Parser (New, Starting from v2.6)

#### Description: The module is available starting from version 2.6!

---

#### Important Notes:

{% hint style="warning" %}
Due to technical reasons, settings from the previous Bestchange Parser module cannot be transferred. Therefore, you will need to reconfigure all exchange rates from scratch to use the new module.
{% endhint %}

{% hint style="danger" %}
To enable automatic currency rate updates, it is **mandatory** to create a [Cron job](https://premium.gitbook.io/rukovodstvo-polzovatelya/osnovnye-nastroiki/faq/kak-sozdat-zadanie-cron-na-servere) on your server. Use the link provided in the "**BestChange API Parser**" -> "**Settings**" section.

![](<../../../.gitbook/assets/image (415).png>)

The hash for the Cron job link is specified in the file **`wp-content/plugins/premiumbox/userdata.php`**.

![](<../../../.gitbook/assets/image (416).png>)

![](<../../../.gitbook/assets/image (1520).png>)
{% endhint %}

{% hint style="warning" %}
Please note that using the Bestchange API Parser does not guarantee a spot in the Bestchange exchanger list for the position you specify in the parser settings.

The module is available to all exchangers using the Premium Exchanger script. This means your competitors can configure the parser just like you, leading to competition for the specified position (most often the 1st position) in the selected exchange direction.

The only guaranteed way to secure the top spot is through **constant undercutting** (price dumping).

Additionally, you can configure minimum and maximum rates using the provided instructions to avoid accidentally incurring losses if another exchanger also decides to undercut prices. Without setting min/max rates, the system will follow the competition, potentially pulling your rates down as well.
{% endhint %}

{% hint style="danger" %}
The Bestchange API Parser will only work for active exchange directions. When configuring the parser, make sure to activate the exchange direction before starting the setup.

<img src="../../../.gitbook/assets/image (733).png" alt="" data-size="original">
{% endhint %}

---

### General Module Settings

<figure><img src="../../../.gitbook/assets/image (2148).png" alt=""><figcaption></figcaption></figure>

- **Domain**: Enter one of the domains listed below the field. If the field is left empty (when the parser uses the main BC domain) and the parser does not work (currencies and cities are not displayed in the list below on the same page), specify a domain from the list.

- **API Key**: The API key from your [Bestchange account](https://www.bestchange.ru/partner/profile.html).

<figure><img src="../../../.gitbook/assets/image (419).png" alt="" width="563"><figcaption></figcaption></figure>

- **Timeout (sec.)**: The waiting time for a response from Bestchange. The recommended value is 20 seconds. If set to 0, the default value of 20 seconds will also apply.

- **Site Version**: The language version of the Bestchange website (either `en` or `ru`).

- **Position**:  
  - **Rate**: The base exchange rate (calculated as `rate = from_amount / to_amount`).  
  - **Rankrate**: The rate with additional fees applied, calculated for an exchange amount of $300. This is the default rate displayed on Bestchange. If you want to get a ranking of exchangers sorted by the exchange rate as shown on Bestchange, it’s better to use `rankrate`.

- **Blacklist of Exchanger IDs (comma-separated)**: IDs of exchangers whose rates will be ignored during parsing.

<details>
<summary>How to find an exchanger's ID?</summary>
Click the image below to see how to locate an exchanger's ID on the Bestchange website.

<img src="../../../.gitbook/assets/Clip2net_230726151417.png" alt="" data-size="original">
</details>

- **Whitelist of Exchanger IDs (comma-separated)**: IDs of exchangers whose rates will be used during parsing. If at least one ID is specified, the parser will only use rates from these sources, ignoring all others.

- **Delete Old Data**:  
  - **Yes**: Data retrieved by the parser will be deleted before each new rate update. If the rate is not updated for any reason, it will display as `0 = 0` until the next successful update.  
  - **No**: Data retrieved by the parser will not be deleted before each new rate update. If the rate is not updated for any reason, the previous value will remain displayed until the next successful update.

- **Disable Protection**:  
  - **Yes**: Disables protection against rate fluctuations.  
  - **No**: Enables protection against rate fluctuations. The protection uses data from the top 5 positions in the Bestchange listing to calculate the difference between rates. The rate cannot exceed this difference.

{% hint style="info" %}
**Protection Mechanism Description**

To prevent abnormal rate fluctuations, we use data from the top five exchangers (highlighted in the table accessible via the "**Show Rating**" button in the Bestchange parser settings for the exchange direction). We analyze the differences between these rates and set a limit: the rate cannot exceed the maximum difference calculated from this data.

**Key Terms:**

<img src="../../../.gitbook/assets/image (323).png" alt="" data-size="original">

The screenshot shows an email sent to the administrator if protection is enabled and the "**Bestchange Security Error**" email template is activated.

- **First Rate**: The rate of the first position among the five sources.  
- **Your Rate**: Your current rate.  
- **Min Security Rate**: The minimum rate considered safe based on our calculations.

![](<../../../.gitbook/assets/image (324).png>)

**Why Protection Was Introduced**

In the past, we encountered situations where Bestchange experienced sudden rate spikes due to changes in the rate format (e.g., from `1 to XXX` to `XXX to 1`). This protection was developed to monitor such anomalies.

**Protection Conditions**

This protection works effectively if you add small step values, such as `0.0001`. If you add larger values, such as `0.5%` or more, the rate will already be considered abnormal.
{% endhint %}

- **Select Currencies**: A list of available currencies from Bestchange for parsing (this list will only appear after entering a valid API key in the parser settings).

<figure><img src="../../../.gitbook/assets/image (420).png" alt="" width="395"><figcaption></figcaption></figure>

- **Select Cities**: A list of cities from Bestchange for parsing (this list will only appear after entering a valid API key in the parser settings).

<figure><img src="../../../.gitbook/assets/image (421).png" alt="" width="363"><figcaption></figcaption></figure>

---

### Parser Settings for Exchange Directions

In the admin panel, go to "**Exchange Directions**" -> "**Exchange Directions**" and edit the desired exchange direction.

On the "**Auto Rate Adjustment**" and "**Bestchange Parser**" tabs, disable any active auto rate adjustments before configuring the BestChange API Parser.

<div><figure><img src="../../../.gitbook/assets/image (423).png" alt="" width="359"><figcaption></figcaption></figure> <figure><img src="../../../.gitbook/assets/image (422).png" alt="" width="443"><figcaption></figcaption></figure></div>

On the "**BestChange API Parser**" tab, you will see the settings block. Configure the necessary options:

<figure><img src="../../../.gitbook/assets/image (424).png" alt="" width="563"><figcaption></figcaption></figure>

- **Enable Parser**:  
  - **Yes**: The parser is enabled for this exchange direction.  
  - **No**: The parser is not used.

{% hint style="warning" %}
To activate the parser, you must select two currencies in the "**Currencies (You Give)**" and "**Currencies (You Receive)**" fields.
{% endhint %}

- **Blacklist of Exchanger IDs (comma-separated)**: IDs of exchangers whose rates will be ignored during parsing.

- **Whitelist of Exchanger IDs (comma-separated)**: IDs of exchangers whose rates will be used during parsing. If at least one ID is specified, the parser will only use rates from these sources, ignoring all others.

{% hint style="warning" %}
If similar fields are filled in the general parser settings, they will be ignored for this exchange direction. Settings in the exchange direction take higher priority.

If the fields in the exchange direction settings are empty but the general settings are filled, the general settings will apply to the exchange direction.
{% endhint %}

- **City**: A list of cities selected in the general parser settings (used for cash exchange directions).

- **Currencies (You Give)**: Select the currency for the "**You Give**" side.

- **Currencies (You Receive)**: Select the currency for the "**You Receive**" side.

- **Rate Side**:  
  - **Auto**: Automatically selects the rate side for the values in the "**Min Rate**" and "**Max Rate**" fields.  
  - **1 = XXX**: Forces the rate to be set as `1 to XXX`.  
  - **XXX = 1**: Forces the rate to be set as `XXX to 1`.

- **Position**: The position in the Bestchange ranking for the selected exchange direction (if left empty, the 1st position is used).

- **Step**: Adjusts the rate obtained from the parser (e.g., `0.001`). By default, the system always makes your rate more favorable than the rate of the specified position. The step can also be set as a percentage (e.g., `3%`).

Here’s the text translated into naturalistic English:

---

The value of a step with the "**-**" sign will make your rate worse than the rate of the specified position (e.g., -0.001 or -3%). You can also use multiplication and division (\*2 or /2, \*3% or /3%).

**Min. Reserve for Position** — This is the minimum reserve value for the position (for the "**Receive**" currency). Exchangers with reserves below the specified value will be ignored by the module.

**Show Rating** — A page displaying currency rates from Bestchange along with the recommended step.

<figure><img src="../../../.gitbook/assets/image (1763).png" alt="" width="563"><figcaption></figcaption></figure>

**Min. Rate** — The lower limit of the rate at which the position will remain active. If a competitor for the specified position goes below the minimum rate, the module will reset your rate to the standard one (if the option is enabled).

{% hint style="warning" %}
If rates for one or all options ("**Minimum Rate**", "**Maximum Rate**", "**Standard Rate**") are specified both manually and through the "**Auto-Adjust Rate**" option,  
![](<../../../.gitbook/assets/image (1785).png>)  
then the rate from the "**Auto-Adjust Rate**" field will always take priority and will be used by the parser.
{% endhint %}

**Auto-Adjust Min. Rate** — Links the minimum rate to the selected source from the "**Parsers 2.0**" -> "**Rates**" section.  
&#xNAN;**• Add to Rate** — Adjusts the minimum rate obtained from the source (e.g., adding 3% or subtracting -3%).

**Max. Rate** — The upper limit of the rate at which the position will remain active. If a competitor for the specified position exceeds the maximum rate, the module will reset your rate to the standard one (if the option is enabled).

**Auto-Adjust Max. Rate** — Links the maximum rate to the selected source from the "**Parsers 2.0**" -> "**Rates**" section.  
&#xNAN;**• Add to Rate** — Adjusts the maximum rate obtained from the source (e.g., adding 3% or subtracting -3%).

**Reset to Standard Rate:**  
&#xNAN;**• Yes** — Enables the option to reset to the standard rate when the rate goes outside the min/max range.  
&#xNAN;**• No** — The option is not used.

**Standard Rate (Give)** — Manually specify the standard rate for the "**Give**" side.

**Standard Rate (Receive)** — Manually specify the standard rate for the "**Receive**" side.

**Auto-Adjust Rate** — Links the standard rate to the selected source from the "**Parsers 2.0**" -> "**Rates**" section.  
&#xNAN;**• Add to Rate (Give)** — Adjusts the maximum rate obtained from the source (e.g., adding 3% or subtracting -3%) for the "**Give**" side.  
&#xNAN;**• Add to Rate (Receive)** — Adjusts the maximum rate obtained from the source (e.g., adding 3% or subtracting -3%) for the "**Receive**" side.

**Convert Rate:**  
&#xNAN;**• Yes** — Forces the exchange rate to be converted into the format 1 to XXX.  
&#xNAN;**• No** — The option is not used.

--- 

Let me know if you need further clarification or adjustments!