# G14 2022 Power Manager for Linux

---

This is a fork of https://gitlab.com/marcaux/asus-g14-2022

---

## status suspend

### s0ix

- finally works from kernel 6.1 (or before release the current ROG / G14 kernel) and up

For reference:

- https://www.phoronix.com/news/AMD-s2idle-Rembrandt-ASUS
- https://lore.kernel.org/lkml/a5f1976a3b8e905a09ebb08f3baad0996101c5bb.camel@ljones.dev/

## GPU freezes

There are still some issues around the GPU under Linux that are not resolved.

The system could hang and crash at times (for some not at all, for others once a day).

It could be that the combination of power management, VAAPI, GPU firmware and Mesa lead to this issue but it is not clear and the AMD issue tracker is not marked as solved, yet.

For reference:

- https://gitlab.freedesktop.org/drm/amd/-/issues/2068

## scripts and quirks

- `sudo ./install` to install
- `sudo ./uninstall` to uninstall

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

### autopm

`etc/systemd/system/autopm.service`

`usr/local/bin/autopm`

adjusts the CPU gov and boost depending on the power profile

ryzenadj and iGPU profiles can also be adjusted if needed
