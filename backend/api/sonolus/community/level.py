from sonolus_models import ServerForm, ServerTextAreaOption, SonolusText, SonolusIcon

level_comment = ServerForm(
    type="comments",
    title=SonolusText.COMMENT,
    icon=SonolusIcon.Comment,
    requireConfirmation=False,
    options=[
        ServerTextAreaOption(
            query="comment",
            name=SonolusText.COMMENT,
            required=True,
            type="textArea",
            def_="",
            placeholder=SonolusText.COMMENT_PLACEHOLDER,
            limit=512,
            shortcuts=[]
        )
    ]
)