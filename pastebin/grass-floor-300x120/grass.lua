-- Grass floor: solid fill 300 x 120, snake pattern, WITH RESUME.
-- Turtle sits ON TOP, one level above the floor line, facing along the 300 side.
-- Grass blocks in slots 1-15. Coal (fuel) in slot 16.
-- Fills EVERY tile (no gaps). 36,000 tiles total.
-- Rerun after a stop/refill and it continues from where it left off.

local LEN, WID = 300, 120
local PROG = "grass_progress"

-- how many tiles already placed on earlier runs
local done = 0
if fs.exists(PROG) then
  local h = fs.open(PROG, "r")
  done = tonumber(h.readAll()) or 0
  h.close()
end

local step = 0

local function save()
  local h = fs.open(PROG, "w")
  h.write(tostring(step))
  h.close()
end

local function fuelCheck()
  if turtle.getFuelLevel() ~= "unlimited" and turtle.getFuelLevel() < 40 then
    turtle.select(16)
    turtle.refuel()          -- burns whole coal stack in one go
  end
end

local function nextBlock()     -- pick a slot 1-15 that still has grass
  for s = 1, 15 do
    if turtle.getItemCount(s) > 0 then turtle.select(s) return true end
  end
  return false
end

local function fwd()
  fuelCheck()
  local tries = 0
  while not turtle.forward() do
    turtle.dig()
    tries = tries + 1
    if tries > 40 then error("blocked moving forward at tile "..step) end
  end
end

local function place()
  step = step + 1
  if step <= done then return end            -- already placed, skip
  if not nextBlock() then error("out of grass - refill slots 1-15 and rerun") end
  if not turtle.placeDown() then             -- tile occupied? clear and retry
    turtle.digDown()
    turtle.placeDown()
  end
  save()
end

local function uturn(dir)
  if dir == "right" then turtle.turnRight(); fwd(); turtle.turnRight()
  else turtle.turnLeft(); fwd(); turtle.turnLeft() end
end

for line = 1, WID do
  for pos = 1, LEN do
    place()
    if pos < LEN then fwd() end
  end
  if line < WID then
    if line % 2 == 1 then uturn("right") else uturn("left") end
  end
end

fs.delete(PROG)
print("Grass floor complete.")