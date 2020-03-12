#!/bin/sh

# tabletmode values:
#  -1 indicates unsupported $3 value
#  -2 unsupported $4 value for known $3
# 0 tablet mode disabbled
# 1 tablet mode enabled
TABLETMODE=-1

DEBUG=1		# Set to 1 to log all events
DBUS=1		# Set to 1 to send DBus mode changes to org.grimthorpe.TabletMode


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

if [ "$DBUS" == "1" ]; then
	case "$TABLETMODE" in
		0)
			dbus-send --system --type=method_call --dest=org.grimthorpe.TabletMode /TabletMode org.grimthorpe.TabletMode.SetTabletMode boolean:false
			;;
		1)
			dbus-send --system --type=method_call --dest=org.grimthorpe.TabletMode /TabletMode org.grimthorpe.TabletMode.SetTabletMode boolean:true
			;;
		-1)
			logger "tabletmode: Unsupported ACPI $1 $2 \$3: $3 ($4)"
			;;
		-2)
			logger "tabletmode: Unsupported mode value for ACPI $1 $2 $3 \$4: $4"
			;;
	esac
fi

