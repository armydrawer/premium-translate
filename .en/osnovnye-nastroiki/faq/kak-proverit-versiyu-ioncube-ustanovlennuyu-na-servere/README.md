# How to Check the IonCube Version Installed on Your Server

## Method 1

The IonCube version is displayed at the very bottom of any page in the admin panel:

<figure><img src="../../../.gitbook/assets/изображение (87).png" alt=""><figcaption></figcaption></figure>

## Method 2

Create a temporary file with any name (for example, `test.php`) in the root directory of your website on the server, containing the following code:

```php
<?php phpinfo(); ?>
```

<figure><img src="../../../.gitbook/assets/изображение (102).png" alt="" width="563"><figcaption></figcaption></figure>

Open the page `https://your_domain/test.php` in your browser and look for the ionCube Loader section:

<figure><img src="../../../.gitbook/assets/изображение (29).png" alt=""><figcaption></figcaption></figure>

{% hint style="warning" %}
Be sure to delete this file from the server after checking!
{% endhint %}