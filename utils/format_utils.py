def split_string_with_digital(text, delimiter):
    """ Разделяет строку, содержащую цифры, на текстовую часть и цифровую
    Вначале строки должен быть текст, а цифры после пробела"""

    count_smb = text.strip().find(delimiter)

    if count_smb == -1:
        return text, None

    part_text = text[:count_smb]
    part_digital = text[count_smb + 1:]

    return part_text, part_digital


def mask_card_number(number):
    """Номер карты замаскирован: отображается в формате XXXX XX** **** XXXX
    (видны первые 6 цифр и последние 4, разбито по блокам по 4 цифры, разделенных пробелом)"""

    # определим позиции первых и последних символов, к-рые отображаются
    count_fist_smb = 6
    count_last_smb = 4

    # выделим текстовую и цифровую часть номера карты - разделены пробелом
    # текстовую часть помещаем в результат - к ней будем добавлять замаскированный номер
    result, part_numeral = split_string_with_digital(number, ' ')

    # если цифровая часть короче числа первых или последних символов, то возвращаем исходный текст
    if part_numeral is None or len(part_numeral) <= max(count_fist_smb, count_last_smb):
        return number

    # определим с какой позиции выводим последние цифры
    count_last = len(part_numeral) - 4

    for i in range(0, len(part_numeral)):

        # если позиция кратна 4м, то добавляем пробел
        if i % 4 == 0:
            result += ' '

        # если позиция цифровой части меньше 6 или больше последних 4х, то выводим цифры
        # иначе *
        if i < count_fist_smb or i >= count_last:
            result += part_numeral[i]
        else:
            result += '*'

    return result


def mask_account_number(number):
    """Номер счета замаскирован и не отображается целиком в формате **XXXX
    (видны только последние 4 цифры номера счета)"""

    # определим позиции первых и последних символов, к-рые отображаются
    count_last_smb = 4

    # выделим текстовую и цифровую часть номера карты - разделены пробелом
    # текстовую часть помещаем в результат - к ней будем добавлять замаскированный номер
    part_text, part_numeral = split_string_with_digital(number, ' ')

    # если цифровая часть короче числа первых или последних символов, то возвращаем исходный текст
    if part_numeral is None or len(part_numeral) <= count_last_smb:
        return number

    # определим с какой позиции выводим последние цифры
    count_last = len(part_numeral) - 4

    mask = ['*' for i in range(0, len(part_numeral) - count_last_smb)]

    return f'{part_text} {''.join(mask)}{number[-4:]}'


def mask_number(number):
    """Маскирует номер карты или счета"""
    if number.strip().find('Счет') == 0:
        return mask_account_number(number)
    else:
        return mask_card_number(number)



