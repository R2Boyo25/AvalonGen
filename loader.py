import plugins

class Loader:
    def __init__(self, parser):
        self.parser = parser
        self.handlers = plugins.getHandlers(plugins.loadPlugins())

        for loader in self.handlers["load"]:
            loader(self)
    
    def add(self, function, name, help = ""):
        self.parser.command(name, help)(function)
