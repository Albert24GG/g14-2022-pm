import time
from typing import NamedTuple, Dict
import sys
import os
import subprocess

# integrated/dedicated GPU number
# either card1 or card0
# ! IMPORTANT - an automated way has to be found
# the order of those identifiers is not always the same
# therefore GPU_PM_ALLOWED should be disabled for now
# IGPU=card1
# DGPU=card0

# allow the change of power_dpm_force_performance_level
# as of 5.18.13 "cat /sys/class/drm/card0/device/power_dpm_force_performance_level" wakes the dGPU up all the time so let's keep it disabled
GPU_PM_ALLOWED = 0

# One might want to have this 0 if another thing controls boost
# There is a GNOME Shell extension where one can switch boost
#    on / off for example
CHANGE_BOOST_ALLOWED = 0

# One might not want to have ryzenadj values changed
# Silverblue users for example can't install it globally atm
# perhaps an adjustable path would be solution (?)
RYZENADJ_ALLOWED = 0


class PowerSettings(NamedTuple):
    a: int  # Sustained Power Limit (mW)
    b: int  # ACTUAL Power Limit    (mW)
    c: int  # Average Power Limit   (mW)
    k: int  # VRM EDC Current       (mA)
    f: int  # Max Tctl              (C)
    governor: str  # conservative ondemand userspace powersave performance schedutil
    boostclock: bool  # enable CPU boost clocks (set 1 for on, 0 for off)


power_modes: Dict[str, PowerSettings] = {
    # Power-Saver profile
    "power-saver" : PowerSettings(7000, 7000, 7000, 90000, 85, "conservative", False) ,
    
    # Balanced profile
    "balanced"    : PowerSettings(35000, 35000, 35000, 95000, 95, "schedutil", True),
    
    # Performance profile
    "performance" : PowerSettings(45000, 45000, 45000, 100000, 100, "performance", True)
}


def runCommand(command: str) -> None:
    subprocess.run(command, shell=True)


def getCommandOutput(command: str) -> str:
    return subprocess.run(command, capture_output=True, shell=True).stdout


def readFromFile(path: str) -> str:
    file = open(path, 'r')
    text = file.read()
    file.close()
    return text


def writeToFile(path: str, content: str) -> None:
    file = open(path, 'w')
    file.write(content)
    file.close()


def setGovernor(mode: str) -> None:
    cpu_gov: str = readFromFile("/sys/devices/system/cpu/cpu0/cpufreq/scaling_governor")
    
    if(cpu_gov == power_modes[mode].governor):
        return
    
    cpu_gov = power_modes[mode].governor
    
    print(f"{mode} profile: setting {cpu_gov} governor")
    
    dir_prefix: str = "/sys/devices/system/cpu/cpu"
    dir_suffix: str = "/cpufreq/scaling_governor" 
    cpu_cores: int = getCommandOutput("grep -c processor /proc/cpuinfo")
    
    for coreNumb in range(0, cpu_cores):
        path: str = dir_prefix + coreNumb + dir_suffix
        writeToFile(path, cpu_gov)



def managePower() -> None:
    power_profile: str = getCommandOutput("powerprofilesctl get")



def isRoot() -> bool:
    return (os.getuid() == 0)


def main() -> None:
    if not isRoot():
        sys.exit("Error: Script must be run as root")
    while True:
        managePower()
        time.sleep(10)


if __name__ == "__main__":
    main()
