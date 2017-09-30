

from neo4j.v1 import GraphDatabase, basic_auth
user_input = raw_input("Please Enter in Social Id for Facebook Data set. options 0, 107, 348, 414, 686, 1684, 1912, 3437, 3980: ")
username_input = raw_input("Enter in your neo4j server username: ")
password_input = raw_input("Enter in your neo4j server password: ")


driver = GraphDatabase.driver("bolt://localhost", auth=basic_auth(str(username_input), str(password_input)))
session = driver.session()

# Insert data
insert_query = '''
UNWIND {pairs} as pair
MERGE (p1:Person {name:pair[0]})
MERGE (p2:Person {name:pair[1]})
MERGE (p1)-[:KNOWS]-(p2);
'''

#data = [["Jim","Mike"],["Jim","Billy"],["Anna","Jim"],
        #  ["Anna","Mike"],["Sally","Anna"],["Joe","Sally"],
        #  ["Joe","Bob"],["Bob","Sally"]]


data = []
file = open('facebook/'+ str(user_input)+'.edges', 'r')
for f in file.readlines():
    temp = []
    temp = f.split(" ")
    temp[-1] = temp[-1].strip()
    data.append(temp)
file.close()

edata = []
Num_of_nodes = 0
refNodes = []
file = open('facebook/'+ str(user_input)+'.edges', 'r')
edata = file.read().split()
Num_of_nodes = len(set(edata))
refNodes = list(set(edata))

file.close()

session.run(insert_query, parameters={"pairs": data})

friendlist = []
CC = 0.0
cclist = []
# How many friends
k = 0
while(k < Num_of_nodes):
    friends_query = """
    MATCH (person:Person)-[:KNOWS]-(friend)
    WHERE person.name = {name}
    RETURN friend.name AS friend
    """
    results = session.run(friends_query, parameters={"name": refNodes[k]})
    friends = 0.0
    for record in results:
            friendlist.append(record["friend"])
            friends = friends + 1
    #print friends
# Common friends

    common_friends_query = """
    MATCH (user:Person)-[:KNOWS]-(friend)-[:KNOWS]-(foaf:Person)
    WHERE user.name = {user} AND foaf.name = {foaf}
    RETURN friend.name AS friend
    """
    Nv = 0.0
    i = 0
    while (i < len(friendlist)):


        Nv = 0.0
        results = session.run(common_friends_query, parameters={"user": refNodes[k], "foaf": friendlist[i]})
        for record in results:
            Nv = Nv + 1
           # print Nv
        if (friends > 1):
            CC = (Nv) / (friends * (friends - 1))
        else:
            CC = 0.0
        cclist.append(CC)
        i = i + 1


    k = k + 1

x = 0
avg = 0.0

avg = sum(cclist) / len(cclist)

# print cclist
# print refNodes
# print Nv
# print friends
# print CC
print "The Clustering Coefficient is:"
print avg

session.close()
