# -*- coding: utf-8 -*-

import subprocess
import optparse
import re
import sys
import signal
print("\033[1;31m")
print(r"""
  ______           __      __  __           __      ______                   
 /_  __/_  _______/ /__   / / / /___ ______/ /__   /_  __/__  ____ _____ ___ 
  / / / / / / ___/ //_/  / /_/ / __ `/ ___/ //_/    / / / _ \/ __ `/ __ `__ \
 / / / /_/ / /  / ,<    / __  / /_/ / /__/ ,<      / / /  __/ /_/ / / / / / /
/_/  \__,_/_/  /_/|_|  /_/ /_/\__,_/\___/_/|_|    /_/  \___/\__,_/_/ /_/ /_/ 
                                                                                                                                        
                """)
print("Turk Hack Team".center(75))
print("\033[1;37m Livcon\n".center(85))


def get_user_input():
    parse_object = optparse.OptionParser()
    parse_object.add_option("-i", "--interface", dest="interface", help="interface to change")
    parse_object.add_option("-m", "--mac", dest="mac_address", help="new mac address")
    return parse_object.parse_args()


def change_mac(i, m):
    subprocess.call(["ifconfig", i, "down"])
    subprocess.call(["ifconfig", i, "hw", "ether", m])
    subprocess.call(["ifconfig", i, "up"])


def control_new_mac(interface):
    ifconfig = subprocess.check_output(["ifconfig", interface])
    new_mac = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", str(ifconfig))
    if new_mac:
        return new_mac.group(0)
    else:
        return None


def signal_handler(sig, frame):
    print('\n\nCtrl+C tuş kombinasyonuna bastınız\nSistem kapatıldı\n')
    sys.exit()


signal.signal(signal.SIGINT, signal_handler)


try:
    (user_input, arguments) = get_user_input()
    old_mac = control_new_mac(user_input.interface)
    if len(user_input.mac_address) < 17 or len(user_input.mac_address) > 17:
        print("Hata! Mac adresiniz AA:BB:CC:DD:EE:FF formatında olmalıdır!")
        sys.exit()
    elif not user_input.interface == "wlan0" or not user_input.interface == "eth0" :
        print("Hata! Interface böyle bir interface değeri yok!")
        sys.exit()
    else:
        change_mac(user_input.interface, user_input.mac_address)

        if control_new_mac(str(user_input.interface)) == user_input.mac_address:
            print(f"\nMac Adresiniz Başarıyla Değiştirildi!\n")
            print("Eski Mac Adresiniz: " + old_mac)
            print("Yeni Mac Adresiniz: " + user_input.mac_address + "\n")
        else:
            print("Hata! Mac adresiniz değiştirilemedi! Lütfen tekrar deneyin\n")
        sys.exit()
except:
    interface = input("Interface değeri girin (varsayılan: eth0): ")
    if len(interface) < 4:
        interface = "eth0"
    mac_address = input("Kullanmak istediğiniz mac adresini girin (AA:BB:CC:DD:EE:FF): ")
    if len(mac_address) < 2:
        mac_address = "00:31:31:31:31:31"
    if (len(mac_address) < 17 and len(mac_address) > 2) or len(mac_address) > 17:
        print("Hata! Mac adresiniz AA:BB:CC:DD:EE:FF formatında olmalıdır!")
        sys.exit()
    else:
        old_mac = control_new_mac(interface)
        change_mac(interface, mac_address)

        if control_new_mac(interface) == mac_address:
            print(f"\nMac Adresiniz Başarıyla Değiştirildi!\n")
            print("Eski Mac Adresiniz: " + old_mac)
            print("Yeni Mac Adresiniz: " + mac_address + "\n")
        else:
            print("Hata! Mac adresiniz değiştirilemedi! Lütfen tekrar deneyin\n")
        sys.exit()