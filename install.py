import os
import platform
import subprocess


def install():
    origin_folder = os.getcwd()
    origin_file = origin_folder + "/phoenix.py"
    system = platform.system()

    if ("Linux" == system):
        import stat

        folder = subprocess.run(["which", "git"], stdout=subprocess.PIPE)
        folder = folder.stdout.decode('utf-8').replace("\n", "")
        folder = folder.replace("git", "")

        symbolic_link_array = ["sudo", "ln", "-s", origin_file, ""]

        scripts = [folder + "git-phoenix", folder + "git-px"]

        for script in scripts:
            symbolic_link_array[-1] = script

            subprocess.run(symbolic_link_array)
            st = os.stat(script)
            os.chmod(script, st.st_mode | stat.S_IEXEC)
    elif ("Windows" == system):
        folder = subprocess.run(["where", "git"], stdout=subprocess.PIPE)
        folder = folder.stdout.decode('utf-8').replace("\n", "")
        folder = folder.replace("cmd\\git.exe", "")
        folder = folder + "usr\\bin\\"

        origin_file = origin_file.replace("/", "\\")
        origin_commons = origin_folder + "\\commons"
        origin_core = origin_folder + "\\core"
        origin_exception = origin_folder + "\\exception"
        origin_parser_local = origin_folder + "\\parser_local"

        scripts = [folder + "git-phoenix", folder + "git-px"]
        folders = [folder + "commons", folder + "core", folder + "exception", folder + "parser_local"]
        dest_folders = [origin_commons, origin_core, origin_exception, origin_parser_local]
        symbolic_link_script_array = ["cmd", "/c", "mklink", "", origin_file]
        symbolic_link_folder_array = ["cmd", "/c", "mklink", "/J", "", ""]

        for script in scripts:
            symbolic_link_script_array[-2] = script
            subprocess.run(symbolic_link_script_array)

        for i in range(0, len(folders)):
            symbolic_link_folder_array[-2] = folders[i]
            symbolic_link_folder_array[-1] = dest_folders[i]
            subprocess.run(symbolic_link_folder_array)

    subprocess.run(["pip", "install", "colorlog"])
    subprocess.run(["pip", "install", "regex"])


if (__name__ == "__main__"):
    install()
