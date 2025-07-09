# Currency Rates Parser (Parsers 2.0)

{% embed url="https://www.youtube.com/watch?v=KJieFpov2JE" %}

{% hint style="danger" %}
To enable automatic currency rate updates, you **must** create a [Cron job](https://premium.gitbook.io/rukovodstvo-polzovatelya/osnovnye-nastroiki/faq/kak-sozdat-zadanie-cron-na-servere) on your server using the link found in the "**Parsers 2.0**" — "**Settings**" section.

![](<../../../.gitbook/assets/image (1481).png>)
{% endhint %}

{% hint style="warning" %}
The hash for the Cron job URL is set in the file **`wp-content/plugins/premiumbox/userdata.php`**

![](<../../../.gitbook/assets/image (1520).png>)![](<../../../.gitbook/assets/image (1522).png>)
{% endhint %}

In the website control panel under the "**Parsers 2.0**" section, you will find a list of currency rate sources. You can link these sources to the exchange directions on your site, as well as see the last update time for the currency rates from each source.

## Parser Settings

<figure><img src="../../../.gitbook/assets/image (86).png" alt="" width="527"><figcaption></figcaption></figure>

* Sorting:  
  • **Manual** — manually sort courses according to the "**Parsers 2.0**" section ➔ "**Course Sorting**"  
  • **By name** — courses will be sorted automatically by their names  

* **Parser type:**  
  • **Multithreaded** — allows running multiple threads simultaneously, each processing a separate source  
  • **CURL** — can handle only one request at a time and may be simpler and more convenient for fetching small amounts of data  

* **Parsing logging:**  
  • **No** — course parsing from sources will not be logged  
  • **Yes** — all requests and responses from course sources will be logged  
  • **Errors only** — only errors encountered while fetching courses will be logged  

* **Timeout (seconds):** — the amount of time the site waits for a response from an external service. If no response is received within this time, the site will continue working without it. If no value is set or it is 0, the default timeout of 20 seconds applies. There is no universal timeout value since it depends on the speed of the specific service.  

* **Last updated:** — date and time of the parser’s most recent update  

* **Delete old data:** — whether to delete old courses before running the parser:  
  • **No**  
  • **Yes**  

* **Course sources:** — all available sources for parsing courses  

{% hint style="info" %}
If needed, you can parse your own currency rates file or an XML file from another exchanger to use those rates in other formulas.  
To do this, open the "**Parsers 2.0**" section ➔ "**Add Site**" and enter the link to your XML rates file in the "**XML file URL**" field in the new window.  
![](<../../../.gitbook/assets/image (851).png>)  
Then, check the box next to the added source.  
{% endhint %}

To activate the parser, go to the "**Parsers 2.0 → Settings**" section and check the boxes next to the sources you want to use. Then, start the Cron task from the same page.

{% endhint %}

If the currency rates update successfully, you will see the word "**Completed**" on the page that opens.

If this does not happen or you see a different message, check the [**Parser Logs** section](https://premium.gitbook.io/rukovodstvo-polzovatelya/navigaciya/nastroiki/logirovanie/logi-parserov-2.0) (make sure "**Parsing Logging**" is enabled in the general settings) and review the logs generated.

{% hint style="warning" %}
If currency rates are not updating from one or more sources, or if the parser doesn’t work at all, verify that your server’s IP address has access to the data source.

If you use ISP Manager, open the "**Shell Client**" section.

![](<../../../.gitbook/assets/image (668).png>)

In the window that opens, enter the command:  
`curl [parsing URL]`

For example, to check the currency parsing from Garantex:

![](<../../../.gitbook/assets/image (669).png>)

If the response shows currency rates, the source is accessible from your server. ![](<../../../.gitbook/assets/image (671).png>)
{% endhint %}

{% hint style="info" %}
To receive prompt notifications about parser errors so you can fix them quickly, you can set up alerts via [email](https://premium.gitbook.io/rukovodstvo-polzovatelya/osnovnye-nastroiki/uvedomleniya-administratoram-i-polzovatelyam/uvedomleniya-po-e-mail) and [Telegram](https://premium.gitbook.io/rukovodstvo-polzovatelya/osnovnye-nastroiki/uvedomleniya-administratoram-i-polzovatelyam/uvedomleniya-v-telegram).

![](<../../../.gitbook/assets/image (1434).png>)![](<../../../.gitbook/assets/image (1435).png>)
{% endhint %}

## Source Rates

This section displays all currency rates retrieved from the sources. You can use the shortcodes shown in the "**Code**" column to create complex rates in the "**Rates**" section.

<figure><img src="../../../.gitbook/assets/image (206).png" alt=""><figcaption></figcaption></figure>

To easily find specific data, you can use the filter with up to three conditions:

<figure><img src="../../../.gitbook/assets/image (1118).png" alt=""><figcaption></figcaption></figure>

Here is a natural, fluent English translation of the provided text:

---

* **Source** — show exchange rates only from the selected source  
* **Currency I Give** — show only pairs where the "**I Give**" currency matches the currency specified in this field  
* **Currency I Receive** — show only pairs where the "**I Receive**" currency matches the currency specified in this field  

## Exchange Rates

{% hint style="warning" %}
To use exchange rates in your exchange directions, it is **necessary** to transfer the selected rates from the "**Parsers 2.0**" ➔ "**Source Rates**" section into this "**Exchange Rates**" section.

Only after transferring the rates will they become available for selection on the "**Auto Rate Adjustment**" tab in the exchange direction settings, as well as for automatic rate adjustments in the Bestchange parser.
{% endhint %}

In this section, you can also create new currency pairs. Use the default pairs as examples.

You can combine rates from the "Source Rates" section, use decimal fractions in formulas, and apply mathematical operations such as:  
• multiplication — `[cbr_usdrub] * [bitfinex_bchusd_last_price]`  
• division — `1 / [exmo_bchbtc_last_trade]`  
• subtraction — `[ecb_eurrub] - [cbr_eurrub]`  
• addition — `[index_support] + 2`

Clicking the "**Copy**" button will create a duplicate of the currency on the row where the button was clicked.

{% hint style="info" %}
If any rate in the "**Rate for I Give**" or "**Rate for I Receive**" column shows 0, it means the shortcode used in the "**Rate Formula for I Give**" or "**Rate Formula for I Receive**" fields is invalid — please replace it.
{% endhint %}

<figure><img src="../../../.gitbook/assets/image (207).png" alt=""><figcaption></figcaption></figure>

{% hint style="warning" %}
If the required rate is not available in the "**Parsers 2.0**" ➔ "**Source Rates**" section, transfer the inverse rate to the "**Exchange Rates**" section and use the formula **`1/[currency_rate]`** — this will give you the desired rate.
{% endhint %}

{% hint style="success" %}
## "Converter" Module

To quickly transfer rates from a specific source in the "**Rate Sources**" section to the "**Exchange Rates**" section, you can use the "**Converter**" module.

<img src="../../../.gitbook/assets/image (405).png" alt="" data-size="original">

---

If you need the text adapted for a particular audience or style, just let me know!

Select the currency rate source from the dropdown menu, then enter the [currency codes](https://www.bestchange.ru/wiki/rates.html) separated by commas in the "**Currencies**" field for which you want to create currency pairs, and click "**Apply**."

![](<../../../.gitbook/assets/image (406).png>)&#x20;

In the "**Rates**" section, pairs will be created where the listed currencies will appear on the "**Giving**" side.

![](<../../../.gitbook/assets/image (407).png>)

To create all available rates involving the listed currencies, check the "**Reverse rate**" box before clicking "**Apply**."

![](<../../../.gitbook/assets/image (408).png>)

Repeat these steps for each source whose rates you want to use.
{% endhint %}

## Custom Coefficients

<figure><img src="../../../.gitbook/assets/image (1231).png" alt=""><figcaption></figcaption></figure>

In this section, you can add coefficients that can also be used in formulas within the "**Rates**" section. This feature is useful for those who work with variable coefficients across multiple directions — instead of entering a fixed value, you can use a shortcode created here in your formulas and change its value without having to edit the "**Rates**" section directly.

Starting from version 2.7, the custom coefficients settings have been moved to a separate section.

<figure><img src="../../../.gitbook/assets/image (1971).png" alt=""><figcaption><p>Sidebar section</p></figcaption></figure>

<figure><img src="../../../.gitbook/assets/image (1972).png" alt="" width="449"><figcaption><p>Coefficient settings</p></figcaption></figure>

**Index Name** — the desired name to be used as a shortcode in formulas  
**Value Formula** — enter a number or a mathematical formula here  
**Index Value** — the value used in the formula above (if a formula is specified)  
**Index Type:**  
• Formula substitution in rate

<figure><img src="../../../.gitbook/assets/image (1974).png" alt=""><figcaption><p>The formula will be inserted directly into the rate without parentheses, and then the rate value will be calculated</p></figcaption></figure>

• Index value

<figure><img src="../../../.gitbook/assets/image (1973).png" alt=""><figcaption><p>The coefficient value will be calculated first, then inserted into the rate</p></figcaption></figure>

**Comment** — a field for your notes

## Websites (XML file parsing)

You can parse open XML files from other exchangers if you know their URL (often it’s `https://domain/request-exportxml.xml`). To use this feature, enable the "**Parsing XML Files with Exchanger Rates**" module in the "**Modules**" section.

<figure><img src="../../../.gitbook/assets/image (596).png" alt=""><figcaption></figcaption></figure>

Next, add a new source in the "**Parsers 2.0**" ➔ "**Add Site**" section. In the window that opens, enter a name for the source (as you prefer) and provide the link to the rates XML file.

<figure><img src="../../../.gitbook/assets/image (598).png" alt="" width="477"><figcaption></figcaption></figure>

After saving the source, go to "**Parsers 2.0**" ➔ "**Settings**" and activate the source you just added.

<figure><img src="../../../.gitbook/assets/image (599).png" alt="" width="435"><figcaption></figcaption></figure>

Once activated, the data from this source will appear in "**Parsers 2.0**" ➔ "**Source Rates**."

<figure><img src="../../../.gitbook/assets/image (600).png" alt=""><figcaption></figcaption></figure>

## Automatic Rate Updates

To enable automatic rate updates, you need to set up a [task scheduler (cron) on your server](https://premium.gitbook.io/main/osnovnye-nastroiki/faq/kak-sozdat-zadanie-cron-na-servere). At the top of the "**Parsers 2.0**" ➔ "**Settings**" page, you’ll find a link labeled "**Cron URL for updating Central Bank and cryptocurrency rates**." Add this URL to your server’s cron scheduler to automate updates.