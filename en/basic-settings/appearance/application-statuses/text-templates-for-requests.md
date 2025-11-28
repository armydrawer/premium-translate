# Text Templates for Requests

To display different text for various states of a request on the exchange page, you can use templates.

## General Templates

To create templates, go to the "**Exchange Directions**" section -> "**Currency Exchange Direction Templates**."

In this section, select the desired item and proceed to edit it. Please note that the set of fields available for editing varies for different items in the dropdown list.

<figure><img src="../../../.gitbook/assets/image (152) (1).png" alt=""><figcaption></figcaption></figure>

Let's take a look at the template settings for the status "**New Request**":

**Website Title** - This is the header for the status that will be displayed on the page (for multilingual exchanges, you need to set up different language versions of the text by clicking on the flag above the field and filling in the opened field).

**Brief Status Description** - This describes the current state of the request (for multilingual exchanges, you need to set up different language versions of the text by clicking on the flag above the field and filling in the opened field).

**Page Refresh:**\
• **No** - The user will need to manually refresh the request page.\
• **Auto-refresh** - The page will automatically refresh at a specified interval (the user can disable auto-refresh by clicking the "**Turn Off Refresh**" button).\
\
• **On Button Click** - A button will be displayed on the request page to enable "**Auto-refresh**" mode.<br>

**Automatically refresh the page every (sec.)** - This is the interval at which the page will refresh.

**How to display the description from the form below:**\
• **Show only the relevant description from the exchange direction** - The text from the exchange direction will always be displayed on the request page for the corresponding status (if no text is provided, an empty field will be shown).\
• **If no description is provided in the exchange direction, show it from the form below** - If text is provided in the "**User Information**" section of the exchange direction (in any language version), it will be displayed; otherwise, the text from the template below will be shown.\
• **Always show the description from the form below** - The text from the template below will always be displayed on the request page for the corresponding status.

**Text** - This is the text that will be displayed on the request page for the corresponding status. Use shortcodes to include variables in the text.

## Individual Templates

For different directions, you can also use custom text. To do this, in the exchange direction settings, on the "**User Information**" tab, fill in the corresponding templates with text (for multilingual exchanges, you need to set up different language versions of the text by clicking on the flag above the field and filling in the opened field).

{% hint style="info" %}
If both general and individual templates are filled out for a single status, to ensure that the text from the exchange direction is displayed, set the option as shown in the screenshot in the "**Exchange Directions**" -> "**Currency Exchange Direction Templates**" section:<br>
{% endhint %}

## **Bulk User Information Editor**

Starting from version 2.6, a module has been added to the script that allows you to edit text for each type of template for multiple directions on a single page.

The module settings can be found in the "**Exchange Directions**" -> "**Bulk User Information Editor**" section.

In the dropdown list, select the currency and/or payment system to display only the relevant templates from the exchange directions.

<figure><img src="../../../.gitbook/assets/image (1673)_eng.png" alt="" width="466"><figcaption></figcaption></figure>

You can apply from 1 to 4 filters or choose not to use any filters (but in this case, there is a high likelihood of the page freezing if a large number of directions are displayed on it (more than 50)).

<div><figure><img src="../../../.gitbook/assets/image (1674)_eng.png" alt="" width="473"><figcaption></figcaption></figure> <figure><img src="../../../.gitbook/assets/image (1676)_eng.png" alt="" width="420"><figcaption></figcaption></figure></div>

After filtering by currencies and payment systems, select the template you want to edit for the remaining exchange directions on the page and click the "**Filter**" button.

{% hint style="info" %}
You can also filter exchange directions by their status **after filtering** using the "**Filter**" button.

<img src="../../../.gitbook/assets/image (1680)_eng.png" alt="" data-size="original">
{% endhint %}

<figure><img src="../../../.gitbook/assets/image (1677)_eng.png" alt="" width="521"><figcaption></figcaption></figure>

After clicking the "**Filter**" button, the templates will be displayed in edit mode on the page — you can edit them as you wish (including using shortcodes):

<figure><img src="../../../.gitbook/assets/image (1678)_eng.png" alt=""><figcaption></figcaption></figure>

Then click the "**Save**" button to apply the changes.

<figure><img src="../../../.gitbook/assets/image (1679)_eng.png" alt="" width="563"><figcaption></figcaption></figure>

After these actions, the new/edited texts will be used on the request pages for these exchange directions.
