# encoding: utf-8

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

	def settings(self):
		self.menuName = Glyphs.localize({
			'en': u'Glyphs in their Label Colors', 
			'de': u'Glyphen in ihrer Etikettenfarbe'
		})
	
	def drawLayerInLabelColor( self, layer ):
		try:
			color = layer.colorObject
			if not color:
				color = layer.parent.colorObject
			if color:
				color.set()
				layer.completeBezierPath.fill()
				return True
			else:
				return False
		except Exception as e:
			self.logToConsole( "drawLayerInLabelColor: %s\n" % str(e) )
			import traceback
			print traceback.format_exc()

	def background(self, layer):
		if not self.drawLayerInLabelColor( layer ):
			pass
	
	def inactiveLayers(self, layer):
		print self.drawLayerInLabelColor( layer )

	def needsExtraMainOutlineDrawingForInactiveLayer_(self, layer):
		if not layer.colorObject and not layer.parent.colorObject:
			return True
		else:
			return False
