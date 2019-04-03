import pip
import json

#reads json file
with open('dependencies.json') as myfile:
#Json decodes to dict
   data=myfile.read()
   obj=json.loads(data)
i=0
flag = 0
dict = {}
for (k,v) in obj.items():
    #Installs python packages
     failed=pip.main(["install",k+"=="+str(v)])
     if failed == 1:
         flag = 1
         dict[i] = k+ "==" +str(v)
         i = i + 1

if flag == 0:
    print("Success")
else:
    print("Fail \n")
#list of failed packages
    print("{" + "\n".join("{}: {}".format(k, v) for k, v in dict.items()) + "}")