-- file: program
-- orange block in slot 1 (need 20)
-- coal in slot 16, fuel 21

local SIDE = 5

turtle.select(1)
turtle.up()

for side = 1, 4 do
  for i = 1, SIDE do
    turtle.placeDown()
    turtle.forward()
  end
  turtle.turnRight()
end
