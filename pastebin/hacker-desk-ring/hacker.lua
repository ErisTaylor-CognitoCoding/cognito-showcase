-- hacker desk ring — Zero's spec
-- Slots: 1=corner FULL block, 2=black slab, 3=white slab, 4=computer, 16=coal
-- Place ONE corner block, sit turtle ON it facing along the long wall.
-- Run:  hacker 330 120
local a = {...}
local L, W = tonumber(a[1]), tonumber(a[2])
if not L or not W then print("Usage: hacker <L> <W>") return end
local sides = { L, W, L, W }

local function fuel()
  if turtle.getFuelLevel() < 20 then turtle.select(16); turtle.refuel(1) end
end
local function fwd()
  fuel()
  while not turtle.forward() do turtle.dig() end
end

-- PASS 1: desk floor. Turtle rides one block above, digs then places down.
-- corners = full block, everything between = alternating black/white slab.
local black = true
for s = 1, 4 do
  local n = sides[s] - 1
  for i = 1, n do
    fwd()
    if i == n then
      if s < 4 then                    -- fresh corner (s4 arrival = start, already down)
        turtle.select(1); turtle.digDown(); turtle.placeDown()
      end
    else                               -- slab cell
      if black then turtle.select(2) else turtle.select(3) end
      black = not black
      turtle.digDown(); turtle.placeDown()
    end
  end
  turtle.turnRight()
end

-- PASS 2: computers on every slab (corners stay bare). Up one, walk it again.
turtle.up()
for s = 1, 4 do
  local n = sides[s] - 1
  for i = 1, n do
    fwd()
    if i < n then turtle.select(4); turtle.placeDown() end
  end
  turtle.turnRight()
end

print("Hacker desk ring done")