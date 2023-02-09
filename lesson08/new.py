def print_long_words(words, n):
    for w in words:
        if (len(w) >= n):
            print(w)


def filter_long_words(words, n):
    list = []
    for w in words:
        if (len(w) >= 4):
            list.append(w)
    return list


def annealing_temp(dna_string):
    return 81.5 + 0.41*findGCPercent(dna_string) - (675/len(dna_string))


def findGCPercent(dna_string):
    i = 0
    for l in dna_string:
        if l == "G" or l == "C":
            i += 1
    return i/len(dna_string)


def find_house(redata, beds):
    list = []
    for element in redata:
        if element['beds'] == str(beds):
            list.append((element['price'], element['street']))
    return list


def average_house_cost(redata):
    list = []
    for element in redata:
        list.append(int(element['price']))
    return sum(list)/len(list)


# print_long_words(['A', 'road', 'diverged', 'in', 'a', 'yellow', 'wood'], 4)
# a1 = ['A', 'road', 'diverged', 'in', 'a', 'yellow', 'wood']
# print(filter_long_words(a1, 4))
shopping_list = [['Item', 'Quantity', 'Price per item in Dollars'], [
    'Bag of carrots', '2', '5'], ['Box of cookies', '1', '1'], ['Brie Cheese', '5', '2']]
# print(annealing_temp("ATGCATGCATGCATGCATGC"))
# print(len(list))
# print(int(shopping_list[1][1])*int(shopping_list[1][2]))
redata = [{'street': '3526 HIGH ST',
          'city': 'SACRAMENTO',
           'zip': '95838',
           'state': 'CA',
           'beds': '2',
           'baths': '1',
           'sq__ft': '836',
           'type': 'Residential',
           'sale_date': 'Wed May 21 00:00:00 EDT 2008',
           'price': '92549',
           'latitude': '38.631913',
           'longitude': '-121.434879'},
          {'street': '35 HIGH ST',
          'city': 'SACRAMENTO',
           'zip': '95838',
           'state': 'CA',
           'beds': '2',
           'baths': '1',
           'sq__ft': '836',
           'type': 'Residential',
           'sale_date': 'Wed May 21 00:00:00 EDT 2008',
           'price': '99',
           'latitude': '38.631913',
           'longitude': '-121.434879'},
          {'street': '35 HIGH ST',
          'city': 'SACRAMENTO',
           'zip': '95838',
           'state': 'CA',
           'beds': '2',
           'baths': '1',
           'sq__ft': '836',
           'type': 'Residential',
           'sale_date': 'Wed May 21 00:00:00 EDT 2008',
           'price': '9913243',
           'latitude': '38.631913',
           'longitude': '-121.434879'}]

print(average_house_cost(redata))
