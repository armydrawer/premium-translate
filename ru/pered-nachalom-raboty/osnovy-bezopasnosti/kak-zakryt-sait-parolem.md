# Как закрыть сайт паролем

### Создание файла с логином и паролем

Зайдите в Shell-клиент в ispmanager под <mark style="color:red;">root-пользователем</mark>.

<figure><img src="../../.gitbook/assets/image (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

Выполните команду, в которой укажите имя пользователя (в данном случае, для примера будет пользователь sysadmin):\
`sh -c "echo -n 'sysadmin:' >> /etc/nginx/.htpasswd"`

<figure><img src="../../.gitbook/assets/image (1) (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

Затем выполните команду, при помощи которой будет зашифрован пароль доступа:\
`sh -c "openssl passwd -apr1 >> /etc/nginx/.htpasswd"`

<figure><img src="../../.gitbook/assets/image (2) (1) (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

**После этого действия система запросит пароль и подтверждение пароля — укажите их.**&#x20;

Настройка файла с логином и паролем закончена.

### Настройки файла конфигурации nginx:

Под пользователем root зайдите во вкладку "Sites" и выберите в меню "Configuration files"

<figure><img src="../../.gitbook/assets/image (5) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

В файле конфигурации найдите блок location, который расположен в блоке server ssl (в конце файла), вставьте следующие строки:

```
allow 123.123.123.123;
deny all;

auth_basic "Restricted Access";
auth_basic_user_file /etc/nginx/.htpasswd;

satisfy any;
```

<figure><img src="../../.gitbook/assets/image (2178).png" alt=""><figcaption></figcaption></figure>

**IP адрес 123.123.123.123 сервера с сайтом (web), в вашем случае он будет другим!**

После чего сохраните изменения и перегрузите сервер.

<figure><img src="../../.gitbook/assets/image (2177).png" alt=""><figcaption></figcaption></figure>

Чтобы отключить пароль к сайту, удалите строки (2), сохраните изменения и перегрузите сервер.
