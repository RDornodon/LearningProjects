import json

class JSONObject:
  def __init__( self, dict ):
      vars(self).update( dict )

list_of_dicts = """{
  "persons": [{
     "name": "Oliver",
     "ipAdress":23241312342,
     "userToken":"NzDwLzLceGLyoPYwykwxFHzCFDVtynVs-wHGKT.WgnyAfQsIjBg.hHpLlELHhtYk"
  },
  {
     "name": "Jackson",
     "ipAdress":"Hidden",
     "userToken":"DaJNaFojJbnCqJVPCcUEaXnkrpugsRg=="
  }]
}"""
#lol

dict_object = json.loads(list_of_dicts, object_hook= JSONObject)

for person in dict_object.persons:
    print(f'User: {person.name} connected from [{person.ipAdress}] with the token of [{person.userToken}]')
