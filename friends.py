import requests
from datetime import date

#прога, которая считает сколько друзей в вк определенного возраста 

# function for returning age in years
def calc_birthday(birthday):

    birthday = date(int(birthday[-1]), int(birthday[-2]), int(birthday[-3]))
    today = date.today()
    if (today.month, today.day) > (birthday.month, birthday.day):
        return (today.year - birthday.year)
    else:
        return (today.year - birthday.year) - 1




class Counter(dict):
    def __missing__(self, key):
        return 0


def calc_age(user_name):

    result_dict = Counter()
    api_url = 'https://api.vk.com/method/users.get?v=5.87&access_token=3d044f423d044f423d044f42033d62b1c933d043d044f4266edd604bde25a0f05f8eeb1&user_ids='
    r = requests.get(api_url + user_name)
    user_id = r.text.split(':')[2]

    api_url = 'https://api.vk.com/method/friends.get?v=5.87&access_token=3d044f423d044f423d044f42033d62b1c933d043d044f4266edd604bde25a0f05f8eeb1&user_id='

    r = requests.get(api_url + user_id[:-13] + '&fields=bdate')
    data = r.json()

    friend_list = data['response']['items']

    for friends in friend_list:
        try:
            birthday = friends['bdate'].split('.')
            if (len(birthday) == 3):  ##all three fields of age are filled DD.MM.YYYY
                result_dict[calc_birthday(birthday)] += 1


        except KeyError:
            continue  # the quantity of friends without filled age row

    intermediate_sort = sorted(result_dict.items(), key=lambda x: x[0])  # sorting by age increasing
    return sorted(intermediate_sort, key=lambda x: x[1], reverse=True)  # sorting by quantity decreasing


if __name__ == '__main__':

    sorted_dict = calc_age('reigning')
    print(type(sorted_dict))
    print(sorted_dict)
