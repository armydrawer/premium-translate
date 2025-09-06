# Инструкция по обновлению скрипта

{% hint style="warning" %}
Перед тем, как приступать к обновлению скрипта, ознакомитесь со списком изменений новой версии скрипта **Premium Exchanger** в разделе "[**Обновления**](https://premiumexchanger.com/obnovleniya/)".

Обновилась стандартная тема, поэтому при загрузке файлов темы под предыдущую версию, ваши правки кода в стандартной теме будут утеряны. Если вы не хотите, чтобы ваши правки кода в стандартной теме были утеряны — не загружайте стандартную тему из дистрибутива во время обновления. В противном случае мы не сможем гарантировать корректную работу вашего сайта.

Если вы используете уникальную тему сайта, **которая была заказана у нас**, то обратитесь в техническую поддержку для адаптации темы перед обновлением скрипта — для этого пришлите архив с вашей темой из папки **`wp-content/themes` (**<mark style="color:red;">**но для обновления скрипта с версии 2.5 на 2.6 обновление темы не требуется!**</mark>**)**.

<img src="../../.gitbook/assets/image (1178).png" alt="" data-size="original">

Обновление дизайна с нашей стороны может занять до 10 дней.

Если вы используете уникальную тему, которая была разработана вами или сторонними специалистами — вам потребуется адаптировать тему **самостоятельно** после обновления скрипта.

Если вы используете дополнительные платные модули — обратитесь в [техническую поддержку](https://premiumexchanger.com/podderzhka/) за обновленными версиями модулей.
{% endhint %}

{% embed url="https://youtu.be/PpNKzThZsCs" %}
Видеоинструкция по обновлению скрипта
{% endembed %}

{% hint style="warning" %}
Возможно, что вам потребуется обновить **ionCube Loader** и **WordPress** для корректной работы скрипта.

[Инструкция по обновлению ionCube Loader](https://premium.gitbook.io/rukovodstvo-polzovatelya/osnovnye-nastroiki/faq/kak-obnovit-ioncube-loader)

[Инструкция по обновлению WordPress](https://premium.gitbook.io/rukovodstvo-polzovatelya/osnovnye-nastroiki/faq/kak-obnovit-wordpress)
{% endhint %}

### Устранение неполадок после обновления

* При некорректной работе панели администратора замените файл `userdata.php` файлом с этой страницы в папке `wp-content/plugins/premiumbox`, если содержимое файла на вашем сервере не совпадает с указанным ниже кодом (за исключением паролей, указываемых в кавычках):

{% file src="../../.gitbook/assets/userdata (2).php" %}

<details>

<summary>userdata.php (базовый файл)</summary>

```php
<?php
/*
Будьте внимательны! Данный файл необходимо редактировать только в кодировке UTF-8 без (BOM).
Attention please! You should edit this file in UTF-8 w/o (BOM) only.
*/

/**************** user data ******************/

	/* 
	Код безопасности для настроек мерчантов и автовыплат
	Security code for merchant settings and auto payouts
	*/
	if(!defined('MERCH_ACTION_PASSWORD')){
		define('MERCH_ACTION_PASSWORD', '');
	}
	
	/* 
	Код безопасности для подтверждения платежей
	Security code to confirm payments
	*/
	if(!defined('PAY_ACTION_PASSWORD')){
		define('PAY_ACTION_PASSWORD', '');
	}

	/* 
	Код безопасности для редактирования заявок
	Security code for editing orders
	*/
	if(!defined('EDIT_ACTION_PASSWORD')){
		define('EDIT_ACTION_PASSWORD', '');
	}	
	
	/* 
	Код для шифрования данных мерчантов и автовыплат (задается один раз). В качестве кода используйте произвольный набор цирф и букв.
	Code for encrypting data of merchants and auto payouts (set once). Use an arbitrary set of numbers and letters as a code.
	*/
	if (!defined('EXT_SALT')) {
		define('EXT_SALT', '');
	}
	
	/* 
	Персональный хэш для URL кронов и файлов с курсами
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
