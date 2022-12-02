from pyodide.http import XMLHttpRequest,pyfetch
from pyodide.ffi import JsException
import pandas as pd
import json

async def guild_tibia(name):
    try:
        response = await pyfetch(
            url=f"https://api.tibiadata.com/v3/guild/{name}",
            method="GET",
            header={"Content-Type": "application/json"},
        )
        if response.ok:
            data = await response.json()
            return data
        
    except JsException as e:
        return e

async def get_guild(name):
    guild = await guild_tibia(name)
    if guild is None:
        return None
    else:
        return guild

async def json_to_dataframe(json):
    #alterar
    df=await pd.read_json(json)
    return df