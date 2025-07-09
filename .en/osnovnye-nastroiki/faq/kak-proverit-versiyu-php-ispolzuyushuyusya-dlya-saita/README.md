# How to Check the PHP Version Used by Your Website

## Using ISP Manager

Log in to ISP Manager with any user account that has access to the website files, then go to the "**Sites**" section. In the "**Handler**" column, you will see the PHP version currently used by the site.

<figure><img src="../../../.gitbook/assets/image (1718).png" alt=""><figcaption></figcaption></figure>

## Checking the PHP Version in Your Browser

Connect to your server via FTP or SSH and navigate to your website’s root directory. There, create a file named [`phpversion.php`](#user-content-fn-1)[^1] with the following content:

```php
<?php phpinfo(); ?>
```

<figure><img src="../../../.gitbook/assets/image (1720).png" alt="" width="488"><figcaption></figcaption></figure>

Next, open your website in a browser and add the filename to the URL:

<figure><img src="../../../.gitbook/assets/image (1719).png" alt=""><figcaption></figcaption></figure>

If everything is set up correctly, a detailed table will appear showing information about PHP and installed extensions. The PHP version will be displayed at the very top of the page.

If you prefer not to display the full PHP info table and only want to show the PHP version, replace the content of `phpversion.php` with this line:

```php
<?php echo phpversion(); ?>
```

<figure><img src="../../../.gitbook/assets/image (1722).png" alt="" width="473"><figcaption></figcaption></figure>

This will produce a page like this:

<figure><img src="../../../.gitbook/assets/image (1721).png" alt=""><figcaption></figcaption></figure>

[^1]: The filename is just an example—you can use any name you like.