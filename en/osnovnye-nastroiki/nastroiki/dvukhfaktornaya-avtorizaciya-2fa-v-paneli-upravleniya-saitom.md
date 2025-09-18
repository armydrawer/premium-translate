**Two-Factor Authentication (2FA) in the Website Control Panel**

## 2FA via Email

Set up email notifications from the script according to the [instructions](https://premium.gitbook.io/main/osnovnye-nastroiki/uvedomleniya-administratoram-i-klientam/uvedomleniya-po-e-mail#nastroika-smtp).

In the website control panel, go to the "**Messages**" → "**Email Templates**" section. For the templates "**PIN Code Authentication**" and "**Notify User Login to Personal Account**," enable message sending and add the corresponding shortcodes from the panel above the text input field.

<figure><img src="../../.gitbook/assets/image (2).png" alt="" width="563"><figcaption><p>Template for "<strong>PIN Code Authentication</strong>"</p></figcaption></figure>

<figure><img src="../../.gitbook/assets/image (1) (1).png" alt="" width="563"><figcaption><p>Template for "<strong>Notify User Login to Personal Account</strong>"</p></figcaption></figure>

In the "**Users**" section (select a user), set "**Yes**" for the options "**Notification on Login (Email)**" and "**PIN Code Authentication (Email)**."

<figure><img src="../../.gitbook/assets/изображение (57).png" alt=""><figcaption></figcaption></figure>

These settings need to be enabled for all users who have access to the control panel. Each time an administrator/operator logs into the control panel, they will receive a PIN code via email for access.

If you want to use Telegram for receiving login notifications, set up similar options in the "**Messages**" ➔ "**Telegram Templates**" section.

You can also configure PIN code sending via [SMS](https://premium.gitbook.io/rukovodstvo-polzovatelya/navigaciya/uvedomleniya/opovesheniya-po-sms) or [Telegram](https://premium.gitbook.io/main/osnovnye-nastroiki/uvedomleniya-administratoram-i-klientam/uvedomleniya-v-telegram). In this case, you will need to set up SMS or Telegram templates in the "**Messages**" section and enable the corresponding options in the user profile.

## 2FA Using an App

In your personal account on the website, go to the "**Security Settings**" section and enable the 2FA option. Then scan the QR code using a suitable [app](https://trashexpert.ru/mobile/apps/best-two-factor-authentication-apps).

<figure><img src="../../.gitbook/assets/image (6) (1).png" alt="" width="563"><figcaption></figcaption></figure>

In the "**2FA Code**" field, enter the code provided by the app and click the "**Save**" button.

To verify that 2FA is activated, log out of your account and try to log in without entering the code.

If you receive an error and can log in again (with the code), the option is set up correctly.

<div><figure><img src="../../.gitbook/assets/image (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption><p>Logging into the admin panel</p></figcaption></figure> <figure><img src="../../.gitbook/assets/image (4) (1) (1) (1) (1) (1).png" alt="" width="563"><figcaption><p>Logging into the personal account on the exchange website</p></figcaption></figure></div>

If necessary, you can disable 2FA for any user in their profile settings (in the "**Users**" section).

<div><figure><img src="../../.gitbook/assets/image (2) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption><p>Disabling 2FA in the admin panel</p></figcaption></figure> <figure><img src="../../.gitbook/assets/image (3) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt="" width="563"><figcaption><p>Disabling 2FA in the personal account</p></figcaption></figure></div>