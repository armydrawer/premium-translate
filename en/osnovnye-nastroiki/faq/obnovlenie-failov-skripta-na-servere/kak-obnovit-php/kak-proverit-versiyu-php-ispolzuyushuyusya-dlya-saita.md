# How to Check the PHP Version Used by Your Website

## Using ISP Manager

Log in to ISP Manager with any user account that has access to the website's files, and navigate to the "**Sites**" section. In the "**Handler**" column, you will see the PHP version currently being used by the website.

<figure><img src="../../../../.gitbook/assets/image (1718)_eng.png" alt=""><figcaption></figcaption></figure>

## Checking the PHP Version in a Browser

Connect to your server via FTP or SSH and navigate to the root directory of your website. Create a file named [`phpversion.php`](#user-content-fn-1)[^1] with the following content:

```php
<?php phpinfo(); ?>
```

<figure><img src="../../../../.gitbook/assets/image (1720)_eng.png" alt="" width="488"><figcaption></figcaption></figure>

Next, open your website in a browser and append the file's name to the URL in the address bar:

<figure><img src="../../../../.gitbook/assets/image (1719)_eng.png" alt=""><figcaption></figcaption></figure>

If everything is set up correctly, a large table containing information about PHP and its installed extensions will be displayed. At the very top of the page, you will see the PHP version.

If you don’t want to display the entire table of PHP information, you can output just the PHP version. To do this, replace the content of the `phpversion.php` file with the following line:

```php
<?php echo phpversion(); ?>
```

<figure><img src="../../../../.gitbook/assets/image (1722)_eng.png" alt="" width="473"><figcaption></figcaption></figure>

As a result, you will see a page like this:

<figure><img src="../../../../.gitbook/assets/image (1721)_eng.png" alt=""><figcaption></figcaption></figure>

[^1]: The file name is just an example; you can use any name you prefer.