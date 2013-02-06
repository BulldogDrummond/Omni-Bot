#######################################################################
# Trim trailing whitespace, set line end format to Win, optionally set 
# Debug to 0 and save. Committing to SVN does not work atm.
#######################################################################
import re
match0 = ""
msgBoxResult = MESSAGEBOXFLAGS.RESULTNO

def regExFunc( lineNum, match ):
	global match0
	match0 = match.group(0)
	# console.write( str(match0) )

editor.beginUndoAction()
notepad.menuCommand( MENUCOMMAND.EDIT_TRIMTRAILING )
editor.endUndoAction()

editor.beginUndoAction()
notepad.menuCommand( MENUCOMMAND.FORMAT_TODOS )
editor.endUndoAction()

editor.pysearch( "^\tDebug = true,\r$", regExFunc )
if match0 != "\tDebug = true,":
	editor.pysearch( "^\tDebug = [1-2],\r$", regExFunc )

if match0 != "":
	msgBoxResult = notepad.messageBox("Do you want to set Debug to 0?", "Confirmation", MESSAGEBOXFLAGS.YESNO )

if msgBoxResult == MESSAGEBOXFLAGS.RESULTYES:
	editor.beginUndoAction()
	editor.pyreplace( r"^\tDebug = true,\r$\n", "\tDebug = 0,\r\n", 1, Editor.INCLUDELINEENDINGS )
	editor.pyreplace( r"^\tDebug = [1-2],\r$\n", "\tDebug = 0,\r\n", 1, Editor.INCLUDELINEENDINGS )
	editor.endUndoAction()

notepad.save()
editor.setSavePoint()

# Committing to SVN does not work atm
# result = notepad.runPluginCommand( 'Subversion', 'Commit File', True )
# console.write( str(result) )