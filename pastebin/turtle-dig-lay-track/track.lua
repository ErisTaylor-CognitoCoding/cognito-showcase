-- track.lua : dig a tunnel and lay rail behind
-- slot 1 = rails, slots 2-16 = coal

local args = { ... }
local n = tonumber(args[1]) or 20

local function refuel()
  if turtle.getFuelLevel() == "unlimited" then return end
  if turtle.getFuelLevel() > 10 then return end
  for s = 2, 16 do
    turtle.select(s)
    if turtle.refuel(1) then turtle.select(1) return end
  end
  turtle.select(1)
  print("Out of fuel - put coal in slots 2-16")
end

local function digTo(dig, detect, move)
  while detect() do
    dig()
    sleep(0.4) -- gravel / sand
  end
  return move()
end

-- get to head height so we can lay rail on the original floor
digTo(turtle.digUp, turtle.detectUp, turtle.up)

for i = 1, n do
  refuel()
  if not digTo(turtle.dig, turtle.detect, turtle.forward) then
    print("Blocked at block " .. i)
    break
  end
  while turtle.detectDown() do turtle.digDown() end
  turtle.select(1)
  if not turtle.placeDown() then
    print("Out of rails at block " .. i)
    break
  end
end

digTo(turtle.digDown, turtle.detectDown, turtle.down)
print("Done.")
