# 2
# you cannot change a tuple and you can change a list
# you can use tuples as a strong data for dicts
# a tuple can have different types of signs
# would prefer a list for data that changed- so i can add new data
# / remove old and change the way its written

# 3
data_tuple = ({
                  "name": "Alice",
                  "age": 30,
                  "city": "New York"
              }, 1000, "secret-code")
data_tuple[0]["age"] = 31
print(data_tuple)
data_tuple[0].clear()
print(data_tuple)
# you can change the values & keys inside of a dict, even though its inside a tuple
# for example, if you try to change data_tuple[2]["secret-code"] = "none"-
# -it will be an error because its outside the dict

