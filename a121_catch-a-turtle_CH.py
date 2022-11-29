# a121_catch_a_turtle.py
#-----import statements-----
import turtle
import random
import leaderboard as lb
#-----game configuration----
shapefillcolor = 'blue'
shapesize = 5
shape = 'circle'
shape_color = ''
shape_colors = ['orange','lime','green','blue','purple']
shape_sizes = [7,6,5,4.5,4,3.5,3,2.5,2,1.5,1]
score = 0
highscores = []
font_setup = ("Arial", 20, "normal")
game_started = False
#-----countdown variables-----
timer = 5
counter_interval = 1000
timer_up = False
# initialize and define leaderbaord
leaderboard_file_name = 'leaderboard.txt'
player_name = input('Welcome! Please enter your name: ')
#-----initialize turtle-----
plr = turtle.Turtle()
plr.penup()
plr.fillcolor(shapefillcolor)
plr.shapesize(shapesize)
plr.shape(shape)
turtle.bgcolor("aqua")
#-----score writer----------
score_writer = turtle.Turtle()
score_writer.hideturtle()
score_writer.penup()
score_writer.goto(-250,200)
#-----timer writer----------
counter = turtle.Turtle()
counter.hideturtle()
counter.penup()
counter.goto(-250,170)
counter.write("Click the screen to start.", font=font_setup)

#-----game functions--------
def replace_key(string,replace):
  for letter in string[::1]:
    if letter == replace:
      letter.replace(str(replace),'')
  return string
def change_pos():
  plr.hideturtle()
  spotxcor = random.randint(-250,250)
  spotycor = random.randint(-250,250)
  while spotxcor > 15 and spotycor > 125:
    spotxcor = random.randint(-250,250)
    spotycor = random.randint(-250,250)
  plr.goto(spotxcor,spotycor)
  plr.shapesize(random.choice(shape_sizes))
  plr.color(random.choice(shape_colors))
  plr.showturtle()
def update_score():
  global score 
  global plr
  global shape_sizes
  global shape_color
  global shape_colors
  score = int(score)
  score = score + 1
  score = str(score)
  current_score = str('Current Score: ' + score)
  score_writer.clear()
  score_writer.write(current_score, font=font_setup)
def countdown():
  global timer, timer_up
  counter.clear()
  if timer <= 0:
    counter.write("Time's Up", font=font_setup)
    timer_up = True
    manage_leaderboard()
  else:
    counter.write("Timer: " + str(timer), font=font_setup)
    timer -= 1
    counter.getscreen().ontimer(countdown, counter_interval) 
def plr_clicked(x,y):
  global game_started
  global timer_up
  global plr
  if game_started == False: 
    update_score()
    change_pos()
    game_started = True
  else:
    global timer_up
    if timer_up == False:
      update_score()
      change_pos()
    else:
      plr.hideturtle()
def manage_leaderboard():
  global score
  global spot
  # get the names and scores from the leaderboard file
  leader_names_list = lb.get_names(leaderboard_file_name)
  leader_scores_list = lb.get_scores(leaderboard_file_name)
  # show the leaderboard with or without the current player
  if (len(leader_scores_list) < 5 or score >= leader_scores_list[4]):
    lb.update_leaderboard(leaderboard_file_name, leader_names_list, leader_scores_list, player_name, score)
    lb.draw_leaderboard(True, leader_names_list, leader_scores_list, score_writer, score)
  else:
    lb.draw_leaderboard(False, leader_names_list, leader_scores_list, spot, score)
#-----events----------------
wn = turtle.Screen()
wn.ontimer(countdown, counter_interval)
plr.onclick(plr_clicked)
wn.mainloop()