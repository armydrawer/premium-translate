# Examples of Configuring a Complex Reserve Using Formulas

## Formulas for Reserve <a href="#delaem_y_valyut_odinakovii_rezerv_rezerv" id="delaem_y_valyut_odinakovii_rezerv_rezerv"></a>

Using shortcodes, you can configure a combined reserve for multiple currencies, convert reserves between currencies (for example, from USD to BTC), and much more.

Go to **"Modules" → "Modules"** and enable the **"Reserve Formula"** module if it is disabled.

### List of Available Shortcodes <a href="#spisok-dostupnykh-shortkodov" id="spisok-dostupnykh-shortkodov"></a>

* **corresXX** — the total amount of reserve adjustments for the currency.
* **excursum_giveXX** — the total reserve amount of orders in the "**Give**" currency.
* **excursum_getXX** — the total reserve amount of orders in the "**Receive**" currency.
* **excursum_autoXX** — the total reserve amount of orders in the "**Receive**" currency with order statuses set in "**Exchange Settings** → _Reserve Settings_".
* **cfilereserve_ZZ** — the reserve value of the currency for line ZZ from the reserve file used for parsing.
* **dfilereserve_ZZ** — the reserve value for the exchange direction for line ZZ from the reserve file used for parsing.
* **payoutsXX** — the total amount of partner payouts for the currency.

{% hint style="warning" %}
If the partner program for the exchange direction is disabled, the **payoutsXX** parameter will return zero values.
{% endhint %}

* **[parser_binance_btcusdt]** — the rate from the "**Parsers 2.0** → _Source Rates_" section.  
  In that section, the shortcode appears as **[binance_btcusdt]**, but when used in a reserve formula, you need to add the prefix **parser_** to the shortcode, making it **[parser_binance_btcusdt]**.  
  The same rule applies to shortcodes for custom coefficients.

**XX** — the currency ID as shown in the site admin panel under "**Currencies**". You can specify multiple IDs separated by commas.

**ZZ** — the line number in the reserve file used for parsing. You can specify multiple line numbers separated by commas.

<figure><img src="https://2722984412-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2Fm9kqZXsNykrN6VyxxXBO%2Fuploads%2FLcRDZqj1mr6KF7T7g2M1%2FScreenshot_27.png?alt=media&#x26;token=840d5521-2a75-4cc0-b5d3-2d9fc7809ef7" alt="" width="375"><figcaption></figcaption></figure>

## Example: Linking the Reserve of One Currency to Another

Let's look at an example to demonstrate how to link the currency reserve of "Monobank" to the reserve of "Privat24."

1. In the control panel, go to the "**Currencies**" section and find the currency IDs for "Privat24" (ID 5) and "Monobank" (ID 47):

<figure><img src="https://2722984412-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2Fm9kqZXsNykrN6VyxxXBO%2Fuploads%2F2vxayvvjfY0XlJIFOwB3%2FScreenshot_28.png?alt=media&#x26;token=69d1cfad-a304-4349-acfa-93a4c0b39d73" alt="" width="563"><figcaption></figcaption></figure>

2. Next, edit the currencies "Privat24" and "Monobank." In the settings for both currencies, set the "**Currency reserve**" parameter to "**By formula**."
3. In the "**Reserve formula**" field that appears below, enter the following formula for both currencies:

<figure><img src="https://2722984412-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2Fm9kqZXsNykrN6VyxxXBO%2Fuploads%2FEKbpy716s588HTtlzvOk%2FScreenshot_29.png?alt=media&#x26;token=bbe3df74-35bc-4820-8b1a-3a7c49d7c385" alt="" width="563"><figcaption></figcaption></figure>

Let's complicate the example: link the currency reserves of "Monobank" (ID 47) and "Oschadbank" (ID 23) to the reserve of "Privat24" (ID 5). In this case, you need to set the following formula for all three currencies:

<figure><img src="https://2722984412-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2Fm9kqZXsNykrN6VyxxXBO%2Fuploads%2FtfZYh5QcT3fhuHOTJnrF%2FScreenshot_30.png?alt=media&#x26;token=e4febef0-7543-44b0-aa1d-bdc582cc58e7" alt=""><figcaption></figcaption></figure>

4. In the website control panel, go to "**Modules** → "Modules"** and activate the module "**Currency reserve update link (via Cron)**" if it is disabled. In the "**Currencies**" section, a "**Link**" button will appear for the currencies "Monobank," "Oschadbank," and "Privat24." For each currency in the example, click this button and copy the URL of the page that opens.

<figure><img src="https://2722984412-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2Fm9kqZXsNykrN6VyxxXBO%2Fuploads%2FerCRVhx6m7YcC6jSdX7K%2FScreenshot_31.png?alt=media&#x26;token=779f67ee-d4b4-477d-bc7a-bd0a82f80793" alt=""><figcaption></figcaption></figure>

5. Add each copied link to the server’s task scheduler (cron). You can run the link every minute. Here is an example of a cron command in Unix format for the ISP Manager control panel:

<figure><img src="https://2722984412-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2Fm9kqZXsNykrN6VyxxXBO%2Fuploads%2FhAiLwEeIOhzl291Y42mm%2FScreenshot_32.png?alt=media&#x26;token=8b91ff1d-777e-4d4d-ac8d-8a6d5fa3829c" alt=""><figcaption></figcaption></figure>

where **XX** is the currency ID.

Here is a natural, fluent English translation of the provided text:

---

{% hint style="info" %}
The command may look different on each server. Changes usually affect the part of the command `/usr/bin/wget -t 1 -O —`. You can check the correct command with your hosting provider’s technical support.
{% endhint %}

<figure><img src="../../../../.gitbook/assets/image (778).png" alt="" width="375"><figcaption></figcaption></figure>

## Example: Single Reserve for Multiple Currencies (Using Reserve Calculated from Orders)

Suppose we have 4 currencies with the following IDs: **5, 42, 47, 61**. Our goal is to set the same reserve amount for all these currencies.

First, we need to decide which currency will be the main one. In this example, let’s choose the currency with **ID 47** as the main currency.

The formula will be:

**[sum of reserve adjustments for currencies with IDs 5, 42, 47, 61]** + **[sum of “given for reserve” amounts from orders where the “give” currency ID is 5, 42, 47, or 61]** (this is what our site received through orders) - **[sum of “received for reserve” amounts from orders where the “receive” currency ID is 5, 42, 47, or 61]** (this is what our site gave through orders) - **[partner payouts for currencies with IDs 5, 42, 47, 61]**

So, for the main currency (**ID 47**), we create the formula:

**[corres5,42,47,61] + [excursum_give5,42,47,61] – [excursum_get5,42,47,61] – [payouts5,42,47,61]**

This formula will output the correct reserve value. The only catch is that the reserve for a currency updates only when there are transactions involving that currency.

To ensure that when the reserve for the main currency (ID 47) is updated, the same value is applied to the other currencies, we need to enter the following in the field "**Link reserve to the reserve of currency ID**":

**5,42,61**

Now, whenever there are transactions involving currency **ID 47**, the following will happen:

* The reserve will be calculated using the formula
* The formula’s result will be written to the linked currencies

This almost achieves what we want. But what about when transactions happen with the other currencies? How do we update the reserve of the main currency **ID 47** in that case?

To handle this, in the settings for each of the other currencies, we select:

"**Take currency reserve from**" "**reserve field**". This saves server resources by avoiding unnecessary recalculations, since the value will be overwritten anyway.

---

Let me know if you need the translation adapted for a specific audience or style!

In the field "**Link reserve to currency reserve ID**," enter the value:

**rc47**

This way, when working with our currencies, the following will happen:

* The value from this field will be used and assigned to our currency.
* The reserve for the currency with **ID 47** will be updated according to the formula.
* The binding set in the currency settings for **ID 47** will trigger, updating all linked fields with the new reserve value.

## Example: Creating identical reserves for multiple currencies (using the reserve obtained from auto payouts) <a href="#creating_identical_reserves_for_currencies" id="creating_identical_reserves_for_currencies"></a>

Suppose we have 4 currencies with IDs **5, 42, 47, 61**. Our goal is to make sure all these currencies have the same reserve.

First, we need to decide which currency will be the main one. In this case, let’s choose the currency with **ID 47**.

The formula will be as follows:

**[auto_payout_shortcode] – [amount "received for reserve" from requests where the currency received is ID 5,42,47,61 (i.e., what our site has paid out)] – [partner payouts for currencies with our IDs 5,42,47,61]**

So, for the main currency with **ID 47**, we create the formula:

**[auto_payout_shortcode] – [excursum_auto5,42,47,61] – [payouts5,42,47,61]**

This formula will output the correct value. The only catch is that the currency reserve updates only when actions occur with our currency.

To ensure that when the reserve of the main currency is updated, the same value is applied to the other currencies, we need to enter the following in the "**Link reserve to currency reserve ID**" field:

**5,42,61**

Now, when actions occur with the currency with **ID 47**, the following will happen:

* The reserve will be calculated using the formula.
* The formula’s value will be written to the linked currencies.

This almost achieves what we want. But what about when actions happen with the other currencies? How do we update the reserve of the main currency with **ID 47**?

To handle this, in the settings of each currency, we will select the following:

Here is a natural, fluent English translation of the provided text:

---

**"Currency Reserve"** is taken from the **"Reserve Field"** to save our server’s resources and avoid recalculating the value (since it will be overwritten anyway).

In the field **"Link reserve to currency reserve ID"**, enter the value:

**rc47**

This way, when performing operations with our currencies, the following will happen:

* The value from the field is used and assigned to our currency.
* The reserve for the currency with **ID 47** is updated according to the formula.
* The link set in the currency settings for **ID 47** triggers, updating the reserve value across all related fields.

---

## Example: Creating a unified reserve for multiple currencies (using the reserve obtained from auto payouts) with conversion to other currencies

In this example, we use USDT as the base currency. The reserve value for USDT is obtained from the merchant, and for the other currencies, we convert the reserve from USDT.

Base currency:  
**USDT TRC (368)**  
Currencies receiving the base currency’s reserve value:  
**BTC (348),**  
**DOGE (362),**  
**ETH (355),**  
**SOL (404)**

Reserve settings:  
**USDT TRC (368)**  
**Reserve:** calculated by formula  
**Reserve formula:**  
\[usdttrc_westwallet] - \[excursum_auto368] - (\[excursum_auto348] * \[parser_usdtbtc]) - (\[excursum_auto362] * \[parser_usdtdoge]) - (\[excursum_auto355] * \[parser_usdteth]) - (\[excursum_auto404] * \[parser_usdtsol])

{% hint style="info" %}
Let’s break down the formula:  
- **\[usdttrc_westwallet]** — the reserve value received from the merchant (a shortcode set in the merchant’s settings)

<img src="../../../../.gitbook/assets/image (1103).png" alt="" data-size="original">

- **\[excursum_auto368], \[excursum_auto348], \[excursum_auto362], \[excursum_auto355], \[excursum_auto404]** — shortcodes that sum the "Received for reserve" amounts from all exchanges where the specified currencies appear in the "Received" field.

- **\[parser_usdtbtc], \[parser_usdtdoge], \[parser_usdteth], \[parser_usdtsol]** — parser shortcodes from the "**Parsers 2.0**" section → "**Exchange Rate Sources**". To use these shortcodes correctly, prefix them with **parser_** (e.g., **parser_usdtbtc**).
{% endhint %}

**Link reserve to:** 348, 362, 355, 404

<figure><img src="../../../../.gitbook/assets/image (314).png" alt=""><figcaption></figcaption></figure>

---

BTC (348)  
**Reserve:** calculated by formula  
**Reserve formula:**  
(\[usdttrc_westwallet] - \[excursum_auto368] - (\[excursum_auto348] * \[parser_usdtbtc]) - (\[excursum_auto362] * \[parser_usdtdoge]) - (\[excursum_auto355] * \[parser_usdteth]) - (\[excursum_auto404] * \[parser_usdtsol])) / \[parser_usdtbtc]

**Link reserve to:** rc368

---

If you need any further clarification or adjustments, feel free to ask!

DOGE (362)  
**Reserve**: calculated by formula  
**Reserve formula**:  
(\[usdttrc_westwallet] - \[excursum_auto368] - (\[excursum_auto348] × \[parser_usdtbtc]) - (\[excursum_auto362] × \[parser_usdtdoge]) - (\[excursum_auto355] × \[parser_usdteth]) - (\[excursum_auto404] × \[parser_usdtsol])) ÷ \[parser_usdtdoge]  
**Linked to reserve**: rc368

---

ETH (355)  
**Reserve**: calculated by formula  
**Reserve formula**:  
(\[usdttrc_westwallet] - \[excursum_auto368] - (\[excursum_auto348] × \[parser_usdtbtc]) - (\[excursum_auto362] × \[parser_usdtdoge]) - (\[excursum_auto355] × \[parser_usdteth]) - (\[excursum_auto404] × \[parser_usdtsol])) ÷ \[parser_usdteth]  
**Linked to reserve**: rc368

---

SOL (404)  
**Reserve**: calculated by formula  
**Reserve formula**:  
(\[usdttrc_westwallet] - \[excursum_auto368] - (\[excursum_auto348] × \[parser_usdtbtc]) - (\[excursum_auto362] × \[parser_usdtdoge]) - (\[excursum_auto355] × \[parser_usdteth]) - (\[excursum_auto404] × \[parser_usdtsol])) ÷ \[parser_usdtsol]  
**Linked to reserve**: rc368