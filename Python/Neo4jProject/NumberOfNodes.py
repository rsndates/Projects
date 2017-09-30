user_input = raw_input("Please Enter in Social Id for Facebook Data set. options 0, 107, 348, 414, 686, 1684, 1912, 3437, 3980: ")

data = []
Num_of_nodes = 0
refNodes = []
file = open('facebook/'+ str(user_input)+'.edges', 'r')
data = file.read().split()
Num_of_nodes = len(set(data))
refNodes = list(set(data))
file.close()
print "Number of Nodes:"
print Num_of_nodes
