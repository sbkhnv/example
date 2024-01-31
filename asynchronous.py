import asyncio
from datetime import datetime

async def task1():
    await asyncio.sleep(1)
    print("Task 1 completed")
    print(datetime.now().time())

async def task2():
    await asyncio.sleep(2)
    print("Task 2 completed")
    print(datetime.now().time())


async def task3():
    await asyncio.sleep(3)
    print("Task 3 completed")
    print(datetime.now().time())

async def task4():
    await asyncio.sleep(4)
    print("Task 4 completed")
    print(datetime.now().time())

async def task5():
    await asyncio.sleep(5)
    print("Task 5 completed")
    print(datetime.now().time())

async def task6():
    await asyncio.sleep(56)
    print("Task 6 completed")
    print(datetime.now().time())

async def task7():
    await asyncio.sleep(7)
    print("Task 7 completed")
    print(datetime.now().time())

async def task8():
    await asyncio.sleep(8)
    print("Task 8 completed")
    print(datetime.now().time())

async def task9():
    await asyncio.sleep(9)
    print("Task 9 completed")
    print(datetime.now().time())

async def task10():
    await asyncio.sleep(10)
    print("Task 10 completed")
    print(datetime.now().time())

async def task11():
    await asyncio.sleep(11)
    print("Task 11 completed")
    print(datetime.now().time())

async def task12():
    await asyncio.sleep(12)
    print("Task 12 completed")
    print(datetime.now().time())

async def task13():
    await asyncio.sleep(13)
    print("Task 13 completed")
    print(datetime.now().time())

async def task14():
    await asyncio.sleep(14)
    print("Task 14 completed")
    print(datetime.now().time())

async def task15():
    await asyncio.sleep(15)
    print("Task 15 completed")
    print(datetime.now().time())

async def task16():
    await asyncio.sleep(16)
    print("Task 16 completed")
    print(datetime.now().time())

async def task17():
    await asyncio.sleep(17)
    print("Task 17 completed")
    print(datetime.now().time())

async def task18():
    await asyncio.sleep(18)
    print("Task 18 completed")
    print(datetime.now().time())

async def task19():
    await asyncio.sleep(19)
    print("Task 19 completed")
    print(datetime.now().time())

async def task20():
    await asyncio.sleep(20)
    print("Task 20 completed")
    print(datetime.now().time())

async def main():
    await asyncio.gather(task1(), task2(),task3(),task4(),task5(),task6(),task7(),task8(),task9(),task10(),task11(),task12(),task13(),task14(),task15(),task16(),task17(),task18(),task19(),task20())

if __name__ == "__main__":
    print(datetime.now().time())
    asyncio.run(main())
    print(datetime.now().time())
