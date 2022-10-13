import json

# read a json in python


# my Json:
x ='{"city":"Bern", "age":42, "name":"Alex"}'

# json to var y:
y = json.loads(x)

# the data return as dictionary:
print(y["age"])
# output
# 42




