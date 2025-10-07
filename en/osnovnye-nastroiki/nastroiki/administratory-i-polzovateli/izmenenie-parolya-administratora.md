---
layout:
  width: default
  title:
    visible: true
  description:
    visible: false
  tableOfContents:
    visible: true
  outline:
    visible: true
  pagination:
    visible: true
  metadata:
    visible: true
---

# Changing the Administrator Password

## Password Change

Go to the "**Users**" section ➔ **"Users"**, find the relevant administrator account, and go to the settings by clicking the "**edit**" link.

<figure><img src="../../../.gitbook/assets/Screenshot_25 (1)_eng.png" alt=""><figcaption></figcaption></figure>

Locate the "**New Password**" field, enter a new password manually or use the password generator (the gear icon to the right of the field), and save the changes.

<figure><img src="../../../.gitbook/assets/Screenshot_26 (1)_eng.png" alt=""><figcaption></figcaption></figure>

After changing the password for the administrator/manager/operator (any user with access to the admin panel), <mark style="color:red;">**be sure to**</mark> log out of all active sessions by clicking the "**log out of all devices**" button.\
Then, log back into the chosen account.

{% hint style="warning" %}
**Why this is important:**\
Logging out immediately ends all active sessions, including those of potential intruders, even if they accessed the account using stolen tokens or cookies. This helps prevent data theft, unauthorized changes, and the installation of hidden backdoors. Quick action minimizes damage, reduces the risk of further breaches, and simplifies incident investigation.
{% endhint %}

Steps to follow:

* Log into the administrator profile settings (in the "**Users**" section).
* Click the **"log out of all devices"** button (including the current session).

    <figure><img src="../../../.gitbook/assets/image (2198)_eng.png" alt="" width="430"><figcaption></figcaption></figure>
* Immediately change the password for this account to a new, more complex one (that hasn't been used before).
* Enable [**two-factor authentication (2FA)**](https://premium.gitbook.io/main/osnovnye-nastroiki/nastroiki/administratory-i-polzovateli/dvukhfaktornaya-avtorizaciya-2fa-v-paneli-upravleniya-saitom) if it hasn't been turned on yet.
* Notify the security team or senior administrator.