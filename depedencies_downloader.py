print("❗ Loading Modules...\n")
import pkg_resources, os

def installed_packages() -> list:
    installed_packages = pkg_resources.working_set
    installed_packages_list = sorted([f"{i.key}=={i.version}" for i in installed_packages])
    print(f"Packages installed: {str(installed_packages_list)}\n")
    return installed_packages_list


def checker_packages(packages_list: list):
    with open('./requirements.txt', encoding='UTF-8', mode='+rt') as file:
        ordened_packages = [i.replace('\n','').strip() for i in file.readlines()]
        for request in ordened_packages:
            if request in packages_list:
                print('- %s installed ✅\n' %request)
            elif request not in packages_list:
                try:
                    print('- %s NOT installed ❌\n' %request)
                    os.system("pip install %s" % request)
                except SystemError as SE:
                    print('%s causing exit ⚠'%SE)
                    try:    
                        os.system("py -m pip install %s" %request)
                    except:
                        os.system("python -m pip install %s" %request)
            else:
                print('An issue found')
            
checker_packages(packages_list = installed_packages())
