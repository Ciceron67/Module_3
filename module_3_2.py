def send_email(message, recipient, sender='university.help@gmail.com'):
    if '@' not in sender or '@' not in recipient:
        return print(f'Невозможно отправить письмо с адреса {sender} на адрес {recipient}')
    if recipient[-4:] != '.com' and recipient[-3:] != '.ru' and recipient[-4:] != '.net':
        return print(f'Невозможно отправить письмо с адреса {sender} на адрес {recipient}')
    if sender[-4:] != '.com' and sender[-3:] != '.ru' and sender[-4:] != '.net':
        return print(f'Невозможно отправить письмо с адреса {sender} на адрес {recipient}')
    if sender == recipient:
        return print(f'Нельзя отправить письмо самому себе!')
    if sender == 'university.help@gmail.com':
        return print(f'Письмо успешно отправлено с адреса {sender} на адрес {recipient}.')
    else:
        return print(f'НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipient}.')


send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')
send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender='urban.info@gmail.com')
send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')
send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')
