import json

r = {'is_claimed': 'True', 'rating': 3.5}

r = json.dumps(r)

loaded_r = json.loads(r)

print(loaded_r)

