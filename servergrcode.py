import uvicorn
from fastapi import FastAPI
from starlette.responses import RedirectResponse
import json
app = FastAPI()


@app.get("/redirect/{link_id}")
async def update_data(link_id: str):
    try:
        link_map = json.loads(
            open('link_check.json', 'r', encoding='utf-8').read())
        url = link_map.get(link_id, "https://example.com/not-found")
        return RedirectResponse(url=url)
    except Exception as e:
        return {"error": str(e)}

if __name__ == "__main__":
    uvicorn.run("servergrcode:app", host="0.0.0.0", port=8000, reload=False)
