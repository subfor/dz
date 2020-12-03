persons = [{"name": "John", "age": 35}, {"name": "Bob", "age": 19}, {"name": "Jack", "age": 15},
           {"name": "Thomas", "age": 45}, {"name": "Richard", "age": 25}, {"name": "Richird", "age": 15}]

ages_list = [value_age.get("age") for value_age in persons]
age_min = min(ages_list)
for index_dict in persons:
    if index_dict.get("age") == age_min:
        print(index_dict.get("name"))
