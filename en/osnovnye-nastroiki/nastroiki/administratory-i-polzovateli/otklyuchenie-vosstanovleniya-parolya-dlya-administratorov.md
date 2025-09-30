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

# Disabling Password Recovery for Administrators

This setting is used to enhance security:\
users with access to the admin panel (including administrators and managers) **should not be able to recover their passwords through the standard recovery form**.\
This eliminates the risk of account takeover via email access.

#### How to Disable Password Recovery

<figure><img src="../../../.gitbook/assets/image (2) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1)_eng.png" alt="" width="432"><figcaption></figcaption></figure>

1. Go to the user management section (under "Users").
2. Find all users with the role:
   * **Administrator**
   * **Manager** (or any other role with admin access).
3. Open each user's profile.
4. Locate the **"Password Recovery"** setting.
5. Set the value to **"No"** (to disable it).
6. Save the changes.

#### How to Verify That the Setting Worked

* Attempt to initiate the password recovery process for such a user through the login form.
* The system should **deny the recovery** (displaying a message that the feature is unavailable).

#### Recommendations

* Use [2FA (two-factor authentication)](https://premium.gitbook.io/main/osnovnye-nastroiki/nastroiki/administratory-i-polzovateli/dvukhfaktornaya-avtorizaciya-2fa-v-paneli-upravleniya-saitom) for all users with admin access.
* For password resets, administrators should manually change the password through the admin panel or directly edit it in the database.
* Check this setting after adding new users with admin access rights.