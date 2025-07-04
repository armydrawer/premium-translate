<?php
/*
Будьте внимательны! Данный файл необходимо редактировать только в кодировке UTF-8 без (BOM).
Attention please! You should edit this file in UTF-8 w/o (BOM) only.
*/

/**************** user data ******************/

	/* 
	Ваш личный код безопасности
	Your personal security code
	*/
	if(!defined('PN_SECRET_KEY')){
		define('PN_SECRET_KEY', '');
	}
	
	/* 
	Код для шифрования данных мерчантов и автовыплат (задается один раз). В качестве кода используйте произвольный набор цирф и букв.
	Code for encrypting data of merchants and auto payouts (set once). Use an arbitrary set of numbers and letters as a code.
	*/
	if(!defined('PN_HASH_KEY')){
		define('PN_HASH_KEY', '');
	}	
	
	/* 
	Персональный хэш для URL кронов и файлов с курсами
	Personal hash for cron URLs and files with exchange rates
	*/
	if(!defined('PN_HASH_CRON')){
		define('PN_HASH_CRON', ''); 
	}	
	
	/* 
	Время жизни сессии авторизации, в днях
	Authorization session length (days)
	*/
	if(!defined('PN_USERSESS_DAY')){
		define('PN_USERSESS_DAY', 7);
	}
	/* 
	Если забыли доступ, ставим true и заходим как обычно через /wp-admin. Также будет отключена ссылка авторизация по e-mail
	If you forgot to access the system, then set up the «True» and enter the system through /wp-admin. Note that in this case the authorization via e-mail link will be disabled.

	true(да/yes) false(нет/no)
	*/
	if(!defined('PN_ADMIN_GOWP')){
		define('PN_ADMIN_GOWP', 'false'); 
	}		

/**************** end user data ******************/