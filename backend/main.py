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

if __name__ == "__main__":
    # サーバー起動、基本的にはgunicornなどで起動することが多いと思いますが、開発中はこの方法で起動できます。
    sonolus.run()