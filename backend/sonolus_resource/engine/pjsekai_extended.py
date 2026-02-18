from sonolus_models import EngineItem, Tag, SonolusText, SonolusIcon, SonolusResourceLocator
from sonolus_fastapi import Sonolus

SRL = SonolusResourceLocator

def create_pjsekai_extended(sonolus: Sonolus) -> EngineItem:
    """
    エンジンアイテムを作成する関数
    """
    return EngineItem(
        name="pjsekai_extended",
        title="プロセカ",
        author="Burrito",
        description="",
        tags=[
            Tag(
                title=SonolusText.ENGINE,
                icon=SonolusIcon.Engine
            )
        ],
        subtitle="プロジェクトセカイ カラフルステージ！ feat. 初音ミク",
        skin=sonolus.items.skin.get("CC_skin"),
        background=sonolus.items.background.get("black"),
        effect=sonolus.items.effect.get("chcy-pjsekai-fixed"),
        particle=sonolus.items.particle.get("CC_particle"),
        thumbnail=SRL(
            hash="Extendedthumbnail.png",
            url="/sonolus/repository/Extendedthumbnail.png"
        ),
        playData=SRL(
            hash="ExtendedEnginePlayData",
            url="/sonolus/repository/ExtendedEnginePlayData"
        ),
        watchData=SRL(
            hash="ExtendedEngineWatchData",
            url="/sonolus/repository/ExtendedEngineWatchData"
        ),
        previewData=SRL(
            hash="ExtendedEnginePreviewData",
            url="/sonolus/repository/ExtendedEnginePreviewData"
        ),
        tutorialData=SRL(
            hash="ExtendedEngineTutorialData",
            url="/sonolus/repository/ExtendedEngineTutorialData"
        ),
        rom=None,
        configuration=SRL(
            hash="ExtendedEngineConfiguration",
            url="/sonolus/repository/ExtendedEngineConfiguration"
        )
    )