-- hacker: turtle lays the perimeter desk ring
-- Run:  hacker <length> <width>     (default 330 120)
-- Setup: sit the turtle on the START CORNER, facing ALONG the long wall,
--        at the height you want the desk row. Desk blocks in slot 1,
--        coal/fuel in slot 16.
local a = {...}
local L = tonumber(a[1]) or 330
local W = tonumber(a[2]) or 120

local function fuel()
  if turtle.getFuelLevel() > 10 then return end
  turtle.select(16)
  turtle.refuel(1)
  turtle.select(1)
end

-- lay n desks along a wall, ending ON the far corner block
local function lay(n)
  for i = 1, n do
    fuel()
    turtle.select(1)
    turtle.digDown()      -- clear whatever's there
    turtle.placeDown()    -- drop the desk
    if i < n then
      if not turtle.forward() then
        turtle.dig()       -- something in the way
        turtle.forward()
      end
    end
  end
end

-- walk all four walls; corners overlap by one block (harmless, guarantees no gap)
lay(L); turtle.turnRight()
lay(W); turtle.turnRight()
lay(L); turtle.turnRight()
lay(W)

print("Desk ring done: " .. L .. " x " .. W)