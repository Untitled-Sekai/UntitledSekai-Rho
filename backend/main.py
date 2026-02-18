from sonolus_fastapi.pack import freepackpath
from sonolus_resource.pack import custompackpath
from sonolus_resource.files import resource_file_path
from api.sonolus.handler import * # ハンドラのインポート
from api.instance import sonolus

sonolus.load([
    freepackpath,
    custompackpath
])
sonolus.add(resource_file_path)
app = sonolus.app
