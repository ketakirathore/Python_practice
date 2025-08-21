
#d = {"key":"value","Name": "john", "age": 21}
#print(type(d)) = dictionary type


#replace methods = if you want to replace the value it will change the value by given methodd.
#d["Name"] = "max"
#d["Name1"] = "max" = key always have to be uique if you want to add the given format "name1" : "max"
#key shoudnt be duplicate but value can be duplicate

#d = {"key":"value","name": "john", "age": 21, "skills": ["python", "SQL", "html"]}

#get method
#print(d.get("age")) = 21 to get the value of given key 

#membership operator = true /false
#print("john" in d) = false, in dictionary you have to provide key not value by membership operator.
#print("name" in d) = true

#you can save multiple values in dictionary

#print(d["skills"][2]) = "html"

#d = {12 : "abc"} = as key int is allow but its not use as a list is not allow not symbol, tuple is ca be use

#d = {"key":"value","name": "john", "age": 21, "skills": {"web": "html", "DA": "Python"}}
#print(d["skills"]["DA"]) = "Python"
#to get the value from perticular value have to follow this method

#you can add dict in dict, set and list in dict

#pop method = provide atleast one key to remove the perticular item
#d.pop("skills")

#delete method = to delete the perticular item
#del d["skills"]

#d.clear() = to clear all the elements

#print(d.keys()) = for only key
#print(d.values()) = for values 
#print(d*2) = dict doesnt support integer
#dictionary doesnt support integer multiple cause of the nature of the dict as it is 
#doesnt print duplicate items as key should be unique

#print(d.items()) = key value pair in the form of tuple ('key','value')

#d.popitem() = it remove the last elements
#print(d)








