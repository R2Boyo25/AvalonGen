import os
import json
import shutil
import tempfile
import CLIParse  # type: ignore


def apmGenerator(flags: CLIParse.flags.Flags, *arguments: str) -> None:
    "Generate .apm file"

    if len(arguments) < 1:
        print("Specify directory to package! (not . or ./)")
        quit(1)

    dir = arguments[0]

    if not os.path.exists(dir):
        print("That directory does not exist.")
        quit(1)

    if not os.path.exists(f"{dir}/.avalon"):
        print(".avalon directory missing")
        quit(1)

    if not os.path.exists(f"{dir}/.avalon/package"):
        print(".avalon/package file is missing")
        quit(1)

    package = json.load(open(f"{dir}/.avalon/package", "r"))

    if "author" not in package:
        name = input(
            "No spaces or special characters - use GitHub account if it exists\nUsername/Organization: "
        )
        package["author"] = name

    else:
        name = package["author"]

    if "repo" not in package:
        repo = input(
            "No spaces or special characters - use GitHub repository name (minus the username) if it exists\nRepository Name: "
        )
        package["repo"] = repo

    else:
        repo = package["repo"]

    with tempfile.TemporaryDirectory() as tmpdir:

        os.system(f"cp -a {dir}/. {tmpdir}")

        with open(f"{tmpdir}/.avalon/package", "w") as packagefile:
            packagefile.write(json.dumps(package, indent=4))

        cwd = os.getcwd()
        os.chdir(tmpdir)

        os.system(f"tar -czf {cwd}/{name.lower()}.{repo.lower()}.apm $(find -printf \"%P\n\")")

        os.chdir(tmpdir)


def load(plugins: CLIParse.Parse) -> None:
    plugins.add(apmGenerator, "package")
