# encoding: utf-8
from __future__ import division, print_function, unicode_literals

###########################################################################################################
#
#
#	Reporter Plugin
#
#	Read the docs:
#	https://github.com/schriftgestalt/GlyphsSDK/tree/master/Python%20Templates/Reporter
#
#
###########################################################################################################


from GlyphsApp.plugins import *

class ShowGlyphsInLabelColor(ReporterPlugin):

	@objc.python_method
	def settings(self):
		self.menuName = Glyphs.localize({
			'en': 'Glyphs in their Label Colors', 
			'de': 'Glyphen in ihrer Etikettenfarbe',
			'fr': 'les glyphes dans leurs couleurs',
			'es': 'los glifos en sus colores',
		})
	
	@objc.python_method
	def drawLayerInLabelColor( self, layer, alpha=0.67 ):
		try:
			# layer color:
			color = layer.colorObject
			if not color:
				# glyph color
				color = layer.parent.colorObject
			if color:
				color.colorWithAlphaComponent_(alpha).set()
				layer.completeBezierPath.fill()
		except Exception as e:
			self.logToConsole( "drawLayerInLabelColor: %s\n" % str(e) )
			import traceback
			print(traceback.format_exc())
	
	@objc.python_method
	def background(self, layer):
		self.drawLayerInLabelColor( layer )
	
	@objc.python_method
	def inactiveLayerBackground(self, layer):
		self.drawLayerInLabelColor( layer )
	
	@objc.python_method
	def preview(self, layer):
		self.drawLayerInLabelColor( layer, alpha=1.0 )

	def needsExtraMainOutlineDrawingForInactiveLayer_(self, layer):
		if not layer.colorObject and not layer.parent.colorObject:
			return True
		else:
			return False

	@objc.python_method
	def __file__(self):
		"""Please leave this method unchanged"""
		return __file__
