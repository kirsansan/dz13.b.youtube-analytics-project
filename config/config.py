import os
from dotenv import load_dotenv


load_dotenv()

YOUTUBE_ID = os.getenv('YOUTUBE_ID')

FILE_FOR_WRITE = "./result.json"

