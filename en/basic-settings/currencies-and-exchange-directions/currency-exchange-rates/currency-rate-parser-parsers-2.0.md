# Currency Rate Parser (Parsers 2.0)

{% embed url="https://www.youtube.com/watch?v=KJieFpov2JE" %}

{% hint style="danger" %}
To automatically update currency rates, **make sure to create a** [**Cron job**](https://premium.gitbook.io/main/en/basic-settings/faq/kak-sozdat-zadanie-cron-na-servere) on your server using the link from the "**Parsers 2.0**" section — "**Settings**"

<img src="../../../.gitbook/assets/image (1481)_eng.png" alt="" data-size="original">
{% endhint %}

{% hint style="warning" %}
The hash for the Cron job link is specified in the **`wp-content/plugins/premiumbox/userdata.php`** file.

<img src="../../../.gitbook/assets/image (1520)_eng.png" alt="" data-size="original"><img src="../../../.gitbook/assets/image (1522)_eng.png" alt="" data-size="original">
{% endhint %}

In the website control panel under the "**Parsers 2.0**" section, you will find a list of currency rate sources that can be linked to the exchange rate on the site, as well as the last update time for the rates from these sources.

## Parser Settings

<figure><img src="../../../.gitbook/assets/image%20(86)_eng.png" alt="" width="527"><figcaption></figcaption></figure>

* Sorting:\
  • **Manually** — manually sort rates according to the "**Parsers 2.0**" ➔ "**Sort Rates**" section\
  • **By Name** — rates will be automatically sorted by name
* **Parser Type**:\
  • **Multithreaded** — allows multiple execution threads, each processing a separate source\
  • **CURL** — can retrieve data from only one request at a time and may be more convenient and simpler for obtaining a small amount of data
* **Parsing Logging**:\
  • **No** — parsing rates from sources will not be logged\
  • **Yes** — all requests and responses from currency sources will be logged\
  • **Errors Only** — only errors in retrieving rates will be logged
* **Timeout (sec.)** — this is the time the site waits for a response from an external service. If a response is not received within the specified time, the site will continue its operation without an answer. If the time is not set or is equal to 0, the default timeout of 20 seconds applies. There is no universal timeout value, as it depends on the speed of the specific service.
* **Last Update Date** — date and time of the last parser update
* **Delete Old Data** — delete old rates before running the parser:\
  • **No**\
  • **Yes**
* **Rate Sources** — all available sources for parsing rates

{% hint style="info" %}
If needed, you can parse your own currency rates file or an XML file from another exchange to use these rates in other formulas.\
To do this, go to the "**Parsers 2.0**" ➔ "**Add Site**" section and in the new window, specify the link to your XML file with rates in the "**XML File Address**" field.\
![](<../../../.gitbook/assets/image (851)_eng.png>)\
After that, check the box next to the added source.

![](../../../.gitbook/assets/image%20\(205\)_eng.png)\
To activate the parser, go to the "**Parsers 2.0" → "Settings"** section and check the boxes next to the names of the sources you want to use. After that, run the Cron job from the same page.
{% endhint %}

Upon successful update of the currency rates, you will see the word "**Completed**" on the opened page.

If this does not happen or a different message is displayed, check the [**Parser Logs**](https://premium.gitbook.io/main/en/navigaciya/nastroiki/logirovanie/logi-parserov-2.0) (the "**Parsing Logging**" option in the general settings must be enabled beforehand) and read the logs received.

{% hint style="warning" %}
If rates are not updating for one or more sources, or if the parser is not working initially, check access to the data source from your server's IP address.

If you are using ISP Manager — go to the "**Shell Client**" section.

<img src="../../../.gitbook/assets/image (668)_eng.png" alt="" data-size="original">

In the opened window, enter the command "`curl link for parsing`".

For example, let's check the parsing of rates from Garantex:

<img src="../../../.gitbook/assets/image (669)_eng.png" alt="" data-size="original">

If the response shows currency rates, then the source is accessible from your server. ![](<../../../.gitbook/assets/image (671)_eng.png>)
{% endhint %}

{% hint style="info" %}
To quickly receive notifications about parsing errors for currency rates, you can set up notifications via [email](https://premium.gitbook.io/main/en/basic-settings/uvedomleniya-administratoram-i-polzovatelyam/uvedomleniya-po-e-mail) and in [Telegram](https://premium.gitbook.io/main/en/basic-settings/uvedomleniya-administratoram-i-polzovatelyam/uvedomleniya-v-telegram).

<img src="../../../.gitbook/assets/image (1434)_eng.png" alt="" data-size="original"><img src="../../../.gitbook/assets/image (1435)_eng.png" alt="" data-size="original">
{% endhint %}

## Source Rates

This section will display all currency rates obtained from sources. You can use the displayed shortcodes from the "**Code**" column to create complex rates in the "**Rates**" section.

<figure><img src="../../../.gitbook/assets/image%20(206)_eng.png" alt=""><figcaption></figcaption></figure>

For easier searching of specific data, you can use filters based on 3 conditions:

<figure><img src="../../../.gitbook/assets/image (1118)_eng.png" alt=""><figcaption></figcaption></figure>

* **Source** — display currency rates only from the selected source
* **Currency I Give** — display only pairs where the currency in "**I Give**" is the one specified in the field
* **Currency I Receive** — display only pairs where the currency in "**I Receive**" is the one specified in the field

## Rates

{% hint style="warning" %}
To use rates in exchange directions, it is **necessary** to transfer the selected rates from the "**Parsers 2.0**" ➔ "**Source Rates**" section to this section.

Only after transferring the rates will they become available for selection in the "**Auto-Correction of Rate**" tab in the exchange direction settings, as well as for auto-correction of rates in the Bestchange parser.
{% endhint %}

In this section, you can also create new currency pairs. Use the default pairs as examples.

You can combine rates from the "Source Rates" section, use decimal fractions in formulas, and perform mathematical operations:\
• multiplication — `[cbr_usdrub] * [bitfinex_bchusd_last_price]`\
• division — `1 / [exmo_bchbtc_last_trade]`\
• subtraction — `[ecb_eurrub] - [cbr_eurrub]`\
• addition — `[index_support] + 2`

Clicking the "**Copy**" button will create a copy of the currency in the row where the button was clicked.

{% hint style="info" %}
If any rate in the "**Rate for Giving**" or "**Rate for Receiving**" column shows 0, it means that the shortcode used in the "**Rate Formula for Giving**" or "**Rate Formula for Receiving**" fields is invalid — replace it.
{% endhint %}

<figure><img src="../../../.gitbook/assets/image%20(207)_eng.png" alt=""><figcaption></figcaption></figure>

{% hint style="warning" %}
If the desired rate is not available in the "**Parsers 2.0**" ➔ "**Source Rates**" section, transfer the reverse rate to the "**Rates**" section and use the formula **`1/[currency_rate]`** — in this case, you will obtain the required rate.
{% endhint %}

{% hint style="success" %}
#### Converter Module

To quickly transfer rates from a specific source in the "**Rate Sources**" section to the "**Rates**" section, you can use the "**Converter**" module.

<img src="../../../.gitbook/assets/image%20(405)_eng.png" alt="" data-size="original">

Select the currency rate source from the dropdown list, and in the "**Currencies**" field, specify the [currency codes](https://www.bestchange.ru/wiki/rates.html) you want to create currency pairs for, separated by commas, and click "**Apply**".

<img src="../../../.gitbook/assets/image%20(406)_eng.png" alt="" data-size="original">

In the "**Rates**" section, pairs will be created where the listed currencies will be on the "**Giving**" side.

<img src="../../../.gitbook/assets/image%20(407)_eng.png" alt="" data-size="original">

To create all available rates with the listed currencies, check the "**Reverse Rate**" box before clicking "**Apply**".

<img src="../../../.gitbook/assets/image%20(408)_eng.png" alt="" data-size="original">

Repeat the steps for each source whose rates you want to use.
{% endhint %}

## Custom Coefficients

<figure><img src="../../../.gitbook/assets/image (1231)_eng.png" alt=""><figcaption></figcaption></figure>

In this section, you can add coefficients that can also be applied in formulas in the "**Rates**" section. This option will be useful for those who use floating coefficients in multiple directions — instead of specifying a specific value, you can use the created shortcode in formulas and change its value without needing to edit the "**Rates**" section.

Starting from version 2.7, the custom coefficients setting has been moved to a separate section.

<figure><img src="../../../.gitbook/assets/image (1971)_eng.png" alt=""><figcaption><p>Section in the sidebar</p></figcaption></figure>

<figure><img src="../../../.gitbook/assets/image (1972)_eng.png" alt="" width="449"><figcaption><p>Coefficient Settings</p></figcaption></figure>

Index Name — the desired name that will be used in formulas as a shortcode\
Value Formula — the field where a number or mathematical formula is specified\
Index Value — the value for the formula specified above (if a formula is provided)\
Index Type:\
• Formula substitution in the rate

<figure><img src="../../../.gitbook/assets/image (1974)_eng.png" alt=""><figcaption><p>The formula will be inserted directly into the exchange rate without parentheses, and then the exchange rate value will be calculated.</p></figcaption></figure>

• Index Value

<figure><img src="../../../.gitbook/assets/image (1973)_eng.png" alt=""><figcaption><p>First, the coefficient value will be calculated, and then it will be used in the exchange rate.</p></figcaption></figure>

Comment — a space for your notes

## Websites (Parsing XML Files)

You can parse open XML files from other exchanges if you know their URL (often it is `https://domain/request-exportxml.xml`). To use this option, activate the module "**Parsing XML Files with Exchange Rates**" in the "**Modules**" section.

<figure><img src="../../../.gitbook/assets/image (596)_eng.png" alt=""><figcaption></figcaption></figure>

After that, add a new source in the "**Parsers 2.0**" ➔ "**Add Site**" section. In the window that opens, specify a name for the source of your choice and the link to the file with the exchange rates.

<figure><img src="../../../.gitbook/assets/image (598)_eng.png" alt="" width="477"><figcaption></figcaption></figure>

Once you save the source, go to the "**Parsers 2.0**" ➔ "**Settings**" section and activate the newly added source.

<figure><img src="../../../.gitbook/assets/image (599)_eng.png" alt="" width="435"><figcaption></figcaption></figure>

After that, the data from the source will appear in the "**Parsers 2.0**" ➔ "**Source Rates**" section.

<figure><img src="../../../.gitbook/assets/image (600)_eng.png" alt=""><figcaption></figcaption></figure>

## Automatic Rate Updates

To automatically update the rates, you need to set up a [cron job on the server](https://premium.gitbook.io/main/en/basic-settings/faq/kak-sozdat-zadanie-cron-na-servere). In the "**Parsers 2.0**" ➔ "**Settings**" section, at the top of the page, there is a link labeled "**Cron URL for Updating Central Bank and Cryptocurrency Rates**," which you need to add to the cron job scheduler on the server.
