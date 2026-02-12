from fastapi import FastAPI, WebSocket
from typing import List

app = FastAPI(title="Jarvis Backend Core")

@app.get("/")
async def root():
    return {"status": "Jarvis Online", "version": "1.0.0"}

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    while True:
        data = await websocket.receive_text()
        await websocket.send_text(f"Message received: {data}")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
