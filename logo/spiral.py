from tealight.logo import move, turn, color

def spiral(size):
  
  if size > 300:
    return
  
  color(3)
  move(size)
  turn(60)
  spiral(size + 1)
  
  
spiral(30)