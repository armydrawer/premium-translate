#!/bin/bash

#пароль от кошелька НА ПРИЕМ (default_wallet_in)
WALLET_PASSWORD_IN="пароль_от_кошелька"


#пароль от кошелька НА ВЫПЛАТУ (default_wallet_out)
WALLET_PASSWORD_OUT="пароль_от_кошелька"


echo -e "\nОстановка службы electrum_in: \c"
sleep 5 && electrum_in/Electrum-4.4.6/run_electrum stop -P
echo -e "Запуск службы electrum_in: \c"
sleep 5 && electrum_in/Electrum-4.4.6/run_electrum daemon --noonion -P -d
echo -e "Генерация пароля electrum_in: \c"
sleep 5 && electrum_in/Electrum-4.4.6/run_electrum load_wallet -W "${WALLET_PASSWORD_IN}" -P
echo -e "Служба electrum_in перезапущена"

echo -e "\nОстановка службы electrum_out: \c"
sleep 5 && electrum_out/Electrum-4.4.6/run_electrum stop -P
echo -e "Запуск службы electrum_out: \c"
sleep 5 && electrum_out/Electrum-4.4.6/run_electrum daemon --noonion -P -d
echo -e "Генерация пароля electrum_out: \c"
sleep 5 && electrum_out/Electrum-4.4.6/run_electrum load_wallet -W "${WALLET_PASSWORD_OUT}" -P
echo -e "Служба electrum_out перезапущена"
