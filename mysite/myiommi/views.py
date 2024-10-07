from iommi import Page, html


class TopPage(Page):
    heading = html.h1("Discography App")
    artists = html.div(html.a("Artist Data", attrs__href="artists"))
    albums = html.div(html.a("Album Data", attrs__href="artists"))
