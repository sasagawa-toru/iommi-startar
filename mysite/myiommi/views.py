from iommi import Header, Page, html


class TopPage(Page):
    title = Header("Discography App")
    artists = html.div(html.a("Artist Data", attrs__href="artists"))
    albums = html.div(html.a("Album Data", attrs__href="artists"))
