from lcu_driver import Connector

connector = Connector()

@connector.ready
async def connect(connection):
    summoner = await connection.request('get', '/lol-chat/v1/friends')
    list = await summoner.json()

    print("========================")
    print("   Your Friends List:   ")
    print("========================")
    for key in list:
        print(key['name'], "is", key['availability'])
    print("========================")
            
connector.start()
