from tealight.logo import move, turn, color

def spiral(size):
  
  if size > 300:
    return
  
  color("RGB(255,102,0)")
  move(size)
  turn(120)
  spiral(size + 8)
  
  
spiral(30)