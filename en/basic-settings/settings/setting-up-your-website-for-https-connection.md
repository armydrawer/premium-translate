# Setting Up Your Website for HTTPS Connection

{% hint style="warning" %}
If needed, you can [request our service](https://premiumexchanger.com/uslugi/#usl4) to configure your website for HTTPS connection.
{% endhint %}

To ensure your website loads securely over HTTPS, you need to:

1. Purchase an SSL certificate from your hosting provider.
2. In your website's control panel, go to the "**Settings" → "General"** section, specify your website's address using the HTTPS protocol, and save the changes.

<figure><img src="../../.gitbook/assets/image (1021)_eng.png" alt=""><figcaption></figcaption></figure>

## How to Specify Your Website Address Using HTTPS if You Can't Access the Control Panel?

On the server, open the file `/wp-content/themes/exchanger/functions.php` and add the following lines after `<?php` (make sure to replace "**your domain**" with your actual domain) and save the changes:

```
update_option('siteurl', 'https://ваш_домен');
update_option('home', 'https://ваш_домен');
```

After completing the setup, be sure to remove the added lines.

3. Contact your hosting provider's technical support to request the installation of the SSL certificate (be prepared to provide any necessary information) and ask them to set up a redirect from HTTP to HTTPS.

{% hint style="info" %}
Here’s an example of redirect code for the hosting provider reg.ru. It may also work with other hosting providers. This code should be added at the beginning of the `.htaccess` file located in your website's root folder.

**`Options +FollowSymLinks`**

**`RewriteEngine On`**

**`RewriteBase /`**

**`RewriteCond %{SERVER_PORT} |^443$`**

**`RewriteCond %{HTTPS} off`**

**`RewriteRule ^(.*)$ https://ваш_домен/$1 [R=301,L]`**
{% endhint %}

4. On the server, open the file `ваш_домен/wp-config.php` and add the following lines after `define(‘WP_DEBUG’, false);`, then save the changes:

```
define('FORCE_SSL_LOGIN', true);
define('FORCE_SSL_ADMIN', true);
```

If you encounter errors, experience a redirect loop, or see your site without styles after making these changes, follow these steps:

* In the file `ваш_домен/wp-config.php`, add the line:

```
$_SERVER['HTTPS'] = 'on';
```

* At the very end of the file `ваш_домен/index.php`, add the line:

```
($_SERVER['HTTP_X_HTTPS'] == 'on') ? $_SERVER['HTTPS'] = 'on' : "";
```

If the error persists, please refer to the [diagnostic guide.](https://premium.gitbook.io/main/en/basic-settings/faq/diagnostika-i-reshenie-oshibok-pri-rabote-so-skriptom#nestabilnaya-rabota-saita-na-protokole-https)