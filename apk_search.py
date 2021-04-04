import argparse
import os
import subprocess
import platform
parser = argparse.ArgumentParser()
parser.add_argument('permission', help = "Android permission (will be updated to positional) like INTERNET")
parser.add_argument('folder_path', help = "Path to folder with apk")
args = parser.parse_args()
aapt_path = {'Linux':'./aapt/aapt_lin','Darwin':'./aapt/aapt_mac', 'Windows':'.\\aapt\\aapt_wind.exe'}

def check_path(path):
    return os.path.exists(path)


def get_apk_names(path):
    if check_path(path):
        return [path+item for item in os.listdir(path) if item.endswith('.apk')]
    else:
        print ('Wrong folder')

def check_permissions(apk_list, permission, aapt_loc):
    result = []
    for item in apk_list:
        proc = subprocess.run([aapt_loc, "d", "permissions", item], capture_output=True)
        perms = str(proc.stdout)
        if permission in perms:
            result.append(item)
    return result
def main():
    path = args.folder_path
    os_type = platform.system()
    aapt_loc = aapt_path[os_type]
    if os_type == "Windows":
        path = path if path.endswith('\\') else path+"\\"
    else:
        path = path if path.endswith('/') else path+"/"
    res = (check_permissions(get_apk_names(path),args.permission,aapt_loc))
    for item in res:
        print (item)
    # if not check_path(path):
    #     print("No such file or directory")
    #     exit()

main()
