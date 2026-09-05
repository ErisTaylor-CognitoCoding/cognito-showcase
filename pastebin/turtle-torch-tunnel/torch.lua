-- torch: dig forward and place a torch every few blocks
-- Slot 1 = torches, fuel anywhere in slots 2-16

local length  = tonumber(({...})[1]) or 30
local spacing = tonumber(({...})[2]) or 8
local TORCH   = 1

local function refuel()
  if turtle.getFuelLevel() == "unlimited" then return true end
  if turtle.getFuelLevel() > 0 then return true end
  for i = 2, 16 do
    turtle.select(i)
    if turtle.refuel(1) then turtle.select(TORCH) return true end
  end
  print("Out of fuel")
  return false
end

local function forward()
  local tries = 0
  while turtle.detect() do
    turtle.dig()
    sleep(0.4)
    tries = tries + 1
    if tries > 40 then print("Stuck - bedrock?") return false end
  end
  while not turtle.forward() do
    turtle.attack()
    sleep(0.4)
  end
  return true
end

local function torch()
  turtle.select(TORCH)
  if turtle.getItemCount(TORCH) == 0 then
    print("Out of torches at block " .. length)
    return
  end
  -- face back down the tunnel: that space is air with solid floor,
  -- so the torch has something to stand on
  turtle.turnLeft()
  turtle.turnLeft()
  turtle.place()
  turtle.turnLeft()
  turtle.turnLeft()
end

print("Digging " .. length .. " blocks, torch every " .. spacing)

for i = 1, length do
  if not refuel() then break end
  if not forward() then break end
  if i % spacing == 0 then torch() end
end

print("Done.")
