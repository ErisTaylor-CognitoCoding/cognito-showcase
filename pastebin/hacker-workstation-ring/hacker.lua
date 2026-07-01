-- hacker: perimeter workstation row (dig-then-place, never skips)
-- Corners = full block. Between corners: step, computer, step, computer...
-- Slot 1 = full corner block | Slot 2 = step (stair) | Slot 3 = computer | Slot 16 = coal
-- Sit turtle ON your first placed corner block, facing along the LONG wall.
-- Run:  hacker 330 120
local a = {...}
local L, W = tonumber(a[1]), tonumber(a[2])
if not L or not W then print("Usage: hacker <length> <width>") return end

local n = 0  -- non-corner counter -> alternates step/computer

local function fuel()
  if turtle.getFuelLevel() < 10 then turtle.select(16); turtle.refuel(1); turtle.select(1) end
end

local function fwd()
  fuel()
  while not turtle.forward() do turtle.dig() end
end

local function drop(slot)
  turtle.select(slot)
  turtle.digDown()
  turtle.placeDown()
end

local function corner() drop(1) end

local function desk()
  if n % 2 == 0 then drop(2) else drop(3) end
  n = n + 1
end

corner()                        -- starting corner
local sides = { L - 1, W - 1, L - 1, W - 1 }
for s = 1, 4 do
  for i = 1, sides[s] do
    fwd()
    if i == sides[s] then corner() else desk() end
  end
  turtle.turnRight()
end

print("Workstation ring done")