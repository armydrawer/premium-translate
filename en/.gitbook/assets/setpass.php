<?php
require_once('wp-load.php');
$user_login = 'testuser2023';  // Укажите логин пользователя, для которого вы задаете новый пароль
$pass = 'qwerty'; // Укажите новый пароль, который вы хотите задать
$pass = is_password($pass); 
/*$user_id = '';*/

$user_id = intval($user_id); 
if(!$user_id and $user_login){
 $ui = get_user_by('login', $user_login);
 $user_id = intval(is_isset($ui,'ID'));
} 

if($user_id and $pass){
 wp_set_password($pass, $user_id);
}
?>