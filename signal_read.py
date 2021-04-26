import minqlx
from pydbus import SystemBus
from gi.repository import GLib

bus = SystemBus()
loop = GLib.MainLoop()
signal = bus.get('org.asamk.Signal', '/org/asamk/Signal/_<insert phone number here>')

class signal_read(minqlx.Plugin):

	def __init__(self):
		super().__init__()
		global signal
		signal.onMessageReceived = self.msgRcv
		self.add_hook("unload", self.handle_unload)
		self.start_loop()

	def handle_unload(self, plugin):
		if plugin == self.__class__.__name__:
			loop.quit()
			global signal
			signal.onMessageReceived = None

	@minqlx.thread
	def start_loop(self):
		loop.run()

	def msgRcv(self, timestamp, source, groupID, message, attachments):
		if groupID == []:
			return
		try:
			group_name = signal.getGroupName(groupID)
		except:
			minqlx.log_exception()
			return
		if group_name != "<insert group name here":
			return
		if (not message.startswith(".s ")) and (not message.startswith(".sa ")):
			return
		mod_message = message[3:]
		mod_message = mod_message.split("\n",1)[0]
		mod_message = mod_message[:150]
		try:
			mod_name = signal.getContactName(source)
		except:
			minqlx.log_exception()
			signal.sendGroupMessage("Exception: Couldn't send message! Try using !sa command (anonymous)", [], groupID)
			return
		if message.startswith(".sa "):
			payload_string = mod_message
			self.msg("^5(Signal Anonymous):"+payload_string)
		else :
			payload_string = mod_name+": "+mod_message
			self.msg("^5(Signal) "+payload_string)
