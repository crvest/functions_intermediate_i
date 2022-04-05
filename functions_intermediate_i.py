# # 1.
x = [[5, 2, 3], [10, 8, 9]]
students = [
    {'first_name': 'Michael', 'last_name': 'Jordan'},
    {'first_name': 'John', 'last_name': 'Rosales'}
]
sports_directory = {
    'basketball': ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer': ['Messi', 'Ronaldo', 'Rooney']
}
z = [{'x': 10, 'y': 20}]

x[1][0] = 15
students[0]['last_name'] = 'Bryant'
sports_directory['soccer'][0] = 'Andres'
z[0]['y'] = 30

print(x)
print(students)
print(sports_directory)
print(z)


# 2.
students = [
    {'first_name':  'Michael', 'last_name': 'Jordan'},
    {'first_name': 'John', 'last_name': 'Rosales'},
    {'first_name': 'Mark', 'last_name': 'Guillen'},
    {'first_name': 'KB', 'last_name': 'Tonel'}
]

# # print(students[0])
# # print(students[0].keys())
# # print(students[0].items())

def iterateDictionary(some_list):
    for i in range(len(some_list)):
        for x,y in some_list[i].items():
            print(f"{x} - {y}")

iterateDictionary(students)


# # 3. Get Valyes From a List of Dictionaries
def iterateDictionary2(key_name, some_list):
    for i in range(len(some_list)):
        print(some_list[i][key_name])

iterateDictionary2("first_name", students)
iterateDictionary2("last_name", students)


# 4. Iterate through a Dictionary with List Values
dojo = {
    'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
    'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}
def printInfo(some_dict):
    for x in some_dict:
        print(str(len(some_dict[x])) + " " + x)
        for j in some_dict[x]:
            print(j)
        print("")

printInfo(dojo)
