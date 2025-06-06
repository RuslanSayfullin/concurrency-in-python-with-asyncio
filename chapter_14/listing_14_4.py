# Использование uvloop в качестве цикла событий
import asyncio
from asyncio import StreamReader, StreamWriter
import uvloop

async def connected(reader: StreamReader, writer: StreamWriter):
    line = await reader.readline()
    writer.write(line)
    await writer.drain()
    writer.close()
    await writer.wait_closed()

async def main():
    server = await asyncio.start_server(connected, port=9000)
    await server.serve_forever()

# Установить uvloop в качестве цикла событий
uvloop.install()
asyncio.run(main())