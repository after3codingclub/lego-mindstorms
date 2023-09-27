import turtle
t = turtle.Turtle()
t.speed(5) # 1:slowest, 3:slow, 5:normal, 10:fast, 0:fastest
t.color("dark orchid")

colors=[ "yellow", "gold", "orange", "red", "maroon", "violet", "magenta", "purple", "navy", "blue", "skyblue", "cyan", "turquoise", "lightgreen", "green", "darkgreen", "chocolate", "brown", "black", "gray", "white"]

def shape():
  t.circle(45)
  t.right(23)
 
i = 0
while i < 500:
  for c in colors:
    shape()
    t.color(c)
    i+=1


# import turtle
# t = turtle.Turtle()
# t.speed(0) # 1:slowest, 3:slow, 5:normal, 10:fast, 0:fastest
# t.color("dark orchid")
# d = 0
# i = 0

# colors=[ "yellow", "gold", "orange", "red", "maroon", "violet", "magenta", "purple", "navy", "blue", "skyblue", "cyan", "turquoise", "lightgreen", "green", "darkgreen", "chocolate", "brown", "black", "gray", "white"]

# def shape(d):
#   t.circle(d)
#   t.right(23)
  
# while i < 500:
#   for c in colors:
#     shape(d+i/5)
#     t.color(c)
#     i+=1

  
