import pandas as pd
import pytest

from src.reports import spending_by_category
from pandas import DataFrame, Series


@pytest.fixture
def operations_1():
    transactions_df = pd.read_excel("../data/operations_1.xlsx")
    return transactions_df


def test_filtering_by_date(operations_1):
    assert spending_by_category(operations_1, "Фастфуд", "2021-12-29 15:45:34") == [
        {
          'MCC': 7512,
          'Бонусы (включая кэшбэк)': 20,
          'Валюта операции': 'RUB',
          'Валюта платежа': 'RUB',
          'Дата операции': '26.12.2021 22:09:56',
          'Дата платежа': '27.12.2021',
          'Категория': 'Фастфуд',
          'Кэшбэк': 0,
          'Номер карты': '*5091',
          'Округление на инвесткопилку': 0,
          'Описание': 'Ситидрайв',
          'Статус': 'OK',
          'Сумма операции': -415.32,
          'Сумма операции с округлением': 415.32,
          'Сумма платежа': -415.32}]
