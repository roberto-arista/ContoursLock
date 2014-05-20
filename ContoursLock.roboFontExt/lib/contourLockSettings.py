from robofab import *
from mojo.events import addObserver, removeObserver
from mojo.drawingTools import *
from vanilla import *
from AppKit import *
from mojo.UI import UpdateCurrentGlyphView
from mojo.roboFont import CurrentFont, CurrentGlyph
from mojo.roboFont import OpenWindow

from contourLockData import ContourLockData


lockedContourKey = 'Locked Contours\n'

class ContourLockSettingsDialog(object):
	def __init__(self):
		
		self.s = FloatingWindow((200,170), "Settings")
		self.s.onOff = CheckBox((7,7,-7,23),"lock locked contours", value=ContourLockData.onOff, callback=self.onOffCallback)
		self.s._stokeWidthTxt = TextBox((7,35,-7,23),"stroke width",sizeStyle="small")
		self.s.stokeWidth = Slider((7,50,-7,23), minValue=0, maxValue=6, 
			value=ContourLockData.lineWidth, 
			stopOnTickMarks=True, continuous=True, tickMarkCount=7, sizeStyle="small", 
			callback=self.lineWidthCallback)
		
		self.s.lineWidtTxt = TextBox((0,35,-0,23), int(self.s.stokeWidth.get()),sizeStyle="small", alignment="center")
		
		self.s._lineTxt = TextBox((0,80,100,23),"line", alignment="center",sizeStyle="small")
		self.s._fillTxt = TextBox((100,80,100,23),"fill", alignment="center",sizeStyle="small")
		self.s.lineColor = ColorWell((7,95,-105,25), color=ContourLockData.lineColor, callback=self.lineColorCallback)
		self.s.fillColor = ColorWell((105,95,-7,25), color=ContourLockData.fillColor, callback=self.fillColorCallback)
		
		self.s.prepareGlyphNote = SquareButton((7,140,-7,-7),"add contour lock to glyph note", sizeStyle="mini", callback=self.prepareGlyphNote)

		self.s.bind("close",self._close)
		self.s.open()

	def onOffCallback(self, sender):
		ContourLockData.onOff = sender.get()
		ContourLockData.save()
		self.updateView()	

	def lineWidthCallback(self, sender):
		ContourLockData.lineWidth = sender.get()
		ContourLockData.save()
		self.s.lineWidtTxt.set(int(sender.get()))
		self.updateView()

	def lineColorCallback(self, sender):
		ContourLockData.lineColor = sender.get()
		ContourLockData.save()

		lineRGBA_ = (
			float(str(sender.get()).split(" ")[1]), 
			float(str(sender.get()).split(" ")[2]), 
			float(str(sender.get()).split(" ")[3]), 
			float(str(sender.get()).split(" ")[4]))
		ContourLockData.lineRGBA = lineRGBA_
		self.updateView()

	def fillColorCallback(self, sender):
		ContourLockData.fillColor = sender.get()
		ContourLockData.save()
		fillRGBA_ = (
			float(str(sender.get()).split(" ")[1]), 
			float(str(sender.get()).split(" ")[2]), 
			float(str(sender.get()).split(" ")[3]), 
			float(str(sender.get()).split(" ")[4]))
		ContourLockData.fillRGBA = fillRGBA_
		self.updateView()


	def prepareGlyphNote(self, sender):
		g = CurrentGlyph()
		if g.note:
			if lockedContourKey in g.note:
				return
			else:
				g.note += "\n%s\n" % lockedContourKey
		else:
			g.note = lockedContourKey

	def _close(self,sender):
		#updateDefaults
		pass

	def updateView(self):
		UpdateCurrentGlyphView()

OpenWindow(ContourLockSettingsDialog)
