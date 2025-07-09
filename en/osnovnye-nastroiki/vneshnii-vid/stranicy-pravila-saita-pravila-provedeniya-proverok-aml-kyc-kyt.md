# Pages "Site Rules," "AML/KYC/KYT Verification Rules"

## Settings for v2.4

### "Site Rules" Page

The site rules page comes pre-installed and is usually located at _https://your_domain/**tos**_ (you can change the page URL if needed via the **"Edit"** button in the **"Pages"** section).

You can edit the page content and other settings (SEO text, keywords, title) through the admin panel under **Pages**, or directly on the page using the **"Edit Page"** button.

<figure><img src="../../.gitbook/assets/image (1191).png" alt=""><figcaption><p>The "<strong>Pages</strong>" section</p></figcaption></figure>

<figure><img src="../../.gitbook/assets/image (1055).png" alt=""><figcaption><p>Exchange site page</p></figcaption></figure>

### "AML/KYC/KYT Verification Rules" Page

You need to create this page manually and add your own text. Be sure to note the page URL, as you will need it later.

<figure><img src="../../.gitbook/assets/image (969).png" alt=""><figcaption></figcaption></figure>

{% hint style="info" %}
If you are using version 2.4, you must download and unzip the module into the `wp-content/plugins/premiumbox/moduls` folder.
{% endhint %}

{% file src="../../.gitbook/assets/additionalrules.zip" %}
Module download
{% endfile %}

Go to **Modules** -> **Modules** and activate the "**Additional Rules**" module.

<figure><img src="../../.gitbook/assets/image (1132).png" alt=""><figcaption></figcaption></figure>

To create the page, go to **Pages** and create a new page with your AML/KYC/KYT rules.

Then go to **Exchange Settings** -> **General Settings** and enter the consent text for the rules, as well as the error message text that will appear if the rules are not accepted.

<figure><img src="../../.gitbook/assets/image (1058).png" alt=""><figcaption></figcaption></figure>

{% hint style="info" %}
Replace **/aml/** with the URL of the page you created.
{% endhint %}

## Settings for v2.5 and Later

Go to **Exchange Settings** -> **General Settings** and in the field **"Text for the acceptance checkbox before submitting a request"**, enter the following text:

```
I have read and agree to the <a href="/tos/" target="_blank">exchange terms</a> and the <a href="/aml/" target="_blank">AML verification rules</a>.
```

<figure><img src="../../.gitbook/assets/image (1035).png" alt=""><figcaption></figcaption></figure>

## Display Settings



You can choose the step at which the rules text and the acceptance checkbox will be displayed. In the "**Exchange Settings**" section -> "**General Settings**," find the option "**Use exchange step #2, where the user confirms their details**."

<figure><img src="../../.gitbook/assets/изображение (81).png" alt=""><figcaption></figcaption></figure>

If you select "No," the text will appear immediately on the exchange page:

<figure><img src="../../.gitbook/assets/изображение (135).png" alt=""><figcaption></figcaption></figure>

If you select "Yes," the text will be shown on the next step, after the application details have been filled in:

<figure><img src="../../.gitbook/assets/изображение (140).png" alt=""><figcaption></figcaption></figure>