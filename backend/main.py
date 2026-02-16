from sonolus_fastapi.pack import freepackpath
from api.sonolus.handler import * # ハンドラのインポート
from api.instance import sonolus

sonolus.load(freepackpath)
app = sonolus.app
