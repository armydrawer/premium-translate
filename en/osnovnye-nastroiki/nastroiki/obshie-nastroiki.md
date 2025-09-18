# General Settings

## General Settings

<figure><img src="../../.gitbook/assets/image (84).png" alt=""><figcaption></figcaption></figure>

**Site Icon** — This is the icon you see in browser tabs, bookmarks, and within mobile WordPress applications. It should be square with a resolution of at least 512 x 512 pixels.

**WordPress Address (URL)** — Your domain.

**Site Address (URL)** — If you want the site address to differ from the WordPress installation directory, enter the address here.

**Membership** — This option is not used.

**New User Role** — The role assigned to users registering on the exchange (select the role "**User**").

**Time Zone** — Choose a city in your time zone or a UTC (Coordinated Universal Time) offset.

**Date Format** — Select the date format **d.m.Y** (1 option).

**Time Format** — Select the time format **H:i** (1 option).

**First Day of the Week** — Choose Monday.

## Permalinks

<figure><img src="../../.gitbook/assets/image (1276).png" alt=""><figcaption></figcaption></figure>

**Permalink Structure** — Select "**Post Name**" (5 option).

**Category Prefix** — Leave this field empty.

**Tag Prefix** — Leave this field empty.

## Main Settings

<figure><img src="../../.gitbook/assets/image (1277).png" alt="" width="498"><figcaption></figcaption></figure>

**Page Title** — The title of the page for the admin panel.

**Description** — The description of the page for the admin panel.

**Administrator Email** — The email address of the administrator, where emails from the script will be sent.

**Link to Terms Page** — A link to the terms of exchange page (default URL — `/tos/`).

**Checkbox for Personal Data Processing** — Mark the checkbox for personal data processing in the exchange form.

* **Check by default**
* **Do not check by default**

**Maintenance Text** — The text that will be displayed on the site when it is in maintenance mode.

**Admin Panel URL** — The URL for logging into the site's admin panel (default URL — `/prmmxchngr/`). If you forget the login URL, you can recover it by following the [instructions](https://premium.gitbook.io/main/osnovnye-nastroiki/faq/kak-vosstanovit-dostup-v-panel-upravleniya-obmennikom#uteryan-url-dlya-vkhoda-v-panel-upravleniya).

**Jivosite.ru ID** — The ID for setting up [online chat on the site](https://premium.gitbook.io/main/osnovnye-nastroiki/faq/kak-ustanovit-onlain-chat).

**Jivosite.ru ID (Yandex)** — The ID for tracking statistics with [Yandex.Metrica](https://yandex.ru/support/metrica/integrated-goal/jivo-goal.html).

**Comments Form for "Posts"** — Enable the ability to leave comments on news articles on the site.

## Language Settings

<figure><img src="../../.gitbook/assets/image (1278).png" alt=""><figcaption></figcaption></figure>

**Auto-detect User Language** — Automatically detect the user's language based on their IP address.

**Admin Panel Language** — Choose the primary language for the admin panel.

**Site Language** — Choose the primary language for the site.

**Multilingual Support** — Select the languages supported by your site.

## Admin Panel

<figure><img src="../../.gitbook/assets/image (1280).png" alt="" width="267"><figcaption></figcaption></figure>

**Widgets on the Homepage** — Hide specified widgets on the site's homepage.

**Menu Sections** — Hide specified sections in the admin panel menu.

**Disable RSS Feed** — Disable the site's news RSS feed.

## AJAX Settings

<figure><img src="../../.gitbook/assets/image (1281).png" alt=""><figcaption></figcaption></figure>

**AJAX Checker for Admin Panel** — Enable a checker to update application data without reloading the page for the "**Applications**" and "**Applications**" ➔ "**LIVE Applications**" sections.

**Request Frequency from Admin Panel (seconds)** — The frequency of requests from the admin panel for new applications.

**AJAX Checker for Site** — Enable a checker to update application data from the site.

**Request Frequency from Site (seconds)** — The frequency of requests from the site for new applications (this option may create additional load on the server).

## Cron

In this section, you choose how often data will be updated for the specified options.

{% hint style="warning" %}
**"Out of the box"** optimal parameters are set for the specified options — we do not recommend changing them.
{% endhint %}

**"On Site" Option (pseudo-cron)**:

For the task to execute for the "On Site" option, a user must visit the site. You can set an interval for the task to run if there have been users on the site during that interval. If you choose the "On Request" option, the task will execute with each visit to the site by a unique user.

If your site has low traffic, we recommend always using the "On Server" option.

<figure><img src="../../.gitbook/assets/image (1559).png" alt="" width="143"><figcaption></figcaption></figure>

**"On Server" Option**:

For example, if an interval of 5 minutes is set for the "On Server" option, a task will run every 5 minutes to check the cron task on the server (but if the [cron task](https://premium.gitbook.io/main/osnovnye-nastroiki/faq/kak-sozdat-zadanie-cron-na-servere) for the specified task has **not been created** on the server (link for the task is on the "**Cron File**" button), then the option will not work).

**Optimal Settings for the Section:**

<div><figure><img src="../../.gitbook/assets/image (2066).png" alt="" width="392"><figcaption></figcaption></figure> <figure><img src="../../.gitbook/assets/image (2065).png" alt="" width="371"><figcaption></figcaption></figure> <figure><img src="../../.gitbook/assets/image (2064).png" alt="" width="386"><figcaption></figcaption></figure></div>

## CAPTCHA

<figure><img src="../../.gitbook/assets/image (1287).png" alt=""><figcaption></figcaption></figure>

Select the options for which CAPTCHA will be required when clients submit data.

## Logging Settings

<figure><img src="../../.gitbook/assets/image (1288).png" alt=""><figcaption></figcaption></figure>

**Logging Settings** — Set the frequency of archiving and deleting data for the specified options (the optimal settings are shown in the screenshot ("out of the box")).

## Contact Form

<figure><img src="../../.gitbook/assets/image (1289).png" alt=""><figcaption></figcaption></figure>

**Stop Words** — A list of stop words; if found in a client's/spammer's message, the message will not be processed.

**Blacklist** — A list of specific email addresses; messages from these addresses will not be processed.

**Blocked Email Domains** — Email domains from which messages will not be processed.

**Blocked IP Addresses** — IP addresses from which messages will not be processed.

## Personal Data Processing

<figure><img src="../../.gitbook/assets/image (1290).png" alt=""><figcaption></figcaption></figure>

**Display "Consent to Personal Data Processing" Checkbox in Forms** — Select the items for which the consent checkbox will be displayed on the site.

## HTML Sitemap Settings

<figure><img src="../../.gitbook/assets/image (1294).png" alt=""><figcaption></figcaption></figure>

**Section Title for "Posts"** — The title for the section on the HTML sitemap page (`your_domain + /sitemap/`).

**Show "Posts" in Sitemap** — Display news articles on the HTML sitemap page.

**Exclude "Posts" from Sitemap** — Select news articles to be excluded.

**Section Title for "Pages"** — The title for the section on the HTML sitemap page.

**Show "Pages" in Sitemap** — Display pages in the HTML sitemap.

**Exclude "Pages" from Sitemap** — Select pages to be excluded.

**Show Exchange Directions** — Display exchange directions in the HTML sitemap.

## Notification Icons

<figure><img src="../../.gitbook/assets/image (1295).png" alt=""><figcaption></figcaption></figure>

**Notification Icons** — Disable specific notification icons for the admin panel.

<figure><img src="../../.gitbook/assets/image (85).png" alt=""><figcaption></figcaption></figure>