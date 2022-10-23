#simple python program to plant trees for you :)

#if you are running this program on a cloud or if your pc is on 24/7, you can comment line 18 and
#.. uncomment the lines below to automatically open the browser every 24 hours.

import webbrowser   

count = 0

def open():
    global count
    count+=1
    urL= "https://www.msn.com/en-xl/weather/forecast/"
    edge_path="C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe" #change this if you have altered your browser's path.
    webbrowser.register('edge', None,webbrowser.BackgroundBrowser(edge_path))
    webbrowser.get('edge').open_new_tab(urL)
    print(f"opened {count} times")
open()

#task open() every day

# import sched
# import time
# s = sched.scheduler(time.time, time.sleep)
# def do_something(sc):  # argument is a reference to the scheduler instance
#     open()
#     s.enter(86400, 1, do_something, (sc,)) #86400 is one day in seconds
# s.enter(0, 1, do_something, (s,))
# s.run()