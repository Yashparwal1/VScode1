import banner
import os
import subprocess
import threading
import time
import requests
from bs4 import BeautifulSoup


def check_installed(name, needargs=False):
    proc = subprocess.Popen(
        [f"dpkg -s {name}"], stdout=subprocess.PIPE, shell=True)
    # there keyfor success output and noththere for error output
    (there, notthere) = proc.communicate()
    if "install ok installed" not in there.decode():
        print("[-] not installed")
        print("[+] it is not installed in your Kali")
        download = input("[+] Do you want to install it?(y/n)")
        if download == "y" or download == "Y" or download == "Yes" or download == "yes":
            os.system(f"apt install {name} -y")
            if needargs:
                download = input("Do you want to run the tool?(y/n)")
                if download == "y" or download == "Y" or download == "Yes" or download == "yes":
                    # when tool is of cli no need of thread
                    thread_run(name, needargs)
            else:
                download = input("Do you want to run the tool?(y/n)")
                if download == "y" or download == "Y" or download == "Yes" or download == "yes":
                    # when tool is of gui it needs thread
                    threading.Thread(target=thread_run, args=(name,)).start()
    else:
        print("[+] Installed")
        print("[+] it is installed in your kali")
        if needargs:
            download = input("Do you want to run the tool?(y/n)")
            if download == "y" or download == "Y" or download == "Yes" or download == "yes":
                # when tool is of cli no need of thread
                thread_run(name, needargs)
        else:
            download = input("Do you want to run the tool?(y/n)")
            if download == "y" or download == "Y" or download == "Yes" or download == "yes":
                # when tool is of gui it needs thread
                threading.Thread(target=thread_run, args=(name,)).start()


def run_on_browser(URL):
    # print("[+] Opening url")
    print("[+] Opening Article")
    os.system(f"firefox {URL} 2>/dev/null")


def thread_run(command, needargs=False):
    print("\n")
    if needargs == "False":
        # it will run only help because it is in cli
        os.system(f"{command}")
    elif needargs == '-h':
        os.system(f"{command} -h")
    elif needargs == '--help':
        os.system(f"{command} --help")
    else:
        # for gui all errors/output will go in null
        # time.sleep(1)
        # subprocess.Popen(["xdotool", "key", "ctrl+shift+t"])
        os.system(f"{command} > /dev/null 2>&1")


def main():
    os.system("clear")
    banner.main()
    banner.attack("Information Gathering")
    list_attacks = [" Nmap", " Maltego", " Dracnmap", " RED_HAWK",
                    " Th3inspector", " Hping3", " Arping", " Netdiscover", " Wafw00f"]
    for i in range(len(list_attacks)):
        print(f"{i}) {list_attacks[i]}")
    option = input("\n Select an option ->  ")
    if option == "0":
        print("\n[+] Nmap")
        os.system("clear")
        Nmap()
    elif option == "1":
        print("\n[+] Maltego")
        os.system("clear")
        Maltego()
    elif option == "2":
        print("\n[+] Dracnmap")
        os.system("clear")
        Dracnmap()
    elif option == "3":
        print("\n[+] RED_HAWK")
        os.system("clear")
        RED_HAWK()
    elif option == "4":
        print("\n[+] Th3inspector")
        os.system("clear")
        Th3inspector()
    elif option == "5":
        print("\n[+] Hping3")
        os.system("clear")
        Hping3()
    elif option == "6":
        print("\n[+] Arping")
        os.system("clear")
        Arping()
    elif option == "7":
        print("\n[+] Netdiscover")
        os.system("clear")
        Netdiscover()
    elif option == "8":
        print("\n[+] Wafw00f")
        os.system("clear")
        Wafw00f()
    else:
        return


def Nmap():
    while True:
        os.system("clear")
        banner.main()
        banner.attack("Nmap")
        banner.description("Nmap (Network Mapper) is a network scanner created by Gordon Lyon (also known by his pseudonym Fyodor Vaskovich). Nmap is used to discover hosts and services on a computer network by sending packets and analyzing the responses.")
        ask = tool_options()
        if ask == "1":
            check_installed("nmap", "-h")
            waiting()
        elif ask == "2":
            # first argument for dictionary(key=title,value=url) second argument for banner
            writeup({"Nmap Cheat-Sheet": "https://www.stationx.net/nmap-cheat-sheet/",
                    "Official website": "https://nmap.org/ ", "Other resources": "https://linux.die.net/man/1/nmap"}, Nmap)
        else:
            return


def Maltego():
    while True:
        os.system("clear")
        banner.main()
        banner.attack("Maltego")
        banner.description("Maltego is software used for open-source intelligence and forensics, developed by Paterva from Pretoria, South Africa. Maltego focuses on providing a library of transforms for discovery of data from open sources, and visualizing that information in a graph format, suitable for link analysis and data mining")
        ask = tool_options()
        if ask == "1":
            check_installed("maltego")
        elif ask == "2":
            # first argument for dictionary(key=title,value=url) second argument for banner
            writeup({"Official website": "https://www.maltego.com/ ", "How to use it": "https://www.geeksforgeeks.org/maltego-tool-in-kali-linux/ ",
                    "Other resources": "https://www.cyberpratibha.com/information-gathering-with-maltego/ "})
        else:
            return


def Dracnmap():
    while True:
        os.system("clear")
        banner.main()
        banner.attack("Dracnmap")
        banner.description("Dracnmap is an open source program which is using to exploit the network and gathering information with nmap help. Nmap command comes with lots of options that can make the utility more robust and difficult to follow for new users. Hence Dracnmap is designed to perform fast scaning with the utilizing script engine of nmap and nmap can perform various automatic scanning techniques with the advanced commands.")
        ask = tool_options()
        if ask == "1":
            print("Checking Dracnmap is installed or not......")
            if not os.path.isdir("Dracnmap"):
                print("[-] Dracnmap is not installed")
                check_y = input("[+] Do you want to install it?(y/n)")
                if check_y == "y" or check_y == "Y" or check_y == "yes" or check_y == "YES":
                    print("[+] Installing .......")
                    os.system(
                        "git clone https://github.com/Screetsec/Dracnmap.git")
                    print(
                        f"\Dracnmap is installed at ' {os.getcwd()} ' path\n")
                    use = input("[+] Do you want to start Dracnmap? (y/n)")
                    if use[0].lower() == "y":
                        os.system(
                            "cd Dracnmap && chmod +x dracnmap-v2.2.sh && sudo ./dracnmap-v2.2.sh.sh")
            else:
                print("[+] Dracnmap is already Installed !!")
                use = input("[+] Do you want to start Dracnmap? (y/n)")
                if use[0].lower() == "y":
                    os.system(
                        "cd Dracnmap && chmod +x dracnmap-v2.2.sh && ./dracnmap-v2.2.sh.sh")
        elif ask == "2":
            writeup({"How to use": "https://www.geeksforgeeks.org/dracnmap-information-gathering-and-network-exploitation-tool/ ",
                    "Other resources": "https://www.hacking.land/2016/10/dracnmap-exploit-network-and-gathering.html?utm_source=dlvr.it&utm_medium=facebook&m=1 "}, Dracnmap)
        else:
            print("[+] Press Enter to go back")


def RED_HAWK():
    while True:
        os.system("clear")
        banner.main()
        banner.attack("RED_HAWK")
        banner.description("Red Hawk is a free and open-source tool available on GitHub. Red Hawk is used to scanning websites for information gathering and finding vulnerabilities. Red Hawk is written in PHP. It uses PHP script to do reconnaissance. Red Hawk is so powerful that it can detect content management system while scanning, it can detect IP address, it can detect webserver record, it can detect Cloudflare information, and can detect robots.txt. Red Hawk can detect WordPress, Drupal, Joomla, and Magento CMS. Red Hawk looks for error-based SQL injections, WordPress sensitive files, and WordPress version-related vulnerabilities. RedHawk uses different modules for doing all the scannings.")
        ask = tool_options()
        if ask == "1":
            print("Checking RED_HAWK is installed or not......")
            if not os.path.isdir("RED_HAWK"):
                print("[-] RED_HAWK is not installed")
                check_y = input("[+] Do you want to install it?(y/n)")
                if check_y.lower() == "y" or check_y.lower() == "YES":
                    print("[+] Installing .......")
                    os.system(
                        "git clone https://github.com/Tuhinshubhra/RED_HAWK.git")
                    print(
                        f"\RED_HAWK is installed at ' {os.getcwd()} ' path\n")
                    ask_s = input("[+] Do you want to start RED_HAWK? (y/n)")
                    if ask_s == "y" or ask_s == "Y" or ask_s == "yes" or ask_s == "YES":
                        os.system("cd RED_HAWK && php rhawk.php")
            else:
                print("[+] RED_HAWK is already Installed !!")
                ask_s = input("[+] Do you want to start RED_HAWK? (y/n)")
                if ask_s == "y" or ask_s == "Y" or ask_s == "yes" or ask_s == "YES":
                    os.system("cd RED_HAWK && php rhawk.php")

        elif ask == '2':
            writeup({"How to use": "https://systemweakness.com/red-hawk-an-information-gathering-tool-d12a66da7c63 ",
                    "Other resources": "https://www.geeksforgeeks.org/red-hawk-information-gathering-and-vulnerability-scanning-tool-in-kali-linux/ "}, RED_HAWK)
        else:
            print("[+] Press Enter to go back")


def Th3inspector():
    while True:
        os.system("clear")
        banner.main()
        banner.attack("Th3inspector")
        banner.description("Th3inspector is an open source program which is using to exploit the network and gathering information with nmap help. Nmap command comes with lots of options that can make the utility more robust and difficult to follow for new users. Hence Dracnmap is designed to perform fast scaning with the utilizing script engine of nmap and nmap can perform various automatic scanning techniques with the advanced commands.")
        ask = tool_options()
        if ask == "1":
            print("Checking Th3inspector is installed or not......")
            if not os.path.isdir("Th3inspector"):
                print("[-] Th3inspector is not installed")
                check_y = input("[+] Do you want to install it?(y/n)")
                if check_y.lower() == "y" or check_y.lower() == "YES":
                    print("[+] Installing .......")
                    os.system(
                        "git clone https://github.com/Moham3dRiahi/Th3inspector.git")
                    print(
                        f"\Th3inspector is installed at ' {os.getcwd()} ' path\n")
                    ask_s = input(
                        "[+] Do you want to start Th3inspector? (y/n)")
                    if ask_s == "y" or ask_s == "Y" or ask_s == "yes" or ask_s == "YES":
                        os.system("cd Th3inspector && perl Th3inspector.pl")
            else:
                print("[+] Th3inspector is already Installed !!")
                ask_s = input("[+] Do you want to start Th3inspector? (y/n)")
                if ask_s == "y" or ask_s == "Y" or ask_s == "yes" or ask_s == "YES":
                    os.system("cd Th3inspector && perl Th3inspector.pl")

        elif ask == '2':
            writeup({"github description": "https://github.com/Moham3dRiahi/Th3inspector ", "First resource": "https://www.geeksforgeeks.org/red-hawk-information-gathering-and-vulnerability-scanning-tool-in-kali-linux/ ",
                    "Second resource": "https://pentesttools.net/th3inspector-tool-for-information-gathering/"}, Th3inspector)
        else:
            print("[+] Press Enter to go back")


def Hping3():
    while True:
        os.system("clear")
        banner.main()
        banner.attack("Hping3")
        banner.description("hping is a command-line oriented TCP/IP packet assembler/analyzer. It supports TCP, UDP, ICMP and RAW-IP protocols, has a traceroute mode, the ability to send files between a covered channel, and many other features.")
        ask = tool_options()
        if ask == "1":
            check_installed("hping3", "--help")
        elif ask == "2":
            writeup(
                {"First resource": "https://hacksheets.in/all-categories/useful-resources-main/hping3/"}, Hping3)
        else:
            print("[+] Press Enter to go back")


def Arping():
    while True:
        os.system("clear")
        banner.main()
        banner.attack("Arping")
        banner.description("hping is a command-line oriented TCP/IP packet assembler/analyzer. It supports TCP, UDP, ICMP and RAW-IP protocols, has a traceroute mode, the ability to send files between a covered channel, and many other features.")
        ask = tool_options()
        if ask == "1":
            check_installed("arping", "-h")
        elif ask == "2":
            writeup(
                {"First resource": "https://hacksheets.in/all-categories/useful-resources-main/hping3/"}, Arping)
        else:
            print("[+] Press Enter to go back")


def Netdiscover():
    while True:
        os.system("clear")
        banner.main()
        banner.attack("Netdiscover")
        banner.description("Netdiscover is a command-line oriented TCP/IP packet assembler/analyzer. It supports TCP, UDP, ICMP and RAW-IP protocols, has a traceroute mode, the ability to send files between a covered channel, and many other features.")
        ask = tool_options()
        if ask == "1":
            check_installed("netdiscover")
        elif ask == "2":
            writeup({"First resource": "https://subscription.packtpub.com/book/networking-and-servers/9781789341768/5/ch05lvl1sec50/scanning-with-netdiscover"}, Netdiscover)
        else:
            print("[+] Press Enter to go back")


def Wafw00f():
    while True:
        os.system("clear")
        banner.main()
        banner.attack("Wafw00f")
        banner.description("Netdiscover is a command-line oriented TCP/IP packet assembler/analyzer. It supports TCP, UDP, ICMP and RAW-IP protocols, has a traceroute mode, the ability to send files between a covered channel, and many other features.")
        ask = tool_options()
        if ask == "1":
            check_installed("wafw00f", "--help")
        elif ask == "2":
            writeup({"First resource": "https://www.briskinfosec.com/tooloftheday/toolofthedaydetail/wafw00f-tool-to-fingerprint-and-identify-web-application-firewall",
                    "Second resource": "https://null-byte.wonderhowto.com/how-to/identify-web-application-firewalls-with-wafw00f-nmap-0198145/"}, Wafw00f)
        else:
            print("[+] Press Enter to go back")


def tool_options():
    print("1) TOOL(about,installation)")
    print("2) Write ups")
    print("3) go back..")
    ask = input("Select an option ->  ")
    return ask


def writeup(writeup_dist, name):
    while True:
        os.system("clear")
        banner.main()
        banner.attack(name)
        # convert dict keys in list(type casting)
        key = list(writeup_dist.keys())
        key.append("go back")
        for i in range(len(key)):
            print(f"{i} {key[i]}")
        option = input("\n Select an option ->  ")
        # 1-9=int kdsjfhgkjds=int X to type cast safely
        try:
            threading.Thread(target=run_on_browser, args=(
                writeup_dist[key[int(option)]],)).start()
            # a={"a":1,"b":2}
            # print(2)
        except:
            return

def waiting():
    input("\n[+]press ENTER to go back ")


if __name__ == "__main__":
    main()
