--- computers.lua  (Advanced Turtle, CC:Tweaked)

local STAIR_SLOT    = 1
local FUEL_SLOT     = 16
local FLOOR_SLOT    = 5
local NETMODEM_SLOT = 9   -- wired modems (full block)

local SLOTS = {
  advanced = 3,
  disk     = 6,
  printer  = 7,
  modem    = 8,   -- wireless modem
}

local STATION  = { "advanced", "disk", "printer", "modem" }
local GAP      = 2       -- empty blocks between stations
local STATIONS = 1       -- how many stations
local TRAVEL   = "right" -- row runs "right" or "left"
local WIRE     = true    -- lay the network line after building

local function refuelIfLow()
  if turtle.getFuelLevel() == "unlimited" then return end
  if turtle.getFuelLevel() > 20 then return end
  turtle.select(FUEL_SLOT)
  turtle.refuel(1)
end

local function up()      refuelIfLow(); while not turtle.up()      do sleep(0.3) end end
local function down()    refuelIfLow(); while not turtle.down()    do sleep(0.3) end end
local function forward() refuelIfLow(); while not turtle.forward() do turtle.dig(); sleep(0.3) end end

local function turnTravel()
  if TRAVEL == "left" then turtle.turnLeft() else turtle.turnRight() end
end
local function turnBack()
  if TRAVEL == "left" then turtle.turnRight() else turtle.turnLeft() end
end

local function placeUpFrom(slot)
  if turtle.getItemCount(slot) < 1 then error("Out of items in slot " .. slot) end
  turtle.select(slot)
  turtle.placeUp()
end

-- move to the next spot, then fill the floor block we just left
local function moveAndFill()
  turnTravel()
  forward()
  turnTravel(); turnTravel()   -- spin 180 to face the block we left
  if turtle.getItemCount(FLOOR_SLOT) < 1 then
    error("Out of floor blocks in slot " .. FLOOR_SLOT)
  end
  turtle.select(FLOOR_SLOT)
  turtle.place()
  turnTravel()                 -- face the viewer again
end

-- build the plan: each station's caps, then a gap, repeated
local plan = {}
for station = 1, STATIONS do
  for _, item in ipairs(STATION) do
    plan[#plan + 1] = item
  end
  if station < STATIONS then
    for space = 1, GAP do plan[#plan + 1] = "gap" end
  end
end

-- lay a wired-modem line on top of the caps (one network per station)
local function layNetwork()
  up(); up(); up(); up()   -- rise above the caps
  turnBack()               -- face back along the row
  for index = #plan, 1, -1 do
    forward()
    if plan[index] ~= "gap" then
      if turtle.getItemCount(NETMODEM_SLOT) < 1 then
        error("Out of wired modems in slot " .. NETMODEM_SLOT)
      end
      turtle.select(NETMODEM_SLOT)
      turtle.placeDown()   -- modem lands on top of the cap
    end
  end
end

-- ===== build =====
for index = 1, #plan do
  local item = plan[index]
  if item ~= "gap" then
    up()                     -- rise to stair level
    placeUpFrom(SLOTS[item]) -- cap floats one above
    down()                   -- drop to the low lane
    placeUpFrom(STAIR_SLOT)  -- tuck stair under cap
  end
  if index < #plan then moveAndFill() end
end
moveAndFill()                -- floor under the final spot

if WIRE then
  print("Laying network line...")
  layNetwork()
end

turtle.select(STAIR_SLOT)
print("Done! Built " .. STATIONS .. " stations.")
