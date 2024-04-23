async def is_served_user(client, user_id: int) -> bool:
    userdb = await get_data(client)
    userdb = userdb.users
    user = await userdb.find_one({"user_id": user_id})
    if not user:
        return False
    return True
    
async def add_served_user(client, user_id: int):
    userdb = await get_data(client)
    userdb = userdb.users
    is_served = await is_served_user(client, user_id)
    if is_served:
        return
    return await userdb.insert_one({"user_id": user_id})
    
async def get_dev(bot_username):
  devv = dev.get(bot_username)
  if not devv:
   Bots = botss.find({})
   for i in Bots:
       bot = i["bot_username"]
       if bot == bot_username:
         devo = i["dev"]
         dev[bot_username] = devo
         return devo
  return devv


async def get_dev(bot_username):
  devv = dev.get(bot_username)
  if not devv:
   Bots = botss.find({})
   for i in Bots:
       bot = i["bot_username"]
       if bot == bot_username:
         devo = i["dev"]
         dev[bot_username] = devo
         return devo
  return devv


