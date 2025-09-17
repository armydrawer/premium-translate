# Script Update Instructions

{% hint style="warning" %}
Before proceeding with the script update, make sure to review the list of changes in the new version of the **Premium Exchanger** script in the "[**Updates**](https://premiumexchanger.com/obnovleniya/)" section.

The default theme has been updated. If you upload the theme files from the previous version, any custom code changes you made to the default theme will be lost. To avoid losing your custom code changes in the default theme, **do not upload the default theme from the distribution package during the update process**. Otherwise, we cannot guarantee the proper functioning of your website.

If you are using a custom theme **ordered from us**, please contact technical support to adapt the theme before updating the script. To do this, send an archive of your theme from the **`wp-content/themes`** folder (**<mark style="color:red;">**note: updating the theme is not required when upgrading the script from version 2.5 to 2.6!**</mark>**).

<img src="../../.gitbook/assets/image (1119).png" alt="" data-size="original">

Updating the design on our end may take up to 10 days.

If you are using a custom theme developed by yourself or third-party specialists, you will need to adapt the theme **on your own** after updating the script.

If you are using additional paid modules, please contact [technical support](https://premiumexchanger.com/podderzhka/) to obtain updated versions of the modules.
{% endhint %}

{% embed url="https://youtu.be/PpNKzThZsCs" %}
Video tutorial on updating the script
{% endembed %}

{% hint style="warning" %}
You may need to update **ionCube Loader** and **WordPress** to ensure the script functions correctly.

[Guide to updating ionCube Loader](https://premium.gitbook.io/rukovodstvo-polzovatelya/osnovnye-nastroiki/faq/kak-obnovit-ioncube-loader)

[Guide to updating WordPress](https://premium.gitbook.io/rukovodstvo-polzovatelya/osnovnye-nastroiki/faq/kak-obnovit-wordpress)
{% endhint %}

### Troubleshooting After the Update

* If the admin panel is not functioning correctly, replace the `userdata.php` file in the `wp-content/plugins/premiumbox` folder with the file provided on this page. Do this only if the content of the file on your server does not match the code below (excluding passwords, which are specified in quotation marks):

{% file src="../../.gitbook/assets/userdata (2).php" %}

<details>

<summary>userdata.php (base file)</summary>

```php
<?php
/*
Please note! This file must be edited in UTF-8 encoding without BOM.
Attention please! You should edit this file in UTF-8 w/o BOM only.
*/

/**************** user data ******************/

	/* 
	Security code for merchant settings and auto payouts
	*/
	if(!defined('MERCH_ACTION_PASSWORD')){
		define('MERCH_ACTION_PASSWORD', '');
	}
	
	/* 
	Security code to confirm payments
	*/
	if(!defined('PAY_ACTION_PASSWORD')){
		define('PAY_ACTION_PASSWORD', '');
	}

	/* 
	Security code for editing orders
	*/
	if(!defined('EDIT_ACTION_PASSWORD')){
		define('EDIT_ACTION_PASSWORD', '');
	}	
	
	/* 
	Code for encrypting merchant and auto payout data (set once). Use any combination of numbers and letters as the code.
	*/
	if (!defined('EXT_SALT')) {
		define('EXT_SALT', '');
	}
	
	/* 
	Personal hash for cron URLs and exchange rate files
	*/
	if(!defined('PN_HASH_CRON')){
		define('PN_HASH_CRON', '');
	}	

	if(!defined('PN_ADMIN_GOWP')){
		define('PN_ADMIN_GOWP', 'false'); 
	}		

/**************** end user data ******************/
```

</details>