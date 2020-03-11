# dell-tabletmode
DELL tabletmode ACPI handler

These files provide ACPI handlers for DELL Latitude 7275 (and maybe other)
2-in-1 laptops.

This is based off using acpid in Arch linux on the last commit date in the
repository - I accept no responsibility if this breaks something vital on
your machine.

INSTALLATION:
Copy the contents of acpi/events to /etc/acpi/events
Copy the contents of acpi/actions to /etc/acpi/actions
Run sudo systemctl restart acpid.service

Optionally either copy acpi/handler.sh to /etc/acpi/handler.sh or apply the
patch handler.sh.diff to /etc/acpi/handler.sh to suppress the unknown ACPI
messages the original made.

