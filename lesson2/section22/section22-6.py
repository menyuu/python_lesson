import asyncio

loop = asyncio.get_event_loop()

async def worker1(condition):
    print('worker1 start')
    # async with lock:
    #     print('worker1 got lock')
    #     await asyncio.sleep(3)
    # await event.wait()
    # print('worker1 got event')
    # await asyncio.sleep(3)
    async with condition:
        print('worker1 got condition')
        await asyncio.sleep(3)
        print('worker1 end')

async def worker2(condition):
    print('worker2 start')
    # async with lock:
    #     print('worker2 got lock')
    #     await asyncio.sleep(3)
    # await event.wait()
    # print('worker2 got event')
    # await asyncio.sleep(3)
    async with condition:
        print('worker2 got condition')
        await asyncio.sleep(3)
        print('worker2 end')

async def worker3(condition):
    async with condition:
        print('worker3 start')
        await asyncio.sleep(3)
        print('worker3 end')
        condition.notify_all()

# lock = asyncio.Lock()
event = asyncio.Event()
condition = asyncio.Condition()
loop.run_until_complete(asyncio.wait([
    worker1(condition), worker2(condition), worker3(condition)
]))
loop.close()