-- file: sleep
-- block to place goes in slot 1
-- coal in slot 16
turtle.select(1)

os.sleep(5)

for i = 1, 5 do
  turtle.forward()
end
os.sleep(1)

for i = 1, 5 do
  turtle.place()
  turtle.up()
end
os.sleep(1)

for i = 1, 5 do
  turtle.digDown()
  turtle.forward()
end
os.sleep(1)

for i = 1, 5 do
  turtle.up()
end
os.sleep(3)

for i = 1, 5 do
    turtle.down()
end
