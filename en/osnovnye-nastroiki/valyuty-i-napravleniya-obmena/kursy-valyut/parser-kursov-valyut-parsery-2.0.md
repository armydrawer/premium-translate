# Currency Rates Parser (Parsers 2.0)

{% embed url="https://www.youtube.com/watch?v=KJieFpov2JE" %}

{% hint style="danger" %}
To enable automatic currency rate updates, it is **mandatory** to create a [Cron job](https://premium.gitbook.io/rukovodstvo-polzovatelya/osnovnye-nastroiki/faq/kak-sozdat-zadanie-cron-na-servere) on your server using the link provided in the "**Parsers 2.0**" ➔ "**Settings**" section.

![](<../../../.gitbook/assets/image (1481).png>)
{% endhint %}

{% hint style="warning" %}
The hash for the Cron job link is set in the **`wp-content/plugins/premiumbox/userdata.php`** file.

![](<../../../.gitbook/assets/image (1520).png>)![](<../../../.gitbook/assets/image (1522).png>)
{% endhint %}

In the website's admin panel, under the "**Parsers 2.0**" section, you will find a list of currency rate sources. These sources can be linked to the exchange rate directions on your site, and the time of the last rate update from these sources is also displayed.

## Parser Settings

<figure><img src="../../../.gitbook/assets/image (86).png" alt="" width="527"><figcaption></figcaption></figure>

* **Sorting**:  
  • **Manually** — manually sort rates via the "**Parsers 2.0**" ➔ "**Rate Sorting**" section.  
  • **By Name** — rates will be automatically sorted alphabetically.  
* **Parser Type**:  
  • **Multithreaded** — allows multiple threads to run simultaneously, each processing a separate source.  
  • **CURL** — processes one request at a time, making it simpler and more suitable for retrieving smaller amounts of data.  
* **Parsing Logs**:  
  • **No** — parsing requests and responses will not be logged.  
  • **Yes** — all requests and responses from rate sources will be logged.  
  • **Errors Only** — only errors during rate retrieval will be logged.  
* **Timeout (sec.)** — the time the site waits for a response from an external service. If no response is received within the specified time, the site will continue operating without the data. If left blank or set to 0, the default timeout of 20 seconds will apply. The optimal timeout depends on the speed of the specific service.  
* **Update Date** — the date and time of the parser's last update.  
* **Delete Old Data** — remove old rates before running the parser:  
  • **No**  
  • **Yes**  
* **Rate Sources** — all available sources for parsing currency rates.  

{% hint style="info" %}
If needed, you can parse your own currency rate file or an XML file from another exchange service to use those rates in formulas.  
To do this, go to "**Parsers 2.0**" ➔ "**Add Site**" and enter the link to your XML file in the "**XML File Address**" field in the new window.  
![](<../../../.gitbook/assets/image (851).png>)  
Afterward, check the box next to the added source.  

![](<../../../.gitbook/assets/image (205).png>)  
To activate the parser, go to "**Parsers 2.0**" ➔ "**Settings**" and check the box next to the source you want to use. Then, run the Cron job from the same page.  
{% endhint %}

If the currency rates are successfully updated, you will see the word "**Completed**" on the resulting page.

If this does not happen or another message appears, check the [**Parser Logs**](https://premium.gitbook.io/rukovodstvo-polzovatelya/navigaciya/nastroiki/logirovanie/logi-parserov-2.0) section (ensure the "**Parsing Logs**" option is enabled in the general settings) and review the logs.

{% hint style="warning" %}
If currency rates are not updating for one or more sources, or the parser is not working at all, check the data source's accessibility from your server's IP address.

If you're using ISP Manager, go to the "**Shell Client**" section.

![](<../../../.gitbook/assets/image (668).png>)

In the opened window, enter the command "`curl parsing_link`".

For example, let's check the rates from Garantex:

![](<../../../.gitbook/assets/image (669).png>)

If the response displays currency rates, the source is accessible from your server.  
![](<../../../.gitbook/assets/image (671).png>)
{% endhint %}

{% hint style="info" %}
To quickly address parsing errors, you can set up notifications for errors via [email](https://premium.gitbook.io/rukovodstvo-polzovatelya/osnovnye-nastroiki/uvedomleniya-administratoram-i-polzovatelyam/uvedomleniya-po-e-mail) or [Telegram](https://premium.gitbook.io/rukovodstvo-polzovatelya/osnovnye-nastroiki/uvedomleniya-administratoram-i-polzovatelyam/uvedomleniya-v-telegram).

![](<../../../.gitbook/assets/image (1434).png>)![](<../../../.gitbook/assets/image (1435).png>)
{% endhint %}

## Source Rates

This section displays all currency rates retrieved from sources. You can use the shortcodes from the "**Code**" column to create complex rates in the "**Rates**" section.

<figure><img src="../../../.gitbook/assets/image (206).png" alt=""><figcaption></figcaption></figure>

For easier data searching, you can use the filter with three conditions:

<figure><img src="../../../.gitbook/assets/image (1118).png" alt=""><figcaption></figcaption></figure>

* **Source** — display rates only from the selected source.  
* **Currency I Give** — display only pairs where the specified currency is used in the "**I Give**" field.  
* **Currency I Receive** — display only pairs where the specified currency is used in the "**I Receive**" field.  

## Rates

{% hint style="warning" %}
To use rates in exchange directions, you **must** transfer the selected rates from the "**Parsers 2.0**" ➔ "**Source Rates**" section to this section.

Only after transferring the rates will they become available for selection in the "**Auto Rate Adjustment**" tab in the exchange direction settings, as well as for auto-adjusting rates in the Bestchange parser.
{% endhint %}

In this section, you can also create new rate pairs. Use the default pairs as examples.

You can combine rates from the "**Source Rates**" section, use decimal fractions in formulas, and apply mathematical operations:  
• Multiplication — `[cbr_usdrub] * [bitfinex_bchusd_last_price]`  
• Division — `1 / [exmo_bchbtc_last_trade]`  
• Subtraction — `[ecb_eurrub] - [cbr_eurrub]`  
• Addition — `[index_support] + 2`  

Clicking the "**Copy**" button will create a duplicate of the currency on the row where the button was clicked.

{% hint style="info" %}
If a rate shows 0 in the "**Rate for I Give**" or "**Rate for I Receive**" column, it means the shortcode used in the "**Rate Formula for I Give**" or "**Rate Formula for I Receive**" field is invalid — replace it.
{% endhint %}

<figure><img src="../../../.gitbook/assets/image (207).png" alt=""><figcaption></figcaption></figure>

{% hint style="warning" %}
If the required rate is not available in the "**Parsers 2.0**" ➔ "**Source Rates**" section, transfer the reverse rate to the "**Rates**" section and use the formula **`1/[currency_rate]`** to calculate the desired rate.
{% endhint %}

{% hint style="success" %}
## Converter Module

To quickly transfer rates from a specific source in the "**Source Rates**" section to the "**Rates**" section, you can use the "**Converter**" module.

<img src="../../../.gitbook/assets/image (405).png" alt="" data-size="original">

Select the currency rate source from the dropdown menu, and in the "**Currencies**" field, list the [currency codes](https://www.bestchange.ru/wiki/rates.html) separated by commas for which you want to create rate pairs. Then click "**Apply**."

![](<../../../.gitbook/assets/image (406).png>)  

In the "**Rates**" section, pairs will be created where the listed currencies will appear on the "**I Give**" side.

![](<../../../.gitbook/assets/image (407).png>)

To create all available rates with the listed currencies, check the "**Reverse Rate**" box before clicking "**Apply**."

![](<../../../.gitbook/assets/image (408).png>)

Repeat these steps for each source whose rates you want to use.
{% endhint %}

## Custom Coefficients

<figure><img src="../../../.gitbook/assets/image (1231).png" alt=""><figcaption></figcaption></figure>

In this section, you can add coefficients that can also be used in formulas in the "**Rates**" section. This feature is useful for those who use floating coefficients across multiple directions — instead of specifying a specific value, you can use a shortcode in formulas and update its value without editing the "**Rates**" section.

Starting from version 2.7, custom coefficient settings have been moved to a separate section.

<figure><img src="../../../.gitbook/assets/image (1971).png" alt=""><figcaption><p>Sidebar Section</p></figcaption></figure>

<figure><img src="../../../.gitbook/assets/image (1972).png" alt="" width="449"><figcaption><p>Coefficient Settings</p></figcaption></figure>

**Index Name** — the desired name to be used as a shortcode in formulas.  
**Value Formula** — enter a number or mathematical formula in this field.  
**Index Value** — the value for the formula specified above (if a formula is provided).  
**Index Type**:  
• Formula substitution in the rate.  

Here’s the text translated into naturalistic English:

---

<figure><img src="../../../.gitbook/assets/image (1974).png" alt=""><figcaption><p>The formula will be directly substituted into the rate without brackets, and then the rate value will be calculated.</p></figcaption></figure>

• Index Value

<figure><img src="../../../.gitbook/assets/image (1973).png" alt=""><figcaption><p>First, the coefficient value will be calculated, and then it will be substituted into the rate.</p></figcaption></figure>

**Comment** — A field for your notes.

## Websites (Parsing XML Files)

You can parse open XML files from other exchange services if you know their URL (this is often something like `https://domain/request-exportxml.xml`). To use this feature, activate the "**Parsing XML Files from Exchange Services**" module in the "**Modules**" section.

<figure><img src="../../../.gitbook/assets/image (596).png" alt=""><figcaption></figcaption></figure>

After that, add a new source in the "**Parsers 2.0**" section ➔ "**Add Website**". In the window that opens, specify a name for the source (you can choose any name) and provide the link to the file with the rates.

<figure><img src="../../../.gitbook/assets/image (598).png" alt="" width="477"><figcaption></figcaption></figure>

Once the source is saved, go to the "**Parsers 2.0**" section ➔ "**Settings**" and activate the added source.&#x20;

<figure><img src="../../../.gitbook/assets/image (599).png" alt="" width="435"><figcaption></figcaption></figure>

After this, the data from the source will appear in the "**Parsers 2.0**" section ➔ "**Source Rates**".&#x20;

<figure><img src="../../../.gitbook/assets/image (600).png" alt=""><figcaption></figcaption></figure>

## Automatic Rate Updates

To enable automatic rate updates, you need to configure a [cron job on your server](https://premium.gitbook.io/main/osnovnye-nastroiki/faq/kak-sozdat-zadanie-cron-na-servere). In the "**Parsers 2.0**" ➔ "**Settings**" section, at the top of the page, you’ll find a link labeled "**Cron URL for Updating Central Bank and Cryptocurrency Rates**". This link needs to be added to the cron job scheduler on your server.

--- 

Let me know if you need further assistance!