# dell-tabletmode
Tablet Mode ACPI event handler

These files provide ACPI handlers for convertable laptops and present the
state as a system DBus object.


The ACPI event it works off is video/tabletmode TBLT 0000008A 0000000x
where

x=0 - tablet is connected to the keyboard

x=1 - tablet is disconenected from the keyboard


The state of the tabletmode can be read from the system DBus address
org.grimthorpe.TabletMode/TabletMode

Methods:

GetTabletMode() - returns boolean true if in tablet mode, otherwise false.

SetTabletMode(boolean mode) - sets the mode

Signals:

TabletModeChanged(boolean mode) - called if the tablet mode is changed by the last call to SetTabletMode

