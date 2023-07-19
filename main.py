from CLIParse import Parse  # type: ignore


p = Parse("apm gen", "Avalon Generator V0.1.3 Copyright (C) R2Boyo25 2023")

p.flag(
    "noavalon",
    short="n",
    long="noavalon",
    help="Use CWD instead of a .avalon directory",
    type=bool,
    default=False,
)

p.loadDir("generators")

p.run()
