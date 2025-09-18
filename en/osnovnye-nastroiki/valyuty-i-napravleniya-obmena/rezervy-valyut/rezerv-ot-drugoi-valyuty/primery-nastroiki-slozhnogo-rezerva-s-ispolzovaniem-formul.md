# Examples of Setting Up a Complex Reserve Using Formulas

## Formulas for Reserves

Using shortcodes, you can configure a total reserve for multiple currencies, convert reserves into other currencies (for example, from USD to BTC), and much more.

Go to **"Modules" → "Modules"** and enable the **"Reserve Formula"** module if it is turned off.

### List of Available Shortcodes

* **corresXX** — the amount of currency reserve adjustments.
* **excursum_giveXX** — the total reserve of requests for the currency "Giving."
* **excursum_getXX** — the total reserve of requests for the currency "Receiving."
* **excursum_autoXX** — the total reserve of requests for the currency "Receiving" with statuses from the settings in the **"Exchange Settings" → "Reserve Settings"** section.
* **cfilereserve_ZZ** — the reserve value for currency in row ZZ from the parsing reserve file.
* **dfilereserve_ZZ** — the exchange direction reserve value for row ZZ from the parsing reserve file.
* **payoutsXX** — the total of partner payouts for the currency.

{% hint style="warning" %}
If the partner program for the exchange direction is turned off, the **payoutsXX** parameter will have zero values.
{% endhint %}

* **\[parser_binance_btcusdt]** — the rate from the **"Parsers 2.0" → "Source Rates"** section.\
  In this section, the shortcode appears as **\[binance_btcusdt]**, but when used in the reserve formula, you need to add the prefix **parser_**, making it look like **\[parser_binance_btcusdt]**.\
  The same rule applies to shortcodes for custom coefficients.

**XX** — the currency ID displayed in the site management panel under the **"Currencies"** section. You can specify multiple IDs separated by commas.

**ZZ** — the row number in the reserve file for parsing. You can specify multiple IDs separated by commas.

## Example: Linking the Reserve of One Currency to Another

Let's consider an example that demonstrates how to link the reserve of the "Monobank" currency to the reserve of "Privat24."

1. In the management panel under the **"Currencies"** section, find the currency IDs for "Privat24" (ID 5) and "Monobank" (ID 47).

2. Proceed to edit the currencies "Privat24" and "Monobank." In the settings for both currencies, select the option **"Reserve Currency"** as **"By Formula."**
3. In the field **"Reserve Formula"** that appears below, enter the following formula in the settings for both currencies:

Now, let's complicate the example: we will link the reserves of "Monobank" (ID 47) and "Oschadbank" (ID 23) to the reserve of "Privat24" (ID 5). For all three currencies, we need to set the following formula:

4. In the site management panel under **"Modules" → "Modules,"** activate the module **"Link to Update Currency Reserve (by Cron)"** if it has been deactivated. In the **"Currencies"** section for "Monobank," "Oschadbank," and "Privat24," a **"Link"** button will appear. For each currency in the example, click this button and copy the address of the opened page.

5. Add each copied link to the task scheduler (cron) on the server. The link can be run every minute. Here’s an example command for the task scheduler in Unix format for the ISP Manager control panel:

where **XX** — is the currency ID.

{% hint style="info" %}
The command may vary for each server. Changes pertain to the part of the command `/usr/bin/wget -t 1 -O —`. You can confirm the correct command with your hosting technical support.
{% endhint %}

## Example: Unified Reserve for Multiple Currencies (Using Reserve Calculated from Requests)

For instance, we have 4 currencies with IDs **5, 42, 47, 61**. Our goal is to ensure that all currencies have the same reserve.

We need to determine which currency will be the primary one. In our case, let’s say it will be the currency with **ID 47.**

The formula will be as follows:

**\[sum of reserve adjustments for currencies with our IDs 5,42,47,61]** + **\[sum of "giving for reserve" from requests where currency giving is ID 5,42,47,61]** - **\[sum of "receiving for reserve" from requests where currency receiving is ID 5,42,47,61]** - **\[partner payouts for currencies with our IDs 5,42,47,61]**

Thus, for the primary currency (**ID 47**), we create the formula:

**\[corres5,42,47,61] + \[excursum_give5,42,47,61] – \[excursum_get5,42,47,61] – \[payouts5,42,47,61]**

This formula will yield the correct value. The only issue is that the currency reserve changes only when actions occur with our currency.

To ensure that when the primary currency reserve (ID 47) is updated, the same value is applied to other currencies, we need to specify the value in the field **"Link Reserve to Currency ID"**:

**5,42,61**

Now, when actions occur with currency **ID 47**, the following will happen:

* The reserve will be calculated according to the formula.
* The formula value will be recorded in the linked currencies.

This is almost what we need. But what happens when actions occur with other currencies? How do we update the reserve of the primary currency **ID 47**?

For this, in the settings of each currency, we will select the following:

Take the **"Currency Reserve"** from the **"Reserve Field."** This is to save our server resources and avoid recalculating the value (it will be overwritten anyway).

## Example: Creating the Same Reserve for Currencies (Using Reserve from Auto Payout)

For instance, we have 4 currencies with IDs **5, 42, 47, 61**. Our goal is to ensure that all currencies have the same reserve.

We need to determine which currency will be the primary one. In our case, let’s say it will be the currency with **ID 47.**

The formula will be as follows:

**\[auto payout shortcode]** - **\[sum of "receiving for reserve" from requests where currency receiving is ID 5,42,47,61]** - **\[partner payouts for currencies with our IDs 5,42,47,61]**

Thus, for the primary currency with **ID 47**, we create the formula:

**\[auto payout shortcode] – \[excursum_auto5,42,47,61] – \[payouts5,42,47,61]**

This formula will yield the correct value. The only issue is that the currency reserve changes only when actions occur with our currency.

To ensure that when the primary currency reserve is updated, the same value is applied to other currencies, we need to specify the value in the field **"Link Reserve to Currency ID"**:

**5,42,61**

Now, when actions occur with the currency with **ID 47**, the following will happen:

* The reserve will be calculated according to the formula.
* The formula value will be recorded in the linked currencies.

In the field labeled "**Link Reserve to Currency Reserve ID**," we enter the value:

**rc47**

This means that when we perform actions with our currencies, the following will occur:

* We use the value from this field and apply it to our currency.
* We update the reserve for the currency with **ID 47** using a specific formula.
* The link in the settings for the currency with **ID 47** is activated, which updates all fields with its reserve value.

## Example: Creating Identical Reserves for Currencies (Using Reserve from Auto-Payout) with Conversion to Other Currencies

In this example, we use USDT as the primary currency, obtaining its reserve value from the merchant, and we use conversion from USDT for the other currencies.

Primary Currency:\
**USDT TRC (368)**\
Currencies for receiving the reserve value of the primary currency:\
**BTC (348),**\
**DOGE (362),**\
**ETH (355),**\
**SOL (404)**

Reserve Settings:\
**USDT TRC (368)**\
**Reserve**: according to the formula\
**Reserve Formula**: \[usdttrc\_westwallet] - \[excursum\_auto368] - (\[excursum\_auto348] * \[parser\_usdtbtc]) - (\[excursum\_auto362] * \[parser\_usdtdoge]) - (\[excursum\_auto355] * \[parser\_usdteth]) - (\[excursum\_auto404] * \[parser\_usdtsol])

{% hint style="info" %}
Let's break down the formula:\
**\[usdttrc\_westwallet]** - the reserve obtained from the merchant (shortcode in the merchant settings)

<img src="../../../../.gitbook/assets/image (1103).png" alt="" data-size="original">

**\[excursum\_auto368], \[excursum\_auto348], \[excursum\_auto362], \[excursum\_auto355], \[excursum\_auto404]** - shortcodes that sum the values "Received for Reserve" from all exchanges where the specified currencies are listed as "Received."

**\[parser\_usdtbtc], \[parser\_usdtdoge], \[parser\_usdteth], \[parser\_usdtsol]** - shortcodes from the "**Parsers 2.0**" ➔ "**Rate Sources**" section. To use the shortcode correctly, you need to prefix **parser\_** to the shortcode itself (**parser\_usdtbtc**).
{% endhint %}

**Link to Reserve**: 348, 362, 355, 404

<figure><img src="../../../../.gitbook/assets/image (314).png" alt=""><figcaption></figcaption></figure>

BTC (348)\
**Reserve**: according to the formula\
**Reserve Formula**: (\[usdttrc\_westwallet] - \[excursum\_auto368] - (\[excursum\_auto348] * \[parser\_usdtbtc]) - (\[excursum\_auto362] * \[parser\_usdtdoge]) - (\[excursum\_auto355] * \[parser\_usdteth]) - (\[excursum\_auto404] * \[parser\_usdtsol])) / \[parser\_usdtbtc]\
**Link to Reserve**: rc368

<figure><img src="../../../../.gitbook/assets/image (831).png" alt=""><figcaption></figcaption></figure>

DOGE (362)\
**Reserve**: according to the formula\
**Reserve Formula**: (\[usdttrc\_westwallet] - \[excursum\_auto368] - (\[excursum\_auto348] * \[parser\_usdtbtc]) - (\[excursum\_auto362] * \[parser\_usdtdoge]) - (\[excursum\_auto355] * \[parser\_usdteth]) - (\[excursum\_auto404] * \[parser\_usdtsol])) / \[parser\_usdtdoge]\
**Link to Reserve**: rc368

<figure><img src="../../../../.gitbook/assets/image (983).png" alt=""><figcaption></figcaption></figure>

ETH (355)\
**Reserve**: according to the formula\
**Reserve Formula**: (\[usdttrc\_westwallet] - \[excursum\_auto368] - (\[excursum\_auto348] * \[parser\_usdtbtc]) - (\[excursum\_auto362] * \[parser\_usdtdoge]) - (\[excursum\_auto355] * \[parser\_usdteth]) - (\[excursum\_auto404] * \[parser\_usdtsol])) / \[parser\_usdteth]\
**Link to Reserve**: rc368

<figure><img src="../../../../.gitbook/assets/image (1190).png" alt=""><figcaption></figcaption></figure>

SOL (404)\
**Reserve**: according to the formula\
**Reserve Formula**: (\[usdttrc\_westwallet] - \[excursum\_auto368] - (\[excursum\_auto348] * \[parser\_usdtbtc]) - (\[excursum\_auto362] * \[parser\_usdtdoge]) - (\[excursum\_auto355] * \[parser\_usdteth]) - (\[excursum\_auto404] * \[parser\_usdtsol])) / \[parser\_usdtsol]\
**Link to Reserve**: rc368

<figure><img src="../../../../.gitbook/assets/image (944).png" alt=""><figcaption></figcaption></figure>