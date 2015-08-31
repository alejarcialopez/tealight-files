from tealight.logo import move, turn

def spiral(size):
  
  if size > 300:
    return
  
  move(size)
  turn(120)
  spiral(size + 1)
  
  
spiral(30)