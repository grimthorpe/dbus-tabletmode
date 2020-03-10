#!/bin/sh

# tabletmode values:
#  -1 indicates unsupported $3 value
#  -2 unsupported $4 value for known $3
# 0 tablet mode disabbled
# 1 tablet mode enabled
TABLETMODE=-1

DEBUG=1		# Set to 1 to log all events
# onboard doesn't work as we need access to the user's session rather than the ACPI session
ONBOARD=0	# Set to 1 to show / hide the onboard keyboard when tablet mode changes



case "$3" in
	# Dell latitude 7275
	0000008A)
		case "$4" in
			00000000)
				TABLETMODE=0
				;;
			00000001)
				TABLETMODE=1
				;;
			*)
				TABLETMODE=-2
				;;
		esac
				;;
			*)
				TABLETMODE=-1
				;;
esac

if [ "$DEBUG" == "1" ]; then
	case "$TABLETMODE" in
		0)
			logger "tabletmode: Table mode disabled"
			;;
		1)
			logger "tabletmode: Table mode enabled"
			;;
		-1)
			logger "tabletmode: Unsupported ACPI \$3: $3 ($4)"
			;;
		-2)
			logger "tabletmode: Unsupported mode value for ACPI \$3: $3 $4"
			;;
	esac
fi

if [ "$ONBOARD" == "1" ]; then
	case "$TABLETMODE" in
		0)
			dbus-send --type=method_call --dest=org.onboard.Onboard /org/onboard/Onboard/Keyboard org.onboard.Onboard.Keyboard.Hide
			;;
		1)
			#dbus-send --type=method_call --dest=org.onboard.Onboard /org/onboard/Onboard/Keyboard org.onboard.Onboard.Keyboard.Show
			dbus-send --type=method_call --dest=org.onboard.Onboard /org/onboard/Onboard/Keyboard org.onboard.Onboard.Keyboard.Hide
			dbus-send --type=method_call --dest=org.onboard.Onboard /org/onboard/Onboard/Keyboard org.onboard.Onboard.Keyboard.ToggleVisible
			;;
		-1)
			logger "tabletmode: Unsupported ACPI $1 $2 \$3: $3 ($4)"
			;;
		-2)
			logger "tabletmode: Unsupported mode value for ACPI $1 $2 $3 \$4: $4"
			;;
	esac
fi

