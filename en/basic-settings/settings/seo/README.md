# SEO

## Settings

In the website control panel, under the "**SEO" → "Settings"** section, you will find the available SEO settings for your site.

<figure><img src="../../../.gitbook/assets/image (1130)_eng.png" alt=""><figcaption></figcaption></figure>

OGP (Open Graph Protocol) is a set of meta tags used to define how content will appear on social media platforms like Facebook, Twitter, LinkedIn, and others. OGP allows you to set the title, description, image, and other attributes that will be displayed when a link to your page is shared on social media. This helps enhance the visual representation of your content and makes it more appealing to users, which can, in turn, increase the number of clicks on links and drive traffic to your site.

{% tabs %}
{% tab title="General Settings" %}
<figure><img src="../../../.gitbook/assets/image (915) (1).png" alt=""><figcaption></figcaption></figure>
{% endtab %}

{% tab title="Homepage" %}
<figure><img src="../../../.gitbook/assets/image (1236)_eng.png" alt=""><figcaption></figcaption></figure>
{% endtab %}

{% tab title="Posts" %}
<figure><img src="../../../.gitbook/assets/image (859) (1).png" alt=""><figcaption></figcaption></figure>
{% endtab %}

{% tab title="Pages" %}
<figure><img src="../../../.gitbook/assets/image (1033)_eng.png" alt=""><figcaption></figcaption></figure>
{% endtab %}

{% tab title="Exchange Form" %}
<figure><img src="../../../.gitbook/assets/image (930) (1).png" alt=""><figcaption></figcaption></figure>
{% endtab %}
{% endtabs %}

Explanations for some parameters:

* **Title** — the page title for search engines;
* **Keywords** — keywords for search engines;
* **Description** — the page description for search engines;
* **OGP title** — the page title for social media when published;
* **OGP description** — the page description for social media when published;
* **OGP image** — the image for social media when published.
* **News Title Template** — the title template for news articles published on the site.
* **Page Title Template** — the title template for pages created on the site.
* **Exchange Title Template** — the title template for pages that open after selecting an exchange direction.
* **Exchange Title Template (H1)** — the H1 title template for the exchange direction that appears on the exchange direction page.

## Meta Tags and Metrics

Meta tags are HTML tags that contain information about a webpage that users do not see. These tags help search engine bots better understand the content of the page and determine its relevance to user search queries. Some examples of meta tags include the page title, page description, keywords, and other metadata.

Metrics are numerical indicators used to measure the effectiveness of a website and its interaction with users. These indicators include the number of visitors to the site, time spent on the site, user return rates, bounce rates, and other metrics. Metrics help webmasters and marketers analyze user behavior on the site and optimize it to improve user experience and conversion rates.

This section specifies tags, goals, and counters for subsequent data analytics in third-party services.

1. To create a Yandex.Metrica counter code, log in or register in the [system](https://metrika.yandex.ru).
2. On the counter list page, [add a counter](https://metrika.yandex.ru/add). The settings page will open.
3. Specify the main settings for the counter. Fill in the fields:
   * **Counter Name**. The name you provide will be displayed on the "My Counters" page and in the top menu for switching between counters. If no name is specified, the value of the "Website Address" field will be used.
   *   **Website Address (main domain of the site)**. This field is mandatory. Do not include the scheme/protocol prefix (`http://`, `https://`).

       In this field, you can specify the path of the site (path in the URL structure). For example, example.com/category/. Do not specify the address to a specific file or page fragment (the "#" symbol) — these indications will cause an error in the input field. Additionally, URL parameters (the part of the address after the "?" symbol) will not be considered.
4. Accept the terms of the [User Agreement](https://yandex.ru/legal/metrica_termsofuse/).
5. Click the "Create Counter" button.
6.  On the opened page, in the "**Counter Code**" block, copy the **counter ID** and enter it in the **"Yandex.Metrica Counter ID"** field in the admin panel under the **SEO** section.

    To set goals in Yandex.Metrica, specify the goal name in the corresponding field.

<figure><img src="../../../.gitbook/assets/image (2122)_eng.png" alt=""><figcaption></figcaption></figure>

<figure><img src="../../../.gitbook/assets/image (2123)_eng.png" alt=""><figcaption></figcaption></figure>

## XML Sitemap Settings

An XML sitemap is a file that contains information about the structure and content of a website in XML format. It is designed for search engine bots to simplify the indexing of the site's pages and the collection of information about them. The XML sitemap contains a list of all the site's pages, as well as additional information such as update frequency, page priority, and the date of the last update. It helps search engine bots understand which pages of the site should be indexed, increasing the site's chances of achieving high positions in search results.

**Show "Posts" in the sitemap** — option to display news in the XML sitemap created in the "**Posts**" section.

**Exclude "Posts" from the sitemap** — selective display of news in the XML sitemap.

**Show "Pages" in the sitemap** — option to display pages in the XML sitemap created in the "**Pages**" section.

**Exclude "Pages" from the sitemap** — selective display of pages in the XML sitemap.

**Show exchange directions** — option to display exchange directions in the XML sitemap.

## robots.txt Settings

The robots.txt file is a text file placed on the website to inform search engine bots which pages of the site should be indexed and which should not. In this file, you can specify which directories and files should be excluded from indexing, as well as provide links to sitemaps and other useful resources for search engine bots. The robots.txt file is an important tool for SEO and can help improve the site's positions in search results.

**Text** — specify the necessary rules for indexing the site, following [Google's instructions](https://developers.google.com/search/docs/crawling-indexing/robots/create-robots-txt?hl=ru).

## Exchange Directions

In this section, you create the appearance of the exchange direction window that will be displayed on social media.

**Exchange Description** — the description that will be displayed in the window on social media.

**Page Title** — the title of the exchange page.

**Exchange Name (H1)** — the name of the exchange direction.

**Canonical URL** — the primary URL of the webpage used to identify the unique page of the website, regardless of which URL was used to access that page.

**Keywords** — keywords that help search engines understand which topics are most relevant to a specific page and how it can be displayed in search results.

**OGP title** — the title used to define the page title that will be displayed when it is published on social media.

## Example of Filling Out

An example of filling out SEO parameters for a website:

<figure><img src="../../../.gitbook/assets/image (1913)_eng.png" alt=""><figcaption></figcaption></figure>

1. Log in to the admin panel.
2. Go to the "**SEO**" -> "**Settings**" section.

<figure><img src="../../../.gitbook/assets/image (1914)_eng.png" alt=""><figcaption></figcaption></figure>

3. Select the settings for the homepage:

<figure><img src="../../../.gitbook/assets/image (1917)_eng (1).png" alt=""><figcaption></figcaption></figure>

4. On the opened page:

<figure><img src="../../../.gitbook/assets/image (1919)_eng.png" alt=""><figcaption></figcaption></figure>

5. Fill in the data from the **Title** field:

<figure><img src="../../../.gitbook/assets/image (1920)_eng.png" alt=""><figcaption></figcaption></figure>

6. Fill in the data from the **Description** field:

<figure><img src="../../../.gitbook/assets/image (1921)_eng.png" alt=""><figcaption></figcaption></figure>

7. Fill in the data from the **Keywords** field:

<figure><img src="../../../.gitbook/assets/image (1922)_eng.png" alt=""><figcaption></figcaption></figure>

8. After filling in the data, click the "**Save**" button.

<figure><img src="../../../.gitbook/assets/image (1923)_eng.png" alt=""><figcaption></figcaption></figure>

9. Go to the "**Appearance**" -> "**Homepage**" section and fill in the "**Title**" field in the "**Welcome Message**" block.

<figure><img src="../../../.gitbook/assets/image (1927)_eng.png" alt=""><figcaption></figcaption></figure>

10. Fill in the data from the "**H1 for Homepage**" field:

<figure><img src="../../../.gitbook/assets/image (1924)_eng.png" alt=""><figcaption></figcaption></figure>

11. Fill in the information from the line "**Description text for the main page**":

<figure><img src="../../../.gitbook/assets/image (1926)_eng.png" alt=""><figcaption></figcaption></figure>
