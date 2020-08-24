import bs4
from decimal import Decimal
import requests
from decimal import Decimal





def convert(amount, cur_from, cur_to, date):

    response = requests.get(f'https://www.cbr.ru/scripts/XML_daily.asp?date_req={date}')  # Использовать переданный requests
    soup = bs4.BeautifulSoup(response.content, 'xml')
    cur_from = [soup.find('CharCode', text=f'{cur_from}').find_next_sibling('Value').string,
                soup.find('CharCode', text=f'{cur_from}').find_next_sibling('Nominal').string]
    amount = amount * (Decimal(cur_from[0].replace(',','.')) / Decimal(cur_from[1]))
    cur_to = [soup.find('CharCode', text=f'{cur_to}').find_next_sibling('Value').string,
              soup.find('CharCode', text=f'{cur_to}').find_next_sibling('Nominal').string]
    amount = amount / (Decimal(cur_to[0].replace(',','.')) / Decimal(cur_to[1]))

    return amount.quantize(Decimal("1000.1000")) # не забыть про округление до 4х знаков после запятой


if __name__ == '__main__':
    result = convert(Decimal("1.00"), 'EUR', 'JPY', "24/08/2020")