#Changes the default roblox cursors to be the ones that you would like.
#place your own cursors into .\Custom.
#To come later:
# -Ability to check director
import shutil
import os
versionfolder = os.environ['USERPROFILE']+"\AppData\Local\Roblox\Versions"
new_cursor_file = "\content\\textures\Cursors\KeyboardMouse"
custom_cursors = ".\Cursors"
Options = {
    "Old": ".\OldCursors",
    "New": ".\\NewCursors",
    "Classic": ".\Classic",
    "Custom": ".\Custom",
}
def main():
    if True: #Later-Check to see what operating system the user is using. Add Mac Support.
        print("Avaiable Options:\n • 'New': Roblox's new cursors\n • 'Old': Roblox's old cursors\n • 'Classic': Roblox's classic cursors\n • 'Custom': Your own preset\nOr enter an directory.")
        startdir = input("> ")
        startdir = startdir[0].upper() + startdir[1:].lower()
        cursor_dir = Options["New"]
        if (startdir in Options.keys()):
            cursor_dir = Options[startdir]
        elif (os.path.isdir(startdir)):
            cursor_dir = startdir
        else:
            print("Invalid option, using 'New' as default.")
        files = os.listdir(versionfolder)
        for f in files:
            full_file = versionfolder+"\\"+f
            if os.path.isdir(full_file):
                new_cursors = os.listdir(cursor_dir)
                for f1 in new_cursors:
                    shutil.copy(cursor_dir+"\\"+f1, full_file+new_cursor_file+"\\"+f1)   
        print("Operation complete")



if __name__ == "__main__":
    main()