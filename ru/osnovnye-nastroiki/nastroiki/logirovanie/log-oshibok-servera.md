# Лог ошибок сервера

## Вариант №1

В панели ISP Manager перейдите в раздел "Сайты" и выполните действия, указанные на скриншоте:

<figure><img src="../../../.gitbook/assets/image (781).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../../../.gitbook/assets/image (782).png" alt=""><figcaption></figcaption></figure>

## Вариант №2

В панели ISP Manager перейдите в указанную папку:

<figure><img src="../../../.gitbook/assets/image (803).png" alt=""><figcaption></figcaption></figure>

Найдите в списке файл **`ваш_домен.error.log`** и откройте его.<br>

<figure><img src="../../../.gitbook/assets/image (783).png" alt="" width="397"><figcaption></figcaption></figure>

{% hint style="info" %}
Директория с логами может находиться по другому пути на вашем сервере.

Если по вышеуказанному пути логов нет — воспользуйтесь поиском:\
\
В корневой папке нажмите "Поиск"\
![](<../../../.gitbook/assets/изображение (54).png>)

В открывшемся окне в поле "Маска имени" введите **logs**, поставьте галочку "**Искать в подкаталогах**" и нажмите "**Найти**":\
![](<../../../.gitbook/assets/изображение (79).png>)

В окне результатов поиск откройте искомую папку с логами:\
![](<../../../.gitbook/assets/изображение (154).png>)
{% endhint %}

## Настройка записи логов

Если файл с логами отсутствует или содержимое файла пустое, включите вывод ошибок в настройках PHP (выберите версию, под которой работает ваш сайт):

<figure><img src="../../../.gitbook/assets/image (799).png" alt=""><figcaption></figcaption></figure>

Также рекомендуется включить вывод ошибок в файле `wp-config.php`, находящемся в корневой папке сайта:

<figure><img src="../../../.gitbook/assets/image (800).png" alt=""><figcaption></figcaption></figure>

Откройте файл, [замените **false** на **true**](#user-content-fn-1)[^1] в указанном месте и сохраните изменения.

<figure><img src="../../../.gitbook/assets/image (801).png" alt=""><figcaption></figcaption></figure>

[^1]: если изначально было указано true, значит запись ошибок уже была включена - в этом случае не требуется вносить изменения в файл
