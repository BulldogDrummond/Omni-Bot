Introduction: Notepad++ for Omni-bot
====================================

This is a portable distribution of Notepad++ version 6.3 as available
from http://notepad-plus-plus.org that includes some customizations for
use with Omni-bot 0.8+.

"Portable distribution" means that no changes will be made to your
registry, and the settings of existing installations of Notepad++ you may
already have on your computer will be left alone. It can be run from
portable media—such as USB drives—without installation.

Notepad++ is a free Windows-based source code editor distributed under
the GPL License (see included license.txt file). It is developed and
maintained by the people listed here: http://notepad-plus-plus.org/members

The core Notepad++ files and plugins that come with this distribution
are unchanged and provided "as is" in accordance with the terms detailed
in the included license files. The copyright remains with the respective
authors.


Omni-bot Extensions/Customizations
==================================

Some extensions are provided in the package for the convenience of Omni-bot
users:

- Omni-bot.chm script help file (note that this is a bit dated)
- Customized syntax highlighting for GM files
- Customized TagsView settings for GM files
- Auto-completion for GM files
- QuickText shortcuts (see below)
- gmCompiler.exe (see below)


Minor Caveat About Localizations
================================

Please note that the included localizations may or may not work with Notepad++.
If the menu structure of your Notepad++ installation seems corrupted after
switching to a localization, close Notepad++, delete the file nativeLang.xml
in the Notepad++ directory, and start over again.


Useful Keyboard Shortcuts
=========================

Fast editing/clipboard
	Ctrl+,: Move cursor to the previous change in capitalization
	Ctrl+Shift+,: Select up to the previous change in capitalization
	Ctrl+.: Move cursor to the next change in capitalization
	Ctrl+Shift+.: Select up to the next change in capitalization
	Ctrl+C: Copy to clipboard
	Ctrl+Shift+C: Append selection to clipboard (append-copy)
	Ctrl+X: Cut
	Ctrl+Shift+X: Append selection to clipboard & delete (append-cut)
	Ctrl+Shift+V: View extended clipboard content (plugin)
	Ctrl+Down: Move current line down
	Ctrl+Up: Move current line up
	Ctrl+D: Duplicate current line/selection
	Ctrl+Shift+D: Copy current line
	Ctrl+Shift+L: Cut current line
	Ctrl+L: Delete current line

Bookmarks
	Ctrl+F2: Set/unset bookmark (same as left-click on margin)
	F2: Go to next bookmark
	Shift+F2: Go to previous bookmark

Coding
	Ctrl+Q: Comment/uncomment selected lines (toggle)
	Ctrl+K: Comment selected lines
	Ctrl+Shift+K: Uncomment selected lines
	Alt+I: Indent selected lines and surround with curly braces
	Ctrl+T: Trim trailing whitespace
	Alt+Shift+S: Trim trailing whitespace and save (macro)
	Ctrl+B: Jump to matching brace
	Ctrl+Shift+B: Select to matching brace
	Ctrl+Shift+Up: Mark current word or find backward
	Ctrl+Shift+Down: Mark current word or find forward

Auto-completion
	Ctrl+J: Word auto-completion (based on words in currently opened file)
	Ctrl+Space: Function auto-completion
	Ctrl+Shift+Space: Show function parameters/help

Omni-bot/GM specific
	Ctrl+F9: Send current file to gmCompiler.exe
	Alt+F1: Search for current word in Omni-bot Wiki (Internet access required)
	Ctrl+F1: Search for current word in included Omni-bot.chm

QuickText
	In addition to keyboard shortcuts in the usual sense, a lot of
	abbreviations are configured in the file QuickText.ini (included in
	the download). Substitution of the abbreviations is triggered by the
	shortcut Ctrl+Enter. Refer to section [15] of the QuickText.ini file
	for a list of preconfigured abbreviations.
	Example: Type "ie" and press Ctrl+Enter three times.


Web Sites
=========

Notepad++ official site:
	http://notepad-plus-plus.org

Notepad++ project site:
	http://sourceforge.net/projects/notepad-plus

Notepad++ Wiki:
	http://sourceforge.net/apps/mediawiki/notepad-plus

Notepad++ support:
	http://sourceforge.net/projects/notepad-plus/support

Notepad++ channel:
	irc://irc.freenode.net:6667/notepad++

Omni-bot official site:
	http://www.omni-bot.com

Omni-bot Wiki:
	http://www.omni-bot.com/wiki
