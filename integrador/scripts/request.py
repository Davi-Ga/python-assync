from pyodide.http import XMLHttpRequest,pyfetch
from pyodide.ffi import JsException
import pandas as pd

async def highscore(page):
    try:
        response = await pyfetch(
            url=f"https://api.tibiadata.com/v3/highscores/Antica/swordfighting/paladins/{page}",
            method="GET",
            header={"Content-Type": "application/json"},
        )
        if response.ok:
            data=await response.json()
            at=data['highscores']['highscore_list']
           
            return at
        
    except JsException as e:
        return e

async def get_highscore(page):
    high=await highscore(page)
    if high is None:
        return None
    else:
        return high

def dict_to_dataframe(highscore):
    df=pd.DataFrame.from_dict(highscore)
    return df

