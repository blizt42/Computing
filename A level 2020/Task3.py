

# Task 3.1
def task3_1(quantity_of_data):
    units = {'KB':10**3, 'MB':10**6, 'GB':10**9, 'TB':10**12}
    unit = quantity_of_data[-2:]
    quantity = quantity_of_data[:-2]

    if unit not in units:
        print('invalid data')
        return 'invalid data'
    for char in quantity:
        if not char.isdigit():
            print('invalid data')
            return 'invalid data'

    byte = int(quantity) * units[unit]
    # print(byte)
    return byte

# Task 3.2
def task3_2(quantity_of_data):
    units = {'KB': 10 ** 3, 'KiB': 2**10, 'MB': 10 ** 6, 'MiB': 2**20, 'GB': 10 ** 9, 'GiB': 2**30,
             'TB': 10 ** 12, 'TiB': 2**40}
    unit = quantity_of_data[-2:]
    if unit not in units:
        unit = quantity_of_data[-3:]
        if unit not in units:
            print('invalid data')
            return 'invalid data'
        quantity = quantity_of_data[:-3]
    else:
        quantity = quantity_of_data[:-2]

    byte = int(quantity) * units[unit]
    # print(byte)
    return byte

# Task 3.3
def task3_3(quantity_of_data, target_unit):
    units = {'KB': 10 ** 3, 'KiB': 2 ** 10, 'MB': 10 ** 6, 'MiB': 2 ** 20, 'GB': 10 ** 9, 'GiB': 2 ** 30,
             'TB': 10 ** 12, 'TiB': 2 ** 40}
    if target_unit not in units:
        print('invalid data')
        return 'invalid data'
    byte = task3_2(quantity_of_data)
    newByte = byte / units[target_unit]
    # print(newByte)
    return newByte

# task3_1("8KB")
# task3_2('2MiB')
print(task3_3('512MiB', 'GiB'))