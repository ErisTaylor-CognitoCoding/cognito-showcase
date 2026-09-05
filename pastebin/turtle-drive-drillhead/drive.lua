-- drive: pushes the turtle forward so mounted drill heads do the cutting
-- usage: drive <blocks> [seconds between steps]
local args = {...}
local n = tonumber(args[1]) or 30
local delay = tonumber(args[2]) or 1

local function fuel()
  if turtle.getFuelLevel() ~= "unlimited" and turtle.getFuelLevel() < 10 then
    for i = 1, 16 do
      turtle.select(i)
      if turtle.refuel(1) then break end
    end
    turtle.select(1)
  end
end

for i = 1, n do
  fuel()
  local tries = 0
  while turtle.detect() and tries < 16 do
    turtle.dig()
    tries = tries + 1
    sleep(0.4)
  end
  if not turtle.forward() then
    print("Blocked at block " .. i)
    break
  end
  sleep(delay)
end
print("Done")
