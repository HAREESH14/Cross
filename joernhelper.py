from joern_lib import client
from clean import Cleaner
import os 
from graphviz import Source


class JoernHelper:
    def __init__(self,conn):
        self.conn = conn

    async def import_source(self,pathcode):
        try:
            data = await client.q(self.conn,f'importCode("{pathcode}")')

            if data is None:
                print("Something went Wrong")
                return None
            else:
                print("Source code is imported succesfully")
        
        except Exception as e:
            print(f"connection error:{e}")
            return 
        
    async def create_graph(self, graphtype="dotAst", method_name=None,filecreate=False):
        if method_name is None:
            print("""
        -------------Enter the method name generating graph-------------

                  usage:- create_graph(dotCfg, main)


                  """)
            return

        # Map graphtype to query index
        graph_type_map = {
            "dotAst": 0,
            "dotCfg": 1,
            "dotPdg": 2,
            "dotCpg14": 3,
            "dotDdg": 4,
            "dotCdg": 5,
        }

        queries = [
            f'cpg.method.name("{method_name}").dotAst.l',
            f'cpg.method.name("{method_name}").dotCfg.l',
            f'cpg.method.name("{method_name}").dotPdg.l',
            f'cpg.method.name("{method_name}").dotCpg14.l',
            f'cpg.method.name("{method_name}").dotDdg.l',
            f'cpg.method.name("{method_name}").dotCdg.l',
        ]
        try:
            if graphtype not in graph_type_map:
                print(f"Invalid graph type '{graphtype}'. Valid types: {list(graph_type_map.keys())}")
                return

            query_index = graph_type_map[graphtype]
            res = await client.q(self.conn, queries[query_index])

            data=Cleaner.clean_content(res["response"])
            if filecreate == True:
                output_dir = os.path.join(os.getcwd(), "output")
                os.makedirs(output_dir, exist_ok=True)
                file_path = os.path.join(output_dir,"result.dot")

                if not os.path.exists(file_path):
                    if not data:
                        print("the data is empty line 68")
                        return
                    try:
                        with open(file_path,"w") as f:
                            f.write(data)
                    except Exception as e:
                        print(f"Error Occured:{e}")
                    # with open(file_path, "w") as f:

                    #     f.write(res["response"])
                    # print(f"Graph written successfully to {file_path}")
                else:
                    print(f"File '{file_path}' already exists. No data written.")
            else:
                return data

        except Exception as e:
            print(f"Error while creating graph: {e}")



    def visualizeGraph(self,data=None,setfilename="result_graph",format="png",veiw=True):
        if data is None:
            print("No data Found Error")
        try:
            graph=Source(data)
            graph.render(f"{setfilename}",format=f"{format}",view=veiw,cleanup=True)
            
        except Exception as e:
            print(f"Exception occured in visualize: {e}")



    def visualizeGraphByFile(self,filepath=None,setfilename="output",format="png",view=True):
        if filepath is None:
            print("please define file name")
        try:
            with open(f"{filepath}") as f :
                dot_code = f.read()
            graph = Source(dot_code)
            graph.render(f"{filepath}",format=f"{format}",view=view)
        except Exception as e:
            print(f"Exception occurred :{e}")