-- track.lua  -- dig forward, lay rail behind/below as it goes
-- Slot 1 = rails. Coal/fuel anywhere in slots 2-16.
-- Usage: track 30

local length = tonumber(({...})[1]) or 20

local function refuel()
  if turtle.getFuelLevel() > 5 then return true end
  for s = 2, 16 do
    turtle.select(s)
    if turtle.refuel(1) then turtle.select(1) return true end
  end
  turtle.select(1)
  print("Out of fuel - put coal in slots 2-16")
  return false
end

local function fwd()
  while not turtle.forward() do
    turtle.dig()
    sleep(0.2)
  end
end

-- lift to head height so the rail can sit on the original floor
turtle.digUp()
if not turtle.up() then print("No room above") return end

for i = 1, length do
  if not refuel() then return end
  turtle.dig()
  fwd()
  turtle.digDown()
  turtle.select(1)
  if not turtle.placeDown() then
    print("No rails left at block " .. i)
    return
  end
end

turtle.down()
print("Laid " .. length .. " track")
