# This module is part of https://github.com/nabilanavab/ilovepdf
# Feel free to use and contribute to this project. Your contributions are welcome!
# copyright ©️ 2021 nabilanavab

file_name = "@AdultManhwa_nation/configs/config.py"

import os

class bot(object):

    # get API_ID, API_HASH values from my.telegram.org (Mandatory)
    API_ID = os.environ.get("23902408")
    API_HASH = os.environ.get("6a36a4ef2f07d63aeba7b53b99c64d73")

    # add API_TOKEN from @botfather (Mandatory)
    API_TOKEN = os.environ.get("6666983442:AAHWN4SKS3QqrzWUYnfXRt8PKhP-rd8vjHA")


class dm(object):

    # add admins Id list by space seperated (Optional)
    ADMINS = list(set(int(x) for x in os.environ.get("5086525318", "").split()))
    ADMINS.append(5086525318)

    ADMIN_ONLY = os.environ.get("ADMIN_ONLY", False)

    # banned Users cant use this bot (Optional)
    BANNED_USERS = list(set(int(x) for x in os.environ.get("BANNED_USERS", "").split()))


class group(object):

    # add admins Id list by space seperated (Optional)
    ADMIN_GROUPS = list(set(int(x) for x in os.environ.get("5086525318", "").split()))

    # if admin group only (True)
    ADMIN_GROUP_ONLY = os.environ.get("ADMIN_GROUP_ONLY", False)

    # banned groups can't use this bot (Optional)
    BANNED_GROUP = list(set(int(x) for x in os.environ.get("BANNED_USERS", "").split()))

    ONLY_GROUP_ADMIN = os.environ.get("ONLY_GROUP_ADMIN", False)


class images(object):

    # DEFAULT THUMBNAIL ❌ NB: Thumbnails can’t be reused and can be only uploaded as a new file ❌
    PDF_THUMBNAIL = None  #  "./images/thumbnail.jpeg"   PDF_THUMBNAIL & THUMBNAIL_URL must point same img
    THUMBNAIL_URL = "https://te.legra.ph/file/8dfa3760df91a218a629c.jpg"  # to inc. meadia edit speed

    # WELCOME IMAGE
    WELCOME_PIC = "https://te.legra.ph/file/8dfa3760df91a218a629c.jpg"

    # BANNED IMAGE
    BANNED_PIC = "https://te.legra.ph/file/8dfa3760df91a218a629c.jpg"

    # BIG FILE
    BIG_FILE = "https://te.legra.ph/file/8dfa3760df91a218a629c.jpg"


class settings(object):

    SEND_RESTART = True

    # set True if you want to prevent users from forwarding files from bot
    PROTECT_CONTENT = (
        True if os.environ.get("PROTECT_CONTENT", "False") == "True" else False
    )

    # channel id for forced Subscription with -100 (Optional)
    UPDATE_CHANNEL = os.environ.get("-1001853231882", True)

    # get convertAPI secret (Optional)
    CONVERT_API = os.environ.get("CONVERT_API", False)

    # set maximum file size for preventing overload (Optional)
    MAX_FILE_SIZE = os.environ.get("MAX_FILE_SIZE", False)

    # default name, caption, lang [if needed]
    DEFAULT_NAME = os.environ.get("DEFAULT_NAME", False)

    DEFAULT_CAPT = os.environ.get("DEFAULT_CAPTION", False)

    DEFAULT_LANG = os.environ.get("DEFAULT_LANG", "eng")  # use small letters

    MULTI_LANG_SUP = (
        True if os.environ.get("MULTI_LANG_SUP", "False") == "True" else False
    )

    REPORT = "https://t.me/ilovepdf_bot/33?comment=1000000000"

    FEEDBACK = "https://telegram.dog/ilovepdf_bot"

    SOURCE_CODE = "https://t.me/ANIME_domain1"

    OWNER_ID, OWNER_USERNAME = 5086525318, "RarelySukuna"

    OWNED_CHANNEL = "https://t.me/ANIME_domain1"

    REFER_BETA = False if os.environ.get("REFER_BETA", "False") == "False" else True

    STOP_BOT = os.environ.get("STOP_BOT", False)


# If you have any questions or suggestions, please feel free to reach out.
# Together, we can make this project even better, Happy coding!  XD
