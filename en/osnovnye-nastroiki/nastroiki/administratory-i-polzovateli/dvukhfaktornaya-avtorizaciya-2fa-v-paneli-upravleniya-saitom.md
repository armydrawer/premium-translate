---
description: >-
  2FA — это проверка личности пользователя с использованием двух разных методов,
  что добавляет дополнительный уровень безопасности для вашего аккаунта и
  уменьшает вероятность взлома.
---

# Двухфакторная аутентификация (2FA) в панели управления сайтом

## 2FA через E-mail или Telegram

Настройте оповещения по E-mail согласно [инструкции](https://premium.gitbook.io/rukovodstvo-polzovatelya/navigaciya/uvedomleniya/opovesheniya-po-e-mail).

Далее в панели управления сайтом в разделе "**Сообщения" → "E-mail шаблоны" →** для шаблонов "**Авторизация по пин-коду**" и “**Уведомить о входе пользователя в ЛК**” разрешите отправку сообщений.

<figure><img src="../../../.gitbook/assets/image (1122).png" alt=""><figcaption><p>Шаблон "<strong>Авторизация по пин-коду</strong>" </p></figcaption></figure>

<figure><img src="../../../.gitbook/assets/image (1222).png" alt=""><figcaption><p>Шаблон “<strong>Уведомить о входе пользователя в ЛК</strong>”</p></figcaption></figure>

Затем в панели управления сайтом в разделе "**Пользователи" (выбрать пользователя) →** установите "**Да**" для параметров "**Уведомление при авторизации (E-mail)**" и "**Авторизация по пин-коду (E-mail)**".&#x20;

<figure><img src="../../../.gitbook/assets/изображение (57).png" alt=""><figcaption></figcaption></figure>

Данные настройки необходимо включить для всех пользователей, у которых есть доступ в панель управления. Каждый раз, при авторизации в панели управления, администратор/оператор будет получать на свой e-mail pin-код для входа в панель управления.

Если вы хотите использовать Telegram для получения сообщений при авторизации, настройте аналогичные опции в разделе "**Сообщения**" ➔ "**Telegram шаблоны**"

Отправку pin-кода можно также настроить через [SMS](https://premium.gitbook.io/rukovodstvo-polzovatelya/navigaciya/uvedomleniya/opovesheniya-po-sms) или [Telegram](https://premium.gitbook.io/main/osnovnye-nastroiki/uvedomleniya-administratoram-i-klientam/uvedomleniya-v-telegram). В этом случае в разделе "**Сообщения**" требуется настройка SMS или Telegram шаблонов, а в профиле пользователя подключение соответствующих параметров.

## 2FA с использованием приложения

В личном кабинете на сайте в разделе "**Настройки безопасности**" активируйте опцию 2FA и отсканируйте QR-код [подходящим приложением](https://trashexpert.ru/mobile/apps/best-two-factor-authentication-apps).&#x20;

<figure><img src="../../../.gitbook/assets/image (42).png" alt="" width="563"><figcaption></figcaption></figure>

В поле "**2FA-код**" введите указанный в приложение код и нажмите кнопку "**Сохранить**".

Для проверки активации 2FA выйдите из своего аккаунта и попробуйте авторизоваться без указания кода.

Если вы получили ошибку, а при повторном входе (с указанием кода) авторизовались — опция настроена корректно.

<div><figure><img src="../../../.gitbook/assets/image (43).png" alt=""><figcaption><p>Вход в админ-панель</p></figcaption></figure> <figure><img src="../../../.gitbook/assets/image (46).png" alt="" width="563"><figcaption><p>Вход в личный кабинет на сайте обменника</p></figcaption></figure></div>

При необходимости вы можете отключить 2FA для любого пользователя в настройках его профиля (раздел "**Пользователи**").

<div><figure><img src="../../../.gitbook/assets/image (44).png" alt=""><figcaption><p>Выключение 2FA в админ-панели</p></figcaption></figure> <figure><img src="../../../.gitbook/assets/image (45).png" alt="" width="563"><figcaption><p>Выключение 2FA в личном кабинете</p></figcaption></figure></div>
