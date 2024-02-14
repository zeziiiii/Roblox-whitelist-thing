_G.key = "urkey"
--thekey ^^^




local url = "https://example.com/?accesskey=" .. _G.key

local function lol()
    local r = game:HttpGet(url)
    if r == "Working" then
        print("Working")
    else
        print("Haha no valid key loser")
    end
end

lol()