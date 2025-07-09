# Payment Details Verification

## Video Tutorial

{% embed url="https://www.youtube.com/watch?v=-UfEsyUv6tk" %}

The script includes verification of accounts/cards by uploading images or photos. It also allows restricting access to exchange directions for accounts that have not been verified on the site.

To enable account verification, follow these steps:

## Enabling **Automatic User Registration**

Go to the "**Modules**" section and make sure the "**Automatic User Registration**" module is enabled. If it’s not active, enable it.

<figure><img src="../../.gitbook/assets/image (788).png" alt=""><figcaption></figcaption></figure>

### Setting Up User Registration Notifications

Navigate to "**Messages**" → "**E-mail Templates**."

<figure><img src="../../.gitbook/assets/image (789).png" alt=""><figcaption></figcaption></figure>

Make sure the email for "**Registration Form**" is enabled. This email will be sent automatically to users when they submit a request on the site.

<figure><img src="../../.gitbook/assets/image (790).png" alt=""><figcaption></figcaption></figure>

Fill out the email template as needed.

<figure><img src="../../.gitbook/assets/image (791).png" alt=""><figcaption></figcaption></figure>

## Configuring Account Verification

In the site control panel, go to the "**Modules**" section and activate the "**User Account Verification**" module.

<figure><img src="../../.gitbook/assets/image (1228).png" alt=""><figcaption></figcaption></figure>

Then, in the control panel under "**User Accounts** → **Settings**," configure the verification settings as required.

<figure><img src="../../.gitbook/assets/image (154).png" alt=""><figcaption></figcaption></figure>

**Create currency accounts when submitting a request:**  
• **Yes** — the account will be automatically added to the user’s profile, allowing them to select it again from a dropdown list for convenience  
• **No**

**Prevent adding an account number if it’s already been added by another user:**  
• **Yes** — users won’t be able to add the same account to multiple accounts  
• **No**

**Text on the account number addition page** — this text will be displayed on the page where users add a new account/card in their personal exchange cabinet.

**Allow adding requests:**  
• **Yes** — users will be able to submit verification requests  
• **No**

**Prevent users from deleting verified accounts:**  
• **Yes** — users will not be able to delete verified accounts once they have been added in their personal account  
• **No**

**Allow creating requests if the account is not verified:**  
• **Yes** — users will be allowed to create a request even if the account is not verified; no error will be shown, and the process will proceed to the next step of creating the request  
• **No**

**Check account number across all currencies** — when adding a new account, the system will check the account number against the database for all currencies supported by the exchanger. If the account number matches an existing one (even if it belongs to a different currency), the user will see an error indicating that the account has already been added by another exchanger user.

**Allow using verified accounts without authorization** — clients will be able to use previously verified accounts without logging into their personal account.

---

## Verification Settings in Currency Configuration

In the website admin panel, go to the "**Currencies**" section. In the settings for the desired currency, set "**Enable account verification**" to "**Yes**", specify the "**Number of images to upload**", and fill in the "**Account verification instructions**" field.

<figure><img src="../../.gitbook/assets/image (1100).png" alt=""><figcaption></figcaption></figure>

* **Enable account verification** — select "**Yes**"  
* **Number of images to upload** — set to **1** (this should be a photo of the front side of the card against the website background)  
* **Account verification instructions** — enter the required text, for example: "Upload a photo of your card against the website background"

To allow users to add account numbers in their personal profiles, enable the option "**Allow users to add account numbers in profile**" on the "**Field Settings**" tab within the selected currency’s settings.

<figure><img src="../../.gitbook/assets/image (1787).png" alt=""><figcaption></figcaption></figure>

---

## Verification Settings in Exchange Direction

[The continuation of this section would follow here.]

Go to the "**Exchange Directions**" section -> "**Exchange Directions**", select the desired direction, and open the "**Verification**" tab.

<figure><img src="../../.gitbook/assets/image (797).png" alt=""><figcaption></figcaption></figure>

On this tab, you will find the options "**Verification of the Account I Give**" and "**Verification of the Account I Receive**".

**Verification of the Account I Give**

If the card is used as the payment details for the currency you are giving, select "**Yes**". This will require card verification whenever the user sends money from this card. In the "**Exchange Amount for Giving**" field, specify the minimum amount above which verification should be requested.

**Verification of the Account I Receive**

If you need to verify the card when the user receives funds, select "**Yes**" and specify the minimum amount in the "**Exchange Amount for Receiving**" field, above which verification will be required.

Next, go to the "**User Information**" tab in the "**Exchange Directions**" -> "**Exchange Directions**" section and find the "**Application Status: Pending**" setting.

Select the shortcode "**Link to Verification of the Account I Give**" so that when a user creates an application, the system displays a link to the verification page.

In the "**Verification Instructions for the Account**" field, enter the text that will be shown to the user. For example:  
"To continue with the exchange, please verify the card \[**Account I Give/account_give]**. To do this, follow the link and follow the instructions **\[Link to Verification of the Account I Give/create_acc_give]**."

{% hint style="info" %}
Typically, the instructions should clearly explain the steps the user needs to take to complete account verification.

For example, for bank card verification, you might ask the user to upload a photo of the front side of the card against the background of your website. The user will see these instructions in their personal account when adding an account number under the "**Your Accounts**" section.
{% endhint %}

In the exchange direction settings, on the "**Verification**" tab, set the "**Only for site-verified accounts**" option to "**Yes**."

This means that requests can only be created involving accounts that have been verified on the site.

## Setting Up Account Verification Notifications

In the site control panel, go to "**Messages** → **E-mail Templates**" and configure and enable the following templates: "**Account Verification Request**," "**Account Successfully Verified**," and "**Account Verification Denied**."

<figure><img src="../../.gitbook/assets/image (798).png" alt=""><figcaption></figcaption></figure>

In the "**User Accounts**" section under "**Account Verification**," you will see verification requests. Here, you can compare the account details from the request with the photo of the card, check the box next to the request, and select "**Account Verified**." Once done, the request status on the user’s site profile will be updated, allowing them to complete the exchange process.