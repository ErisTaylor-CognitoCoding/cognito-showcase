-- drill.lua -- 2 wide x 3 high tunnel
-- Start at the BOTTOM LEFT of the face, facing the wall.
-- Fuel anywhere in the inventory. Usage: drill 30

local len = tonumber(({...})[1]) or 10

local function fuel(need)
  if turtle.getFuelLevel() == "unlimited" then return true end
  if turtle.getFuelLevel() >= need then return true end
  for s = 1, 16 do
    turtle.select(s)
    if turtle.refuel(1) then turtle.select(1) return true end
  end
  turtle.select(1)
  return false
end

local function fwd()
  while turtle.detect() do turtle.dig() end
  while not turtle.forward() do turtle.dig() end
end

local function up()
  while turtle.detectUp() do turtle.digUp() end
  while not turtle.up() do turtle.digUp() end
end

local function dn()
  while turtle.detectDown() do turtle.digDown() end
  while not turtle.down() do turtle.digDown() end
end

local side = "right"

for i = 1, len do
  if not fuel(8) then print("Out of fuel at block " .. i) return end
  fwd()
  up() up()
  if side == "right" then turtle.turnRight() else turtle.turnLeft() end
  fwd()
  if side == "right" then turtle.turnLeft() else turtle.turnRight() end
  dn() dn()
  side = (side == "right") and "left" or "right"
end

print("Done " .. len .. " blocks.")
