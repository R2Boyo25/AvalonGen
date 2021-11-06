import os, json, shutil

def pythonGenerator(arguments):
    print("Paths that are asked for are relative to the repository root.")

    binname = input("Command to use to invoke command (ex: avalongen for avalongen) (case sensitive):\n")

    filepath = input( "Path to file to run when command is run:\n" )

    filestocopy = input("Files/folders needed to run program (separated by spaces) (all for all files & folders in repo):\n").replace(',', '').split()

    deptypes = input("Dependency types (ex: apt, avalon, pip (please use requirements.txt if possible for pip)) (separated by spaces) (blank for none):\n").replace(",", "").split()

    dependencies = {}

    for deptype in deptypes:
        dependencies[deptype] = input(f"Dependencies for {deptype} (separated by spaces):\n").replace(",", "").split()
    
    fpack = {
        "binname": binname,
        "installScript": '.avalon/gen.py',
        "deps": dependencies,
        "toCopy": filestocopy
    } if dependencies != {} else {
        "binname": binname,
        "installScript": '.avalon/gen.py',
        "toCopy": filestocopy
    }

    if os.path.exists('.avalon'):
        shutil.rmtree('.avalon')

    if not '--noavalon' in arguments:

        os.mkdir('.avalon')

        with open('.avalon/package', 'w') as packagefile:
            packagefile.write(json.dumps(fpack, indent = 4))

        with open(f"/{'/'.join(os.path.abspath(__file__).split('/')[:-1])}/templates/gen.py", 'r') as gentemplate:
            with open(".avalon/gen.py", 'w') as gen:
                gen.write(gentemplate.read().replace('|runfile|', filepath))

    else:

        with open('package', 'w') as packagefile:
            packagefile.write(json.dumps(fpack, indent = 4))

        with open(f"/{'/'.join(os.path.abspath(__file__).split('/')[:-1])}/templates/gen.py", 'r') as gentemplate:
            with open("gen.py", 'w') as gen:
                gen.write(gentemplate.read().replace('|runfile|', filepath))
