# example of synchronous programming

from time import perf_counter
import time

start = perf_counter()

def get_movie_ticket():
    time.sleep(4)
    print("Got movie tickets")
    
def like_instagram():
    time.sleep(2)
    print("Liked all instagram pictures")
    
# if __name__=="__main__":
#     get_movie_ticket()
#     like_instagram()

end = perf_counter()
print(end - start)


# ***************************************************************************************************


# example using asyncio works like synchronous only

import asyncio

async def get_movie_tickets2():
    await asyncio.sleep(4)   # sleep ke saath await lagana hai
    print("Got movie tickets")

async def like_instagram2():
    await asyncio.sleep(2)
    print("Liked all instagram pictures")

async def mainn():
    await get_movie_tickets2()
    await like_instagram2()
    
start = perf_counter()
# asyncio.run(mainn())
end = perf_counter()
print(end - start)

# ***************************************************************************************************


import asyncio

async def get_movie_tickets3():
    await asyncio.sleep(4)   # sleep ke saath await lagana hai
    print("Got movie tickets")

async def like_instagram3():
    await asyncio.sleep(2)
    print("Liked all instagram pictures")

async def mainn2():
    await asyncio.gather(get_movie_tickets3(), like_instagram3())
    
    
start = perf_counter()
asyncio.run(mainn2())
end = perf_counter()
print(end - start)
