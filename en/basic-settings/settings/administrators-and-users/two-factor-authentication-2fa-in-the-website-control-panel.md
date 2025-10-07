---
description: >-
  Two-Factor Authentication (2FA) is a method of verifying a user's identity
  using two different methods, which adds an extra layer of security to your
  account and reduces the likelihood of hacking.
---

# Two-Factor Authentication (2FA) in the Website Control Panel

## 2FA via Email

Set up email notifications from the script according to the [instructions](https://premium.gitbook.io/main/osnovnye-nastroiki/uvedomleniya-administratoram-i-klientam/uvedomleniya-po-e-mail#nastroika-smtp).

In the website control panel, go to the "**Messages" → "Email Templates"** section. For the templates "**PIN Code Authentication**" and "**Notify User Login to Personal Account**," enable message sending and add the appropriate shortcodes from the panel above the text input field.

<figure><img src="../../../.gitbook/assets/image%20(2)_eng.png" alt="" width="563"><figcaption><p>Template "<strong>PIN Code Authentication</strong>"</p></figcaption></figure>

<figure><img src="../../../.gitbook/assets/image%20(1)%20(1)_eng.png" alt="" width="563"><figcaption><p>Template “<strong>Notify User Login to Personal Account</strong>”</p></figcaption></figure>

In the "**Users" (select user) →** set "**Yes**" for the options "**Notification on Login (Email)**" and "**PIN Code Authentication (Email)**."

<figure><img src="../../../.gitbook/assets/%D0%B8%D0%B7%D0%BE%D0%B1%D1%80%D0%B0%D0%B6%D0%B5%D0%BD%D0%B8%D0%B5%20(57)_eng.png" alt=""><figcaption></figcaption></figure>

These settings need to be enabled for all users who have access to the control panel. Each time an administrator/operator logs into the control panel, they will receive a PIN code for access via email.

If you want to use Telegram for receiving messages upon login, set up similar options in the "**Messages**" ➔ "**Telegram Templates**" section.

You can also configure PIN code sending via [SMS](https://premium.gitbook.io/rukovodstvo-polzovatelya/navigaciya/uvedomleniya/opovesheniya-po-sms) or [Telegram](https://premium.gitbook.io/main/osnovnye-nastroiki/uvedomleniya-administratoram-i-klientam/uvedomleniya-v-telegram). In this case, you will need to set up SMS or Telegram templates in the "**Messages**" section and enable the corresponding options in the user profile.

## 2FA Using an App

In your personal account on the website, go to the "**Security Settings**" section and enable the 2FA option. Then scan the QR code using a suitable [app](https://trashexpert.ru/mobile/apps/best-two-factor-authentication-apps).

<figure><img src="../../../.gitbook/assets/image%20(6)%20(1)_eng.png" alt="" width="563"><figcaption></figcaption></figure>

In the "**2FA Code**" field, enter the code provided by the app and click the "**Save**" button.

To verify that 2FA is activated, log out of your account and try to log in without entering the code.

If you receive an error and can log in again (with the code), the option is set up correctly.

<div><figure><img src="../../../.gitbook/assets/image%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)_eng.png" alt=""><figcaption><p>Admin Panel Login</p></figcaption></figure> <figure><img src="../../../.gitbook/assets/image%20(4)%20(1)%20(1)%20(1)%20(1)%20(1)_eng.png" alt="" width="563"><figcaption><p>Login to Personal Account on the Exchange Website</p></figcaption></figure></div>

If necessary, you can disable 2FA for any user in their profile settings (under the "**Users**" section).

<div><figure><img src="../../../.gitbook/assets/image%20(2)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)_eng.png" alt=""><figcaption><p>Disabling 2FA in the Admin Panel</p></figcaption></figure> <figure><img src="../../../.gitbook/assets/image%20(3)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)_eng.png" alt="" width="563"><figcaption><p>Disabling 2FA in the Personal Account</p></figcaption></figure></div>
