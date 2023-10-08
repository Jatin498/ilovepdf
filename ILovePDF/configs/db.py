# This module is part of https://github.com/nabilanavab/ilovepdf
# Feel free to use and contribute to this project. Your contributions are welcome!
# copyright ©️ 2021 nabilanavab

file_name = "ILovePDF/configs/db.py"

import os

DATA = {-1001956094156}  # save user api, fname, capt

myID = [-1001956094156]  # saves bot info if UPDATE_CHANNEL

GROUPS = [-1001956094156]  # save groups id and checks each times

ping_list = [-1001956094156] # save users how need notify after bot reastart from stop

invite_link = [-1001956094156]  # just saves invitation link

BANNED_USR_DB, BANNED_GRP_DB = [], []  # Load Banned Users Id

CUSTOM_THUMBNAIL_U, CUSTOM_THUMBNAIL_C = [], []  # Load UsersId with custom thumbnail


class dataBASE(object):

    MONGODB_URI = os.environ.get("MONGODB_URI", False)  # mongoDB Url (Optional)


# If you have any questions or suggestions, please feel free to reach out.
# Together, we can make this project even better, Happy coding!  XD
