import asyncio
import time

async def add(a,b):
    await asyncio.sleep(1)
    return a+b

async def main():
    start = time.perf_counter()
    # print('Hello ...')
    # await asyncio.sleep(1)
    # print('... World!')
    # c =  await add(2,3)
    # print(c)
    
    l = [add(2,3),add(2,3),add(2,3),add(2,3),add(2,3),add(2,3)]    
    
    r = await asyncio.gather(*l)
    print(r)
    end = time.perf_counter()
    print(f"{end-start:.3}")
if __name__=='__main__':
    asyncio.run(main())
