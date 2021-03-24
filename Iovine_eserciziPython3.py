import numpy as np
d = {
              "Mario":{
                        "Matematica":6,
                        "Italiano":6,
                        "Scienze":7,
                        "Inglese":4
                        },
                "Giovanni":{
                            "Matematica":4,
                            "Italiano":6,
                           "Scienze":5,
                            "Inglese":7
                            },
                "Paola":{
                       "Matematica":9,
                        "Italiano":6,
                        "Scienze":8,
                        "Inglese":8
                       }
                }

print(d)

votiMario = [d["Mario"]["Matematica"],d["Mario"]["Italiano"],d["Mario"]["Scienze"],d["Mario"]["Inglese"]]
votiGiovanni = [d["Giovanni"]["Matematica"],d["Giovanni"]["Italiano"],d["Giovanni"]["Scienze"],d["Giovanni"]["Inglese"]]
votiPaola = [d["Paola"]["Matematica"],d["Paola"]["Italiano"],d["Paola"]["Scienze"],d["Paola"]["Inglese"]]

print("La media di Mario è", np.mean(votiMario))
print("La media di Giovanni è", np.mean(votiGiovanni))
print("La media di Paola è", np.mean(votiPaola))


