from sonolus_fastapi import Sonolus
from sonolus_fastapi.backend import StorageBackend
from sonolus_fastapi.utils.session import MemorySessionStore

from api.sonolus.config import config_option
from api.sonolus.search.level import level_search

sonolus = Sonolus(
    address="",
    port=8080,
    dev=True,
    session_store=MemorySessionStore(),
    backend=StorageBackend.DATABASE,
    backend_options={"url": ""},
    enable_cors=True,
)

sonolus.search.level = level_search
sonolus.register_configuration_options(config_option)