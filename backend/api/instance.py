from sonolus_fastapi import Sonolus
from sonolus_fastapi.backend import StorageBackend
from sonolus_fastapi.utils.session import MemorySessionStore

from api.sonolus.config import config_option
from api.sonolus.search.level import level_search
from pathlib import Path

project_root = Path(__file__).resolve().parent.parent
data_dir = project_root / "data"
data_dir.mkdir(parents=True, exist_ok=True)

db_file = data_dir / "sonolus.db"
db_url = f"sqlite:///{db_file.as_posix()}" # あとでPostgreSQLにします

sonolus = Sonolus(
    address="",
    port=8080,
    dev=True,
    session_store=MemorySessionStore(),
    backend=StorageBackend.DATABASE,
    backend_options={"url": db_url},
    enable_cors=True,
)

sonolus.search.level = level_search
sonolus.register_configuration_options(config_option)