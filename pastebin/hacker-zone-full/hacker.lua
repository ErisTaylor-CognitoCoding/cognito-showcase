-- hacker: FULL hacker-zone build in one pass
-- Desk block  -> slot 1
-- Computer    -> slot 2
-- Coal        -> slot 16
-- Place ONE block, sit turtle ON it, facing along the long wall.
-- Run:  hacker <length> <width> [spacing]   e.g.  hacker 330 120 5
local a = {...}
local L, W = tonumber(a[1]), tonumber(a[2])
local N = tonumber(a[3]) or 5
if not L or not W then print("Usage: hacker <length> <width> [spacing]") return end

local function fuel()
  if turtle.getFuelLevel() < 10 then turtle.select(16); turtle.refuel(1); turtle.select(1) end
end

local function fwd()
  fuel()
  while not turtle.forward() do turtle.dig() end
end

-- lay a desk ring at current level: dig then place below every cell
local function deskRing(l, w)
  local s = { l - 1, w - 1, l - 1, w - 1 }
  turtle.select(1); turtle.digDown(); turtle.placeDown()
  for k = 1, 4 do
    for i = 1, s[k] do
      fwd()
      turtle.select(1); turtle.digDown(); turtle.placeDown()
    end
    turtle.turnRight()
  end
end

-- walk a ring one level up, drop a computer below every N cells
local function compRing(l, w, n)
  local s = { l - 1, w - 1, l - 1, w - 1 }
  local c = 0
  turtle.select(2); turtle.digDown(); turtle.placeDown()
  for k = 1, 4 do
    for i = 1, s[k] do
      fwd(); c = c + 1
      if c % n == 0 then turtle.select(2); turtle.digDown(); turtle.placeDown() end
    end
    turtle.turnRight()
  end
end

-- desks: 2 high + stepped-in lip
deskRing(L, W)
turtle.up(); deskRing(L, W)
turtle.up(); turtle.turnRight(); fwd(); turtle.turnLeft()
deskRing(L - 2, W - 2)

-- computers along the top, facing the room
turtle.up()
compRing(L - 2, W - 2, N)

print("Hacker zone done: desks + computers")