-- pick.lua  --  move forward, only collect ores on the list
-- usage: pick 30

local wanted = {
  ["minecraft:coal_ore"]=true,      ["minecraft:deepslate_coal_ore"]=true,
  ["minecraft:iron_ore"]=true,      ["minecraft:deepslate_iron_ore"]=true,
  ["minecraft:copper_ore"]=true,    ["minecraft:deepslate_copper_ore"]=true,
  ["minecraft:gold_ore"]=true,      ["minecraft:deepslate_gold_ore"]=true,
  ["minecraft:redstone_ore"]=true,  ["minecraft:deepslate_redstone_ore"]=true,
  ["minecraft:lapis_ore"]=true,     ["minecraft:deepslate_lapis_ore"]=true,
  ["minecraft:diamond_ore"]=true,   ["minecraft:deepslate_diamond_ore"]=true,
  ["minecraft:emerald_ore"]=true,   ["minecraft:deepslate_emerald_ore"]=true,
  ["minecraft:ancient_debris"]=true,
}

local keepFuel = {
  ["minecraft:coal"]=true, ["minecraft:charcoal"]=true,
}

local function isWanted(ok, data)
  return ok and wanted[data.name] == true
end

local function refuel()
  if turtle.getFuelLevel() == "unlimited" then return end
  if turtle.getFuelLevel() > 80 then return end
  for i = 1, 16 do
    turtle.select(i)
    if turtle.refuel(1) then break end
  end
  turtle.select(1)
end

-- look up, down, left, right -- dig ONLY if it's on the list
local function scan()
  if isWanted(turtle.inspectUp())   then turtle.digUp()   end
  if isWanted(turtle.inspectDown()) then turtle.digDown() end

  turtle.turnLeft()
  if isWanted(turtle.inspect()) then turtle.dig() end
  turtle.turnRight(); turtle.turnRight()
  if isWanted(turtle.inspect()) then turtle.dig() end
  turtle.turnLeft()
end

-- bin anything that isn't an ore or fuel, so the inventory stays clean
local function dumpJunk()
  for i = 1, 16 do
    local d = turtle.getItemDetail(i)
    if d and not wanted[d.name] and not keepFuel[d.name] then
      turtle.select(i)
      turtle.dropDown()
    end
  end
  turtle.select(1)
end

local args = { ... }
local dist = tonumber(args[1]) or 20

for n = 1, dist do
  refuel()
  scan()

  -- clear the lane so it can keep going
  while turtle.detect() do
    turtle.dig()
    sleep(0.4)
  end

  if not turtle.forward() then
    print("Blocked at block " .. n)
    break
  end

  if n % 10 == 0 then dumpJunk() end
end

scan()
dumpJunk()
print("Done. Fuel left: " .. tostring(turtle.getFuelLevel()))
