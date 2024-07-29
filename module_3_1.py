calls = 0


def count_calls():
    global calls
    calls += 1


def is_contains(string, list_to_search):
    count_calls()
    return True if string.lower() in [x.lower() for x in list_to_search] else False


def string_info(string):
    count_calls()
    return (len(string), string.upper(), string.lower())


print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN']))  # Urban ~ urBAN
print(is_contains('cycle', ['recycling', 'cyclic']))  # No matches
print(calls)


