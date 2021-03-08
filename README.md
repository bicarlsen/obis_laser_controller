# OBIS Laser Controller
## Controller for OBIS Lasers.

The controller is built off of the [`easy_scpi`](https://pypi.org/project/easy-scpi/). For more info about running custom commands, consult it's documentation.

### Methods

+ **ObisLaserController( port, timeout = 5, auto_off = True ):** Creates a new laser controller on the given port. [Inherits from easy_scpi.Instrument]

+ **on():** Turns the laser on.

+ **off():** Turns the laser off.

+ **set_power( power = 0 ):** Sets the laser's power.
 

### Properties

+ **nominal_power:** Nominal power of the laser.

+ **max_power:** Maximum power of the laser.

+ **min_power:** Minimum power of the laser.

+ **wavelength:** Wavelength of the laser.

+ **power_rating:** Power rating of the laser.

+ **power:** Present output power of the laser.

+ **current:** Present output current of the laser.

+ **enabled():** Returns if the laser is on or off.

## Example
```python
from obis_laser_controller import ObisLaserController

# create laser controller and connect to device
laser = ObisLaserController( 'COM16' )
laser.connect()

# set power to half of nominal and turn on
laser.set_power( laser.nominal_power / 2 )
laser.on()


# turn laser off and disconnect
# NOTE: By default the laser will turn off when disconnected.
laser.off()
laser.disconnect()
```