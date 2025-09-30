# Profit and Partner Percentage

{% hint style="warning" %}
Make sure to specify the actual internal exchange rate to USD for currencies used in exchange directions with activated partner rewards.

To do this, go to the "**Currencies**" → "**Currency Codes**" section, manually set the exchange rate to USD for the selected currencies, or use the auto-correction feature (add the necessary rates following the [instructions](https://premium.gitbook.io/main/osnovnye-nastroiki/valyuty-i-napravleniya-obmena/kursy-valyut/parser-kursov-valyut-parsery-2.0)).

<h3 align="center"><img src="../../.gitbook/assets/image%20(2206)_eng.png" alt="" data-size="original"></h3>
{% endhint %}

{% hint style="success" %}
Instead of manually calculating profits for each exchange direction, you can activate the "**Automatic Profit Calculation**" module. In this case, the system will automatically calculate the profit for all exchange directions based on its internal algorithm, which determines the difference between the amounts in "**Giving**" and "**Receiving**" in dollar equivalents according to the established internal exchange rate to USD.

When this module is activated, the "**Profit**" block will disappear from the "**Rate**" tab in all exchange directions.
{% endhint %}

{% embed url="https://youtu.be/8Y6-iyQ-TJQ?t=41" %}

## Setting Up **Profit for Exchange Direction**

Go to the "**Exchange Directions**" → "**Exchange Directions**" section, select the desired exchange direction from the list, and click on the "**Edit**" link.

<figure><img src="../../.gitbook/assets/image%20(848)_eng.png" alt=""><figcaption></figcaption></figure>

Open the "**Rate**" tab and find the "**Profit**" parameter.

{% hint style="warning" %}
If the "**Profit**" block does not appear on the tab, disable the "**Automatic Profit Calculation**" module in the "**Modules**" section.

<img src="../../.gitbook/assets/image%20(604)_eng.png" alt="" data-size="original">
{% endhint %}

<figure><img src="../../.gitbook/assets/image%20(931)_eng.png" alt=""><figcaption></figcaption></figure>

In the "**Profit**" section, for each of the "**From Amount Giving/Receiving**" parameters, you will find two fields for "**Giving**" and two fields for "**Receiving**." The first field is a fixed amount for the partner exchange - _"_**S**_"_, and the second is a percentage of the amount "**Giving**" or "**Receiving**" - _"_**%**_"_.

To set the percentage, the administrator must **manually** calculate the total profit for this exchange direction and specify this percentage for the currency "**Giving**" or "**Receiving**" (at the administrator's discretion, but it is usually indicated in the "**Receiving**" column).

The following parameters and settings are responsible for calculating partner rewards:

The profit value in the settings of each direction on the "**Rate**" tab in the exchange direction:\
• If the profit size is set to **100%**, the partner program will operate on the principle of "a percentage of the exchange amount."\
• If the profit size is set to **3%**, the partner program will operate on the principle of "a percentage of the exchanger's profit."

<figure><img src="../../.gitbook/assets/image%20(1022)_eng.png" alt=""><figcaption></figcaption></figure>

## **Setting Up Partner Deductions**

### Deductions from the Exchange Amount

To have the partner program operate on the principle of "deductions from the exchange amount," you need to set the profit to 100% (in percentage) in one of the corresponding fields "Giving" or "Receiving."

Depending on which field you specify the profit value, that will be the exchange amount from which the partner's reward will be calculated.

If this amount is in a currency other than USD, it will be converted to USD at the internal exchange rate of the system (from the "**Currencies**" → "**Currency Codes**" section), and then the partner's reward will be credited to the user.

You can specify the profit value for both "Giving" and "Receiving" fields simultaneously, but it must be in the form of 50% for Giving and 50% for Receiving, or 30% for "Giving" and 70% for "Receiving" — the total percentage must not exceed 100%.

{% hint style="info" %}
Example Calculation:\
Exchanging 50 USD for 40 EUR.\
Profit percentage for the currency "**Giving**" = 100%.\
Partner percentage = 0.5%.\
\
Since the profit = 100%, the 50 USD is the amount from which we take 0.5%, resulting in 0.25 USD.\
This 0.25 USD will be received by the partner as their reward.
{% endhint %}

With such profit settings, it is essential to set the correct partner percentage. Typically, the partner percentage ranges from 0.1% to 1%.

### Deductions from the Exchanger's Profit

To have your partner program operate on the principle of "deductions from the exchanger's profit," you need to specify the profit percentage (for example, 2%) in the corresponding "Giving" or "Receiving" field, depending on the exchange direction.

The value you specify will be the exchange amount from which the partner's reward will be calculated.

If the amount is in a currency other than USD, the system will automatically convert it to USD at the internal exchange rate (from the "**Currencies**" → "**Currency Codes**" section), and then the partner's reward will be credited to the user.

You can also specify the profit value for both "Giving" and "Receiving" fields, distributing the percentages between them.

{% hint style="info" %}
Example Calculation:\
Exchanging 50 USD for 40 EUR.\
Profit = 3% set for the currency "**Giving**".\
Partner percentage = 50%.\
\
We calculate the exchanger's profit for this direction and get [1.5 USD](#user-content-fn-1)[^1].\
We calculate the partner's reward and get [0.75 USD](#user-content-fn-2)[^2].\
This 0.75 USD will be received by the partner as their reward.
{% endhint %}

With such profit settings, it is essential to set the correct partner percentage. Typically, this partner percentage ranges from 10% to 50%.

To become a partner and receive rewards, you need to create at least one level of deductions in the "Deductions" section of the partner program in the control panel. For this level, the parameter "**Amount Greater Than**" must be set to 0.

A partner will only receive their reward if it amounts to at least 0.01 USD. If the reward is less than this amount, it will not be credited to the partner's account.

To avoid such situations, set the "**Min. Payout Amount to Partner**" parameter on the "**Partner Program**" tab for each exchange direction to 0.01.

{% hint style="info" %}
For example, you calculated that the profit in this direction is 1%. You specify this value in the "**Profit**" → "**From Amount Receiving**" field. The system calculates 1% from the total amount to be received during the exchange, converts it to dollars[^3] — this is the profit of the exchange point, which the exchanger will share with partners.
{% endhint %}

Alternatively, you can specify a fixed amount in the "_**S**_" field that the partner will receive in this direction, regardless of their partner percentage.

### Combined Setup

Starting from version 2.6, the script allows for using deductions from the amount or profit for different partners.

To do this, set up the partner program according to the instructions above, selecting the "basic" model in the "**Partner Program**" ➔ "**Settings**" section.

<figure><img src="../../.gitbook/assets/image%20(97)_eng.png" alt=""><figcaption></figcaption></figure>

After that, in the partner settings (in the "**Users**" section), for those partners whose rewards should be calculated using a different model, select an alternative option (if the "**Default**" option is selected, the model from the "**Partner Program**" ➔ "**Settings**" section will apply).

<figure><img src="../../.gitbook/assets/image%20(98)_eng.png" alt=""><figcaption></figcaption></figure>

## Setting Up the Partner Program in the Exchange Direction

<figure><img src="../../.gitbook/assets/image%20(929)_eng.png" alt=""><figcaption></figcaption></figure>

**Partner Deductions** _—_ you can limit payouts under the partner program in the direction.

**Fixed Payout Amount to Partner** — a fixed amount that the partner will receive from the exchange, regardless of the exchanger's profit.

**Min. Payout Amount to Partner** — sets the minimum payout amount to the partner.

**Max. Payout Amount to Partner** — limits the maximum payout amount to the partner.

**Individual Partner Program Percentage** _—_ you can set an individual partner percentage for the direction. This percentage value will override the standard partner percentage settings. You can configure standard partner percentages in the control panel under "**Partner Program**" → "**Deductions**."

**Maximum Partner Percentage** — limits the maximum partner percentage set in the "**Partner Program**" → "**Deductions**" section.

## **Setting Up the Partner Percentage**

### **Setting the Partner Percentage for a Specific User**

The next step is to specify how much the partner will earn from the profits of the exchange point.

Go to the "**Users**" section, find the desired user, and proceed to edit their profile.

<figure><img src="../../.gitbook/assets/Screenshot_31%20(3)_eng.png" alt=""><figcaption></figcaption></figure>

<figure><img src="../../.gitbook/assets/Screenshot_32%20(2)_eng.png" alt=""><figcaption></figcaption></figure>

In the user settings, locate the "**Personal Partner Percentage**" option and enter the desired percentage in that field.

<figure><img src="../../.gitbook/assets/Screenshot_33%20(3)_eng.png" alt=""><figcaption></figcaption></figure>

When an exchange is made through the partner link, a percentage of the transaction amount in dollars is calculated, and 30% of that amount is given to the partner.

### **Setting the Partner Percentage for All Users**

If you want to set a percentage for all users and establish a general value, you need to go to the "**Affiliate Program" -> "Payouts"** section.

<figure><img src="../../.gitbook/assets/Screenshot_34%20(2)_eng.png" alt=""><figcaption></figcaption></figure>

Navigate to the table where some default partner percentage settings have already been created based on the total amount of exchanges.

The table will indicate what percentage a user receives from the exchange amount. This amount is cumulative—the percentage will change depending on the total amount of exchanges made through a specific link.

<figure><img src="../../.gitbook/assets/Screenshot_35%20(1)_eng.png" alt=""><figcaption></figcaption></figure>

This percentage is adjusted for all users who have registered and created a partner account.

[^1]: (50\*0.03)

[^2]: 1.5 USD \* 0.5 (50%)

[^3]: at the specified exchange rate for the currency in the "**Currencies**" -> "**Currency Codes**" section.
