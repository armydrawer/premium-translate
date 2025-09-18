---
description: >-
  If you hack into the website's control panel, you can manipulate exchange rates and the details of the exchange service for manual transactions.
---

# How to Secure the Exchange Control Panel

To protect the exchange control panel and the administrator account, we recommend taking the following steps:

* Change the default administrator password when you first access the system. More details can be found [here](https://premium.gitbook.io/rukovodstvo-polzovatelya/navigaciya/faq/kak-izmenit-parol-administratora).
* Avoid using standard usernames (like admin, superuser, administrator, etc.) for the website administrator. Create an administrator account with a unique and complex username, and delete the original administrator account. When you delete the original administrator account, the system will reassign all pages and posts to the new administrator.
* Set up IP address restrictions for accessing the control panel in the "**Users" → "Your Profile" → "Allowed IP Addresses"** section.
* In the control panel, under "**Messages" → "Email Templates,"** configure the templates for "**Login Notification**" and "**One-Time Link Authorization.**" For more information on setting up templates, see this [section](https://premium.gitbook.io/rukovodstvo-polzovatelya/navigaciya/uvedomleniya/opovesheniya-po-e-mail).
* In the control panel, go to "**Users" →** select your profile **→** set "**Yes**" for the options "**Email Notification on Login**" and "**One-Time Link Authorization.**" These settings should be enabled for all users who have access to the control panel. Each time an administrator logs into the control panel, they will receive a one-time link for access via email. Additionally, the administrator will receive an email notification of successful login to the control panel.
* Every website administrator should use an email account with active SMS confirmation for authorization in their profile settings. Services like Gmail or Mail.ru support SMS authorization.
* We recommend <mark style="color:red;">**not to save**</mark> usernames and passwords in your browser.
* Do not grant access to the control panel to unauthorized users unless absolutely necessary. For such purposes, create a separate administrator account and remember to delete it after access has been granted and tasks completed.
* Avoid using third-party plugins for WordPress. Statistics show that vulnerabilities that could allow access to your site are often found in third-party plugins.