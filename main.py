from CLIParse import Parse

p = Parse("apm gen", "Avalon Generator V0.1.3 Copyright (C) R2Boyo25 2023")

p.flag("noavalon", long = "noavalon", help = "Don't use a .avalon folder, for making main repo things")

p.loadDir("generators")

p.run()
