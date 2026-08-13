-- file: smart
local want = "minecraft:diamond_ore"   -- the block Bob is hunting for
local steps = 0                        -- how far he's walked, so he can walk home

local function turnRound()             -- face back down his own tunnel
  turtle.turnLeft()
  turtle.turnLeft()
end

local function dumpJunk()              -- throw out anything that isn't the target
  for slot = 1, 16 do
    local item = turtle.getItemDetail(slot)
    if item and item.name ~= want then
      turtle.select(slot)
      turtle.drop()
    end
  end
  turtle.select(1)
end

local function stackFull()             -- true the moment any slot hits 64
  for slot = 1, 16 do
    if turtle.getItemCount(slot) == 64 then return true end
  end
  return false
end

while true do
  local found, block = turtle.inspect()
  if not found then break end          -- open air, nothing to dig
  print(block.name)                    -- say its name on screen
  turtle.dig()
  turtle.forward()
  steps = steps + 1
  if stackFull() then                  -- bag's filling up — spit it out here
    turnRound()
    dumpJunk()
    turnRound()
  end
  if block.name == want then break end -- that's the one — stop
end

turnRound()
dumpJunk()                             -- drop the junk before the walk home
for i = 1, steps do
  turtle.forward()                     -- straight back down his own tunnel
end

for slot = 1, 16 do                    -- hand over what's left: the diamond
  turtle.select(slot)
  turtle.drop()
end
