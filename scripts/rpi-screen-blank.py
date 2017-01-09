#!/usr/bin/env python
import time
import glob
import subprocess
import logging
log = logging.getLogger("screenblank")
log.setLevel(logging.INFO)
log.addHandler(logging.StreamHandler())

from evdev import InputDevice
from select import select

timeout = 10  # minutes
screen_blanked = False
status_command = ['/usr/bin/tvservice', '-s']
tv_off = [
        ('/bin/fbset', '-accel', 'false'),
        ('/usr/bin/tvservice', '-o'),
    ]
tv_on = [
        ('/usr/bin/tvservice', '-p'),
        ('/bin/fbset', '-accel', 'true'),
    ]

def is_blanked():
    p = subprocess.Popen(status_command, stdout=subprocess.PIPE)
    output, _ = p.communicate()
    log.debug(output)
    if " [" in output:
        state, text = output.split(" [", 1)
        state, val = state.split(" ", 1)
        log.debug(val)
        if val == "0x120002":
            return True
    return False

def run_script(script):
    for command in script:
        log.info("Running %s" % str(command))
        retval = subprocess.call(command)
        if retval != 0:
            log.error("Error %d in %s" % (retval, str(command)))

# A mapping of file descriptors (integers) to InputDevice instances.
all_devices = map(InputDevice, glob.glob("/dev/input/event*"))
all_devices = {dev.fd: dev for dev in all_devices}

keyboards = {}
for dev in all_devices.values():
    log.debug(dev)
    caps = dev.capabilities(verbose=True)
    for k,v in caps:
        log.debug(k)
        if k == 'EV_KEY':  # should detect all keyboard and mouse devices
            keyboards[dev.fd] = dev

log.info("watching: %s" % str(keyboards))
while True:
    r, w, x = select(keyboards, [], [], timeout * 60)
    if r:
        valid_event = False
        for fd in r:
           for event in keyboards[fd].read():
               log.debug(str(event))
               valid_event = True
        if valid_event and is_blanked():
            run_script(tv_on)
            log.debug("Screen on; waiting %d min before checking again" % timeout)
            time.sleep(timeout * 60)
    else:
        if is_blanked():
            log.debug("Screen already blanked")
        else:
            log.info("Timeout! Blanking screen")
            run_script(tv_off)


# tvservice status
# state 0x120002 [TV is off]
# state 0x120006 [DVI DMT (35) RGB full 5:4], 1280x1024 @ 60.00Hz, progressive
#
# seems to be relatively fragile; successive calls to tvservice -p; fbset -depth 16 seem to blank the screen until reboot
#
# Need mabye a 5 second delay after blanking to ensure settling before allowing a new monitor status
