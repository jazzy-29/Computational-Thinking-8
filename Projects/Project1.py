###############################################
### SETUP ###
import codesters
from codesters import StageClass
stage = StageClass()
###############################################
stage.set_background("flowers")

q1= codesters.Square(100, 100, 175, 'RoyalBlue')
q1= codesters.Square(-100, 100, 175, 'CornflowerBlue')
q1= codesters.Square(-100, -100, 175, 'RoyalBlue')
q1= codesters.Square(100, -100, 175, 'CornflowerBlue')

s1= codesters.Sprite("Volleyball", 100, 100)
s2= codesters.Sprite("Headphones", -100, -100)
s2.set_size(0.5) 
s3= codesters.Sprite("Outline", -100, 100)
s3.set_size(0.4)
s4= codesters.Sprite("Blue disco", 100, -100)
s4.set_size(0.6)

message1= codesters.Text("BY JAZZY AWIL")
message2= codesters.Text("Have a nice day!", 0,-220)
