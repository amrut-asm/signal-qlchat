from pydbus import SystemBus
import minqlx

bus = SystemBus()
signal = bus.get('org.asamk.Signal', '/org/asamk/Signal/_<insert phone number here>')

class signal_write(minqlx.Plugin):

	def __init__ (self):
		super().__init__()
		self.add_hook("chat", self.chat_handler)

	def chat_handler(self, player, msg, channel):
		if not msg.startswith("!s "):
			return
		mod_name = player.name[:-2]
		mod_msg  = msg[3:]
		payload_string = mod_name+": "+mod_msg
		self.push_message(payload_string)

	@minqlx.thread
	def push_message(self, final_payload):
		id = <insert group id here (a byte array like [4, 5, ...])>
		try:
			signal.sendGroupMessage(final_payload, [], id)
		except:
			minqlx.log_exception()
