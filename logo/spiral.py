from tealight.logo import move, turn

def spiral(size):
  
  if size > 300:
    return
  
  move(size)
  turn(70)
  spiral(size + 9)
  
  
spiral(6