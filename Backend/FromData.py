import json


def get_data(tab_name):
    """ Gets all the data and returns it as a list
        :param
            tab_name: The option tab
        :return:
            data: list
    """
    with open('data.txt', 'r') as in_file:
        data = json.load(in_file)
        i = 0
        while i < len(data):
            if data[i][0] == tab_name:
                return remove_empty(data[i])
            i += 1


def remove_empty(data_set):
    """ Removes empty items from the data_set

    :param data_set: List of data
    :return: List of data without blank objects
    """
    while '' in data_set:
        data_set.remove('')
    return data_set


def get_options():
    """ Gets each header from the data file
        :return:
            - list of results
    """
    with open('data.txt', 'r') as in_file:
        data = json.load(in_file)
        results = []
        i = 0
        while i < len(data):
            results.append(data[i][0])
            i += 1
        return results


def get_item_and_price(data, index):
    """ Gets the item name and price from the data set

    :param data: The data list
    :param index: The index of the data you want
    :return: Name, Price
    """
    new_index = (((index + 1) * 2) - 1)
    new_data = data[new_index:new_index + 2]
    return new_data[0], new_data[1]


def get_length(data):
    """ Gets the unreal length of the data list

    :param data: List of data
    :return: Integer size
    """
    return int((len(data) - 1) / 2)


# print(get_data("Hot Food"))
# print(get_length(get_data("Breakfast")))

