from mojo.extensions import getExtensionDefault, setExtensionDefault, getExtensionDefaultColor, setExtensionDefaultColor
from AppKit import NSColor

contourLockDefaultKey = 'nl.thomjanssen.contourLock'
onOffKey = "%s.onOff" % contourLockDefaultKey
lineWidthKey = "%s.lineWidth" % contourLockDefaultKey
lineColorKey = "%s.lineColor" % contourLockDefaultKey
fillColorKey = "%s.fillColor" % contourLockDefaultKey
lineRGBA = "%s.lineRGBA" % contourLockDefaultKey
fillRGBA = "%s.fillRGBA" % contourLockDefaultKey


class ContourLockDataCollection(object):
	
	_fallbackOnOff = True
	_fallbackStrokeWidth = 2
	_fallbackStrokeColor = NSColor.colorWithCalibratedRed_green_blue_alpha_(1, 0, 0, 1)
	_fallbackFillColor = NSColor.colorWithCalibratedRed_green_blue_alpha_(.34, .54, .92, .2)
	_fallbackStrokeRGBA = (1, 0, 0, 1)
	_fallbackFillRGBA = (.34, .54, .92, .2)

	def __init__(self): 
		self.load()

	def load(self):
		self.onOff = getExtensionDefault(onOffKey, self._fallbackOnOff)
		self.lineWidth = getExtensionDefault(lineWidthKey, self._fallbackStrokeWidth)
		self.lineColor = getExtensionDefaultColor(lineColorKey, self._fallbackStrokeColor)
		self.fillColor = getExtensionDefaultColor(fillColorKey, self._fallbackFillColor)
		self.lineRGBA = getExtensionDefault(lineRGBA, self._fallbackStrokeRGBA)
		self.fillRGBA = getExtensionDefault(fillRGBA, self._fallbackFillRGBA)

	def save(self):
		setExtensionDefault(onOffKey, self.onOff)
		setExtensionDefault(lineWidthKey, self.lineWidth)
		setExtensionDefaultColor(lineColorKey, self.lineColor)
		setExtensionDefaultColor(fillColorKey, self.fillColor)
		setExtensionDefault(lineRGBA, self.lineRGBA)
		setExtensionDefault(fillRGBA, self.fillRGBA)


		
ContourLockData = ContourLockDataCollection()