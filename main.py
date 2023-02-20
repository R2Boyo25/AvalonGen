from CLIParse import Parse

p = Parse("apm gen", "Avalon Generator V1.2 Copyright (C) R2Boyo25 2022")
p.flag("noavalon", short="n", long="noavalon", help="Use CWD instead of a .avalon directory", type=bool, default=False)

p.loadDir("generators")

p.run()
