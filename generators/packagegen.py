import os
import json
import shutil

def apmGenerator(flags, *arguments):
    "Generate .apm file"

    if len(arguments) == 1:
        dir = arguments[0]
    else:
        print("Specify directory to package! (not . or ./)")
        quit()

    if dir.rstrip("/") == ".":
        print("Cannot be run from inside of the repository")
        quit()

    if not os.path.exists(f"{dir}/.avalon"):
        print(".avalon directory missing")
        quit()

    if not os.path.exists(f"{dir}/.avalon/package"):
        print(".avalon/package file is missing")
        quit()

    package = json.load(open(f"{dir}/.avalon/package", 'r'))

    if "author" not in package:
        name = input("Your name / Organization's name (NO SPACES OR SPECIAL CHARACTERS)(if there is a github repo use the owner of that repo's username): ")
        package["author"] = name
    else:
        name = package["author"]

    if "repo" not in package:
        repo = input("Program Name (NO SPACES OR SPECIAL CHARACTERS)(If there is a github repo use it's name): ")
        package["repo"] = repo
    else:
        repo = package["repo"]

    if os.path.exists("agentmp"):
        shutil.rmtree("agentmp")

    os.mkdir("agentmp")

    tmpdir = "agentmp"

    os.system(f"cp -a {dir}/. {tmpdir}")

    

    with open(f'{tmpdir}/.avalon/package', 'w') as packagefile:
        packagefile.write(json.dumps(package, indent = 4))

    if os.path.exists(f"{tmpdir}/{tmpdir}"):
        os.rmdir(f"{tmpdir}/{tmpdir}")

    os.system(f"tar -czf {name.lower()}.{repo.lower()}.apm -C {tmpdir} .")

    shutil.rmtree("agentmp")
    
def load(plugins):
    plugins.add(apmGenerator, 'package')