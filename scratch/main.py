import asyncio
import websockets
import git

async def sync_changes(websocket, path):
    while True:
        try:
            data = await websocket.recv()
            # Process the received changes
            # Update local files
            # Commit and push to GitHub
            repo = git.Repo('../.git/')
            repo.git.add(update=True)
            repo.index.commit('Auto-commit: ' + data[:50])
            origin = repo.remote(name='origin')
            origin.push()
        except websockets.exceptions.ConnectionClosed:
            break

start_server = websockets.serve(sync_changes, "localhost", 8765)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
