# Verification of Payment Details

## Video Guide

{% embed url="https://www.youtube.com/watch?v=-UfEsyUv6tk" %}

The script includes a verification process for accounts/cards through the upload of images/photos. There is an option to restrict access to the exchange direction for unverified accounts on the site.

To activate account verification, please follow these steps:

## Activating **Automatic User Registration**

Go to the "**Modules**" section and ensure that the "**Automatic User Registration**" module is active. If necessary, activate it.

<figure><img src="../../../ru/.gitbook/assets/image (788) (1).png" alt=""><figcaption></figcaption></figure>

### Setting Up User Registration Notifications

Navigate to "**Messages**" -> "**Email Templates**".

<figure><img src="../../../ru/.gitbook/assets/image (789) (1).png" alt=""><figcaption></figcaption></figure>

Make sure that the email for the "**Registration Form**" is enabled. Users will automatically receive this email when they submit a request on the site.

<figure><img src="../../../ru/.gitbook/assets/image (790) (1).png" alt=""><figcaption></figcaption></figure>

Fill out the template.

<figure><img src="../../../ru/.gitbook/assets/image (791) (1).png" alt=""><figcaption></figcaption></figure>

## Setting Up Account Verification

In the site management panel, under the "**Modules**" section, activate the "**User Account Verification**" module.

<figure><img src="../../.gitbook/assets/image (1228)_eng.png" alt=""><figcaption></figcaption></figure>

In the site management panel, go to "**User Accounts**" → "**Settings**" and set the necessary verification options.

<figure><img src="../../../ru/.gitbook/assets/image (154) (1).png" alt=""><figcaption></figcaption></figure>

**Create currency accounts when submitting a request:**\
• **Yes** — the account will be automatically added to the user's profile, allowing them to select it again from a dropdown list for convenience.\
• **No**

**Prohibit adding an account number if it has already been added by another user:**\
• **Yes** — the user will not be able to add the same account to different accounts.\
• **No**

**Text on the account number addition page** — the text that will be displayed on the page for adding a new account/card in the personal cabinet of the exchange service.

**Allow users to submit verification requests:**\
• **Yes** — users will be able to send verification requests.\
• **No**

**Prohibit users from deleting verified accounts:**\
• **Yes** — users will not be able to delete verified accounts after they have been added to their personal cabinet.\
• **No**

**Allow creating requests if the account is not verified:**\
• **Yes** — users will be allowed to create a request even if the account is not verified; no error will be displayed, and they will proceed to the next step of creating the request.\
• **No**

**Verify account across all currencies** — when adding a new account, the number will be checked against the database for all currencies used by the exchange service. If the account number matches (even if it belongs to a different currency), the user will see an error indicating that the account has already been added by another user of the exchange service.

**Allow using verified accounts without authorization** — clients will have the option to use previously verified accounts without logging into their personal cabinet.

## Setting Up Verification in Currency Settings

In the site management panel, under the "**Currencies**" section, in the settings for the required currency, set "**Yes**" for the "**Account Verification Option**," specify the "**Number of Images to Upload**," and fill in the "**Account Verification Instructions**" field.

<figure><img src="../../.gitbook/assets/image (1100)_eng.png" alt=""><figcaption></figcaption></figure>

* **Account Verification Option** — select "**Yes**"
* **Number of Images to Upload** — set to **1** — this is a photo of the front side of the card against the website background.
* **Account Verification Instructions** — write the necessary text — for example, "Upload the card against the website background."

To allow account addition in the client's personal cabinet, activate the option "**Allow users to add account numbers in their profile**" on the "**Field Settings**" tab in the selected currency settings.

<figure><img src="../../.gitbook/assets/image (1787)_eng.png" alt=""><figcaption></figcaption></figure>

## Verification Settings in Exchange Direction

Go to "**Exchange Directions**" -> "**Exchange Directions**," select the desired direction, and navigate to the "**Verification**" tab.

<figure><img src="../../../ru/.gitbook/assets/image (797) (1).png" alt=""><figcaption></figcaption></figure>

On this tab, there are options for "**Verification of Account for Sending**" and "**Verification of Account for Receiving**."

**Verification of Account for Sending**

If the card is used as details for the currency being sent, select "**Yes**" — in this case, verification of the card will be requested when the user sends money from it. In the "**Exchange Amount for Sending**" field, specify the necessary amount above which verification is required.

**Verification of Account for Receiving**

If it is necessary to verify the card when the user receives funds, select "**Yes**," and in the "**Exchange Amount for Receiving**" field, specify the necessary amount above which verification is required.

Go to the "**User Information**" tab in the "**Exchange Directions**" section and find the "**Application Status: Pending Request**."\
\
Select the shortcode "**Link for Verification of Account for Sending**," so that when a user creates a request, the system displays a link for verification.\
\
In the "**Account Verification Instructions**" field, write text for the user. For example:\
"To continue the exchange, please verify your card \[**Account for Sending/account\_give]**. To do this, click the link and follow the instructions **\[Link for Verification of Account for Sending/create\_acc\_give]**."

{% hint style="info" %}
Typically, the instructions should describe the steps the user needs to take to complete the account verification.

For example, for verifying a bank card, you might ask the user to upload an image of the front side of the card against your website background. This instruction will be visible to the user in their personal cabinet when adding the account number in the "**Your Accounts**" section.
{% endhint %}

In the exchange direction settings, on the "**Verification**" tab, set the parameter "**Only for accounts verified on the site**" to "**Yes**."\
In this case, a request can only be created using accounts that have been verified on the site.

## Setting Up Notifications for Account Verification

In the site management panel, under "**Messages**" → "**Email Templates**," you need to configure and enable the relevant templates: "**Account Verification Request**," "**Successful Account Verification**," and "**Account Verification Denied**."

<figure><img src="../../../ru/.gitbook/assets/image (798) (1).png" alt=""><figcaption></figcaption></figure>

In the "**User Accounts**" -> "**Account Verification**" section, verification requests will be displayed, where you can compare the account from the request with the photo of the card, check the request, and select the "**Account Verified**" option. After this, the status of the request on the site will be updated for the user, allowing them to complete the exchange process.
