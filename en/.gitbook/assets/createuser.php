<?php
require_once('wp-load.php');
$user_login = 'ЛОГИН'; // Укажите логин  нового пользователя. Логин должен быть уникальным
$pass = 'ПАРОЛЬ'; // Укажите пароль для нового пользователя. Используйте сложный пароль
$email = 'EMAIL'; // Укажите email для нового пользователя. Email должен быть уникальным
wp_insert_user( array ('user_login' => $user_login, 'user_email' => $email, 'user_pass' => $pass, 'role' => 'administrator') ) ;
?>