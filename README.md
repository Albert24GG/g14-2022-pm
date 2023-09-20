# G14 2022 Power Manager for Linux

---

This is a fork of https://gitlab.com/marcaux/asus-g14-2022

---

Autopm is a python script that manages power settings such as the energy performance preferences(EPP) through amd-pstate driver and the scaling governors to optimize power consumption and performance when running on battery or AC. Optionally, ryzenadj and iGPU profiles can also be adjusted if needed.

## Install

### 1. Enable amd-pstate-epp
This can be done by adding some kernel parameters to the grub config file:
```sh 
sudo vim /etc/default/grub 
```
Then edit the `GRUB_CMDLINE_LINUX_DEFAULT` line:
```sh 
GRUB_CMDLINE_LINUX_DEFAULT="quiet splash amd_pstate=active"
```
The last step is to regenerate the grub config:
```sh 
sudo grub-mkconfig -o /boot/grub/grub.cfg
```

### 2. Install the script
```sh 
git clone https://github.com/Albert24GG/g14-2022-pm.git
cd g14-2022-pm
chmod +x install 
sudo ./install
```
## Uninstall
```sh 
chmod +x uninstall 
sudo ./uninstall
```


### fan-curves

`etc/asusd/profile.conf`

The balanced profile by default has a somewhat silent fan profile resulting in throttlling when gaming.

So I made a quick balanced fan profile that it not too obstrusive, yet powerfull enough to not throttle in my use cases.

It represents my everyday profile while at the desk.

The fans are spinning all the time but on lower temps it is super quiet.
Bacause passive cooling is pretty efficient it does not hit the 70c mark often during my daily tasks and stays pretty quiet during the day.

When launching a game I setup the GPU fans to kick in a little earlier.
In my tests now with the Horizon Zero Dawn benchmark this makes a nice difference and keeps the CPU temps a little bit more in place.
When both hit 80c they run at the same rpm and the noise level is okay and more quiet than the performance profile.

With those values the temps in this benchmark at least are quite good, 85c to max 93c, but mostly below 90c.

By default the profiles are disabled. Enable them via `asusctl fan-curve -m balanced -e true`

I also created a more quiet profile for the power saver profile. The fans kick in a little later than usual so they don't spin up and down so often during my daily tasks.

