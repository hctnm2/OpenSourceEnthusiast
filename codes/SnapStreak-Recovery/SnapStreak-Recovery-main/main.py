import npyscreen
import os

with open("credentials.txt", "r") as f:
    data = f.readlines()
    friendsTemp = data[15:-1]
    friends= []
    for i in friendsTemp:
        if i != "\n":
            friends.append(i.split("\n")[0])

class StreakApp(npyscreen.NPSApp):
    def main(self):
        global selection
        F = npyscreen.Form(name = "Welcome to SnapStreak-Recovery",)
        ms2 = F.add(npyscreen.TitleMultiSelect, max_height =-2, value = [], name="Pick your friends with whom you want to recover your streaks",
                values = [i for i in friends], scroll_exit=True)
        F.edit()
        selection = ms2.get_selected_objects()

    def filer(self):
        with open('driver.py', 'r') as original:
            data = original.read()
        for i in range(len(selection)):
            with open(f'execute{i+1}.py', 'w') as modified:
                modified.write(f"friend = '{selection[i].split('=')[1]}'\n" + data)
                
    def executer(self):
        for i in range(len(selection)):
            # exec(open(f'execute{i+1}.py').read())
            os.system(f'python execute{i+1}.py')


if __name__ == "__main__":
    App = StreakApp()
    App.run()
    App.filer()
    App.executer()
