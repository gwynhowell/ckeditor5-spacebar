import webapp2
from webapp2_extras import jinja2


class BasePage(webapp2.RequestHandler):
    @webapp2.cached_property
    def jinja2(self):
        return jinja2.Jinja2(APP)

    def render(self, path, **kwargs):
        self.response.write(self.jinja2.render_template(path, **kwargs))

class MainPage(BasePage):
    def get(self):
        self.redirect('/local')

class LocalPage(BasePage):
    def get(self):
        self.render('main.html', local=True)

class RemotePage(BasePage):
    def get(self):
        self.render('main.html', local=False)

routes = [
    webapp2.Route('/', MainPage),
    webapp2.Route('/local', LocalPage),
    webapp2.Route('/remote', RemotePage)
]

webapp2_config = {'webapp2_extras.jinja2': {'template_path': ['templates']}}

APP = webapp2.WSGIApplication(config=webapp2_config, routes=routes)
