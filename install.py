import os
import pip
import platform
import subprocess


def install():

    origin_folder = os.getcwd()
    origin_file = origin_folder + "/phoenix.py"

    if (platform.system() == "Linux"):
        destination_folder = subprocess.run(["which", "git"], stdout=subprocess.PIPE)
        destination_folder = destination_folder.stdout.decode('utf-8').replace("\n", "")
        destination_folder = destination_folder.replace("git", "")

        destination_file = destination_folder + "git-phoenix"

        subprocess.run(["sudo", "ln", "-s", origin_file, destination_file])
        subprocess.run(["chmod", "+x", destination_file])

        destination_file = destination_folder + "git-px"

        subprocess.run(["sudo", "ln", "-s", origin_file, destination_folder + "git-px"])
        subprocess.run(["chmod", "+x", destination_file])
    elif (platform.system() == "Windows"):
        destination_folder = subprocess.run(["where", "git"], stdout=subprocess.PIPE)
        destination_folder = destination_folder.stdout.decode('utf-8').replace("\n", "")
        destination_folder = destination_folder.replace("cmd\\git.exe", "")
        destination_folder = destination_folder + "usr\\bin\\"

        origin_file = origin_file.replace("/", "\\")
        origin_commons = origin_folder + "\\commons"
        origin_core = origin_folder + "\\core"
        origin_parser_local = origin_folder + "\\parser_local"

        destination_file = destination_folder + "git-phoenix"

        subprocess.run(["cmd", "/c", "mklink", destination_file, origin_file])

        destination_file = destination_folder + "git-px"

        subprocess.run(["cmd", "/c", "mklink", destination_file, origin_file])

        destination_file = destination_folder + "commons"

        subprocess.run(["cmd", "/c", "mklink", "/J", destination_file, origin_commons])

        destination_file = destination_folder + "core"

        subprocess.run(["cmd", "/c", "mklink", "/J", destination_file, origin_core])

        destination_file = destination_folder + "parser_local"

        subprocess.run(["cmd", "/c", "mklink", "/J", destination_file, origin_parser_local])

    try:
        import colorlog
    except ImportError as e:
        subprocess.run(["pip", "install", "colorlog"])


if (__name__ == "__main__"):
    install()
