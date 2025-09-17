# How to Secure the Admin Panel of an Exchange Service

If someone hacks into the admin panel of your website, they can manipulate exchange rates and payment details for manual transactions. To protect the admin panel and the administrator account, we recommend taking the following steps:

- **Change the default admin password** as soon as you first access the system. You can find detailed instructions [here](https://premium.gitbook.io/rukovodstvo-polzovatelya/navigaciya/faq/kak-izmenit-parol-administratora).
  
- **Avoid using default usernames** like "admin," "superuser," or "administrator" for the admin account. Instead, create an admin account with a unique and complex username, and delete the original default admin account. When you delete the original admin account, the system will automatically reassign all pages and records to the new administrator.

- **Restrict access to the admin panel by IP address.** You can configure this in the "**Users → Your Profile → Allowed IP Addresses**" section.

- In the admin panel, go to "**Messages → Email Templates**" and set up the templates for "**Login Notification**" and "**One-Time Link Login.**" For more details on configuring email templates, refer to this [section](https://premium.gitbook.io/rukovodstvo-polzovatelya/navigaciya/uvedomleniya/opovesheniya-po-e-mail).

- In the admin panel, navigate to "**Users → Your Profile**" and enable "**Yes**" for the options "**Email Notification on Login**" and "**One-Time Link Login.**" These settings should be enabled for all users who have access to the admin panel. With these settings, every time an admin logs into the panel, they will receive a one-time login link via email, as well as a notification about the successful login.

- Each site administrator should use an email account that supports **SMS-based login verification**. Services like Gmail or Mail.ru offer this feature.

- **Do not save usernames and passwords in your browser.** This is a critical security measure to prevent unauthorized access.

- **Do not grant access to the admin panel to unauthorized individuals** unless absolutely necessary. If you must provide access, create a separate admin account for this purpose and delete it once the work is completed.

- **Avoid using third-party WordPress plugins.** Statistics show that vulnerabilities allowing unauthorized access to your site are often found in third-party plugins.

By following these recommendations, you can significantly reduce the risk of unauthorized access to your admin panel and ensure the security of your exchange service.