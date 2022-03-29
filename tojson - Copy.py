import os
import csv
import json

files = [f for f in os.listdir("grades")]
print(files)



def mstrip(str):
    whitelist = set('abcdefghijklmnopqrstuvwxyz ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    return ''.join(filter(whitelist.__contains__, str))

# goal of csv json:
"""
{
  term: {
    crs: {
      nbr: [
         {clss},
         ...
      ],
      ...
    },
    ...
  },
  ...
}
"""

# start with files[0]
for file in files:
    to_be_json = {}
    data_path = os.path.join("grades", file)
    with open(data_path, 'r') as csvfile:
        term = file.strip(".csv")
        to_be_json[term] = {}
        print(term)
        reader = csv.reader(csvfile, delimiter=',')
        data_list = []

        idx = 0
        header = []
        for row in reader:
            if idx == 0:
                idx=1
                for prop in row:
                    header.append(mstrip(prop))
            else:
                # make class into dict
                clss = {}
                j = 0
                for h in header:
                    clss[h] = row[j]
                    j += 1

                # set up default structures
                to_be_json[term].setdefault(row[0], {})
                to_be_json[term][row[0]].setdefault(row[1], []).append(clss)
        
        with open(term+".json", "w") as outfile:
            json.dump(to_be_json, outfile)

"""
data=[]
json_str_start=""
json_str=""
for f in fname:
    data_path = os.path.join("resources", f)
    data_path2 = os.path.join("resources", "data.json")
    with open(data_path, 'r') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        year=f.replace('.csv', '')
        json_str_start='{"' + year +'": '

        data_list=list()
        
        for row in reader:
            data_list.append(row)

        data = [dict(zip(data_list[0],row)) for row in data_list]
        data.pop(0)
 
        json_str = json_str + json_str_start + json.dumps(data) + " }, \n"


        
    
print (json_str[0:50])

with open(data_path2, 'w+') as jsonfile:
     
    jsonfile.write(json_str)
"""
