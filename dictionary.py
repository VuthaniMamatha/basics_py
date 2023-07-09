dict = {
   'stud1':{
        'name':'mamatha',
        'rollno':'20hr1a05c2'
    },
   'stud2':{
        'name':'mamatha',
        'rollno':'20hr1a05b2'
    }
}
print(dict)
print(dict['stud1']['name'])
dict['stud1']['name']='rekha'
print(dict)
dict['stud1']['rollno']='20hr1a05b2'
dict['stud2']['rollno']='20hr1a05c2'
print(dict)
print(dict.keys())
print(dict.values())
for x in dict:
  print(x)
for i in dict.values():
  print(i)
for a,b in dict.items():
  print(a,b)
dict_copy=dict.copy()
dict_copy.pop('stud1')
print(dict_copy)
