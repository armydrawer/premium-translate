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