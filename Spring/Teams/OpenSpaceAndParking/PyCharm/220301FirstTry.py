# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

# Trying to Push to GitHub
example = list()
example = []
primes = [2,3,5,7,11,13]
primes.append(17)
primes.append(19)
print(primes[3])
print(primes[2:5])

numbers = [1,2,3]
letters = ['a','b','c']
print(numbers+letters)

print(dir(numbers))

# FriendFace
# user_id = 209
# message = "D5 E5 C5 C4 G4"
# language = "English"
# datetime = "20230215T124231Z"
# location = (44.590533, -104.715556)
post = {"user_id":209, "message":"D5 E5 C5 C4 G4", "language":"English","datetime":"20230215T124231Z", "location":"(44.590533, -104.715556)"}
print(type(post))

post2 = dict(message="SS Cotopaxi", language="English")
print(post2)
post2["user_id"] = 209
post2["datetime"] = "19771116T093001Z"
print(post2)
if 'location' in post2:
    print(post2['location'])
else:
    print("no location value in post2")

try:
    print(post2['location'])
except KeyError:
    print("no location value in post2")

loc = post.get('location',None)
print(loc)
loc = post2.get('location',None)
print(loc)

for key in post.keys():
    value = post[key]
    print(key,"=",value)
for key in post2.keys():
    value = post[key]
    print(key,"=",value)
for key, value in post.items():
    print(key,"=",value)