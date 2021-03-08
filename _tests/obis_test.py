import time
import logging
# logging.basicConfig( level = logging.DEBUG )

from obis_laser_controller import ObisLaserController

laser = ObisLaserController( 'COM16' )
laser.connect()

print( 'id: ', laser.id )
print( 'handshake:', laser.syst.comm.hand() )
print( 'min power: ', laser.min_power )
print( 'max power: ', laser.max_power )
print( 'nom power: ', laser.nominal_power )
print( 'wavelength: ', laser.wavelength )
print( 'power rating: ', laser.power_rating )
print( 'power: ', laser.power )
print( 'current: ', laser.current )
print( 'enabled: ', laser.enabled )


print( 'Set laser power to 0.001 W' )
laser.set_power( 0.001 )
laser.on()
time.sleep( 1 )

print( 'power: ', laser.power )
print( 'current: ', laser.current )
print( 'enabled: ', laser.enabled )
time.sleep( 3 )

print( 'Set laser power to 0.01 W' )
laser.set_power( 0.01 )
time.sleep( 1 )

print( 'power: ', laser.power )
print( 'current: ', laser.current )
print( 'enabled: ', laser.enabled )
time.sleep( 3 )

laser.off()

laser.disconnect()