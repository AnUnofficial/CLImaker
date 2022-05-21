from os import  listdir
from shutil import copy
CLI_NAME = input("Name: ")                                                   # Get name of CLI
CLI_COMMANDS = input("Directory to your .py files: ")                        # Get the directory to the .py scripts
CLI_FILES = []                                                               # Parse files
for PY_FILE in listdir(CLI_COMMANDS):                                        # From one character executer + removing .py
 match PY_FILE.endswith(".py"):
  case True:
   CLI_FILES.append(PY_FILE.replace(".py",""))
CLI = open("./" + CLI_NAME + "_CLI.py", "x")                                 # Create the CLI script
copy("./template.py", CLI)                                                   # Copy the template to the CLI script
CLI_WRITELINES = CLI.readlines()                                             # Add custom lines
CLI_WRITELINES[0] = "CLI_FILES = " + str(CLI_FILES) + "\n"
CLI_WRITELINES[1] = "CLI_DIRECTORY = '" + CLI_COMMANDS + "'\n"
CLI_WRITELINES[8] = "exec(open(CLI_DIRECTORY + command + '.py','r').read())"
CLI.writelines(CLI_WRITELINES)
CLI.close()
print("Wrote to " + CLI_NAME + "_CLI.py!")