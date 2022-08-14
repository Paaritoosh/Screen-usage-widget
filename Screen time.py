import os
import rumps
import subprocess

class Screen_time(rumps.App):
    def __init__(self):
        super(Screen_time, self).__init__("Screen Time")
        self.menu = ["Usage","Quit","Clean Quit"]
        self._quit_button =None

    @rumps.clicked("Usage")
    def prefs(self,_):
        subprocess.run("open /System/Library/PreferencePanes/Screentime.prefPane",shell=True)

    @rumps.clicked('Quit')
    def clean_up_before_quit(self,_):
        To_close_System_prefrences = """osascript -e '

        tell application "System Preferences"
	        quit
        end tell

        '"""
        os.system(To_close_System_prefrences)

    @rumps.clicked('Clean Quit')
    def quit_Screen_time(self,_):
        rumps.quit_application()

if __name__ == "__main__":
    Screen_time().run()