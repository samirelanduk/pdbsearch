def add_ga_javascript(app, pagename, templatename, context, doctree):
    metatags = context.get("metatags", "")
    metatags += """<script async src="https://www.googletagmanager.com/gtag/js?id=G-LW2DFLW14H"></script>
    <script>
    window.dataLayer = window.dataLayer || [];
    function gtag(){dataLayer.push(arguments);}
    gtag("js", new Date());
    gtag("config", "G-LW2DFLW14H");
    </script>"""
    context["metatags"] = metatags


def setup(app):
    app.connect("html-page-context", add_ga_javascript)