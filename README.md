# ShowGlyphsInLabelColor.glyphsReporter

This is a plugin for the [Glyphs font editor](http://glyphsapp.com/) by Georg Seifert.
It displays glyphs in Edit View in their respective label color. 
After installation, it will add the menu item *View > Show Glyphs in Label Color*.
You can set a keyboard shortcut in System Preferences.

![Glyphs are shown in their label colors.](ShowGlyphsInLabelColor.png "Show Glyphs in Label Color Screenshot")

### Installation

Go to *Window > Plugin Manager,* search for *ShowGlyphsInLabelColor,* click on the *Install* button and restart Glyphs.

### Usage Instructions

1. Open one or more glyphs in Edit View.
2. Use *View > Show Glyphs in Label Color* to toggle the display of glyphs in their respective label colors.

### Requirements

The plugin needs Glyphs 2.3.1 or higher, running on OS X 10.9.5 or later. I can only test it in current OS versions, and I assume it will not work in older versions.

For older app versions, there is an unmaintained plug-in marked with `.OLD` in the file name. Note that it works slightly differently. It only colors the backgrounds, so you may need to turn off *View > Fill Preview* if you also want to see inactive glyphs in their label color. If the old plug-in does not work for you, you will have to fix it yourself or leave it. I am only maintaining the code of the current version anymore. Thank you for your understanding.

### License

Copyright 2014 Rainer Erich Scheichelbauer (@mekkablue).
Based on sample code by Georg Seifert (@schriftgestalt).

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

http://www.apache.org/licenses/LICENSE-2.0

See the License file included in this repository for further details.
