import os, serial


# Audio Offset (Audio Button)
def audio_offset():
	os.system("""osascript -e 'tell application "System Events" to keystroke "a"'""")

# Contextual Menu (Setup Button)
def contextual_menu():
	os.system("""osascript -e 'tell application "System Events" to keystroke "c"'""")

# Fast Forward
def fast_forward():
	os.system("""osascript -e 'tell application "System Events" to keystroke "f"'""")

# Info (Title)
def info():
	os.system("""osascript -e 'tell application "System Events" to keystroke "i"'""")

#Next Subtitle
def next_subtitle():
	os.system("""osascript -e 'tell application "System Events" to keystroke "n"'""")

# OSD (Player Controls)
def osd():
	os.system("""osascript -e 'tell application "System Events" to keystroke "m"'""")

# Now playing
def now_playing():
	os.system("""osascript -e 'tell application "System Events" to keystroke "n"'""")

#CPU Usage/Codec
def cpu_usage():
	os.system("""osascript -e 'tell application "System Events" to keystroke "o"'""")

# Play
def play():
	os.system("""osascript -e 'tell application "System Events" to keystroke "p"'""")

# Queue
def queue():
	os.system("""osascript -e 'tell application "System Events" to keystroke "q"'""")

# Rewind
def rewind():
	os.system("""osascript -e 'tell application "System Events" to keystroke "r"'""")

# Shutdown Menu (Power Button)
def shutdown():
	os.system("""osascript -e 'tell application "System Events" to keystroke "s"'""")

# Toggle Subtitles On/Off
def subtitles():
	os.system("""osascript -e 'tell application "System Events" to keystroke "t"'""")

# Visualization settings
def visual_settings():
	os.system("""osascript -e 'tell application "System Events" to keystroke "v"'""")
	
# Mark as Watched/Unwatched
def watched():
	os.system("""osascript -e 'tell application "System Events" to keystroke "w"'""")

# Stop
def stop():
	os.system("""osascript -e 'tell application "System Events" to keystroke "x"'""")

# Zoom/Aspect Ratio
def zoom():
	os.system("""osascript -e 'tell application "System Events" to keystroke "z"'""")

# Play\Pause	
def pause():
	os.system("""osascript -e 'tell application "System Events" to key code 49'""")

# Left
def left():
	os.system("""osascript -e 'tell application "System Events" to key code 123'""")

# Right
def right():
	os.system("""osascript -e 'tell application "System Events" to key code 124'""")

# Up
def up():
	os.system("""osascript -e 'tell application "System Events" to key code 126'""")

# Down
def down():
	os.system("""osascript -e 'tell application "System Events" to key code 125'""")

# Page Up
def page_up():
	os.system("""osascript -e 'tell application "System Events" to key code 116'""")

# Page Down
def page_down():
	os.system("""osascript -e 'tell application "System Events" to key code 121'""")

# Enter
def select():
	os.system("""osascript -e 'tell application "System Events" to keystroke "\r"'""")

# Back/Backspace (Repeat Button)
def back():
	os.system("""osascript -e 'tell application "System Events" to key code 36'""")

# Previous Menu/Esc (Menu Button)
def prev_menu():
	os.system("""osascript -e 'tell application "System Events" to key code 53'""")

# Skip Forward
def skip_forward():
	os.system("""osascript -e 'tell application "System Events" to keystroke "."'""")

# Skip Backward
def skip_backward():
	os.system("""osascript -e 'tell application "System Events" to keystroke ","'""")

# Small step back (7s)
def small_step_back():
	os.system("""osascript -e 'tell application "System Events" to key code 39'""")

# Fullscreen Mode (Angle Button)
def fullscreen():
	os.system("""osascript -e 'tell application "System Events" to key code 48'""")

# Vol+
def vol_up():
	os.system("""osascript -e 'tell application "System Events" to keystroke "="'""")

# Vol-
def vol_down():
	os.system("""osascript -e 'tell application "System Events" to keystroke "-"'""")

# Windowed Mode
def windowed():
	os.system("""osascript -e 'tell application "System Events" to keystroke "\"'""")

# Next Chapter
def next_chapter():
	os.system("""osascript -e 'tell application "System Events" to keystroke "]"'""")

# Prev Chapter
def prev_chapter():
	os.system("""osascript -e 'tell application "System Events" to keystroke "["'""")
	
# Mute
def mute():
	os.system("""osascript -e 'tell application "System Events" to keystroke "mute"'""")
