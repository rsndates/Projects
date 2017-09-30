from neo4j.v1 import GraphDatabase, basic_auth
import operator

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


aDict = {}

t = 0
while (t < len(refNodes)):
    aDict[refNodes[t]] = 0.0
    t = t + 1


session.run(insert_query, parameters={"pairs": data})

w = 0
while (w < len(refNodes)):

# Friends of a friend

    foaf_query = '''
MATCH (person:Person)-[:KNOWS]-(friend)-[:KNOWS]-(foaf)
WHERE person.name = {name}
  AND NOT (person)-[:KNOWS]-(foaf)
RETURN friend.name AS name
'''

    results = session.run(foaf_query, parameters={"name": refNodes[w]})
    for record in results:
        #print(record["name"])
        aDict[record["name"]] = aDict[record["name"]] + 1

    w = w + 1

print "The Betweeness Centrality:"
print max(aDict)
print "Id:"
print max(aDict, key=aDict.get)
session.close()
