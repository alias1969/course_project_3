from utils.format_utils import mask_number, mask_card_number, mask_account_number, split_string_with_digital

import pytest


@pytest.mark.parametrize('text, delimiter, result', [
    ('1111', ',', ('1111', None)),
    ('Счет 35383033474447895560', ' ', ('Счет', '35383033474447895560')),
    ('MasterCard 7158300734726758', ' ', ('MasterCard', '7158300734726758'))
])
def test_split_string_with_digital(text, delimiter, result):
    assert split_string_with_digital(text, delimiter) == result


@pytest.mark.parametrize('text, result', [
    ('Счет 7158300734726758', 'Счет 7158 30** **** 6758'),
    ('MasterCard 35383033474447895560', 'MasterCard 3538 30** **** **** 5560'),
    ('', '')
])
def test_mask_card_number(text, result):
    assert mask_card_number(text) == result


@pytest.mark.parametrize('text, result', [
    ('Счет 35383033474447895560', 'Счет ****************5560'),
    ('MasterCard 7158300734726758', 'MasterCard ************6758'),
    ('', '')
])
def test_mask_account_number(text, result):
    assert mask_account_number(text) == result


@pytest.mark.parametrize('text, result', [
    ('Счет 99895560', 'Счет ****5560'),
    ('Счет 35383033474447895560', 'Счет ****************5560'),
    ('MasterCard 7158300734726758', 'MasterCard 7158 30** **** 6758'),
    ('', '')
])
def test_mask_number(text, result):
    assert mask_number(text) == result

