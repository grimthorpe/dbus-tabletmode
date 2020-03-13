#!/usr/bin/python

import dbus
class TabletModeClient():
    def __init__(self):
        self.tabletmode=False
        self.systembus=dbus.SystemBus()
        self.sessionbus=dbus.SessionBus()
        self.tabletmodeobject=None
        self.onboardobject=None
        self.onboardstatus={True: True, False: False}

    def get_onboard_state(self):
        return self.onboardobject.Get('org.onboard.Onboard.Keyboard', 'Visible')==True

    def update_onboard_state(self, tabletmode):
        self.onboardstatus[tabletmode]=self.get_onboard_state()

    def change_onboard_state(self, tabletmode):
        if(self.onboardstatus[tabletmode]):
            self.onboardobject.Show()
        else:
            self.onboardobject.Hide()

    def tabletmode_changed(self, mode):
        print("Tablet mode changed to ", mode)
        self.update_onboard_state(self.tabletmode)
        self.tabletmode=mode
        self.change_onboard_state(mode)

    def connect_to_dbus(self):
        self.onboardobject=self.sessionbus.get_object("org.onboard.Onboard", "/org/onboard/Onboard/Keyboard")
        self.tabletmodeobject=self.systembus.get_object("org.grimthorpe.TabletMode", "/TabletMode")
        self.tabletmode_changed(self.tabletmodeobject.GetTabletMode())
        self.tabletmodeobject.connect_to_signal("TabletModeChanged", self.tabletmode_changed, dbus_interface="org.grimthorpe.TabletMode")

if __name__ == '__main__':
    import dbus.mainloop.glib
    from gi.repository import GLib

    dbus.mainloop.glib.DBusGMainLoop(set_as_default=True)

    loop=GLib.MainLoop()
    clientobject=TabletModeClient()
    clientobject.connect_to_dbus()
    loop.run()


