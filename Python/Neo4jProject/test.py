

from neo4j.v1 import GraphDatabase, basic_auth

driver = GraphDatabase.driver("bolt://localhost", auth=basic_auth("neo4j", "boonie"))
session = driver.session()

# Insert data
insert_query = '''
UNWIND {pairs} as pair
MERGE (p1:Person {name:pair[0]})
MERGE (p2:Person {name:pair[1]})
MERGE (p1)-[:KNOWS]-(p2);
'''

data = []
file = open('facebook/3980.edges', 'r')
for f in file.readlines():
    temp = []
    temp = f.split(" ")
    temp[-1] = temp[-1].strip()
    data.append(temp)
file.close()


session.run(insert_query, parameters={"pairs": data})

# Friends of a friend

foaf_query = '''
MATCH (person:Person)-[:KNOWS]-(friend)-[:KNOWS]-(foaf)
WHERE person.name = {name}
  AND NOT (person)-[:KNOWS]-(foaf)
RETURN foaf.name AS name
'''

#results = session.run(foaf_query, parameters={"name": "169"})
#for record in results:
   # print(record["name"])


# Common friends

common_friends_query = """
MATCH (user:Person)-[:KNOWS]-(friend)-[:KNOWS]-(foaf:Person)
WHERE user.name = {user} AND foaf.name = {foaf}
RETURN friend.name AS friend
"""

#results = session.run(common_friends_query, parameters={"user": "169", "foaf": "170"})
#for record in results:
#    print(record["friend"])

# Connecting paths

connecting_paths_query = """
MATCH path = shortestPath((p1:Person)-[:KNOWS*..20]-(p2:Person))
WHERE p1.name = {name1} AND p2.name = {name2}
RETURN path
"""

results = session.run(connecting_paths_query, parameters={"name1": "3987", "name2": "4002"})
for record in results:
    print (record["path"])

friends_query = """
MATCH (person:Person)-[:KNOWS]-(friend)
WHERE person.name = {name}
RETURN friend.name AS friend
"""
results = session.run(friends_query, parameters={"name": "169"})
# friends = 0
# for record in results:
#     #print(record["friend"])
#     friends = friends + 1


session.close()
