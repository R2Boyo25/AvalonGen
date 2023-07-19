import sys, os

filesFolder = sys.argv[2]
binf = "avalongen"

if not os.path.exists("bin"):
    os.mkdir("bin")

with open(f"bin/{binf}", "w") as f:
    f.write(
        f"""#!/bin/bash

PYTHONPATH="$PYTHONPATH:{filesFolder}:{filesFolder}/../avalonpackagemanager/" python3 -m avalongen "$@"
"""
    )
    os.system(f"chmod +x bin/{binf}")
