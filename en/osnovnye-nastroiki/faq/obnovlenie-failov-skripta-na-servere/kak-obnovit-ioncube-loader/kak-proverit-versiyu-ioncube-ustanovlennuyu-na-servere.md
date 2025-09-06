# Как проверить версию IonCube, установленную на сервере?

## Вариант №1

Версия IonCube будет отображаться в самом низу любой страницы в панели администратора:

<figure><img src="../../../../.gitbook/assets/изображение (87).png" alt=""><figcaption></figcaption></figure>

## Вариант №2

В корне сайта на сервере создайте временный файл с любым именем, например `test.php` и с содержимым:

```
<? PHP phpinfo(); ?>
```

<figure><img src="../../../../.gitbook/assets/изображение (102).png" alt="" width="563"><figcaption></figcaption></figure>

Откройте страницу `https://ваш_домен/test.php` через браузер и найдите блок ionCube Loader:

<figure><img src="../../../../.gitbook/assets/изображение (29).png" alt=""><figcaption></figcaption></figure>

{% hint style="warning" %}
После проверки обязательно удалите файл с сервера!
{% endhint %}
