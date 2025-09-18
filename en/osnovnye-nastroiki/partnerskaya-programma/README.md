# Affiliate Program

To access the affiliate program page, go to the admin panel's sidebar and select the "**Affiliate Program**" tab. On the opened page, you will see statistics related to the affiliate program:

<figure><img src="../../.gitbook/assets/изображение (170).png" alt=""><figcaption></figcaption></figure>

In the expanded menu on the left, you will find the following sections:

<figure><img src="../../.gitbook/assets/изображение (76).png" alt=""><figcaption></figcaption></figure>

## **Statistics**

View the number of clicks and visits for today and throughout the duration of the affiliate program.

## **Affiliate Exchanges**

A list of exchange transactions made by users referred by your partners.

## **Referrals**

On this page, you can track visits to the site via affiliate links: see the time, user IP address, browser, and the site from which the user came to your exchange point.

## **Referrals List**

A list of users who have been invited by your partners.

## **Payouts**

On this page, you can set the levels of the affiliate program, as well as specify the total amount of exchanges and the corresponding percentage of affiliate payouts for that amount. You can create an unlimited number of levels.

Affiliate rewards are calculated based on either the [profit of the exchange service](https://premium.gitbook.io/rukovodstvo-polzovatelya/osnovnye-nastroiki/partnerskaya-programma/pribyl-i-partnerskii-procent#otchisleniya-ot-pribyli-obmennika) or the [amount of the exchange](https://premium.gitbook.io/rukovodstvo-polzovatelya/osnovnye-nastroiki/partnerskaya-programma/pribyl-i-partnerskii-procent#otchisleniya-ot-summy-obmena). Affiliate rewards are cumulative.

To ensure that partners receive payouts from referred clients, you must set the profit value in the settings of each exchange direction. If the profit value is zero, no affiliate rewards will be paid. Pay attention to the "**Affiliate Program**" tab when creating or editing an exchange direction, as you will find additional settings there.

## **Withdrawals**

Once the minimum withdrawal amount is reached, partners can request a withdrawal. Submitted requests will appear on this page. To process current requests, the administrator must transfer funds to the user’s specified details listed in the table. After that, mark all requests you have paid. In the actions menu, select "**Mark as Paid**." Users who submitted requests will be notified of their completion.

The exchange service administrator receives email notifications when a partner submits a withdrawal request, provided that this notification is not disabled in the exchange settings.

## [**Banners**](https://premium.gitbook.io/rukovodstvo-polzovatelya/osnovnye-nastroiki/partnerskaya-programma/bannery-partnerov)

The service allows the use of two types of promotional materials: graphic and text.

When creating text or graphic materials, the administrator should use shortcodes—custom functions that allow partners to utilize ready-made and tailored promotional materials. The main shortcodes used in the affiliate program are:

**\[partner\_link]** — this shortcode automatically inserts the partner's ID into the link within the promotional materials. For the partner, this shortcode will appear as HTML code with a link containing their personal ID. If a user referred by the partner clicks on this link and completes an exchange, a certain amount will be automatically credited to the partner's account.

**\[url]** — this shortcode inserts your website's domain into the promotional material links.

You can view examples and the order of placing shortcodes in the standard promotional materials.

## **Settings**

### General Settings for the Affiliate Program

{% hint style="warning" %}
Starting from version 2.6, it is possible to configure a separate operational principle for the affiliate program for different users. To do this, you need to select the basic principle in the "**Affiliate Program**" ➔ "**Settings**" section,

![](<../../.gitbook/assets/image (2060).png>)

and then in the specific user's settings, choose a different principle (individual settings take precedence).

![](<../../.gitbook/assets/image (2059).png>)

After this, the selected user will follow an individual operational principle for the affiliate program, while the remaining users will follow the general principle.
{% endhint %}

<figure><img src="../../.gitbook/assets/image (2051).png" alt="" width="515"><figcaption></figcaption></figure>

**Referral Lifespan:**

*   **Users and Cookies** — the referral link will remain active when the referrer is attached in the referral settings (the referred user) (specify the exchange user ID), \

    <figure><img src="../../.gitbook/assets/image (2052).png" alt="" width="329"><figcaption></figcaption></figure>

    and also when the referral clicks on the affiliate link (permanent referral).
* **By Cookies** — the referral link will only remain active when the referral clicks on the affiliate link (temporary referral).

**Cookie Lifespan (days)** — the duration of the referral link's validity when clicking on the affiliate link.

**Minimum Payout (USD)** — the minimum amount that the referrer can request for withdrawal.

**Calculate Affiliate Rewards From:**

*   **Profit in Direction Settings** — profit settings from the exchange direction will be considered\

    <figure><img src="../../.gitbook/assets/image (2053).png" alt=""><figcaption></figcaption></figure>
* **Amount of Exchanges** — the total amount of exchanges by the referral will be considered.

**Calculate Affiliate Rewards With:**

* **All Users** — the partner's earnings will be calculated from exchanges of all users, even if the exchange was made by a guest (without registration in the exchange).
* **Only Registered Users** — the partner's earnings will be calculated only from exchanges made by registered users.

**Consider User Discounts in Affiliate Reward Calculations:**

* **No** — the referral's discount will not be considered in the partner's earnings calculation.
*   **Yes, Discount Percentage** — the personal discount percentage of the referral will be considered\

    <figure><img src="../../.gitbook/assets/image (2054).png" alt="" width="312"><figcaption></figcaption></figure>
* **Yes, Discount Amount** — the discount amount from a specific request will be considered.

**Show Sections** — check the boxes for the sections that [will be displayed](https://premium.gitbook.io/main/osnovnye-nastroiki/vneshnii-vid/lichnyi-kabinet-klienta) in the user's personal account on the exchange.

**Consider Affiliate Payouts in Reserves** — when calculating reserves for currencies, partner withdrawals will be included.

**Show Text Promotional Materials** — text on the page.

**Text Above the Affiliate Fund Withdrawal Form** — text above the affiliate fund withdrawal form (if this field is left empty, the standard text will be displayed)\

<figure><img src="../../.gitbook/assets/image (2055).png" alt="" width="563"><figcaption></figcaption></figure>

**Check User Details Against Blacklists When Requesting Affiliate Rewards** — checks the details before processing the payout (the "**Blacklist**" module must be enabled and configured).

**Check User Details Against Blacklists When Requesting Affiliate Rewards (Bestchange)** — checks the details before processing the payout (the "**Bestchange Blacklist**" module must be enabled and configured).

**No Access to REST API (ppapi):**

* **Yes** — API access keys for working with affiliate transactions can be created from the user's personal account in the exchange (Personal Account - API).
* **No** — API access is closed.
* **Only Selected Users** — API access keys can only be created by the exchange administrator.

### Affiliate Program Settings in User Profile

<figure><img src="../../.gitbook/assets/image (2057).png" alt="" width="563"><figcaption></figcaption></figure>

**Referral** — ID of the partner earning from the exchanges of the selected user.

**Personal Affiliate Percentage** — setting the affiliate percentage.

**Max. Personal Affiliate Percentage** — setting the maximum allowable affiliate percentage.

**Calculate Affiliate Rewards From:**

* **Default** — general affiliate program settings will be used.
* **Profit in Direction Settings** — profit settings from the exchange direction will be considered (higher priority than general settings).
* **Amount of Exchanges** — the total amount of exchanges by the referral will be considered (higher priority than general settings).

**Clicks** — the number of clicks on the affiliate link.

**Partner Exchanges** — the number and total amount of partner exchanges

**Partner Percentage** — the current partner percentage

**Funds in Account** — the current balance of the partner

**Total Earnings** — the partner's overall earnings (current balance + completed payouts)

**Payouts Made** — the total amount paid out to the partner

[^1]: A person who attracts clients with the aim of earning through a partner program.