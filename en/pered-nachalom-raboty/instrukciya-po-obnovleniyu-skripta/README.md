# Script Update Instructions

{% hint style="warning" %}
Before starting the script update, please review the list of changes in the new version of the **Premium Exchanger** script in the "[**Updates**](https://premiumexchanger.com/obnovleniya/)" section.

The default theme has been updated, so if you upload the theme files from the previous version, any custom code changes you made in the default theme will be lost. If you want to keep your customizations in the default theme, **do not upload the default theme from the distribution during the update**. Otherwise, we cannot guarantee your website will function correctly.

If you are using a custom site theme **that was ordered from us**, please contact technical support to adapt the theme before updating the script. To do this, send an archive of your theme folder from **`wp-content/themes`** (**<mark style="color:red;">**but note that updating the theme is not required when upgrading the script from version 2.5 to 2.6!**</mark>**).

<img src="../../.gitbook/assets/image (1119).png" alt="" data-size="original">

Design updates from our side may take up to 10 days.

If you are using a custom theme developed by yourself or third-party specialists, you will need to adapt the theme **yourself** after updating the script.

If you use additional paid modules, please contact [technical support](https://premiumexchanger.com/podderzhka/) to get updated versions of the modules.
{% endhint %}

{% embed url="https://youtu.be/PpNKzThZsCs" %}
Video tutorial on updating the script
{% endembed %}

{% hint style="warning" %}
You may need to update **ionCube Loader** and **WordPress** for the script to work properly.

[ionCube Loader update instructions](https://premium.gitbook.io/rukovodstvo-polzovatelya/osnovnye-nastroiki/faq/kak-obnovit-ioncube-loader)

[WordPress update instructions](https://premium.gitbook.io/rukovodstvo-polzovatelya/osnovnye-nastroiki/faq/kak-obnovit-wordpress)
{% endhint %}

### Troubleshooting After the Update

* If the admin panel is not working correctly, replace the `userdata.php` file in the `wp-content/plugins/premiumbox` folder with the file from this page, if the contents of the file on your server do not match the code below (except for passwords enclosed in quotes):

{% file src="../../.gitbook/assets/userdata (2).php" %}

<details>

Here is a natural, fluent English translation of the given PHP file comments and code:

```php
<?php
/*
Please note! This file should only be edited in UTF-8 encoding without BOM.
*/

/**************** user data ******************/

	/* 
	Security code for merchant settings and automatic payouts
	*/
	if(!defined('MERCH_ACTION_PASSWORD')){
		define('MERCH_ACTION_PASSWORD', '');
	}
	
	/* 
	Security code for payment confirmations
	*/
	if(!defined('PAY_ACTION_PASSWORD')){
		define('PAY_ACTION_PASSWORD', '');
	}

	/* 
	Security code for editing requests/orders
	*/
	if(!defined('EDIT_ACTION_PASSWORD')){
		define('EDIT_ACTION_PASSWORD', '');
	}	
	
	/* 
	Code used to encrypt merchant data and auto payouts (set once). 
	Use any combination of letters and numbers as the code.
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

Let me know if you want the comments rewritten in a more formal or more casual style!