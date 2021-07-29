

class Config:
    API_ID = int(os.environ.get("API_ID", ''))
    ARQ_API=os.environ.get("ARQ_API", "")
    API_HASH = os.environ.get("API_HASH", "")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "") 
    DOWNLOAD_LOCATION = os.environ.get("DOWNLOAD_LOCATION", "./DOWNLOADS/")
    msg = {}
