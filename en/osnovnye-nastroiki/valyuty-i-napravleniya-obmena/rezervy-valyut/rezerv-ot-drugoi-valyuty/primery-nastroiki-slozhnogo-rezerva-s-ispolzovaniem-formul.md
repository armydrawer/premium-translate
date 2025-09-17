# Examples of Configuring Complex Reserves Using Formulas

## Reserve Formulas <a href="#delaem_y_valyut_odinakovii_rezerv_rezerv" id="delaem_y_valyut_odinakovii_rezerv_rezerv"></a>

Using shortcodes, you can configure a shared reserve for multiple currencies, convert reserves into other currencies (e.g., from USD to BTC), and much more.

Go to **"Modules" → "Modules"** and enable the **"Reserve Formula"** module if it is currently disabled.

### List of Available Shortcodes <a href="#spisok-dostupnykh-shortkodov" id="spisok-dostupnykh-shortkodov"></a>

* **corresXX** — the sum of reserve adjustments for a currency.
* **excursum\_giveXX** — the total reserve of requests for the "**Give**" currency.
* **excursum\_getXX** — the total reserve of requests for the "**Receive**" currency.
* **excursum\_autoXX** — the total reserve of requests for the "**Receive**" currency with statuses specified in the "**Exchange Settings**" → "**Reserve Settings**" section.
* **cfilereserve\_ZZ** — the reserve value for currency from line ZZ in the parsing reserve file.
* **dfilereserve\_ZZ** — the reserve value for exchange direction from line ZZ in the parsing reserve file.
* **payoutsXX** — the total partner payouts for a currency.

{% hint style="warning" %}
If the partner program for an exchange direction is disabled, the **payoutsXX** parameter will return zero values.
{% endhint %}

* **\[parser\_binance\_btcusdt]** — the rate from the "**Parsers 2.0**" → "**Source Rates**" section.\
  In this section, the shortcode appears as **\[binance\_btcusdt]**, but when used in a reserve formula, you must add the **parser\_** prefix, making it **\[parser\_binance\_btcusdt]**.\
  The same rule applies to shortcodes for custom coefficients.

**XX** — the currency ID, which is displayed in the site's admin panel under the "**Currencies**" section. You can specify multiple IDs separated by commas.

**ZZ** — the line number in the parsing reserve file. You can specify multiple IDs separated by commas.

<figure><img src="https://2722984412-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2Fm9kqZXsNykrN6VyxxXBO%2Fuploads%2FLcRDZqj1mr6KF7T7g2M1%2FScreenshot_27.png?alt=media&#x26;token=840d5521-2a75-4cc0-b5d3-2d9fc7809ef7" alt="" width="375"><figcaption></figcaption></figure>

## Example: Linking the Reserve of One Currency to Another

Let’s look at an example of how to link the reserve of the "Monobank" currency to the reserve of "Privat24."

1. In the admin panel, under the "**Currencies**" section, find the IDs for "Privat24" (ID 5) and "Monobank" (ID 47):

<figure><img src="https://2722984412-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2Fm9kqZXsNykrN6VyxxXBO%2Fuploads%2F2vxayvvjfY0XlJIFOwB3%2FScreenshot_28.png?alt=media&#x26;token=69d1cfad-a304-4349-acfa-93a4c0b39d73" alt="" width="563"><figcaption></figcaption></figure>

2. Edit the settings for both "Privat24" and "Monobank." In the settings for both currencies, select the "**By Formula**" option for the "**Currency Reserve**" parameter.
3. In the "**Reserve Formula**" field that appears below, enter the following formula for both currencies:

<figure><img src="https://2722984412-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2Fm9kqZXsNykrN6VyxxXBO%2Fuploads%2FEKbpy716s588HTtlzvOk%2FScreenshot_29.png?alt=media&#x26;token=bbe3df74-35bc-4820-8b1a-3a7c49d7c385" alt="" width="563"><figcaption></figcaption></figure>

Let’s make the example more complex: link the reserves of "Monobank" (ID 47) and "Oschadbank" (ID 23) to the reserve of "Privat24" (ID 5). For all three currencies, use the following formula:

<figure><img src="https://2722984412-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2Fm9kqZXsNykrN6VyxxXBO%2Fuploads%2FtfZYh5QcT3fhuHOTJnrF%2FScreenshot_30.png?alt=media&#x26;token=e4febef0-7543-44b0-aa1d-bdc582cc58e7" alt=""><figcaption></figcaption></figure>

4. In the admin panel, under "**Modules**" → "**Modules**," activate the "**Currency Reserve Update Link (via Cron)**" module if it is disabled. In the "**Currencies**" section, a "**Link**" button will appear for "Monobank," "Oschadbank," and "Privat24." Click this button for each currency and copy the URL of the page that opens.

<figure><img src="https://2722984412-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2Fm9kqZXsNykrN6VyxxXBO%2Fuploads%2FerCRVhx6m7YcC6jSdX7K%2FScreenshot_31.png?alt=""><figcaption></figcaption></figure>

5. Add each copied link to the task scheduler (cron) on your server. The link can be executed every minute. Here’s an example of a Unix-format cron command for the ISP Manager control panel:

<figure><img src="https://2722984412-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2Fm9kqZXsNykrN6VyxxXBO%2Fuploads%2FhAiLwEeIOhzl291Y42mm%2FScreenshot_32.png?alt=media&#x26;token=8b91ff1d-777e-4d4d-ac8d-8a6d5fa3829c" alt=""><figcaption></figcaption></figure>

Here, **XX** is the currency ID.

{% hint style="info" %}
The exact command may vary depending on your server. The part of the command `/usr/bin/wget -t 1 -O —` might need to be adjusted. Contact your hosting provider’s technical support for the correct command.
{% endhint %}

<figure><img src="../../../../.gitbook/assets/image (778).png" alt="" width="375"><figcaption></figcaption></figure>

## Example: Unified Reserve for Multiple Currencies (Using Reserves Calculated from Requests)

Suppose we have 4 currencies with IDs **5, 42, 47, 61**. Our goal is to make their reserves identical.

First, decide which currency will be the primary one. In this case, let’s choose the currency with **ID 47.**

The formula will be as follows:

**\[sum of reserve adjustments for currencies with IDs 5,42,47,61]** + **\[sum of "give for reserve" from requests where the "give" currency has IDs 5,42,47,61]** (i.e., what the site received from requests) - **\[sum of "receive for reserve" from requests where the "receive" currency has IDs 5,42,47,61]** (i.e., what the site gave out via requests) - **\[partner payouts for currencies with IDs 5,42,47,61]**

For the primary currency (**ID 47**), the formula will be:

**\[corres5,42,47,61] + \[excursum\_give5,42,47,61] – \[excursum\_get5,42,47,61] – \[payouts5,42,47,61]**

This formula will calculate the correct value. However, the reserve only updates when actions occur with the currency.

To ensure that the reserve value for the primary currency (**ID 47**) is also applied to the other currencies, enter the following in the "**Link Reserve to Currency ID**" field:

**5,42,61**

Now, whenever actions occur with currency **ID 47**, the following will happen:

* The reserve will be calculated using the formula.
* The formula’s result will be applied to the linked currencies.

This setup works well, but what happens when actions occur with other currencies? How do we update the reserve for the primary currency (**ID 47**)?

For this, configure each currency as follows:

Set "**Currency Reserve**" to use the "**Reserve Field**" option. This saves server resources by avoiding unnecessary calculations (since the value will be overwritten anyway).

In the "**Link Reserve to Currency ID**" field, enter:

**rc47**

This ensures that whenever actions occur with any of the currencies:

* The reserve value from the field is used and applied to the currency.
* The reserve for currency **ID 47** is updated using the formula.
* The linked settings for currency **ID 47** propagate the updated reserve value to all linked currencies.

In the "**Link reserve to currency reserve ID**" field, enter the following value:

**rc47**

This ensures that when working with our currencies, the following will occur:

* The value from the field will be used and applied to our currency.
* The reserve for the currency with **ID 47** will be updated according to the formula.
* The currency settings for **ID 47** will trigger a linkage, updating the reserve value across all relevant fields.

## Example: Creating a unified reserve for currencies (using a reserve obtained from auto-payouts) with conversion to other currencies

In this example, we use USDT as the primary currency. The reserve value for USDT is obtained from the merchant, while for other currencies, the reserve is calculated by converting the USDT reserve.

Primary currency:\
**USDT TRC (368)**\
Currencies that will receive the reserve value from the primary currency:\
**BTC (348),**\
**DOGE (362),**\
**ETH (355),**\
**SOL (404)**\
\
Reserve configuration:\
**USDT TRC (368)**\
**Reserve**: calculated by formula\
**Reserve formula**: \[usdttrc\_westwallet] - \[excursum\_auto368] - (\[excursum\_auto348] \* \[parser\_usdtbtc]) - (\[excursum\_auto362] \* \[parser\_usdtdoge]) - (\[excursum\_auto355] \* \[parser\_usdteth]) - (\[excursum\_auto404] \* \[parser\_usdtsol])

{% hint style="info" %}
Let’s break down the formula:\
&#xNAN;**\[usdttrc\_westwallet]** - The reserve obtained from the merchant (shortcode in the merchant settings).

<img src="../../../../.gitbook/assets/image (1103).png" alt="" data-size="original">

**\[excursum\_auto368], \[excursum\_auto348], \[excursum\_auto362], \[excursum\_auto355], \[excursum\_auto404] -** Shortcodes that sum up the "Received for reserve" values of all exchanges where the specified currencies are listed under "Received."

**\[parser\_usdtbtc], \[parser\_usdtdoge], \[parser\_usdteth], \[parser\_usdtsol] -** Parser shortcodes from the "**Parsers 2.0**" ➔ "**Rate Sources**" section. To use the shortcode correctly, prepend **parser\_** to the parser shortcode itself (**parser\_usdtbtc**).
{% endhint %}

**Link to reserve**: 348, 362, 355, 404

<figure><img src="../../../../.gitbook/assets/image (314).png" alt=""><figcaption></figcaption></figure>

BTC (348)\
**Reserve**: calculated by formula\
**Reserve formula**: (\[usdttrc\_westwallet] - \[excursum\_auto368] - (\[excursum\_auto348] \* \[parser\_usdtbtc]) - (\[excursum\_auto362] \* \[parser\_usdtdoge]) - (\[excursum\_auto355] \* \[parser\_usdteth]) - (\[excursum\_auto404] \* \[parser\_usdtsol])) / \[parser\_usdtbtc]\
**Link to reserve**: rc368

<figure><img src="../../../../.gitbook/assets/image (831).png" alt=""><figcaption></figcaption></figure>

DOGE (362)\
**Reserve**: calculated by formula\
**Reserve formula**: (\[usdttrc\_westwallet] - \[excursum\_auto368] - (\[excursum\_auto348] \* \[parser\_usdtbtc]) - (\[excursum\_auto362] \* \[parser\_usdtdoge]) - (\[excursum\_auto355] \* \[parser\_usdteth]) - (\[excursum\_auto404] \* \[parser\_usdtsol])) / \[parser\_usdtdoge]\
**Link to reserve**: rc368

<figure><img src="../../../../.gitbook/assets/image (983).png" alt=""><figcaption></figcaption></figure>

ETH (355)\
**Reserve**: calculated by formula\
**Reserve formula**: (\[usdttrc\_westwallet] - \[excursum\_auto368] - (\[excursum\_auto348] \* \[parser\_usdtbtc]) - (\[excursum\_auto362] \* \[parser\_usdtdoge]) - (\[excursum\_auto355] \* \[parser\_usdteth]) - (\[excursum\_auto404] \* \[parser\_usdtsol])) / \[parser\_usdteth]\
**Link to reserve**: rc368

<figure><img src="../../../../.gitbook/assets/image (1190).png" alt=""><figcaption></figcaption></figure>

SOL (404)\
**Reserve**: calculated by formula\
**Reserve formula**: (\[usdttrc\_westwallet] - \[excursum\_auto368] - (\[excursum\_auto348] \* \[parser\_usdtbtc]) - (\[excursum\_auto362] \* \[parser\_usdtdoge]) - (\[excursum\_auto355] \* \[parser\_usdteth]) - (\[excursum\_auto404] \* \[parser\_usdtsol])) / \[parser\_usdtsol]\
**Link to reserve**: rc368

<figure><img src="../../../../.gitbook/assets/image (944).png" alt=""><figcaption></figcaption></figure>