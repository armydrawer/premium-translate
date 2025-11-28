# Хуки

Через файл хуков вы можете добавить некоторые опции, отсутствующие в скрипте "из коробки".

Для этого разместите необходимые хуки в файле **`wp-content/plugins/premiumhook/premiumhook.php`**

Вставляйте хуки после нижеуказанных строк на новые строчки (после красной черты на скриншоте):

{% code overflow="wrap" %}
```php
<?php
}
```
{% endcode %}

<figure><img src="../../.gitbook/assets/image (21) (1).png" alt="" width="555"><figcaption></figcaption></figure>

Затем в разделе "**Плагины**" активируйте плагин "**Premium Exchanger hooks**".

<figure><img src="../../.gitbook/assets/image (1365).png" alt=""><figcaption></figcaption></figure>

## Доступные хуки:

<details>

<summary>Баннеры в партнерской программе</summary>

В партнерской программе существуют промо-материалы.

По умолчанию, это текстовые материалы и баннеры разных размеров.

Существует фильтр, благодаря которому можно изменять их названия и кол-во:

```php
add_filter('pp_banners','my_pp_banners', 1000);
function my_pp_banners($banners){
	
	$banners = array(
		'text'=> __('Text materials','pn'),
		'banner1'=> __('Banners','pn').'(468 x 60)',
		'banner2'=> __('Banners','pn').'(200 x 200)',
		'banner3'=> __('Banners','pn').'(120 x 600)',
		'banner4'=> __('Banners','pn').'(100 x 100)',
		'banner5'=> __('Banners','pn').'(88 x 31)',
		'banner6'=> __('Banners','pn').'(336 x 280)',
		'banner7'=> __('Banners','pn').'(250 x 250)',
		'banner8'=> __('Banners','pn').'(240 x 400)',
		'banner9'=> __('Banners','pn').'(234 x 60)',
		'banner10'=> __('Banners','pn').'(120 x 90)',
		'banner11'=> __('Banners','pn').'(120 x 60)',
		'banner12'=> __('Banners','pn').'(120 x 240)',
		'banner13'=> __('Banners','pn').'(125 x 125)',
		'banner14'=> __('Banners','pn').'(300 x 600)',
		'banner15'=> __('Banners','pn').'(300 x 250)',
		'banner16'=> __('Banners','pn').'(80 x 150)',
		'banner17'=> __('Banners','pn').'(728 x 90)',
		'banner18'=> __('Banners','pn').'(160 x 600)',
		'banner19'=> __('Banners','pn').'(80 x 15)',
	);	
	
	return $banners;
}
```

Если вы хотите оставить только баннеры 468 на 60, просто удалите все остальные строки из предыдущего хука:

```php
add_filter('pp_banners','my_pp_banners', 1000);
function my_pp_banners($banners){
	
	$banners = array(
		'text'=> __('Text materials','pn'),
		'banner1'=> __('Banners','pn').'(468 x 60)',
	);	
	
	return $banners;
}
```

Если вы хотите добавить свой размер, добавьте строку по аналогии. К примеру, мы хотим добавить баннер 215 на 19:

```php
add_filter('pp_banners','my_pp_banners', 1000);
function my_pp_banners($banners){
	
	$banners = array(
		'text'=> __('Text materials','pn'),
		'banner1'=> __('Banners','pn').'(468 x 60)',
		'banner21519'=> __('Banners','pn').'(215 x 19)',
	);	
	
	return $banners;
}
```

</details>

<details>

<summary>Выбор статуса заявки в виде выпадающего списка в фильтре в разделе "Заявки"</summary>

```php
add_filter('change_bids_filter_list', 'my_change_bids_filter_list');
function my_change_bids_filter_list($lists) {
	if (isset($lists['status']['bidstatus'])) {
		$stats = list_bid_status();
		$statused = array('0'=> '--' . __('All','pn') . '--');
		if (is_array($stats)) { 
			foreach ($stats as $k => $v) {
				$statused[$k] = $v;
			}
		}
		$lists['status']['bidstatus'] = array(
			'title' => __('Status of order','pn'),
			'name' => 'bidstatus',
			'options' => $statused,
			'view' => 'select',
			'work' => 'options',
		);
	}
	return $lists;
}
```

До:\
![](<../../.gitbook/assets/image (1571).png>)\
После:\
![](<../../.gitbook/assets/image (577).png>)

</details>

<details>

<summary>Запуск парсера курсов при импорте направлений обмена из файла</summary>

```php
add_action('premium_action_export_direction','myparser_premium_action_export_direction', 9);
function myparser_premium_action_export_direction(){
	if(function_exists('new_parser_upload_data')){
		new_parser_upload_data();
	}
}
```

</details>

<details>

<summary>Использование прокси при <a data-footnote-ref href="#user-content-fn-1">проблемах</a> с парсерами 2.0</summary>

В кавычках для полей "**ip**", "**port**", "**login**", "**password**" укажите данные от вашего прокси

```php
add_filter('curl_options_parser', '_proxy_curl_options_parser');
function _proxy_curl_options_parser($options) {

	$ip = ''; //ip-адрес
	$port = ''; //port
	$login = ''; //login
	$password = '';	//password
	$tunnel = 1;
		
	if ($ip and $port) {
		if ($tunnel) {
			$options[CURLOPT_HTTPPROXYTUNNEL] = 0;
		}
		
		$options[CURLOPT_PROXY] = $ip;
		$options[CURLOPT_PROXYPORT] = $port;
		
		if ($password and $login) {
			$options[CURLOPT_PROXYUSERPWD] = $login.':'.$password;
		} elseif ($password) {
			$options[CURLOPT_PROXYAUTH] = $password;
		}
	}

	return $options;
}
```

</details>

<details>

<summary>Описание обмена в виджете на главной</summary>

На главной странице в виджете нет описания обмена. Если необходимо его добавить, достаточно воспользоваться хуком:

```php
add_filter('exchange_html_ajax', 'my_exchange_html_ajax');
function my_exchange_html_ajax($html){

	return $html.'[description]';
}
```

</details>

<details>

<summary>Определение IP-адреса</summary>

За определение IP-адреса отвечает функция **pn\_real\_ip**. Задача данной функции - вывести один реальный IP-адрес. Если, по каким-то причинам вас не устраивает работа функции, вы можете воспользоваться фильтром

```php
add_filter('pn_real_ip', 'myhook_pn_real_ip', 10, 2);
function myhook_pn_real_ip($ip, $ips_arr){

$new_ip = '127.0.0.1';

return $new_ip;
}
```

</details>

<details>

<summary>Основная валюта сайта</summary>

Для вычисления скидок, подсчета общих сумм и прочего, все суммы переводятся в определенный тип валюты. По умолчанию, скрипт считает основной валютой USD, но это значение можно изменить:

1\. Создадим необходимый код валюты, к примеру WMZ.

2\. Напишем фильтр:

```php
add_filter('cur_type','myhook_cur_type');
function myhook_cur_type($type){

$type = 'WMZ';

return $type;
}
```

Теперь внутренней валютой нашего сайта стал WMZ.

Стоит обратить внимание, что обмен внутренней валюты будет осуществляться по двойному обмену (через USD).

</details>

<details>

<summary>Отключение иконки проверки безопасности</summary>

```php
remove_action('wp_before_admin_bar_render', 'premium_admin_bar_security', 2);
```

</details>

<details>

<summary>Отображение курса обмена в разделе "Заявки" с учетом скидки</summary>

<mark style="color:red;">В некоторых ситуациях подсчет курса обмена может быть неверным</mark>

```php
add_filter('onebid_col1', 'new_rate_onebid_col1', 10, 3);
function new_rate_onebid_col1($actions, $item, $v){
	$new_actions = array();
	foreach($actions as $action_key => $action_value){
		$new_actions[$action_key] = $action_value;
		if($action_key == 'rate'){
			$course_get = is_sum($item->course_get);
			$course = is_sum($course_get + ($course_get / 100 * $item->user_discount), 20);
			
			$new_actions['rate_with_discount'] = array(
				'type' => 'text',
				'title' => __('Rate with discount','pn'),
				'label' => '[course_give] [currency_code_give] = '. $course .' [currency_code_get]',
			);				
		}
	}
	
	return $new_actions;
}
```

</details>

<details>

<summary>Отображение полной суммы оплаты в заявке</summary>

{% code overflow="wrap" %}
```php
add_filter('exchangestep_all_html_list', 'sum1fromc_exchangestep_all_html_list', 10, 2);
function sum1fromc_exchangestep_all_html_list($array, $bids_data) {
    $array['[sum_give]'] = is_sum($bids_data->sum1c);
    return $array;
}
```
{% endcode %}

</details>

<details>

<summary>Перевод текста по умолчанию</summary>

Если вы используете мультиязычность, в мультиязычных полях задается несколько вариантов текста (для каждого из языков). Когда нужной версии нет, скрипт подставляет первую возможную (соответствует языку админ-панели).

Если вы считаете, что это не корректно, вы можете задать шаблон ошибки с помощью фильтра:

```php
add_filter('ctv_ml_default','myhook_ctv_ml_default');
function myhook_ctv_ml_default($text){
$text = 'ошибка, перевода нет'; //любой ваш вариант
return $text;
}
```

</details>

<details>

<summary>Показывать колонку "Курс" в таблице №5 по умолчанию</summary>

По умолчанию в таблице №5 на главной странице обменника для направлений обмена отображается резерв, а не курс. Если вы хотите, чтобы при открытии страницы отображался курс — установите этот хук

<img src="../../.gitbook/assets/image (388).png" alt="" data-size="original">

```php
add_filter('table5_current_select', 'rate_table5_current_select');
function rate_table5_current_select ($select) {
    
    $select = 'rate';
    
    return $select;
}
```

</details>

<details>

<summary>При <a data-footnote-ref href="#user-content-fn-2">некорректной работе</a> с заявками с мобильных устройств</summary>

```php
add_filter('merchant_payed_button','del_iam_pay_merchant_pay_button', 10000);
add_filter('merchant_pay_button','del_iam_pay_merchant_pay_button', 10000);
function del_iam_pay_merchant_pay_button($link) {
	$link = str_replace('iam_pay_bids','',$link);
	return $link;
}
```

</details>

<details>

<summary>Прокси для работы Bestchange парсера</summary>

### Bestchange парсер (устаревший)

<mark style="color:red;">**Перед установкой хуков обязательно обновите сам скрипт по**</mark> [<mark style="color:red;">**инструкции**</mark>](https://premium.gitbook.io/main/osnovnye-nastroiki/faq/diagnostika-i-reshenie-oshibok-pri-rabote-so-skriptom#obnovlenie-failov-skripta-na-servere)<mark style="color:red;">**!**</mark>

Хук работает на версии модуля 2.6.1/2.7.1 и выше (**использование собственного прокси)**:

{% code overflow="wrap" %}
```php
add_filter('curl_bestchange', 'curl_bestchange_proxy');
function curl_bestchange_proxy($ch) {

    $ip = ''; // proxy ip
    $port = ''; // proxy port
    $login = ''; // proxy login
    $password = ''; // proxy password

    if ($ip and $port) {
        curl_setopt($ch, CURLOPT_PROXY, $ip);
        curl_setopt($ch, CURLOPT_PROXYPORT, $port);

        if ($password and $login) {
            curl_setopt($ch, CURLOPT_PROXYUSERPWD, "{$login}:{$password}");
        } elseif ($password) {
            curl_setopt($ch, CURLOPT_PROXYAUTH, $password);
        }
    }

    return $ch;
}
```
{% endcode %}

### Bestchange API парсер

Хук работает на версии модуля 2.6.2/2.7.2 и выше (**использование собственного прокси)**:

{% code overflow="wrap" %}
```php
add_filter('curl_bestchangeapi', 'curl_bestchangeapi_proxy');
function curl_bestchangeapi_proxy($ch) {

    $ip = ''; // proxy ip
    $port = ''; // proxy port
    $login = ''; // proxy login
    $password = ''; // proxy password

    if ($ip and $port) {
        curl_setopt($ch, CURLOPT_PROXY, $ip);
        curl_setopt($ch, CURLOPT_PROXYPORT, $port);

        if ($password and $login) {
            curl_setopt($ch, CURLOPT_PROXYUSERPWD, "{$login}:{$password}");
        } elseif ($password) {
            curl_setopt($ch, CURLOPT_PROXYAUTH, $password);
        }
    }

    return $ch;
}
```
{% endcode %}

Хук работает на версии модуля 2.6.2/2.7.2 и выше (**возможность смены домена BC (зеркало) в общих настройках модуля)**:\
![](<../../.gitbook/assets/image (28).png>)

{% code overflow="wrap" %}
```php
add_filter('curl_bestchangeapi_domain', 'curl_bestchangeapi_domain');
function curl_bestchangeapi_domain($domain) {

    $new_domain = ''; // https://www.bestchange.app/, https://mirror1.bestchange.app/, https://mirror2.bestchange.app/

    if ($new_domain) {
        return $new_domain;
    }

    return $domain;
}
```
{% endcode %}

</details>

<details>

<summary>Разрешает использовать всего 1 символ для кода валюты</summary>

{% code overflow="wrap" %}
```php
add_filter('is_site_value', 'new_is_site_value', 10, 2);

function new_is_site_value($new_item, $item) {
    if (preg_match("/^[a-zA-Z0-9\.]{1,30}$/", $item, $matches)) {
        return $item;
    }
    return $new_item;
}
```
{% endcode %}

</details>

<details>

<summary>Разрешает использовать всего 2 символа для XML-кода валюты для экспортного XML-файла с курсами</summary>

```php
add_filter('is_xml_value', 'new_is_xml_value', 10, 2);
function new_is_xml_value($new_item, $item) {

  if (preg_match("/^[a-zA-z0-9_.]{2,50}$/", $item, $matches)){
    return $item;
  }
  
  return $new_item;
}
```

</details>

<details>

<summary>Скрытие галочки выбора всех заявок в разделе "Заявки" в панели администратора</summary>

```php
add_filter('bids_datablock', 'my_bids_datablock');
function my_bids_datablock($data_blocks){
    if(isset($data_blocks['check'])){
    unset($data_blocks['check']); }
    return $data_blocks; }
```

</details>

<details>

<summary>Скрытие направлений обмена на сайте в зависимости от заданного расписания для XML-файла.</summary>

Направление останется активным, но будет отображать 404 ошибку при переходе на него по прямой ссылке на сайте и будет скрыто в таблице выбора направлений обмена в админ-панели.

<pre class="language-php" data-overflow="wrap"><code class="lang-php">remove_filter('get_direction_output', 'txtxml_get_direction_output', 10, 3);

add_filter('get_direction_output', 'my_txtxml_get_direction_output', 10, 3);
<strong>function my_txtxml_get_direction_output($ind, $item, $place){
</strong><strong>    if($ind == 1 and function_exists('get_dirxml_show')){
</strong>    return get_dirxml_show($ind, $item); }
    return $ind; }
</code></pre>

</details>

<details>

<summary>Свой стандартный заголовок сайта</summary>

По умолчанию заголовком любой темы на базе Premium Exchanger, является текст вида `[title] — [description]`, где:

`[title]` — название сайта\
`[description]` — описание

Если не используются SEO-плагины, данный заголовок можно изменить с помощью хука.

К примеру, если вы хотите убрать заголовок, воспользуйтесь следующим хуком:

```php
add_filter('premium_wp_title', 'myhook_premium_wp_title');
function myhook_premium_wp_title($title){

return '[description]';
}
```

</details>

<details>

<summary>Своя ссылка-редирект после авторизации</summary>

После авторизации скрипт автоматически перенаправляет пользователя на страницу в личный кабинет. Если необходимо изменить ссылку-редирект, можно воспользоваться следующим хуком:

```php
add_filter('login_auth_redirect', 'my_login_auth_redirect');
function my_login_auth_redirect($url){

	$new_url = 'адрес страницы';

	return $new_url;
}
```

</details>

<details>

<summary>"Хвост" партнерской программы</summary>

\
По умолчанию, "хвостом" партнерской программы является значение «rid». Ссылка выглядит следующим образом: `https://ваш_домен/?rid=[id]`

Чтобы изменить это значение на своё, можно воспользоваться фильтром:

```php
add_filter('refid','myhook_refid');
function myhook_refid($refid){

$refid = 'skidka';

return $refid;
}
```

Таким образом, "хвостом" будет слово "**skidka**"

</details>

<details>

<summary>URL мультиязычных иконок</summary>

Premium Exchanger используют единый фреймворк Premium. Тот скрипт, который был активирован раньше и отвечает за основные функции. К основным функциям, относится и мультиязычность. Если мы хотим добавить дополнительных языков, нам необходимо загрузить иконки мультиязычности во все плагины, что бывает не всегда удобно. Для этих целей, мы можем использовать специальный фильтр, который будет указывать плагин, из которого брать флаги.

К примеру, мы хотим, что бы флаги всегда брались из premiumbox. Напишем свой фильтр:

```php
add_filter('ml_flag_url', 'my_ml_flag_url');
function my_ml_flag_url($plugin_folder){
return 'premiumbox';
}
```

</details>

[^1]: Нет доступа к источнику курсов, ошибка HTTP 451

[^2]: Блокировка уведомлений, всплывающих окон
