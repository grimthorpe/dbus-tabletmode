import dbus

class TabletMode(dbus.service.Object):
    def __init__(self, object_path):
        dbus.service.Object.__init__(self, dbus.SystemBus(), path)
        self.tabletmode=False;

    @dbus.service.method(dbus_interface='org.grimthorpe.TabletMode',
                         in_signature='b', out_signature='')
    def SetTabletMode(self, tabletmode):
        self.tabletmode=tabletmode
        self.TabletModeChanged(tabletmode)

    @dbus.service.method(dbus_interface='org.grimthorpe.TabletMode',
                         in_signature='', out_signature='b')
    def GetTabletMode(self):
        return self.tabletmode

    @dbus.service.signal(dbus_interface='org.grimthorpe.TabletMode',
                         signature='b')
    def TabletModeChanged(self, tabletmode):
        print "Tablet mode changed to %d" % tabletmode


