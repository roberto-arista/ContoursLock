'''
TODO
- makkelijk contouren locken en unlocken:
	-hele c selecteren?
	-ook geselecteerd stukje/punt goed?
	-indexnummer
	-wis glyphgegevens/wis alle glyphs
- contourlijnkleur kunnen aanpassen, dus niet een drawObserver maar 'echt'

Settings:
	-onOff
	-lineWidth
	-cFill
	-cStroke
	-

'''
from robofab import *
from mojo.events import addObserver, removeObserver
from mojo.drawingTools import *
from vanilla import *
from mojo.roboFont import CurrentFont, CurrentGlyph
from AppKit import *

from contourLockData import ContourLockData

lockedContourKey = 'Locked Contours'

class ContoursLockObserver(object):
		
	def __init__(self):
		
		addObserver(self, "drawFill", "drawBackground")
		addObserver(self, "drawStroke", "draw")
			
	def drawStroke(self, info):
		if not ContourLockData.onOff:
			return
		g = info["glyph"]
		lockedContours = self.getLockedContours(g)
		if len(lockedContours) == 0:
			return
		fill(None)
		stroke(*ContourLockData.lineRGBA)
		strokeWidth(ContourLockData.lineWidth)
		for n in range(len(g.contours)):
			if n in lockedContours:
				drawGlyph(g[n])
				for p in g[n].points:
					if p.selected:
						p._set_selected(0)
						fill(1,0,0,.1)
						drawGlyph(g[n])
		#g.update()


	def drawFill(self, info):
		if not ContourLockData.onOff:
			return
		g = info["glyph"]
		lockedContours = self.getLockedContours(g)
		if len(lockedContours) == 0:
			return
		fill(*ContourLockData.fillRGBA)
		stroke(None)
		for n in range(len(g.contours)):
			if n in lockedContours:
				drawGlyph(g[n])
		#g.update()

	def getLockedContours(self, glyph):
		if glyph.note:
			lockedContours=list()
			try:
				for line in range(len(glyph.note.split('\n'))):
					if lockedContourKey in glyph.note.split('\n')[line]:
						for i in glyph.note.split('\n')[line+1].split(','):
							lockedContours.append(int(i))
			except:
				pass
		else:
			lockedContours=list()
		return lockedContours
ContoursLockObserver()
