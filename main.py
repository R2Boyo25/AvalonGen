import sys
from pythongen import pythonGenerator, libPythonGenerator
from packagegen import apmGenerator

generators = {
    'py': pythonGenerator,
    'libpy': libPythonGenerator,
    "apm": apmGenerator,
    "package": apmGenerator
}

print("AvalonGen v1.1")

if len(sys.argv) > 1:

    for generatorprefix in generators:
        if sys.argv[1].lower().startswith(generatorprefix):
            print("---------------------------")
            generators[generatorprefix](sys.argv[2:])
            print("---------------------------")
            quit()

    else:
        print(f'Language {sys.argv[1]} not found.')

else:

    print("Please supply a language:")
    print("\t" + "\n\t".join(generators))
    quit()