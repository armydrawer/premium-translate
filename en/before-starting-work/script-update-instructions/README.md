# Script Update Instructions

{% hint style="warning" %}
Before you begin updating the script, please review the list of changes in the new version of the **Premium Exchanger** script in the "[**Updates**](https://premiumexchanger.com/obnovleniya/)" section.

The standard theme has been updated, so if you upload theme files from the previous version, any code modifications you made to the standard theme will be lost. If you want to keep your code changes in the standard theme, do not upload the standard theme from the distribution during the update. Otherwise, we cannot guarantee the proper functioning of your website.

If you are using a unique theme that was **custom-made by us**, please contact technical support for theme adaptation before updating the script. To do this, send a zip file of your theme from the **`wp-content/themes`** folder (**<mark style="color:red;">**note that for updating the script from version 2.5 to 2.6, theme updates are not required!**</mark>**)**.

<img src="../../.gitbook/assets/image (1119)_eng.png" alt="" data-size="original">

Design updates on our end may take up to 10 days.

If you are using a unique theme that you or third-party specialists developed, you will need to adapt the theme **yourself** after updating the script.

If you are using additional paid modules, please contact [technical support](https://premiumexchanger.com/podderzhka/) for updated versions of the modules.
{% endhint %}

{% embed url="https://youtu.be/PpNKzThZsCs" %}
Video instructions for updating the script
{% endembed %}

{% hint style="warning" %}
You may need to update **ionCube Loader** and **WordPress** for the script to function correctly.

[Instructions for updating ionCube Loader](https://premium.gitbook.io/main/en/basic-settings/faq/kak-obnovit-ioncube-loader)

[Instructions for updating WordPress](https://premium.gitbook.io/main/en/basic-settings/faq/kak-obnovit-wordpress)
{% endhint %}

### Troubleshooting After the Update

* If the admin panel is not functioning correctly, replace the `userdata.php` file with the one from this page located in the `wp-content/plugins/premiumbox` folder, if the contents of the file on your server do not match the code provided below (except for the passwords specified in quotes):

{% file src="../../.gitbook/assets/userdata (2).php" %}

<details>

<summary>userdata.php (base file)</summary>

```php
<?php
/*
Please be careful! This file should only be edited in UTF-8 without (BOM).
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
	Code for encrypting data of merchants and auto payouts (set once). Use an arbitrary set of numbers and letters as a code.
	*/
	if (!defined('EXT_SALT')) {
		define('EXT_SALT', '');
	}
	
	/* 
	Personal hash for cron URLs and files with exchange rates
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