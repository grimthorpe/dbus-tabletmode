#!/usr/bin/python
'''
Simple script that checks the state of the tablet mode.

Returns 0 if in tablet mode, otherwise 1.

Can be used with the "Configurable Button" plasmoid to indicate the tablet mode status
and to run custom scripts (e.g. show OnBoard)
'''

import dbus

bus=dbus.SystemBus()
#bus=dbus.SessionBus()

tabletmode=bus.get_object('org.grimthorpe.TabletMode', '/TabletMode')
mode=tabletmode.GetTabletMode()

print("The current mode is", mode)

if(mode):
    exit(0)
else:
    exit(1)

