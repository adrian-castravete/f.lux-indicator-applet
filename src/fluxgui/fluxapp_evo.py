# =========================================================
# Copyright: (c) 2015 Katharina Sabel
# License  : LGPL 3.0 (See LICENSE)
# Comment  : Main body file of the QT flux indicator applet
#			 rewritten from the ashes of the old shit.
# =========================================================

# class FluxGUIEvo(object):

# 	''' Initialises the fluxgui and terminates the old process if neccesary '''
# 	def __init__(self):
# 		self.pidfile = os.path.expanduser("~/.fluxgui_evo.pid")
# 		self.check_pid()

# 	def check_pid(self):
# 		pid = os.getpid()

# 		running = False # Innocent...
# 		if os.path.isfile(self.pidfile):
# 			try:
# 				oldpid = int(open(self.pidfile).readline().rstrip())
# 				try:
# 					os.kill(oldpid, 0)
# 					running = True # ...until proven guilty
# 				except OSError as err:
# 					if err.errno == errno.ESRCH:
# 						# OSError: [Errno 3] No such process
# 						print "stale pidfile, old pid: ", oldpid
# 			except ValueError:
# 				# Corrupt pidfile, empty or not an int on first line
# 				pass
# 		if running:
# 			print "fluxgui is already running, exiting"
# 			sys.exit()
# 		else:
# 			file(self.pidfile, 'w').write("%d\n" % pid)

# 	def run(self):
# 		pass

# 	def exit(self):
# 		pass

# 	def signal_exit(self):
# 		pass


# if __name__ == '__main__':
# 	try:
# 		app = FluxGUIEvo()
# 		signal.signal(signal.SIGTERM, app.signal_exit)
# 		app.run()
# 	except KeyboardInterrupt:
# 		app.exit()

import sys
 
# Importing the necessary Qt classes.
 
from PyQt4.QtGui import QLabel, QApplication
 
# We use the from foo import * syntax here because
# all of Qt's objects begin with a Q
# and thus we shouldn't run into namespace problems.

if __name__=='__main__':
	App = QApplication(sys.argv)

	# All Qt programs need an
	# QApplication instance.

	# We pass the sys.argv as its arguments
	# because Qt is adept at handling some
	# of the default command-line options
	# like style, size, etc by itself.

	Label = QLabel( "Hello World!" )
	
	# QLabel is the class providing a
	# simple label

	Label.show()

	# Like in most GUI toolkits, we have
	# to manually set it to show

	App.exec_()

	# Notice the _ after exec, this is to
	# avoid the confusion with Python's
	# exec() built-in-function

	# exec_() starts the main application
	# loop. Something like main() of other
	# toolkits.