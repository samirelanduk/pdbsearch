def add_plausible_javascript(app, pagename, templatename, context, doctree):
    metatags = context.get("metatags", "")
    metatags += """<!-- Privacy-friendly analytics by Plausible -->
<script async src="https://plausible.io/js/pa-cwZVKAlQ7fvQ70MYi82ab.js"></script>
<script>
  window.plausible=window.plausible||function(){(plausible.q=plausible.q||[]).push(arguments)},plausible.init=plausible.init||function(i){plausible.o=i||{}};
  plausible.init()
</script>"""
    context["metatags"] = metatags


def setup(app):
    app.connect("html-page-context", add_plausible_javascript)