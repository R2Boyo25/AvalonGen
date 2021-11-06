import sys
from pythongen import pythonGenerator

generators = {
    'py': pythonGenerator
}

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

    print("Please supply a language (python, etc.).")
    quit()