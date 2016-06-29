import web

urls = ('/', 'index', '/about', 'about')

app = web.application(urls, globals())

render = web.template.render('templates/')

class index:
    def GET(self):
        greetings = "Hello World"
        return render.index(greeting = greetings)
        
class about:
    def GET(self):
        name = "Lilith"
        return render.about(greeting = name)

if __name__ == "__main__":
    app.run()
