from ...instance import sonolus
from sonolus_models import ServerItemInfo, ServerItemList, ServerItemDetails, ParticleSection, SonolusText

# --------------------------------------------------------------- 

@sonolus.particle.info(ServerItemInfo)
async def get_particle_info(ctx) -> ServerItemInfo:
    items = sonolus.items.particle.list()[:3]
    searches = []
    return ServerItemInfo(
        creates=[],
        searches=searches,
        sections=[
            ParticleSection(
                title=SonolusText.NEWEST,
                items=items,
            )
        ],
        banner=None
    )
    
# --------------------------------------------------------------- 

@sonolus.particle.list(ServerItemList)
async def list_particles(ctx, query) -> ServerItemList:
    items = sonolus.items.particle.list()
    return ServerItemList(
        pageCount=1,
        items=items,
        searches=[]
    )

# --------------------------------------------------------------- 
    
@sonolus.particle.detail(ServerItemDetails)
async def get_particle_details(ctx, name: str) -> ServerItemDetails:
    item = sonolus.items.particle.get(name)
    return ServerItemDetails(
        item=item,
        description=item.subtitle,
        actions=[],
        leaderboards=[],
        sections=[],
        hasCommunity=False
    )