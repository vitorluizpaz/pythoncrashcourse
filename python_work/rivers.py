rivers = {"nile": "egypt",
    "amazonas": "brasil",
    "cubatao": "brasil"}

for k,v in rivers.items():
    print(f"{k} runs through {v}")

for k in rivers:
    print(f"{k} is in rivers dictionary")

for v in rivers.values():
    print(f"{v}")