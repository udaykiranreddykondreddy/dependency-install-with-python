import os
import json
class DependencyInstall():
    def __init__(self,parameters):
        self.dependencies_list = parameters.get("dependencies",[])

    def install(self):
        try:
            for each_dependency in self.dependencies_list:
                dependency_name  = each_dependency.find("=")
                dependency_name1  = each_dependency[:dependency_name]
                os.system("pip3 install "+dependency_name1)
        except Exception as e:
            print(e)
            print("error install the dependency ",dependency_name1)



if __name__=="__main__":
    parameters = {"dependencies":[]}
    with open('dependencies.json','r') as json_data:  
        d = json.load(json_data)
    parameters["dependencies"] = d["Dependencies"]
    obj = DependencyInstall(parameters)
    obj.install()

