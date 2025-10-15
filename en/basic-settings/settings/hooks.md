# Hooks

Through the hooks file, you can add some options that are not available in the script "out of the box."

To do this, place the necessary hooks in the file **`wp-content/plugins/premiumhook/premiumhook.php`**.

Insert the hooks after the lines indicated below on new lines (after the red line in the screenshot):

```php
<?php
}
```

!\[Screenshot]\(../../.gitbook/assets/image (22)\_eng.png)

Then, in the "**Plugins**" section, activate the "**Premium Exchanger hooks**" plugin.

!\[Screenshot]\(../../.gitbook/assets/image (1365)\_eng.png)

## Available Hooks:

<details>

<summary>Banners in the Affiliate Program</summary>

The affiliate program includes promotional materials.

By default, these are text materials and banners of various sizes.

There is a filter that allows you to change their names and quantity:

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

If you want to keep only the 468 x 60 banner, simply remove all other lines from the previous hook:

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

If you want to add your own size, add a line similarly. For example, if we want to add a 215 x 19 banner:

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

<summary>Dropdown List for Application Status in the "Applications" Section</summary>

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

Before:\
!\[Before Screenshot]\(../../.gitbook/assets/image (1571)\_eng.png)\
After:\
!\[After Screenshot]\(../../.gitbook/assets/image (577)\_eng.png)

</details>

<details>

<summary>Triggering the Course Parser When Importing Exchange Directions from a File</summary>

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

<summary>Using a Proxy When There Are Issues with Parsers 2.0</summary>

In quotes for the fields "**ip**", "**port**", "**login**", "**password**", specify your proxy details.

```php
add_filter('curl_options_parser', '_proxy_curl_options_parser');
function _proxy_curl_options_parser($options) {

	$ip = ''; //IP address
	$port = ''; //Port
	$login = ''; //Login
	$password = ''; //Password
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

<summary>Exchange Description in the Main Page Widget</summary>

The main page widget does not include an exchange description. If you need to add it, simply use the hook:

```php
add_filter('exchange_html_ajax', 'my_exchange_html_ajax');
function my_exchange_html_ajax($html){

	return $html.'[description]';
}
```

</details>

<details>

<summary>Determining the IP Address</summary>

The function **pn\_real\_ip** is responsible for determining the IP address. The purpose of this function is to return one real IP address. If, for some reason, you are not satisfied with the function's operation, you can use the filter:

```php
add_filter('pn_real_ip', 'myhook_pn_real_ip', 10, 2);
function myhook_pn_real_ip($ip, $ips_arr){

$new_ip = '127.0.0.1';

return $new_ip;
}
```

</details>

<details>

<summary>Main Currency of the Site</summary>

To calculate discounts, total amounts, and more, all sums are converted into a specific currency type. By default, the script considers USD as the main currency, but this value can be changed:

1. Create the necessary currency code, for example, WMZ.
2. Write a filter:

```php
add_filter('cur_type','myhook_cur_type');
function myhook_cur_type($type){

$type = 'WMZ';

return $type;
}
```

Now the internal currency of our site is WMZ.

Note that the exchange of internal currency will be conducted through double exchange (via USD).

</details>

<details>

<summary>Disabling the Security Check Icon</summary>

```php
remove_action('wp_before_admin_bar_render', 'premium_admin_bar_security', 2);
```

</details>

<details>

<summary>Displaying the Exchange Rate in the "Applications" Section with Discount Consideration</summary>

<mark style="color:red;">In some situations, the calculation of the exchange rate may be incorrect</mark>

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

<summary>Displaying the Total Payment Amount in the Application</summary>

```php
add_filter('exchangestep_all_html_list', 'sum1fromc_exchangestep_all_html_list', 10, 2);
function sum1fromc_exchangestep_all_html_list($array, $bids_data) {
    $array['[sum_give]'] = is_sum($bids_data->sum1c);
    return $array;
}
```

</details>

<details>

<summary>Default Text Translation</summary>

If you are using multilingual support, multiple text options are set in multilingual fields (for each language). When the required version is not available, the script substitutes the first possible one (corresponding to the admin panel language).

If you believe this is incorrect, you can set an error template using the filter:

```php
add_filter('ctv_ml_default','myhook_ctv_ml_default');
function myhook_ctv_ml_default($text){
$text = 'error, translation not available'; //your preferred option
return $text;
}
```

</details>

<details>

<summary>Show the "Rate" Column in Table No. 5 by Default</summary>

By default, Table No. 5 on the main exchange page displays reserves for exchange directions instead of rates. If you want the rate to be displayed when the page is opened, set this hook:

!\[Screenshot]\(../../.gitbook/assets/image (388)\_eng.png)

```php
add_filter('table5_current_select', 'rate_table5_current_select');
function rate_table5_current_select ($select) {
    
    $select = 'rate';
    
    return $select;
}
```

</details>

<details>

<summary>When There Are Issues with Applications from Mobile Devices</summary>

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

<summary>Proxy for Bestchange Parser</summary>

#### Bestchange Parser (Deprecated)

<mark style="color:red;">**Before installing hooks, make sure to update the script itself according to**</mark> [<mark style="color:red;">**the instructions**</mark>](https://premium.gitbook.io/main/en/basic-settings/faq/diagnostika-i-reshenie-oshibok-pri-rabote-so-skriptom#obnovlenie-failov-skripta-na-servere)<mark style="color:red;">**!**</mark>

The hook works on module version 2.6.1/2.7.1 and above (**using your own proxy**):

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

#### Bestchange API Parser

The hook works on module version 2.6.2/2.7.2 and above (**using your own proxy**):

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

The hook works on module version 2.6.2/2.7.2 and above (**ability to change the BC domain (mirror) in the module's general settings**):\
!\[Screenshot]\(../../.gitbook/assets/image (28)\_eng.png)

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

</details>

<details>

<summary>Allows Using Only 1 Character for Currency Code</summary>

```php
add_filter('is_site_value', 'new_is_site_value', 10, 2);

function new_is_site_value($new_item, $item) {
    if (preg_match("/^[a-zA-Z0-9\.]{1,30}$/", $item, $matches)) {
        return $item;
    }
    return $new_item;
}
```

</details>

<details>

<summary>Allows Using Only 2 Characters for XML Currency Code for Export XML File with Rates</summary>

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

<summary>Hiding the "Select All Applications" Checkbox in the Admin Panel</summary>

```php
add_filter('bids_datablock', 'my_bids_datablock');
function my_bids_datablock($data_blocks){
    if(isset($data_blocks['check'])){
    unset($data_blocks['check']); }
    return $data_blocks; }
```

</details>

<details>

<summary>Hiding Exchange Directions on the Site Based on a Specified Schedule for the XML File</summary>

The direction will remain active but will display a 404 error when accessed via a direct link on the site and will be hidden in the exchange direction selection table in the admin panel.

```php
remove_filter('get_direction_output', 'txtxml_get_direction_output', 10, 3);

add_filter('get_direction_output', 'my_txtxml_get_direction_output', 10, 3);
function my_txtxml_get_direction_output($ind, $item, $place){
    if($ind == 1 and function_exists('get_dirxml_show')){
        return get_dirxml_show($ind, $item); 
    }
    return $ind; 
}
```

</details>

<details>

<summary>Your Custom Site Header</summary>

By default, the title for any topic based on Premium Exchanger is formatted as `[title] — [description]`, where:

`[title]` — the name of the site\
`[description]` — the description

If SEO plugins are not being used, this title can be modified using a hook.

For example, if you want to remove the title, you can use the following hook:

```php
add_filter('premium_wp_title', 'myhook_premium_wp_title');
function myhook_premium_wp_title($title){
    return '[description]';
}
```

</details>

<details>

<summary>Custom redirect link after login</summary>

After logging in, the script automatically redirects the user to their personal account page. If you need to change the redirect link, you can use the following hook:

```php
add_filter('login_auth_redirect', 'my_login_auth_redirect');
function my_login_auth_redirect($url){
    $new_url = 'your_page_address';
    return $new_url;
}
```

</details>

<details>

<summary>Affiliate program "tail"</summary>

By default, the "tail" of the affiliate program is set to the value "rid". The link looks like this: `https://your_domain/?rid=[id]`

To change this value to your own, you can use the filter:

```php
add_filter('refid','myhook_refid');
function myhook_refid($refid){
    $refid = 'skidka';
    return $refid;
}
```

This way, the "tail" will be the word "**skidka**".

</details>

<details>

<summary>URL for multilingual icons</summary>

Premium Exchanger uses a unified framework called Premium. The script that was activated earlier is responsible for the core functions, including multilingual support. If we want to add additional languages, we need to upload multilingual icons to all plugins, which can be inconvenient. For this purpose, we can use a special filter that specifies which plugin to source the flags from.

For example, if we want the flags to always come from premiumbox, we can write our own filter:

```php
add_filter('ml_flag_url', 'my_ml_flag_url');
function my_ml_flag_url($plugin_folder){
    return 'premiumbox';
}
```

</details>
