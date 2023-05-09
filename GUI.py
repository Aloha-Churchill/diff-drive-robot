#See the list of booleans that can integrate outputs/inputs & GUI: https://docs.google.com/document/d/1xmZqPb1MOA_h7leA5A_Wdnwz5-oBN6WWSsotBhpbr8M/edit?usp=sharing

from guizero import App, Text, error, TextBox, PushButton, Picture, info, yesno, ButtonGroup, Window
passed = False 
app = App(title = 'ROBO', width = 194*5, height = 110*5)
app.bg = '#D3ECF5'
app.text_size = 50
app.text_color = '#000000'

def authenticate():
  if password.value == 'password': #change password value here
    passed = True 
    password.hide()
    submit.hide()
    message.hide()
    info('Welcome', 'Indetification accpeted.')
    main_menu()
  else:
    error('Error', 'Your password is incorrect.')

def send_A_B():
  confirmAB = yesno('Confirm Route', 'Confirm route guidance from A to B')
  if confirmAB == True:
                    route_message1.show()
                    main_menu_hide()
                    pause.show()
                    #add command to start route guidance from A to B
  else: 
                    main_menu()
  
def send_B_A():
   confirmAB = yesno('Confirm Route', 'Confirm route guidance from B to A')
  if confirmAB == True:
                    route_message2.show()
                    main_menu_hide()
                    pause.show()
                    #add command to start route guidance from B to A
  else: 
                    main_menu()
  
def show_stats():
  main_menu_hide()
  trips.show()
  battery.show()
  status.show()
  back_to_menu.show()
  
def shut_down():
  main_menu_hide()
  shut_down_message.show()
  pause.show()
  #add command to power off robot
  
def main_menu():
  menu_header.show()
  Send_A_B.show()
  Shut_Down.show()
  Show_Stats.show()
  Shut_down.show()
  back_to_menu.hide()
  pause.hide()
  route_message1.hide()
  route_message2.hide()
  batttery.hide()
  status.hide()
  shut_down_message.hide()
  
def main_menu_hide()
  menu_header.hide()
  Send_A_B.hide()
  Send_B_A.hide()
  Shut_down.hide()
  Show_stats.hide()
  
#definitions
menu_header = Text(app, text = 'Menu', size =80, color = '#000000')
menu_header.hide()
Send_A_B = PushButton(app, command = send_A_B, text = 'Send on A to B') 
Send_A_B.bg = '#E6E6E6'
Send_A_B.hide()
Send_B_A = PushButton(app, command = send_B_A, text = 'Send on B to A')
Send_B_A.bg = '#D3D3D3'
Send_B_A.hide()
Show_Stats = PushButton(app, command = show_stats, text = 'View Stats')
Show_Stats.bg = '#0894FF'
Show_Stats.hide()
Shut_down = PushButton(app, command = shut_down, text = 'Shut Down')
Shut_down.bg = '#D3D3D3'
Shut_down.hide()
back_to_menu = PushButton(app, text = 'Main Menu', command = main_menu)
back_to_menu.bg = '#24A0ED'
back_to_menu.hide()
pause = PushButton(app, text = 'Pause', command = main_menu)  #create/replace command with pause fxn to pause the robot 
pause.bg = '#24A0ED'
pause.hide()

#messages/errors
low_batt_message = Text(app, text = 'LOW BATTERY') #not used add when battery <X, hide all other features or create pop up using info
low_batt_message.hide()
obst_message = Text(app, text = 'OBSTACLE DETECTED') #not used add when obst detected, hide all other features or create pop up using info
obst_message.hide()
route_message1 = Text(app, text = 'Navigating on route from A to B...')
route_message1.hide()
route_message2 = Text(app, text = 'Navigating on route from B to A...')
route_message2.hide()
trips = Text(app, text = 'Trips today: 21') #create/replace with trips fxn to count trips, store and display value
trips.hide()
battery = Text(app, text = 'Battery life: 75%') #create/replace with battery fxn to measure battery %, store and display value
battery.hide()
status = Text(app, text = 'Status: Paused') #create/replace with status fxn that updates value with current status
status.hide()
shut_down_message = Text(app, text = 'Shutting down...') 
shut_down_message.hide()

#authentication
message = Text(app, text = 'Sign In', size = 80, color = '#000000')
password = TextBox(app, hide_text = True, visible = True)
submit = PushButton(app, enabled = True, command = authenticate, text = 'Submit'
submit.bg = '#24A0ED'

app.display()
