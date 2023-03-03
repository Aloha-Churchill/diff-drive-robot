from guizero import App, Text, error, TextBox, PushButtonm, Picture, info, ButtonGroup, Window
passed = False 
app = App(title = 'ROBO', width = 194*5, height = 110*5)
app.bg = 'yellow'

def authenticate():
  if password.value == 'password':
    passed = True 
    password.hide()
    submit.hide()
    message.hide()
    info('Welcome', 'Indetification accpeted.')
    main_menu()
  else:
    error('Error', 'Your password is incorrect.')

def send_A_B:
  route_message.show()
  main_menu_hide()
  back_to_menu.show()
  
def show_stats():
  main_menu_hide()
  stats.show()
  back_to_menu.show()
  
def shut_down():
  main_menu_hide()
  shut_down_message.show()
  back_to_menu.show()
  
def main_menu():
  menu_header.show()
  Send_A_B.show()
  Shut_Down.show()
  back_to_menu.hide()
  route_message.hide()
  stats.hide()
  shut_down_message.hide()
  
def main_menu_hide()
  menu_header.hide()
  Send_A_B.hide()
  Shut_down.hide()
  Show_Stats.hide()
  
#definitions#
menu_header = Text(app, text = 'menu')
menu_header.hide()
Send_A_B = PushButton(app, command = send_A_B, text = 'Send on A to B')
Send_A_B.hide()
Show_Stats = PushButton(app, command = show_stats, text = 'Show Stats')
Show_Stats.hide()
route_message = Text(app, text = 'ON ROUTE FROM A TO B')
route_message.hide()
stats = Text(app, text = 'SEUDO STATS') #will need to create a function to get appropriate stats
stats.hide()
shut_down_message = Text(app, text = 'Shutting down...')
shut_down_message.hide()
back_to_menu = PushButton(app, text = 'Back to Main Menu', command = main_menu)
back_to_menu.hide()

message = Text(app, text = 'surprise SHAWTY', size = 30)
password = TextBox(app, hide_text = True, visible = True, width = 20)
submit = PushButton(app, enabled = True, command = authenticate, text = 'submit', height = 1, width = 6)

app.display()
  
