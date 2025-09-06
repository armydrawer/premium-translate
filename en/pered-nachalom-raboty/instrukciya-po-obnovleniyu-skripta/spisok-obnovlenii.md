# Список обновлений

## Версия 2.7

*   Загрузка чеков клиентами в заявке (модуль "**Платежные чеки**" (**paychecks)**)\


    <figure><img src="../../.gitbook/assets/image (2016).png" alt="" width="563"><figcaption></figcaption></figure>

    Модуль дает возможность клиентам загружать чеки или другие данные через картинки в созданной заявке.

<figure><img src="../../.gitbook/assets/image (2047).png" alt="" width="474"><figcaption><p>Настройки текстов для указанного блока в заявке (раздел "<strong>Модули</strong>" -> "<strong>Платежные чеки</strong>")</p></figcaption></figure>

<figure><img src="../../.gitbook/assets/image (2015).png" alt="" width="327"><figcaption><p>Настройки модуля (вкладка "Платежные чеки" в настройках направления обмена)</p></figcaption></figure>

<figure><img src="../../.gitbook/assets/image (2013).png" alt="" width="563"><figcaption><p>В заявке нажмите кнопку "<strong>Choose file</strong>"</p></figcaption></figure>

<figure><img src="../../.gitbook/assets/image (2011).png" alt="" width="563"><figcaption><p>Выберите нужный файл и загрузите его</p></figcaption></figure>

<figure><img src="../../.gitbook/assets/image (2014).png" alt="" width="563"><figcaption><p>После загрузки картинки клиентом она будет отображаться в заявке в разделе "<strong>Заявки</strong>"</p></figcaption></figure>

*   Объединение направлений обмена в группы для быстрой фильтрации (модуль "**Группы направлений**" (**direction\_groups)**)\


    <figure><img src="../../.gitbook/assets/image (2017).png" alt="" width="563"><figcaption></figcaption></figure>



    <figure><img src="../../.gitbook/assets/image (2018).png" alt="" width="464"><figcaption><p>Добавьте нужное количество групп в разделе "<strong>Группы направлений</strong>"</p></figcaption></figure>



    <figure><img src="../../.gitbook/assets/image (2019).png" alt="" width="563"><figcaption><p>В настройках направления на вкладке "<strong>Основные настройки</strong>" присвойте направлению нужную группу</p></figcaption></figure>



    <div data-full-width="true"><figure><img src="../../.gitbook/assets/image (2020).png" alt=""><figcaption><p>В таблице всех направлений выберите нужную группу и, к примеру, сделайте все направления из этой группы неактивными.</p></figcaption></figure></div>


*   Указание индивидуального % прибыли для каждого города для направлений обмена с наличными по аналогии с [общим % прибыли для направления обмена](https://premium.gitbook.io/main/osnovnye-nastroiki/partnerskaya-programma/pribyl-i-partnerskii-procent#nastroika-pribyli-dlya-napravleniya-obmena).\


    <figure><img src="../../.gitbook/assets/image (2021).png" alt="" width="563"><figcaption><p>Вкладка "<strong>Города</strong>" в настройках направления обмена</p></figcaption></figure>
*   Возможность установки статуса "**Выполненная заявка**" через API (метод `success_bid`). Как и другие API-методы для смены статусов заявок, этот метод распространяется только на заявки, созданные непосредственно по API.\


    <figure><img src="../../.gitbook/assets/image (2022).png" alt=""><figcaption><p>Для определения заявки необходимо передавать её хэш (он отображается в ответе для метода <code>create_bid</code> при создании заявки по API)</p></figcaption></figure>



    <figure><img src="../../.gitbook/assets/image (2023).png" alt=""><figcaption><p>Изменение статусов заявки по API</p></figcaption></figure>
*   Массовый редактор информации — добавлен фильтр по группе направлений,

    <figure><img src="../../.gitbook/assets/image (2024).png" alt="" width="445"><figcaption><p>Фильтр по группе направлений</p></figcaption></figure>

    \
    а также возможность указывать комиссии и суммы обмена в одном окне для выбранных направлений

    <figure><img src="../../.gitbook/assets/image (2025).png" alt="" width="445"><figcaption><p>Выбор сущности для редактирования</p></figcaption></figure>



    <div><figure><img src="../../.gitbook/assets/image (2026).png" alt="" width="563"><figcaption><p>Редактирование комиссий платежных систем</p></figcaption></figure> <figure><img src="../../.gitbook/assets/image (2029).png" alt="" width="563"><figcaption><p>Редактирование сумм обмена</p></figcaption></figure></div>
*   Возможность полного отключения лога мерчантов и автовыплат\


    <figure><img src="../../.gitbook/assets/image (342).png" alt=""><figcaption><p>Опция находится в настройках каждого модуля мерчанта и автовыплаты</p></figcaption></figure>
*   Запрет на создание заявок с одной и той же суммой для направления обмена\


    <figure><img src="../../.gitbook/assets/image (344).png" alt="" width="422"><figcaption><p>Вкладка "<strong>Ограничения и проверки</strong>" в настройках направления обмена</p></figcaption></figure>



    <figure><img src="../../.gitbook/assets/image (345).png" alt="" width="532"><figcaption><p>При создании второй заявки и при наличии неоплаченной первой заявки на ту же сумму, клиент получит ошибку</p></figcaption></figure>
*   Модуль сортировки направлений и валют — в разделе будут отображаться только активные валюты (ранее отображались все валюты)\


    <figure><img src="../../.gitbook/assets/image (333).png" alt="" width="477"><figcaption></figcaption></figure>
*   Модуль "**Оператор live"**(`many_operators`)

    <figure><img src="../../.gitbook/assets/image (334).png" alt="" width="563"><figcaption></figcaption></figure>

    Добавлена возможность отображения только заявок из определенных направлений обмена, а также заявок с определенными мерчантами на приём для каждого пользователя с доступом к админ-панели.

    <figure><img src="../../.gitbook/assets/image (335).png" alt=""><figcaption><p>При такой настройке оператору будут отображаться только заявки, где использовался мерчант Advcash</p></figcaption></figure>



    <figure><img src="../../.gitbook/assets/image (336).png" alt=""><figcaption><p>При такой настройке оператору будут отображаться только заявки из указанных направлений обмена</p></figcaption></figure>



    <figure><img src="../../.gitbook/assets/image (337).png" alt=""><figcaption><p>При такой настройке оператору будут отображаться только заявки из указанных направлений обмена, а также заявки из всех направлений обмена, где использовался мерчант Advcash</p></figcaption></figure>

Также можно использовать обратный фильтр:

<figure><img src="../../.gitbook/assets/image (338).png" alt=""><figcaption><p>При такой настройке оператору будут отображаться заявки из <strong>всех</strong> направлений обмена, кроме указанных </p></figcaption></figure>

{% hint style="warning" %}
Не используйте в фильтрах положительные и отрицательные значения одновременно — фильтрация осуществляется по принципу ИЛИ, поэтому отрицательные фильтры не будут учитываться, если они указаны вместе с положительными.
{% endhint %}

<figure><img src="../../.gitbook/assets/image (340).png" alt=""><figcaption><p>При такой настройке оператору будут отображаться <strong>все</strong> заявки из направления обмена 1340 (даже если в них использовался мерчант Bova), а также заявки из <strong>всех</strong> направлений обмена, где <strong>не</strong> использовался мерчант Bova.<br>Т.е. отрицательный фильтр по мерчанту Bova не будет учитываться, если он использовался в направлении 1340</p></figcaption></figure>

<figure><img src="../../.gitbook/assets/image (341).png" alt=""><figcaption><p>При такой настройке оператору будут отображаться заявки из всех направлений обмена (даже если в них <strong>не</strong> использовался мерчант Bova), а также заявки из <strong>всех</strong> направлений обмена, где использовался мерчант Bova (даже если это направление 1340).<br>Т.е. отрицательный фильтр по направлению 1340 не будет учитываться, если были заявки в этом направлении с мерчантом Bova</p></figcaption></figure>

*   Перенос пользовательских коэффициентов для Парсеров 2.0 в отдельный раздел\


    <figure><img src="../../.gitbook/assets/image (2030).png" alt=""><figcaption><p>Раздел в сайдбаре</p></figcaption></figure>

    <figure><img src="../../.gitbook/assets/image (2031).png" alt="" width="449"><figcaption><p>Настройки коэффициента</p></figcaption></figure>

    Имя индекса — желаемое название, которое будет использоваться в формулах как шорткод\
    Формула значения — в поле указывается число или математическая формула\
    Значение индекса — значение для формулы, указанной выше (если указана формула)\
    Тип индекса:\
    • Подстановка формулы в курс

    <figure><img src="../../.gitbook/assets/image (2033).png" alt=""><figcaption><p>Формула будет подставляться напрямую в курс без скобок, а затем вычисляться само значение курса</p></figcaption></figure>

    • Значение индекса

    <figure><img src="../../.gitbook/assets/image (2032).png" alt=""><figcaption><p>Сначала будет вычислено значение коэффициента, а затем оно будет подставляться в курс</p></figcaption></figure>

    Комментарий — поле для ваших заметок
*   Убрана настройка создания задания для обновления курсов для опции "**На сайте**" (при использовании этой опции сервер перегружал себя лишними запросами)

    <div><figure><img src="../../.gitbook/assets/image (2035).png" alt=""><figcaption><p>Версия 2.6</p></figcaption></figure> <figure><img src="../../.gitbook/assets/image (2034).png" alt=""><figcaption><p>Версия 2.7</p></figcaption></figure></div>
*   Результаты перерасчетов по заявкам вынесены в отдельный раздел "**Лог перерасчетов**"

    <figure><img src="../../.gitbook/assets/image (2036).png" alt="" width="563"><figcaption></figcaption></figure>
*   Модуль "**Черный список**" — добавлена возможность проверки реального счета, с которого пришел платеж от клиента

    <figure><img src="../../.gitbook/assets/image (324).png" alt="" width="404"><figcaption></figcaption></figure>

    Добавлена возможность индивидуальной настройки элементов ЧС

    <figure><img src="../../.gitbook/assets/image (325).png" alt="" width="418"><figcaption></figcaption></figure>

Метод:\
• **Из общих настроек** — будет применен метод, выбранный в общих настройках модуля\
• **Выдавать ошибку** — при наличии этого элемента из ЧС в форме на обмен будет отображаться ошибка при создании заявки, даже если в общих настройках выбран метод "**Останавливать автовыплату**"\
• **Останавливать автовыплату** — при наличии этого элемента из ЧС в форме на обмен заявка будет создаваться (и проверяться на этапе автовыплаты), даже если в общих настройках выбран метод "**Выдавать ошибку**"

*   Модуль "**AML**" - все модули AML и логи по работе модулей AML теперь находятся в одном разделе

    <figure><img src="../../.gitbook/assets/image (327).png" alt=""><figcaption></figcaption></figure>

    <figure><img src="../../.gitbook/assets/image (326).png" alt=""><figcaption></figcaption></figure>

    Добавлена возможность быстрой замены модуля в настройках направления обмена

    <figure><img src="../../.gitbook/assets/image (328).png" alt="" width="241"><figcaption></figcaption></figure>

    Добавлены новые статусы для заявок при долгом ответе от AML-сервиса.\


    <figure><img src="../../.gitbook/assets/image (329).png" alt="" width="287"><figcaption></figcaption></figure>

    Если от сервиса не будет получен ответ за время, указанное в настройках модуля,

    <figure><img src="../../.gitbook/assets/image (330).png" alt="" width="314"><figcaption></figcaption></figure>

    то заявка сменит статус на "**Ожидание**" и вернется в предыдущий статус (при успешной проверке реквизитов клиента) или в "**AML проверка не пройдена**" (при превышении риска) после получения ответа от AML-сервиса. Для работы опции необходимо добавить [задание cron](https://premium.gitbook.io/main/osnovnye-nastroiki/faq/kak-sozdat-zadanie-cron-na-servere) на сервере (ссылка для задания находится в разделе "AML").
*

    <figure><img src="../../.gitbook/assets/image (332).png" alt="" width="528"><figcaption></figcaption></figure>

{% hint style="warning" %}
Вышеуказанная опция распространяется только на уже созданные заявки (если проверка в этом направлении обмена включена как "**При оплате**" или "**Перед автовыплатой**")

![](<../../.gitbook/assets/image (308).png>)
{% endhint %}

*   Добавлено логирование действий оператора/менеджера. Будут отображаться:\
    • дата и время внесения изменений\
    • пользователь, внесший изменения

    • данные, которые были изменены (красным цветом отображаются старые данные, черным — новые)

    <figure><img src="../../.gitbook/assets/image (2037).png" alt="" width="511"><figcaption></figcaption></figure>

    Логируются следующие разделы:\
    • Настройки направлений обмена\
    • Настройки валют\
    • Курсы валют в разделе "**Парсеры 2.0**" -> "**Курсы**"\
    • Настройки **парсеров Bestchange** и **Bestchange API**
*   Добавлена возможность ожидания получения реквизитов от мерчанта (только для фиатных мерчантов, которые предоставляют реквизиты в ответе по API и поддерживают повторные запросы реквизитов).\


    <figure><img src="../../.gitbook/assets/image (2039).png" alt="" width="433"><figcaption><p>Опция в настройках модуля мерчанта</p></figcaption></figure>

    Для работы опции также должна быть включена опция "**Перевести заявку в ошибку мерчанта**" в разделе "**Настройки обменника**" -> "**Основные настройки**" (только в этом случае реквизиты будут запрашиваться повторно или заявка будет переходить в статус "**Ошибка мерчанта**")\


    <figure><img src="../../.gitbook/assets/image (2040).png" alt="" width="467"><figcaption></figcaption></figure>

{% hint style="warning" %}
Обратите внимание, что повторные запросы к мерчанту за короткий интервал (если при первом запросе не были получены реквизиты) часто вынуждает мерчанта рассматривать такие запросы как спам и ваш обменник может попасть в спам-фильтр мерчанта.

Во избежание подобных ситуаций рекомендуем заранее сообщить представителям конкретного мерчанта, что от вашего обменника могут быть повторные запросы по одной и той же заявке, если при первом запросе реквизиты не были получены. В этом случае мерчант может добавить ваш обменник в исключения спам-фильтра.
{% endhint %}

## Версия 2.6

<details>

<summary>Список обновлений</summary>



*   **Модуль "Черный список Bestchange" (blacklist\_bestchange)**: Добавлена возможность остановки выплаты по заявке, если один или несколько реквизитов клиента находятся в черном списке Bestchange при использовании модуля. Настройки модуля находятся в разделе "**Модули**" -> "**Черный список Bestchange".**

    ![](https://premium.gitbook.io/~gitbook/image?url=https%3A%2F%2F2574066779-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252Fm9kqZXsNykrN6VyxxXBO%252Fuploads%252FIYShnbIVsQtdyzn1bKip%252Fimage.png%3Falt%3Dmedia%26token%3D69302b5b-7f4f-4847-b874-c928ea29ae01\&width=768\&dpr=4\&quality=100\&sign=52626c56\&sv=1)
* **Черный список (Blacklist)**: Внесены изменения, аналогичные модулю **blacklist\_bestchange**, позволяющие принимать средства и останавливать выплату, если пользователь находится в черном списке. Настройки модуля находятся в разделе "**Черный список** " -> "**Настройки"**\
  ![](https://premium.gitbook.io/~gitbook/image?url=https%3A%2F%2F2574066779-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252Fm9kqZXsNykrN6VyxxXBO%252Fuploads%252F18OpRTbt1jzLD5l2HMZ4%252Fimage.png%3Falt%3Dmedia%26token%3Dcd4f10d7-7da0-49f2-b46a-ebf0e58efe1e\&width=768\&dpr=4\&quality=100\&sign=3df31e7f\&sv=1)

- **AML-проверка**: Добавлена возможность проведения проверки непосредственно перед отправкой валюты на кошелек клиента, с переводом заявки в ошибку при превышении уровня риска. Настройка уровня риска производится в разделе "**Модули**" -> "**AML Bot**" или "**Getblock**" (в зависимости от того, какой сервис вы подключили).\
  \
  Настройка логики выполнения проверки производится в настройках направлении обмена, вкладка "**AML Bot**" или "**Getblock**".

![](https://premium.gitbook.io/~gitbook/image?url=https%3A%2F%2F2574066779-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252Fm9kqZXsNykrN6VyxxXBO%252Fuploads%252FwkCrPNGRW8VjYjVzWBrM%252Fimage.png%3Falt%3Dmedia%26token%3D7df1e4b9-62ea-43c1-b715-55ae021fe80e\&width=768\&dpr=4\&quality=100\&sign=8ab4efdd\&sv=1)

*   **AML-сервис Getblock, функция sleep**: Добавлена возможность установки времени ожидания ответа от сервиса на тот случай, если результат проверки не был выдан сразу. Настройка находится в разделе "**Модули** " -> "**Getblock".**

    ![](https://premium.gitbook.io/~gitbook/image?url=https%3A%2F%2F2574066779-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252Fm9kqZXsNykrN6VyxxXBO%252Fuploads%252FUCwqQIbUxlfFgP0SyEdU%252Fimage.png%3Falt%3Dmedia%26token%3D1a328e43-5f40-46f9-a44f-687546201bdb\&width=768\&dpr=4\&quality=100\&sign=fdf901cd\&sv=1)
*   **Подтверждение e-mail**: Добавлена возможность запроса подтверждения e-mail клиента перед созданием заявки. Модуль "**Подтверждение e-mail перед созданием заявки**" **(confirmexchmail)** необходимо активировать в разделе "**Модули**". Настройки модуля находятся в разделе "**Модули** " -> "**Подтверждение e-mail перед созданием заявки".**

    ![](https://premium.gitbook.io/~gitbook/image?url=https%3A%2F%2F2574066779-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252Fm9kqZXsNykrN6VyxxXBO%252Fuploads%252FNqMA0JHfsAhhn1AdvZ01%252Fimage.png%3Falt%3Dmedia%26token%3D6a490aa4-14e5-45e7-a3fa-2642afb47054\&width=768\&dpr=4\&quality=100\&sign=320c412\&sv=1)
*   **Архивация**: Изменена структура модуля, добавлена фильтрация по **статусу заявки/реквизитам, полученным от мерчанта/хэшу транзакции на приём и выплату средств** в разделе "**Заявки**" -> "**Архивированные заявки**"

    ![](https://premium.gitbook.io/~gitbook/image?url=https%3A%2F%2F2574066779-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252Fm9kqZXsNykrN6VyxxXBO%252Fuploads%252F1n2WBW6PYrXoMCgg71RI%252Fimage.png%3Falt%3Dmedia%26token%3D2e1f1089-95be-4fa0-8867-6bd81a2f8042\&width=768\&dpr=4\&quality=100\&sign=2d57193b\&sv=1)

и просмотр комментариев в архивированной заявке.

![](https://premium.gitbook.io/~gitbook/image?url=https%3A%2F%2F2574066779-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252Fm9kqZXsNykrN6VyxxXBO%252Fuploads%252FivYchvvmMsQYN9c7guAN%252Fimage.png%3Falt%3Dmedia%26token%3D1db134fb-a823-467b-9118-46387ab80d11\&width=768\&dpr=4\&quality=100\&sign=f75c4b9a\&sv=1)

Добавление комментария к заявке в разделе "Заявки"

![](https://premium.gitbook.io/~gitbook/image?url=https%3A%2F%2F2574066779-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252Fm9kqZXsNykrN6VyxxXBO%252Fuploads%252FhhyKRywp6rxpr9vqM7l0%252Fimage.png%3Falt%3Dmedia%26token%3De5e0253c-e7b3-4fe9-9596-adfcf83f4c48\&width=768\&dpr=4\&quality=100\&sign=1af31b4e\&sv=1)

Просмотр заявки в разделе "Заявки" -> "Архивированные заявки"

![](https://premium.gitbook.io/~gitbook/image?url=https%3A%2F%2F2574066779-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252Fm9kqZXsNykrN6VyxxXBO%252Fuploads%252FiaLmFJ4MBhewlPCKBM5O%252Fimage.png%3Falt%3Dmedia%26token%3D438be925-6698-4c02-a250-6ede35195354\&width=768\&dpr=4\&quality=100\&sign=4236fbb4\&sv=1)

Просмотр добавленного комментария

<mark style="color:red;">Поиск по указанным фильтрам и просмотр комментариев к заявкам будут работать только для заявок, архивированных в версии 2.6.</mark>

*   **Bestchange API парсер (bestchangeapi)**: Добавлен модуль для работы по API. Настройки модуля находятся в разделе "**BestChange API парсер"** -> "**Настройки"** и на вкладке **"BestChange API парсер**" в настройках направлений обменов.

    ![](https://premium.gitbook.io/~gitbook/image?url=https%3A%2F%2F2574066779-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252Fm9kqZXsNykrN6VyxxXBO%252Fuploads%252FB0oDC0uNelBlhxx0TmB3%252Fimage.png%3Falt%3Dmedia%26token%3Dca52b0f7-e79d-4128-aefb-58e721f74026\&width=768\&dpr=4\&quality=100\&sign=b8b71d3\&sv=1)

Общие настройки парсера

![](https://premium.gitbook.io/~gitbook/image?url=https%3A%2F%2F2574066779-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252Fm9kqZXsNykrN6VyxxXBO%252Fuploads%252FnGSQZPgneaUqDSB3JUi3%252Fimage.png%3Falt%3Dmedia%26token%3D1a6c6185-bd92-4cac-b27b-bbbb9b52988d\&width=768\&dpr=4\&quality=100\&sign=65b6dce4\&sv=1)

Настройка курса, получаемого от парсера в направлении обмена

* **Фильтрация направлений обмена**: Добавлен фильтр по платежным системам в разделе "**Направления обменов**".\
  ![](https://premium.gitbook.io/~gitbook/image?url=https%3A%2F%2F2574066779-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252Fm9kqZXsNykrN6VyxxXBO%252Fuploads%252F9xdx6Yn7jEL1kWLrC3ga%252Fimage.png%3Falt%3Dmedia%26token%3Dc85f4a49-b77c-4a6e-9c2a-383e9735755d\&width=768\&dpr=4\&quality=100\&sign=51546725\&sv=1)

-   **Значения прибыли в уведомлениях**: Добавлена возможность указывать **заданные (не рассчитанные!) в настройках направлений обмена (вкладка "Курс")** значения прибыли через шорткоды для вывода значений в письмах и сообщениях в Telegram для администраторов.

    ![](https://premium.gitbook.io/~gitbook/image?url=https%3A%2F%2F2574066779-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252Fm9kqZXsNykrN6VyxxXBO%252Fuploads%252FGn0nO1DGfe1mkSE68NZK%252Fimage.png%3Falt%3Dmedia%26token%3Df931870b-2d06-4b0d-9e7d-5401b1f956ce\&width=768\&dpr=4\&quality=100\&sign=fae370a1\&sv=1)
- **Замена модуля для подтверждения e-mail**: После обновления необходимо деактивировать, а затем удалить с сервера модуль **rconfirm** и вместо него использовать модуль **confirmregmail**. Подробнее в [**инструкции по обновлению**](https://premium.gitbook.io/main/pered-nachalom-raboty/instrukciya-po-obnovleniyu-skripta/obnovlenie-s-versii-2.5-do-2.6#izmeneniya-v-paneli-administratora). При установке скрипта версии 2.6 с нуля модуля **rconfirm** не будет "из коробки".
-   **Разделение текста шаблонов**: Добавлена возможность разделить текст из шаблона направления обмена, который будет отображаться при работе с заявками по API и через сайт с помощью шорткодов.

    ![](https://premium.gitbook.io/~gitbook/image?url=https%3A%2F%2F2574066779-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252Fm9kqZXsNykrN6VyxxXBO%252Fuploads%252FXnHpwIL4Npl1eEXPHo7A%252Fimage.png%3Falt%3Dmedia%26token%3D1eecc0b9-2f35-4f5e-b3e2-42c59a5c80e3\&width=768\&dpr=4\&quality=100\&sign=d83209f2\&sv=1)
- **Раздел "Финансовая статистика"**: В модуль финансовой статистики добавлена общая статистика по количеству обменов и сумме обменов в USD за выбранный период.

![](https://premium.gitbook.io/~gitbook/image?url=https%3A%2F%2F2574066779-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252Fm9kqZXsNykrN6VyxxXBO%252Fuploads%252F6aBBfbraijvg0k0U2AcB%252Fimage.png%3Falt%3Dmedia%26token%3Dbac677ff-49d9-4e56-b778-e8e87a64e37d\&width=768\&dpr=4\&quality=100\&sign=86401985\&sv=1)

*   **Кнопка "Перейти к оплате"**: Добавлена возможность скрыть кнопку в настройках модуля мерчанта на приём. Актуально, если реквизиты отображаются в тексте для статуса "**Новая заявка**" через шорткод `[to_account]`.

    ![](https://premium.gitbook.io/~gitbook/image?url=https%3A%2F%2F2574066779-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252Fm9kqZXsNykrN6VyxxXBO%252Fuploads%252FcVHhGXEmtqPWFr6WWRwO%252Fimage.png%3Falt%3Dmedia%26token%3Df47362d8-7e9e-4f76-a5ad-241542e99afe\&width=768\&dpr=4\&quality=100\&sign=d9f8545\&sv=1)
* **Список стран в ограничениях для направления обмена**: Отмеченные галочкой страны выводятся первыми в списке.
*   **Копирование мерчанта**: Добавлена возможность создания копии мерчанта со всеми настройками по кнопке. Для использования опции активируйте модуль "**Копирование мерчантов и авто-выплат**" в разделе "Модули" после обновления скрипта.

    ![](https://premium.gitbook.io/~gitbook/image?url=https%3A%2F%2F2574066779-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252Fm9kqZXsNykrN6VyxxXBO%252Fuploads%252FUIbcN1I2hBLOXtPkEEma%252Fimage.png%3Falt%3Dmedia%26token%3D182102a8-4edd-4974-bf07-f9a4f127060f\&width=768\&dpr=4\&quality=100\&sign=97d415c6\&sv=1)
*   **Массовое добавление мерчанта**: Добавлена возможность массового добавления мерчанта в направления обменов в настройках мерчанта.

    ![](https://premium.gitbook.io/~gitbook/image?url=https%3A%2F%2F2574066779-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252Fm9kqZXsNykrN6VyxxXBO%252Fuploads%252FMHKLG4ktbIASQkO6KAOV%252Fimage.png%3Falt%3Dmedia%26token%3D943737e4-ca45-46bf-ad32-368628a58c25\&width=768\&dpr=4\&quality=100\&sign=df35dbbd\&sv=1)
*   **ID валюты**: Добавлен поиск по ID валюты при создании направления обмена.

    ![](https://premium.gitbook.io/~gitbook/image?url=https%3A%2F%2F2574066779-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252Fm9kqZXsNykrN6VyxxXBO%252Fuploads%252FvJrpKvbx41kndmt8MDC1%252Fimage.png%3Falt%3Dmedia%26token%3Ddf6c8d18-c31a-4f2c-a2e7-68777b03ea14\&width=768\&dpr=4\&quality=100\&sign=f2662af2\&sv=1)Просмотр ID валют

    ![](https://premium.gitbook.io/~gitbook/image?url=https%3A%2F%2F2574066779-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252Fm9kqZXsNykrN6VyxxXBO%252Fuploads%252F45GCw327MjmFggmK5jUp%252Fimage.png%3Falt%3Dmedia%26token%3Dbe4b3846-69ae-48ee-8c82-def0d6591954\&width=768\&dpr=4\&quality=100\&sign=ab050794\&sv=1)Поиск по ID
* **Доступ к модулям:** Доступ открыт всем пользователям, имеющим доступ в панель администратора, но активация и деактивация модулей разрешена только администраторам.
* **Создание заявки без авторизации:** Добавлена возможность создания заявки без авторизации в направлении с верификацией реквизитов, если номер счета/карты был ранее верифицирован
* **Купоны:** Добавлен модуль **"Скидочные купоны" (coupons)** для предоставления персональный скидок клиентам в виде промокодов. Настройки модуля находятся в разделе "**Скидочные купоны".**\
  \
  При активации модуля в форме обмена будет отображаться необязательное для заполнения поле "**Скидочный купон**" (для каждого направления обмена поле активируется на вкладке "**Ограничения и проверки**")

![](https://premium.gitbook.io/~gitbook/image?url=https%3A%2F%2F2574066779-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252Fm9kqZXsNykrN6VyxxXBO%252Fuploads%252Fno8hazDvPmEChFlrW6Pc%252Fimage.png%3Falt%3Dmedia%26token%3D5c50cfed-d54b-4b7b-b393-e8fa05424a9b\&width=768\&dpr=4\&quality=100\&sign=7253b6b8\&sv=1)

Добавление нового купона

![](https://premium.gitbook.io/~gitbook/image?url=https%3A%2F%2F2574066779-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252Fm9kqZXsNykrN6VyxxXBO%252Fuploads%252F1JnchB24ASw1lkvU3gWT%252Fimage.png%3Falt%3Dmedia%26token%3D7b91b645-7654-4c6d-b5af-42d68133c1a0\&width=768\&dpr=4\&quality=100\&sign=4c9271f0\&sv=1)

Список купонов в панели администратора

![](https://premium.gitbook.io/~gitbook/image?url=https%3A%2F%2F2574066779-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252Fm9kqZXsNykrN6VyxxXBO%252Fuploads%252F8RSvOjJ6B2ZdGCNs54Og%252Fimage.png%3Falt%3Dmedia%26token%3Dff8fb0f9-f07f-43bd-b46d-3aed9a8e5564\&width=768\&dpr=4\&quality=100\&sign=e49ff4c9\&sv=1)

Включение опции для направления обмена

![](https://premium.gitbook.io/~gitbook/image?url=https%3A%2F%2F2574066779-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252Fm9kqZXsNykrN6VyxxXBO%252Fuploads%252FhSQUvLPmdKoNPmaXC0e4%252Fimage.png%3Falt%3Dmedia%26token%3Df75ee876-413f-4d96-9528-3cf5abdbcbec\&width=768\&dpr=4\&quality=100\&sign=83970d51\&sv=1)

Поле для ввода купона в форме обмена

* **Использование нескольких мерчантов на приём:** Добавлена опция задействования других мерчантов (если в настройках используется несколько мерчантов) в направлениях обмена, если первый по приоритету мерчант по каким-то причинам не выдал реквизиты для оплаты. Подробнее о работе опции читайте в [**инструкции**](https://premium.gitbook.io/main/osnovnye-nastroiki/merchanty-i-avtovyplaty/merchanty/obshie-nastroiki-merchantov#podklyuchenie-neskolkikh-merchantov).
*   **Платежные системы:** Добавлена возможность сортировки платежных систем по названию в разделе "**Валюты**" -> "**Платежные системы**".

    ![](https://premium.gitbook.io/~gitbook/image?url=https%3A%2F%2F2574066779-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252Fm9kqZXsNykrN6VyxxXBO%252Fuploads%252FrVcx6Fl3VIVnZnUY1Gdb%252Fimage.png%3Falt%3Dmedia%26token%3D930ef314-3dfb-4df4-812a-b739d343dd63\&width=768\&dpr=4\&quality=100\&sign=e448d909\&sv=1)
*   **Поиск парсера:** Добавлено поле для поиска парсера по тексту в настройках направления обмена (вкладка "**Автокорректировка курса**"). Поиск производится по всей строке, включая сам курс.

    ![](https://premium.gitbook.io/~gitbook/image?url=https%3A%2F%2F2574066779-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252Fm9kqZXsNykrN6VyxxXBO%252Fuploads%252FJfHORHxxLfjtQlvr29bI%252Fimage.png%3Falt%3Dmedia%26token%3D761d2bc0-50e6-4a5a-9e7a-d4e72a30eeb5\&width=768\&dpr=4\&quality=100\&sign=c1c75399\&sv=1)
*   **Сортировка стран**: Сортировка по коду страны заменена на сортировку по названию страны на вкладке "**Ограничения и проверки**" в настройках направлений обмена

    ![](https://premium.gitbook.io/~gitbook/image?url=https%3A%2F%2F2574066779-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252Fm9kqZXsNykrN6VyxxXBO%252Fuploads%252Fc37Ig1etNulPLbV5eHNK%252Fimage.png%3Falt%3Dmedia%26token%3Db984986e-2365-4a0e-aa23-15f67e33faea\&width=768\&dpr=4\&quality=100\&sign=7a22a5b0\&sv=1)
*   **Список пересчитанных курсов:** При включенном пересчета по курсу обмена список старых курсов в заявке в разделе "**Заявки**" может занимать большое пространство по вертикали. Для устранения этого блок "**Старые курсы**" сделан фиксированным по размеру, курсы скроллятся вертикально внутри блока.

    ![](https://premium.gitbook.io/~gitbook/image?url=https%3A%2F%2F2574066779-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252Fm9kqZXsNykrN6VyxxXBO%252Fuploads%252FxqYweWqKR7XVkTwR1xwN%252Fimage.png%3Falt%3Dmedia%26token%3Db2b8cf45-16b7-4cc9-9b9b-831b022317d9\&width=768\&dpr=4\&quality=100\&sign=c7425311\&sv=1)
*   **Таймер удаления заявок:** В таймер добавлены секунды

    ![](https://premium.gitbook.io/~gitbook/image?url=https%3A%2F%2F2574066779-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252Fm9kqZXsNykrN6VyxxXBO%252Fuploads%252FzzietmArefDuyHenIeyY%252Fimage.png%3Falt%3Dmedia%26token%3Da0a81ff4-7838-42dd-b33b-a68a1358eeb2\&width=768\&dpr=4\&quality=100\&sign=ad290e50\&sv=1)
*   Шорткод для таймера в настройках шаблона

    ![](https://premium.gitbook.io/~gitbook/image?url=https%3A%2F%2F2574066779-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252Fm9kqZXsNykrN6VyxxXBO%252Fuploads%252FaFZunCkyFjr64vA3GruI%252Fimage.png%3Falt%3Dmedia%26token%3Def8746c2-3d35-4362-a6de-07662a5e7c7b\&width=768\&dpr=4\&quality=100\&sign=3da8cb56\&sv=1)
* Отображение таймера с секундами в заявке
*   **Модуль "Капча для сайта (выбор картинки) " (sitecaptcha\_img):** Модуль модернизирован для улучшения защиты, также он теперь сам генерирует варианты капчи. Возможность создавать свои варианты капчи убрана.

    ![](https://premium.gitbook.io/~gitbook/image?url=https%3A%2F%2F2574066779-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252Fm9kqZXsNykrN6VyxxXBO%252Fuploads%252FJMYQCLioSTk66yjkxu4x%252Fimage.png%3Falt%3Dmedia%26token%3D3ba4e7e4-5974-4fef-bb0d-52d27196d22c\&width=768\&dpr=4\&quality=100\&sign=a982fc09\&sv=1)
* Отображение капчи в форме обмена
* **Telegram-бот для уведомлений:** Добавлена отправка сообщений по ID пользователя без логина (ID можно узнать через бота [@getMyID](https://t.me/getmyid_bot)). Отправка сообщений от бота в группы не поддерживается.\
  ![](https://premium.gitbook.io/~gitbook/image?url=https%3A%2F%2F2574066779-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252Fm9kqZXsNykrN6VyxxXBO%252Fuploads%252FsgS66ZwqNQwLSXqyzGoT%252Fimage.png%3Falt%3Dmedia%26token%3D5b4428e2-0c66-4c7b-ab9f-abb012f51eb5\&width=768\&dpr=4\&quality=100\&sign=d11ad25\&sv=1)
* Просмотр ID через бота [@getMyID](https://t.me/getmyid_bot)

![](https://premium.gitbook.io/~gitbook/image?url=https%3A%2F%2F2574066779-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252Fm9kqZXsNykrN6VyxxXBO%252Fuploads%252FikoOzYbs5LCM0obRzC1R%252Fimage.png%3Falt%3Dmedia%26token%3D67efd5f0-c889-4d43-8a38-b28966f61084\&width=768\&dpr=4\&quality=100\&sign=ba554ab4\&sv=1)

Добавление получателей сообщений в настройках шаблонов

Также добавлены настройки для блокировки ботов. Настройки модуля находятся в разделе "**Telegram"** -> "**Настройки"**

![](https://premium.gitbook.io/~gitbook/image?url=https%3A%2F%2F2574066779-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252Fm9kqZXsNykrN6VyxxXBO%252Fuploads%252FPCQLTFYN6dONk7Vi3NLg%252Fimage.png%3Falt%3Dmedia%26token%3Dcf7e1e61-86c5-460a-92df-963e3d480f6b\&width=768\&dpr=4\&quality=100\&sign=3ded5c2b\&sv=1)

*   **Уведомления для клиентов:** Вкладка "**Шаблон направления обмена**" переименована в "**Настройки уведомлений**" в настройках направлений обменов (с шаблоном для передачи в письме или сообщении в Телеграм через шорткод `[dirtemp]`). Добавлена возможность указать персональные **e-mail/аккаунт в telegram/номер телефона** для получения уведомления о заявке в этом направлении администратору/оператору (если одно или несколько полей для контактов заполнены, передача данных из шаблона выше будет осуществляться **только на указанные контакты**, игнорируя список получателей в общем шаблоне). Настройки опций находятся в настройках направления обмена, вкладка "**Настройки уведомлений**".

    ![](https://premium.gitbook.io/~gitbook/image?url=https%3A%2F%2F2574066779-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252Fm9kqZXsNykrN6VyxxXBO%252Fuploads%252F6OENVKlwLssqKLCDuHfN%252Fimage.png%3Falt%3Dmedia%26token%3D03ad39ae-43cc-451d-9aeb-027df01143c4\&width=768\&dpr=4\&quality=100\&sign=d7bdd293\&sv=1)
* **Выбор момента запроса реквизитов:** Убрана опция выбора момента запроса реквизитов — начиная с версии 2.6 запрос реквизитов у мерчанта всегда будет происходить в момент создания заявки
*   **Замена текста на кнопке при ошибке мерчанта (реквизиты, отображаемые в заявке):** Добавлена опция замены текста, отображаемого вместо шорткода \[to\_account], если по каким-то причинам мерчант не смог предоставить реквизиты для оплаты (опция находится в разделе "**Настройки обменника**" -> "**Основные настройки**")

    ![](https://premium.gitbook.io/~gitbook/image?url=https%3A%2F%2F2574066779-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252Fm9kqZXsNykrN6VyxxXBO%252Fuploads%252FYwxmczrmSFykCqiHOKN7%252Fimage.png%3Falt%3Dmedia%26token%3Dbb68e6c0-7ad1-4863-bdaa-3c60319899a7\&width=768\&dpr=4\&quality=100\&sign=c5c7c199\&sv=1)
*   **Замена текста на кнопке при ошибке мерчанта (ссылка на платежную страницу):** Добавлена опция замены текста на кнопке перехода на платежную страницу мерчанта, если по каким-то причинам мерчант (Bitconce Link, Firekassa Link и др.) не смог предоставить реквизиты для оплаты (опция находится в настройках модулей мерчантов с переходом к реквизитам по кнопке)

    ![](https://premium.gitbook.io/~gitbook/image?url=https%3A%2F%2F2574066779-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252Fm9kqZXsNykrN6VyxxXBO%252Fuploads%252FjppuhwSeQph8BijExiVZ%252Fimage.png%3Falt%3Dmedia%26token%3D7341c172-60fa-4001-9060-6943e90a97f4\&width=768\&dpr=4\&quality=100\&sign=cf12dc0c\&sv=1)\
    Опция в настройках модуля мерчанта

![](https://premium.gitbook.io/~gitbook/image?url=https%3A%2F%2F2574066779-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252Fm9kqZXsNykrN6VyxxXBO%252Fuploads%252FUjIpanbwP0kKiWmVh18G%252Fimage.png%3Falt%3Dmedia%26token%3D994a2160-4376-4afc-bc79-3e6eb816d2e2\&width=768\&dpr=4\&quality=100\&sign=662dc581\&sv=1)

Отображение текста ошибки на кнопке в заявке

*   **Верификация реквизитов:** В общей таблице с заявками на верификацию карты/счета/номера кошелька добавлена возможность указать причину отказа в верификации (просмотр доступен только администраторам и операторам, работающим с модулем). Опция находится в разделе "**Счета пользователей" -> "Верификация счетов**".

    ![](https://premium.gitbook.io/~gitbook/image?url=https%3A%2F%2F2574066779-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252Fm9kqZXsNykrN6VyxxXBO%252Fuploads%252FPN2GX1l8AmJZvGy3xdsr%252Fimage.png%3Falt%3Dmedia%26token%3Dce4d42fc-1038-4a2e-9623-23d1e0611e55\&width=768\&dpr=4\&quality=100\&sign=d0e7014b\&sv=1)
* **Внутренние счета:** Выпущена новая версия модуля внутреннего счета (**iac**), мерчант и автовыплата для внутреннего счета с возможностью выплаты на внутренний счет по API. Старая версия модулей (**domacc**), начиная с версии 2.6 удалена из скрипта. Подробнее о переносе уже добавленных счетов в новый модуль в [**инструкции по обновлению**](https://premium.gitbook.io/main/pered-nachalom-raboty/instrukciya-po-obnovleniyu-skripta/obnovlenie-s-versii-2.5-do-2.6#izmeneniya-v-paneli-administratora)**.**

</details>

## Версия 2.5

<details>

<summary>Список обновлений</summary>



*   Вставка картинки для примера фото для верификации карты в настройках валюты с помощью шорткода img.

    <figure><img src="../../.gitbook/assets/image (521).png" alt=""><figcaption></figcaption></figure>

```
<img src="https://premiumexchanger.com/images.jpg" alt="" />, 
где src - это полный путь до вашей картинки
```

* Список статусов заявки, с которыми будет работать мерчант при получении уведомления об оплате от платежной системы. Если ни один пункт не выбран, то мерчант работает с теми статусами, как было настроено в версии 2.4.

Если один или несколько пунктов выбраны из списка, то мерчант будет работать **только** с выбранными статусами!

Зачем это нужно? Например, если выбрать статус "**Удаленная заявка**", то если заявка будет уже удалена, но от мерчанта придет уведомление о получении оплаты по ней, то мерчант обработает заявку с таким статусом и сделает её оплаченной.

<img src="../../.gitbook/assets/Добавить мерчант ‹ Premium Exchanger — WordPress - Google Chrome_2023-03-18_09_07_40 (1).png" alt="" data-size="original">

* API интерфейс для обменника. [Документация для API интерфейса](https://premium.gitbook.io/main/api-premium-exchanger/api-v1).
* Обновлены все мерчанты и автовыплаты
* Произведен рефакторинг кода и исправлены ошибки
* Добавлена поддержка PHP 8.1
* 3 новых статуса у мерчантов и автовыплат: "**Частичная оплата**", "**Ошибка мерчанта**", "**Частичная выплата**"
* У валют появилась категории
* У формы контактов появились настройки: стоп слова, черный список email, запрещенные почтовые домены, запрещенные ip адреса
* Для страниц добавился hreflang, если отключено автоопределение языка для пользователя
* Ссылка на соглашение при регистрации теперь задается в настройках
* Добавлена отдельная галочка для AML/KYC правил
* Добавились настройки ограничений у отзывов
* В модуль счетов валют добавили значение уникальности: не выводить номер счёта для оплаты в заявке пока с этим счётом есть заявки активные
* Лимит мерчантов по минимальной сумме
* В модуле автоматической регистрации добавил настройку в направление на запрет авто регистрации
* Добавлен парсер Moex
* Возможность отправки уведомлений в телеграм об ошибке парсинга
* В модуль перерасчета добавлены старые курсы
* У внутреннего счета появилась возможность корректировки
* Индивидуальный максимальный партнерский процент
* Верификацию счета можно делать на странице создания заявки через всплывающее окно и можно загрузить пример изображения в инструкцию
* В мерчанты и выплаты добавлена приоритетность подключения в направлении, если их несколько подключено к одному направлению
* В заявках появились новые поля txid\_in, txid\_out, agent
* Для мерчантов можно выбирать в каком шаге создания заявки будет запрос к API происходить
* Шаблоны письма для криптомерчантов стали общими
* Для счетов валют добавлен режим, когда счет не отображается, пока по нему создана активная заявка

</details>
