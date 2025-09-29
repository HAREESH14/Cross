from joern_lib import client,graph

import asyncio
import os ;
from clean import Cleaner
from joernhelper import JoernHelper


async def main():
    filename=input("ENTER THE FILENAME:- ")
    pathcode = os.getcwd()+f"/{filename}"
    connections = await client.get("http://localhost:8080")
    # await importcode(connections,pathcode)
    # await create_graph(connections,method_name="main")
    joern = JoernHelper(connections)
    await joern.import_source(pathcode)
    data=await joern.create_graph(method_name="main")
    # print(data)
    joern.visualizeGraph(data=data)
    


if __name__ == "__main__":
    # Your code here
    asyncio.run(main())
