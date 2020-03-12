#!/usr/bin/python
import dbus
import dbus.service

'''
TabletMode class

Defines 2 DBus methods:
    SetTabletMode(boolean tabletmode)
    boolean GetTabletMode()
Defines 1 DBus signal:
    TabletModeChanged(boolean tabletmode)
'''
class TabletMode(dbus.service.Object):
    def __init__(self):
        self.tabletmode=False;
        self.bus=dbus.SystemBus()
        #self.bus=dbus.SessionBus()
        name=dbus.service.BusName('org.grimthorpe.TabletMode', bus=self.bus)
        super().__init__(name, '/TabletMode')

    ''' Set the TabletMode '''
    @dbus.service.method(dbus_interface='org.grimthorpe.TabletMode',
                         in_signature='b', out_signature='')
    def SetTabletMode(self, tabletmode):
        if(tabletmode != self.tabletmode):
            self.tabletmode=tabletmode
            self.TabletModeChanged(tabletmode)

    ''' Get the TabletMode '''
    @dbus.service.method(dbus_interface='org.grimthorpe.TabletMode',
                         in_signature='', out_signature='b')
    def GetTabletMode(self):
        return self.tabletmode

    ''' Signal that the TabletMode has changed.
        Only signalled when actually changed.'''
    @dbus.service.signal(dbus_interface='org.grimthorpe.TabletMode',
                         signature='b')
    def TabletModeChanged(self, tabletmode):
        print("Tablet mode changed to %d" % tabletmode)

if __name__ == '__main__':
    import dbus.mainloop.glib
    from gi.repository import GLib
    dbus.mainloop.glib.DBusGMainLoop(set_as_default=True)
    loop=GLib.MainLoop()
    serviceobject=TabletMode()
    loop.run()

