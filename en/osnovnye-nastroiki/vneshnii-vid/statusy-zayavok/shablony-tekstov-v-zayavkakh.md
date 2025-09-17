# Text Templates in Applications

To display different text for various application statuses on the exchanger page, the system provides the ability to use templates.

## General Templates

To create templates, navigate to the "**Exchange Directions**" section -> "**Currency Exchange Direction Templates**."

In this section, select the desired item and proceed to edit it. Note that the set of fields available for editing varies depending on the selected item from the dropdown menu.

<figure><img src="../../../.gitbook/assets/изображение (152).png" alt=""><figcaption></figcaption></figure>

Let’s take, for example, the configuration of a template for the "**New Application**" status:

<figure><img src="../../../.gitbook/assets/изображение (40).png" alt=""><figcaption></figcaption></figure>

**Title for the Website** – The status title that will be displayed on the page. (For multilingual exchangers, you need to configure different language versions of the text by clicking the flag above the field and filling in the opened field.)

**Short Description of the Status** – A description of the current application status. (For multilingual exchangers, you need to configure different language versions of the text by clicking the flag above the field and filling in the opened field.)

**Page Refresh Options:**  
• **None** – The user will need to manually refresh the application page.  
• **Auto-refresh** – The page will automatically refresh at a specified interval. (The user can disable auto-refresh by clicking the "**Disable Refresh**" button.)  
![](<../../../.gitbook/assets/изображение (164).png>)  
• **By Button** – A button to enable the "**Auto-refresh**" mode will be displayed on the application page.  
![](<../../../.gitbook/assets/изображение (58).png>)

**Auto-refresh Interval (sec.)** – The interval at which the page will refresh automatically.

**How to Display the Description from the Form Below:**  
• **Display Only the Relevant Description from the Exchange Direction** – The text from the exchange direction will always be displayed for the corresponding status on the application page. (If no text is specified, a blank field will be shown.)  
• **If No Description is Set in the Exchange Direction, Display the One from the Form Below** – If text is specified in the "**User Information**" section of the exchange direction (in any language version), it will be displayed. Otherwise, the text from the template below will be shown.  
• **Always Display the Description from the Form Below** – The text from the template below will always be displayed for the corresponding status on the application page.

**Text** – The text that will be displayed on the application page for the corresponding status. Use shortcodes to include variables in the text.

<figure><img src="../../../.gitbook/assets/изображение (95).png" alt=""><figcaption></figcaption></figure>

## Individual Templates

You can also use individual text for different exchange directions. To do this, go to the exchange direction settings, open the "**User Information**" tab, and fill in the corresponding templates with text. (For multilingual exchangers, you need to configure different language versions of the text by clicking the flag above the field and filling in the opened field.)

{% hint style="info" %}
If both general and individual templates are filled for the same status, and you want the text from the exchange direction to be displayed, set the option in the "**Exchange Directions**" -> "**Currency Exchange Direction Templates**" section as shown in the screenshot:  
![](<../../../.gitbook/assets/изображение (155).png>)
{% endhint %}

<figure><img src="../../../.gitbook/assets/изображение (27).png" alt=""><figcaption></figcaption></figure>

## **Mass Editor for User Information**

Starting from version 2.6, a module has been added to the script that allows you to edit text for each template type across multiple exchange directions on a single page.

The module settings can be found in the "**Exchange Directions**" -> "**Mass Editor for User Information**" section.

In the dropdown menu, select the currency and/or payment system to display only the necessary templates from the exchange directions.

<figure><img src="../../../.gitbook/assets/image (1673).png" alt="" width="466"><figcaption></figcaption></figure>

You can apply between 1 and 4 filters for filtering or choose not to use any filters. (However, if no filters are applied and a large number of exchange directions are displayed on the page—more than 50—there is a high chance of the page freezing.)

<div><figure><img src="../../../.gitbook/assets/image (1674).png" alt="" width="473"><figcaption></figcaption></figure> <figure><img src="../../../.gitbook/assets/image (1676).png" alt="" width="420"><figcaption></figcaption></figure></div>

After filtering by currencies and payment systems, select the template you want to edit for the remaining exchange directions on the page and click the "**Filter**" button.

{% hint style="info" %}
You can also filter exchange directions by their status **after filtering** by clicking the "**Filter**" button.

<img src="../../../.gitbook/assets/image (1680).png" alt="" data-size="original">
{% endhint %}

<figure><img src="../../../.gitbook/assets/image (1677).png" alt="" width="521"><figcaption></figcaption></figure>

After clicking the "**Filter**" button, the templates will be displayed in edit mode on the page. Edit them as needed (including using shortcodes):

<figure><img src="../../../.gitbook/assets/image (1678).png" alt=""><figcaption></figcaption></figure>

Then click the "**Save**" button to apply the changes.

<figure><img src="../../../.gitbook/assets/image (1679).png" alt="" width="563"><figcaption></figcaption></figure>

After completing these steps, the new/edited texts will be used on the application pages for these exchange directions.