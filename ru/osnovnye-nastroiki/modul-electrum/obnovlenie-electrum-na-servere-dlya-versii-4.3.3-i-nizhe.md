# Обновление Electrum на сервере (для версии 4.3.3 и ниже)

{% hint style="danger" %}
На текущий момент последняя поддерживаемая версия Electrum — **4.4.6**.

Если у вас уже установлена эта версия — данная инструкция для вас неактуальна.
{% endhint %}

1.  В панели управления ISP Manager через раздел "**Сайты**" выделите нужный сайт кликом мыши и нажмите на пункт **"Войти как владелец"**. Вы будете авторизованы как <mark style="color:green;">пользователь, созданный для сайта.</mark><br>

    <figure><img src="../../.gitbook/assets/изображение (71) (1).png" alt=""><figcaption></figcaption></figure>
2.  Откройте раздел "**Менеджер файлов**".<br>

    <figure><img src="../../.gitbook/assets/изображение (67) (1).png" alt="" width="330"><figcaption></figcaption></figure>
3. Перейдите в папку `/Electrum/Electrum-X.X.X/`, где `X.X.X` — будет номер версии модуля Electrum на момент его установки на сервер.

<figure><img src="../../.gitbook/assets/image (1362).png" alt=""><figcaption></figcaption></figure>

4. Скачайте версию Electrum 4.4.6 с [официального сайта](https://download.electrum.org/4.4.6/).
5. Содержимое скачанного архива загрузите на сервер в директорию из пункта 3 (с заменой файлов).

{% hint style="warning" %}
Обратите, что нужно загрузить на сервер файлы и папки именно так, как показано на скриншоте ниже.
{% endhint %}

<figure><img src="../../.gitbook/assets/image (1363).png" alt=""><figcaption></figcaption></figure>

При появлении окна о совпадении файлом подтвердите запись новых файлов.

<figure><img src="../../.gitbook/assets/image (1364).png" alt=""><figcaption></figcaption></figure>

6. **Обязательно** перезагрузите сервер после обновления файлов.
