# Security Passwords

To set security passwords, you need to open the file `wp-content/plugins/premiumbox/userdata.php` on the server and enter the corresponding passwords in the lines specified below. Without entering the designated password in the admin panel, you will not be able to perform any action that is password-protected.

{% hint style="warning" %}
Use numbers and Latin letters in both uppercase and lowercase. A minimum length of 8 characters is recommended.
{% endhint %}

1. Security passwords for saving API keys for merchants and auto payouts. If the password is not entered, you will not be able to change the authorization details in the module.

```php
	/* 
	Security password for merchant settings and auto payouts
	*/
	if(!defined('MERCH_ACTION_PASSWORD')){
	    define('MERCH_ACTION_PASSWORD', 'ENTER_HERE');
	}
```

2. For automatic exchanges requiring confirmation from the operator, a security password must be entered by the operator after clicking the "**Transfer**" button. If the security password is not entered, the automatic payout will not be processed. Using this code enhances the security of your exchange service.

```php
        /* 
        Security password to confirm payments
        */
        if(!defined('PAY_ACTION_PASSWORD')){
            define('PAY_ACTION_PASSWORD', 'ENTER_HERE');
        }	
```

3. Security password for editing requests in the "**Requests**" section. Without entering this password, you will not be able to edit any data in the request.

```php
	/* 
	Security password for editing orders
	*/
	if(!defined('EDIT_ACTION_PASSWORD')){
	    define('EDIT_ACTION_PASSWORD', 'ENTER_HERE');
	}
```