user_input = raw_input("Please Enter in Social Id for Facebook Data set. options 0, 107, 348, 414, 686, 1684, 1912, 3437, 3980: ")

data = []
file = open('facebook/'+ str(user_input)+'.edges', 'r')
for f in file.readlines():
    temp = []
    temp = f.split(" ")
    temp[-1] = temp[-1].strip()

    data.append(temp)
file.close()
print len(data)

