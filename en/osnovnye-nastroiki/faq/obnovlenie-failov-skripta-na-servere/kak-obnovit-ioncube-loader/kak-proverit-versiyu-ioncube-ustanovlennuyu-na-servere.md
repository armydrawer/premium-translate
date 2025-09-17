# How to Check the Version of IonCube Installed on Your Server?

## Method #1

The IonCube version will be displayed at the very bottom of any page in the admin panel:

<figure><img src="../../../../.gitbook/assets/изображение (87).png" alt=""><figcaption></figcaption></figure>

## Method #2

In the root directory of your website on the server, create a temporary file with any name, for example, `test.php`, and include the following content:

```
<?php phpinfo(); ?>
```

<figure><img src="../../../../.gitbook/assets/изображение (102).png" alt="" width="563"><figcaption></figcaption></figure>

Open the page `https://your_domain/test.php` in a browser and locate the ionCube Loader section:

<figure><img src="../../../../.gitbook/assets/изображение (29).png" alt=""><figcaption></figcaption></figure>

{% hint style="warning" %}
Make sure to delete the file from the server after checking!
{% endhint %}