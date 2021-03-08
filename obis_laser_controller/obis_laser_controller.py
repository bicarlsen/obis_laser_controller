import easy_scpi as scpi

class ObisLaserController( scpi.Instrument ):
	"""
	Represent an OBIS Laser Controller.
	"""
	def __init__( self, port, timeout = 5, auto_off = True ):
		"""
		:param port: Port to connect to.
		:param timeout: Communication timeout in seconds.
			[Default: 5]
		:param auto_off: Turn laser off on disconnect.
			[Default: True]
		""" 
		super().__init__( 
			port, 
			handshake = 'OK',
			timeout = timeout* 1000,
			read_termination = '\r\n', 
            write_termination = '\r\n', 
		)

		self.auto_off = auto_off

		# static properties
		self._nominal_power = None
		self._max_power = None
		self._min_power = None
		self._wavelength = None
		self._power_rating = None


	@property
	def nominal_power( self ):
		"""
		:returns: Nominal power of the laser.
		"""
		if self._nominal_power is None:
			self._nominal_power = float( self.source.power.nominal() )

		return self._nominal_power


	@property
	def max_power( self ):
		"""
		:returns: Maximum power of the laser.
		"""
		if self._max_power is None:
			self._max_power = float( self.source.power.limit.high() )

		return self._max_power


	@property
	def min_power( self ):
		"""
		:returns: Minimum power of the laser.
		"""
		if self._min_power is None:
			self._min_power = float( self.source.power.limit.low()	)

		return self._min_power


	@property
	def wavelength( self ):
		"""
		:returns: Wavelength of the laser.
		"""
		if self._wavelength is None:
			self._wavelength = float( self.system.information.wavelength() )

		return self._wavelength


	@property
	def power_rating( self ):
		"""
		:returns: Power rating of the laser.
		"""
		if self._power_rating is None:
			self._power_rating = float( self.system.information.power() )
		
		return self._power_rating


	@property
	def power( self ):
		"""
		:returns: Present output power of the laser.
		"""
		return float( self.source.power.level() )


	@property
	def current( self ):
		"""
		:returns: Present output current of the laser.
		"""
		return self.source.power.current()


	@property
	def enabled( self ):
		"""
		:returns: True if the laser is on, False otherwise.
		"""
		return scpi.Property.val2bool( self.source.am.state() )


	def connect( self ):
		"""
		Connect to the device.
		"""
		try:
			super().connect()

		except RuntimeError as err:
			pass

		# set handshake mode to off
		self.syst.comm.hand( 'on' )


	def disconnect( self ):
		# reset static properties
		self._nominal_power = None
		self._max_power = None
		self._min_power = None
		self._wavelength = None
		self._power_rating = None

		if self.auto_off:
			self.off()

		super().disconnect()


	def on( self ):
		"""
		Turns the laser on.
		"""
		self.source.am.state( 'on' )


	def off( self ):
		"""
		Turns the laser on.
		"""
		self.source.am.state( 'off' )


	def set_power( self, power = 0 ):
		"""
		Set the power level.

		:param power: Power in Watts. [Default: 0]
		"""
		if power < self.min_power:
			raise ValueError( 'Power is too low.')

		elif power > self.max_power:
			raise ValueError( 'Power is too high.')

		self.source.power.level.immediate.amplitude( power )
