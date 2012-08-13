import mac_controls

xbox = {		repr("7A56B2D9\r\n"): mac_controls.contextual_menu,	# C
			repr("89DEE1B9\r\n"): mac_controls.fast_forward,		# F
			repr("BD0B58F5\r\n"): mac_controls.info,				# I
			repr("5A03C83E\r\n"): mac_controls.play,				# P
			repr("E8572B7A\r\n"): mac_controls.rewind,			# R
			repr("8F3A25F9\r\n"): mac_controls.shutdown,			# S
			repr("1CF35919\r\n"): mac_controls.subtitles,		# T
			repr("32A6223E\r\n"): mac_controls.stop,				# X
			repr("EAEBC955\r\n"): mac_controls.zoom,				# Z
			repr("BAD4D9DE\r\n"): mac_controls.pause,			# Space
			repr("DAF86EDD\r\n"): mac_controls.left,				# Left
			repr("BFA9B6DE\r\n"): mac_controls.right,			# Right
			repr("EEB21A42\r\n"): mac_controls.up,				# Up
			repr("A003A639\r\n"): mac_controls.down,				# Down
			repr("CEBCDBD9\r\n"): mac_controls.select,			# Enter
			repr("2EF93F1A\r\n"): mac_controls.back,				# Backspace
			repr("A11E6F9\r\n"): mac_controls.prev_menu,			# Esc
			repr("C5EF9F9\r\n"): mac_controls.skip_forward,		# . (period)
			repr("94DF0175\r\n"): mac_controls.skip_backward,	# , (comma)
			repr("F14FF65A\r\n"): mac_controls.vol_up,			# + (Plus)
			repr("39297135\r\n"): mac_controls.vol_down,			# - (Minus)
			repr("49641316\r\n"): mac_controls.next_chapter,		# ] (Right Bracket)
			repr("3E81CB71\r\n"): mac_controls.prev_chapter}		# [ (Left Bracket)

coby = {		repr("B08CB7DF\r\n"): mac_controls.audio_offset, 	# A
			repr("EE886D7F\r\n"): mac_controls.contextual_menu,	# C
			repr("E318261B\r\n"): mac_controls.fast_forward,		# F
			repr("E5CFBD7F\r\n"): mac_controls.info,				# I
			repr("3195A31F\r\n"): mac_controls.osd,				# M
			repr("8AB3679B\r\n"): mac_controls.rewind,			# R
			repr("13549BDF\r\n"): mac_controls.shutdown,			# S
			repr("97483BFB\r\n"): mac_controls.subtitles,		# T
			repr("1BC0157B\r\n"): mac_controls.stop,				# X
			repr("D7E84B1B\r\n"): mac_controls.zoom,				# Z
			repr("B953793F\r\n"): mac_controls.pause,			# Space
			repr("3D9AE3F7\r\n"): mac_controls.left,				# Left
			repr("35A9425F\r\n"): mac_controls.right,			# Right
			repr("F076C13B\r\n"): mac_controls.up,				# Up
			repr("F63C8657\r\n"): mac_controls.down,				# Down
			repr("52A3D41F\r\n"): mac_controls.select,			# Enter
			repr("AB91951F\r\n"): mac_controls.back,				# Backspace
			repr("5BE75E7F\r\n"): mac_controls.prev_menu,		# Esc
			repr("A6C4637B\r\n"): mac_controls.fullscreen,		# Tab
			repr("410109DB\r\n"): mac_controls.vol_up,			# + (Plus)
            repr("DC0197DB\r\n"): mac_controls.vol_down}			# - (Minus)

sunflower = {repr('DCC99F1F\r\n'): mac_controls.audio_offset, 	# A
			repr('E9C74319\r\n'): mac_controls.contextual_menu,	# C
			repr('66E97044\r\n'): mac_controls.fast_forward,		# F
			repr('4666CC0D\r\n'): mac_controls.info,				# I
			repr('19EB3488\r\n'): mac_controls.osd,				# M
			repr('70F06FB7\r\n'): mac_controls.now_playing,		# N
			repr('313599EC\r\n'): mac_controls.play,				# P
			repr('AE7CDBE\r\n'): mac_controls.queue,				# Q
			repr('FEF03E2C\r\n'): mac_controls.rewind,			# R
			repr('736ED82E\r\n'): mac_controls.shutdown,			# S
			repr('AC101205\r\n'): mac_controls.subtitles,		# T
			repr('D6599F48\r\n'): mac_controls.stop,				# X
			repr('E61D2DFB\r\n'): mac_controls.zoom,				# Z
			repr('D922D768\r\n'): mac_controls.pause,			# Space
			repr('9578646A\r\n'): mac_controls.left,				# Left
			repr('DC18602C\r\n'): mac_controls.right,			# Right
			repr('2C2E80FF\r\n'): mac_controls.up,				# Up
			repr('5A1A483D\r\n'): mac_controls.down,				# Down
			repr('603F1D32\r\n'): mac_controls.page_up,			# PageUp
			repr('9715433C\r\n'): mac_controls.page_down,		# PageDown
			repr('CB3CC07F\r\n'): mac_controls.select,			# Enter
			repr('E28725E3\r\n'): mac_controls.back,				# Backspace
			repr('2935B9A7\r\n'): mac_controls.prev_menu,		# Esc
			repr('3875B722\r\n'): mac_controls.skip_forward,		# . (period)
			repr('401C2B6C\r\n'): mac_controls.skip_backward,	# , (comma)
			repr('7A68C48\r\n'): mac_controls.small_step_back,	# " (quote)
			repr('FC67AFAE\r\n'): mac_controls.fullscreen,		# Tab
			repr('68733A46\r\n'): mac_controls.vol_up,			# + (Plus)
			repr('83B19366\r\n'): mac_controls.vol_down,			# - (Minus)
			repr('8A67822\r\n'): mac_controls.next_chapter,		# [ (Left Bracket)
			repr('FBACE420\r\n'): mac_controls.prev_chapter,		# ] (Right Bracket)
			repr('2340B922\r\n'): mac_controls.mute}				# Mute

CodeNames = {'Coby': coby, 'Xbox': xbox, 'Sunflower': sunflower}
