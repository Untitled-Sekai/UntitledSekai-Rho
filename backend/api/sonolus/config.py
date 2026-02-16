from sonolus_models import ServerToggleOption

config_option = [
    ServerToggleOption(
        query="include_my_levels",
        name="自分の譜面のみのセクションを表示",
        required=False,
        type="toggle",
        def_=False
    ),
]