import os, json, shutil

def pythonGenerator(flags, *arguments):
    "Generate Python program package"

    print("Paths that are asked for are relative to the repository root.")

    binname = input("Command to use to invoke command (ex: avalongen for avalongen) (case sensitive):\n")

    filepath = input( "Path to file to run when command is run:\n" )

    filestocopy = input("Files/folders needed to run program (separated by spaces) (all for all files & folders in repo):\n").replace(',', '').split()

    deptypes = input("Dependency types (ex: apt, avalon, pip (please use requirements.txt if possible for pip)) (separated by spaces) (blank for none):\n").replace(",", "").split()

    name = input("Your name / Organization's name (NO SPACES OR SPECIAL CHARACTERS)(if there is a github repo use the owner of that repo's username): ")

    repo = input("Program Name (NO SPACES OR SPECIAL CHARACTERS)(If there is a github repo use it's name): ")

    dependencies = {}

    for deptype in deptypes:
        dependencies[deptype] = input(f"Dependencies for {deptype} (separated by spaces):\n").replace(",", "").split()
    
    fpack = {
        "author": name,
        "repo": repo,
        "binname": binname,
        "installScript": '.avalon/gen.py',
        "mvBinAfterInstallScript": True,
        "deps": dependencies,
        "toCopy": filestocopy
    } if dependencies != {} else {
        "author": name,
        "repo": repo,
        "binname": binname,
        "installScript": '.avalon/gen.py',
        "mvBinAfterInstallScript": True,
        "toCopy": filestocopy
    }

    if os.path.exists('.avalon'):
        shutil.rmtree('.avalon')

    if not flags.noavalon:

        prefix = '.avalon/'

        os.mkdir(prefix)
    
    else:

        prefix = ''

    with open(f'{prefix}package', 'w') as packagefile:
        packagefile.write(json.dumps(fpack, indent = 4))

    with open(f"/{'/'.join(os.path.abspath(__file__).split('/')[:-1])}/../templates/gen.py", 'r') as gentemplate:
        with open(f"{prefix}gen.py", 'w') as gen:
            gen.write(gentemplate.read().replace('|runfile|', filepath))

def libPythonGenerator(flags, *arguments):
    "Generate Python library package"

    name = input("Your name / Organization's name (NO SPACES OR SPECIAL CHARACTERS)(if there is a github repo use the owner of that repo's username): ")

    repo = input("Program Name (NO SPACES OR SPECIAL CHARACTERS)(If there is a github repo use it's name): ")

    pkgName = input('Package name (defined in setup.py):\n')

    deptypes = input("Dependency types (ex: apt, avalon, pip (please use requirements.txt if possible for pip)) (separated by spaces) (blank for none):\n").replace(",", "").split()

    dependencies = {}

    for deptype in deptypes:
        dependencies[deptype] = input(f"Dependencies for {deptype} (separated by spaces):\n").replace(",", "").split()
    
    fpack = {
        "author": name,
        "repo": repo,
        "installScript": '.avalon/install.sh',
        "uninstallScript": '.avalon/uninstall.sh',
        "deps": dependencies
    } if dependencies != {} else {
        "author": name,
        "repo": repo,
        "installScript": '.avalon/install.sh',
        "uninstallScript": '.avalon/uninstall.sh'
    }

    if os.path.exists('.avalon'):
        shutil.rmtree('.avalon')

    if not flags.noavalon:

        prefix = '.avalon/'

        os.mkdir(prefix)
    
    else:

        prefix = ''

    with open(f'{prefix}package', 'w') as packagefile:
        packagefile.write(json.dumps(fpack, indent = 4))

    with open(f"/{'/'.join(os.path.abspath(__file__).split('/')[:-1])}/../templates/libin.sh", 'r') as installtemplate:
        with open(f'{prefix}install.sh', 'w') as install:
            install.write(installtemplate.read())
    
    with open(f"/{'/'.join(os.path.abspath(__file__).split('/')[:-1])}/../templates/libun.sh", 'r') as uninstalltemplate:
        with open(f'{prefix}uninstall.sh', 'w') as uninstall:
            uninstall.write(uninstalltemplate.read().replace('|pkgname|', pkgName))

def pythonLibraryTemplateGenerator(flags, *arguments):
    "Generate Python library package"

    name = input("Your name / Organization's name (NO SPACES OR SPECIAL CHARACTERS)(if there is a github repo use the owner of that repo's username): ")

    repo = input("Program Name (NO SPACES OR SPECIAL CHARACTERS)(If there is a github repo use it's name): ")

    pkgName = input('Import name:\n')
    description = input('Library Description:\n')

    deptypes = input("Dependency types (ex: apt, avalon, pip (please use requirements.txt if possible for pip)) (separated by spaces) (blank for none):\n").replace(",", "").split()

    dependencies = {}

    for deptype in deptypes:
        dependencies[deptype] = input(f"Dependencies for {deptype} (separated by spaces):\n").replace(",", "").split()
    
    fpack = {
        "author": name,
        "repo": repo,
        "installScript": '.avalon/install.sh',
        "uninstallScript": '.avalon/uninstall.sh',
        "deps": dependencies
    } if dependencies != {} else {
        "author": name,
        "repo": repo,
        "installScript": '.avalon/install.sh',
        "uninstallScript": '.avalon/uninstall.sh'
    }

    os.mkdir(pkgName)
    os.chdir(pkgName)

    if os.path.exists('.avalon'):
        shutil.rmtree('.avalon')

    if not flags.noavalon:

        prefix = '.avalon/'

        os.mkdir(prefix)
    
    else:

        prefix = ''

    with open(f'{prefix}package', 'w') as packagefile:
        packagefile.write(json.dumps(fpack, indent = 4))

    with open(f"/{'/'.join(os.path.abspath(__file__).split('/')[:-1])}/../templates/libin.sh", 'r') as installtemplate:
        with open(f'{prefix}install.sh', 'w') as install:
            install.write(installtemplate.read())
    
    with open(f"/{'/'.join(os.path.abspath(__file__).split('/')[:-1])}/../templates/libun.sh", 'r') as uninstalltemplate:
        with open(f'{prefix}uninstall.sh', 'w') as uninstall:
            uninstall.write(uninstalltemplate.read().replace('|pkgname|', pkgName))

    os.mkdir(pkgName)
    os.system(f"touch \"{pkgName}\"/__init__.py")
    os.system(f"touch requirements.txt")

    with open("setup.py", "w") as setuppy:
        setuppy.write(f"""from setuptools import find_packages, setup\n\nsetup(
    name='{pkgName}',
    packages=find_packages(include=['{pkgName}']),
    version='1.0',
    description='{description}',
    author='{name}'
)""")
    
    with open(".gitignore", "w") as gitignore:
        gitignore.write("*.egg-info\nbuild\ndist\n__pycache__")


def load(plugins):
    plugins.add(pythonGenerator, 'py')
    plugins.add(libPythonGenerator, 'libpy')
    plugins.add(pythonLibraryTemplateGenerator, "libpytemplate")