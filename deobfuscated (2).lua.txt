local Env = getfenv();
local w = {};
local v1 = {...};
local r216 = true;
local r225 = string.gmatch;
local function r1(...)
    error("Tamper Detected!");
    return; 
end;
local r228 = false;
local v2 = pcall(function(...)
    r228 = true;
    return; 
end);
local v3 = v2;
if v2 then
    v3 = r228;
end;
local v4 = v3;
local r219 = math.random;
local v5 = table.concat;
local v6 = table;
local function v7(...)
    while true do
        l1 = l2;
        l2 = l1;
        r1(); 
    end;
    return; 
end;
if v6 then
    r = table.unpack;
end;
local r227 = v6 or unpack;
local r224 = r219(3, 65);
local v8 = ({
    pcall(function(...)
        return "4xSuq0ROhD4sb3o" / (12725462 - "7zJxYyIC24MOMNp" ^ 14370284); 
    end)
})[2];
local r226 = tonumber(r225(tostring(v8), ":(%d*):")());
local v9 = 1 < 0;
for A = 1, r224 do
    r217 = A;
    r218 = math.random(1, 100);
    r220 = r219(0, 255);
    r221 = r219(1, r218);
    r222 = r219(1, 2) == 1;
    r223 = v8:gsub(":(%d*):", ":" .. tostring(r219(0, 10000)) .. ":");
    if r222 then
        r216 = r216 and pcall(function(...)
            local R = {
                153,
                110,
                50,
                151,
                149,
                51,
                114,
                115,
                111,
                113,
                112,
                49
            };
            if w[R[1]](1, 2) == 1 or w[R[2]] == w[R[3]] then
                w[R[5]] = w[R[5]] and w[R[6]] == tonumber(w[R[4]](tostring(({
                    pcall(function(...)
                        return "gAPi5ag6aK" / (11698798 - "EdHq9U4By" ^ 12167420); 
                    end)
                })[2]), ":(%d*):")());
            end;
            if w[R[7]] then
                error(w[R[8]], 0);
            end;
            v1 = {};
            v4 = 1 < 0;
            for x = 1, w[R[9]] do
                v1[x] = w[R[1]](0, 255); 
            end;
            v1[w[R[10]]] = w[R[11]];
            return w[R[12]](v1); 
        end) == false;
    end; 
end;
local r216 = r216 and 0 == 0;
if r216 then
    r4 = math.floor;
    x = math.random;
    r5 = 0;
    o = {};
    r6 = 2;
    r7 = {};
    v6 = 0;
    B = 1 < 0;
    for Y = 1, 256 do
        o[Y] = Y; 
    end;
    v8 = #o == 0;
    Y = table.remove(o, x(1, #o));
    r7[Y] = string.char(Y - 1);
    if #o == 0 then
        r8 = {};
        local function r9(...)
            local R = {
                298,
                215,
                214,
                213
            };
            if #w[R[1]] == 0 then
                w[R[2]] = (w[R[2]] * 105 + 7970519764607) % 35184372088832;
                v3 = w[R[3]] ~= 1;
                w[R[3]] = w[R[3]] * 91 % 257;
                if w[R[3]] ~= 1 then
                    v1 = w[R[3]] % 32;
                    U = w[R[4]](w[R[2]] / 2 ^ (13 - (w[R[3]] - v1) / 32)) % 4294967296 / 2 ^ v1;
                    x = w[R[4]](U % 1 * 4294967296) + w[R[4]](U);
                    q = x % 65536;
                    j = (x - q) / 65536;
                    v4 = q % 256;
                    v7 = j % 256;
                    w[R[1]] = {
                        v4,
                        (q - v4) / 256,
                        v7,
                        (j - v7) / 256
                    };
                    return table.remove(w[R[1]]);
                end;
            end; 
        end;
        r10 = {};
        r3 = setmetatable({}, {
            ["__index"] = r10,
            ["__metatable"] = nil
        });
        local function r2(arg1, arg2, ...)
            local R = {
                300,
                298,
                211,
                215,
                214,
                299
            };
            x = w[R[1]];
            U = arg2;
            if x[U] then
            else
                w[R[2]] = {};
                w[R[4]] = U % 35184372088832;
                w[R[5]] = U % 255 + 2;
                x[U] = "";
                a = 1 < 0;
                for t = 1, string.len(arg1) do
                    x[U] = x[U] .. w[R[3]][(string.byte(arg1, t) + w[R[6]]() + 232) % 256 + 1]; 
                end;
                return U;
            end; 
        end;
        x = {};
        r11 = getfenv();
        r12 = {};
        r13 = true;
        r14 = {
            ["getfenv"] = getfenv,
            ["setfenv"] = setfenv,
            ["rawget"] = rawget,
            ["rawset"] = rawset,
            ["getmetatable"] = getmetatable,
            ["setmetatable"] = setmetatable,
            ["newproxy"] = newproxy,
            ["tostring"] = tostring,
            ["require"] = require,
            ["type"] = type,
            ["next"] = next,
            ["pairs"] = pairs,
            ["pcall"] = pcall
        };
        local function r15(...)
            local R = {
                212,
                210
            };
            v1 = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789";
            v4 = 1 < 0;
            for q = 1, math.random(25, 40) do
                v2 = q;
                U = U .. string.sub(v1, math.random(1, #v1), math.random(1, #v1)); 
            end;
            return ""; 
        end;
        local function t(arg1_2, ...)
            local R = {
                305,
                212,
                210
            };
            v1 = arg1_2;
            U = w[R[1]]();
            v2 = 1 < 0;
            for q = 1, #v1 do
                x = x .. string.char(bit32.bxor(string.byte(v1, q), string.byte(U, q % #U + 1))); 
            end;
            return "", U; 
        end;
        r16 = {};
        v9 = 1 < 0;
        for o = 1, 15 do
            return; 
        end;
        x.Initialize = function(arg1_3, ...)
            local R = {
                212,
                210,
                301,
                306,
                303,
                304,
                302
            };
            r17 = {};
            v1 = arg1_3;
            x = {
                ["__index"] = function(arg1_4, arg2_4, ...)
                    local R = {
                        R[3],
                        R[4],
                        R[5]
                    };
                    v1 = arg1_4;
                    U = arg2_4;
                    v5 = w[R[1]];
                    q = w[R[1]];
                    v5[U] = (w[R[1]][U] or 0) + 1;
                    if w[R[2]][U] then
                        w[R[2]][U]();
                        return nil;
                    end;
                    return w[R[3]][U]; 
                end,
                ["__newindex"] = function(arg1_5, arg2_5, arg3_5, ...)
                    local R = {
                        R[1],
                        R[2],
                        R[5]
                    };
                    v1 = arg1_5;
                    U = arg2_5;
                    v2 = "script";
                    v4 = v2[3];
                    j = v2[2];
                    v2 = "ipairs";
                    for v4, r in ipairs({
                        "getfenv",
                        "setfenv",
                        "require",
                        "game",
                        v2,
                        "getmetatable",
                        "setmetatable"
                    }) do
                        v7 = v4;
                        if U == r then
                            return;
                        else
                            
                        end; 
                    end;
                    w[R[3]][U] = arg3_5;
                    return; 
                end,
                ["__metatable"] = "Locked",
                ["__tostring"] = function(...)
                    local R = {
                        R[6],
                        R[1],
                        R[2],
                        R[5]
                    };
                    v1 = w[R[1]].getfenv(2);
                    v3 = w[R[4]];
                    if v1 ~= v3 then
                        v3 = w[R[1]];
                        q = w[R[3]];
                        U = q[2];
                        x = q[3];
                        q = v3;
                        for x, v4 in v3.pairs(v1) do
                            w[R[1]].rawset(w[R[1]][U[q]](2), x, nil); 
                        end;
                        return "";
                    end;
                    return "Environment"; 
                end
            };
            setmetatable(r17, x);
            r18 = getfenv;
            getfenv = function(...)
                local R = {
                    222,
                    R[7],
                    R[5],
                    221
                };
                if w[R[2]] and w[R[1]](2) ~= w[R[3]] then
                    return w[R[4]];
                end;
                return w[R[1]](select(-1, ...)); 
            end;
            v4 = getmetatable(newproxy(true));
            v4.__index = x.__index;
            v4.__newindex = x.__newindex;
            local function r19(...)
                q = {
                    pcall(function(...)
                        return getfenv(), getmetatable(game); 
                    end)
                };
                U = q[2];
                if not q[1] then
                    w[302] = true;
                    return true;
                end;
                return false; 
            end;
            r19();
            spawn(function(...)
                while wait(0.5) do
                    r19(); 
                end;
                return; 
            end);
            return r17; 
        end;
        setfenv(1, x:Initialize());
        o = game;
        o:IsLoaded();
        task.wait();
        o = game;
        if o:IsLoaded() then
            o = game.Players.LocalPlayer.Character;
            task.wait();
            if game.Players.LocalPlayer.Character then
                r20 = 0;
                Y = game;
                o = Y:GetService("RunService").Heartbeat;
                o:Connect(function(...)
                    local R = {
                        297
                    };
                    w[R[1]] = w[R[1]] + 1;
                    return; 
                end);
                o = r20 >= 2;
                task.wait();
                if r20 >= 2 then
                    Y:Disconnect();
                    if TBOjjs then
                        return;
                    end;
                    getgenv().TBOjjs = true;
                    o = game.DescendantAdded;
                    o:Connect(function(arg1_6, ...)
                        local R = {
                            212,
                            210
                        };
                        v1 = arg1_6;
                        if v1 then
                            v5 = v5;
                            v3 = v1:IsA("TextLabel") or (v1:IsA("TextButton") or v1:IsA("Message"));
                            v5 = v5;
                        end;
                        if v1 then
                            if string.find(string.lower(v1.Text), "https://peeky.pythonanywhere.com/alive") then
                                while true do end;
                            end;
                        end;
                        return; 
                    end);
                    r21 = {
                        ["setclipboard"] = setclipboard,
                        ["writefile"] = writefile,
                        ["appendfile"] = appendfile
                    };
                    getgenv().setclipboard = function(...)
                        return; 
                    end;
                    getgenv().writefile = function(...)
                        return; 
                    end;
                    getgenv().appendfile = function(...)
                        return; 
                    end;
                    F = game;
                    if string.find(F:HttpGet("https://peeky.pythonanywhere.com/Alive"), "yes") then
                        v5 = v5;
                        v5 = v5;
                        v5 = v5;
                        r22 = http_request or (request or syn and syn.request);
                        if r22 then
                            r22({
                                ["Url"] = "https://okei.pythonanywhere.com/execution",
                                ["Method"] = "POST",
                                ["Headers"] = {
                                    ["Content-Type"] = "application/json"
                                },
                                ["Body"] = "{}"
                            });
                        end;
                        task.wait(.2);
                        o = game;
                        r23 = o:GetService("HttpService");
                        p = game;
                        m = p:GetService("UserInputService");
                        if m:GetPlatform() == Enum.Platform.Windows then
                            device = "Windows";
                        else
                            m = game;
                            S = m:GetService("UserInputService");
                            if S:GetPlatform() == Enum.Platform.OSX then
                                device = "macOS";
                            else
                                S = game;
                                Z = S:GetService("UserInputService");
                                if Z:GetPlatform() == Enum.Platform.IOS then
                                    device = "iOS";
                                else
                                    Z = game;
                                    K = Z:GetService("UserInputService");
                                    if K:GetPlatform() == Enum.Platform.UWP then
                                        device = "Windows (Microsoft Store)";
                                    else
                                        K = game;
                                        G = K:GetService("UserInputService");
                                        if G:GetPlatform() == Enum.Platform.Android then
                                            device = "Android Device";
                                        else
                                            device = "Unknown";
                                        end;
                                        local function r24(...)
                                            local R = {
                                                212,
                                                210,
                                                245
                                            };
                                            x = {
                                                pcall(function(...)
                                                    local R = {
                                                        R[1],
                                                        R[2],
                                                        R[3]
                                                    };
                                                    v5 = w[R[3]];
                                                    v4 = "headers";
                                                    j = v5:JSONDecode(request({
                                                        ["Url"] = "https://peeky.pythonanywhere.com/headers"
                                                    }).Body)[v4];
                                                    q = v4[3];
                                                    j = v4[1];
                                                    for q, v2 in j, pairs(j) do
                                                        v7 = tostring(q);
                                                        if string.find(v7:lower(), "fingerprint") then
                                                            return v2;
                                                        else
                                                            
                                                        end; 
                                                    end;
                                                    return; 
                                                end)
                                            };
                                            if x[1] then
                                                return x[2];
                                            end;
                                            return "unavailable"; 
                                        end;
                                        local function r29(...)
                                            local R = {
                                                364,
                                                277,
                                                212,
                                                210,
                                                245,
                                                362,
                                                363
                                            };
                                            if w[R[1]] ~= nil then
                                                return w[R[1]];
                                            end;
                                            v5 = pcall;
                                            x = {
                                                v5(function(...)
                                                    local R = {
                                                        R[2],
                                                        R[3],
                                                        R[4],
                                                        R[5],
                                                        R[6]
                                                    };
                                                    r = w[R[4]];
                                                    return w[R[1]]({
                                                        ["Url"] = "https://peeky.pythonanywhere.com/use_key",
                                                        ["Method"] = "POST",
                                                        ["Headers"] = {
                                                            ["Content-Type"] = "application/json"
                                                        },
                                                        ["Body"] = r:JSONEncode({
                                                            ["key"] = getgenv().Key,
                                                            ["hwid"] = w[R[5]]()
                                                        })
                                                    }); 
                                                end)
                                            };
                                            v1 = x[2];
                                            if not x[1] or not v1 then
                                                w[R[1]] = false;
                                                return false;
                                            end;
                                            v5 = v5;
                                            r27 = v1.Body or v1.body;
                                            if not r27 then
                                                w[R[1]] = false;
                                                return false;
                                            end;
                                            v7 = not pcall(function(...)
                                                local R = {
                                                    o,
                                                    157,
                                                    48
                                                };
                                                v5 = w[R[1]];
                                                w[R[3]] = v5:JSONDecode(w[R[2]]);
                                                return; 
                                            end);
                                            v2 = v5;
                                            if v7 then
                                                v5 = v5;
                                                if v7 then
                                                    w[TA] = false;
                                                    return false;
                                                end;
                                                if r28.ok then
                                                    w[R[1]] = true;
                                                    w[R[7]] = r28;
                                                    v5 = v5;
                                                    Notify({
                                                        ["Title"] = "TBO Premium",
                                                        ["Description"] = "Welcome, " .. (r28.discord_username or "User") .. "!",
                                                        ["Duration"] = 5
                                                    });
                                                    return true;
                                                end;
                                                if r28.reason == "hwid_mismatch" then
                                                    Notify({
                                                        ["Title"] = "TBO Premium",
                                                        ["Description"] = "HWID mismatch detected!",
                                                        ["Duration"] = 5
                                                    });
                                                else
                                                    if r28.reason == "expired" then
                                                        Notify({
                                                            ["Title"] = "TBO Premium",
                                                            ["Description"] = "Your key has expired.",
                                                            ["Duration"] = 5
                                                        });
                                                    else
                                                        if r28.reason == "invalid_key" then
                                                            Notify({
                                                                ["Title"] = "TBO Premium",
                                                                ["Description"] = "Invalid key.",
                                                                ["Duration"] = 5
                                                            });
                                                        end;
                                                        w[R[1]] = false;
                                                        return false;
                                                    end;
                                                end;
                                            else
                                                q = not r28;
                                            end; 
                                        end;
                                        local function vA(...)
                                            local R = {
                                                365,
                                                363,
                                                212,
                                                210
                                            };
                                            if not w[R[1]]() then
                                                return false;
                                            end;
                                            return w[R[2]] and w[R[2]].infinite == true; 
                                        end;
                                        RA = game;
                                        IA = RA:GetService("RbxAnalyticsService");
                                        WA = "fields";
                                        HA = game;
                                        yA = HA:GetService("MarketplaceService");
                                        YA = game;
                                        aA = YA:GetService("Stats").Network.ServerStatsItem["Data Ping"];
                                        if r22 then
                                            WA = r23;
                                            r22({
                                                ["Url"] = "https://peeky.pythonanywhere.com/webhook/SBipt8v8iZUx",
                                                ["Method"] = "POST",
                                                ["Headers"] = {
                                                    ["Content-Type"] = "application/json"
                                                },
                                                ["Body"] = WA:JSONEncode({
                                                    ["embeds"] = {
                                                        {
                                                            ["title"] = "`` | Script executed: | ``",
                                                            ["description"] = "**| TBO Jujutsu Shenanigans gui free version has been executed! |**",
                                                            ["type"] = "rich",
                                                            ["color"] = tonumber(255),
                                                            [WA] = {
                                                                {
                                                                    ["name"] = "**Users Profile:**",
                                                                    ["value"] = "[" .. game.Players.LocalPlayer.Name .. "'s Avatar](https://www.roblox.com/users/" .. game.Players.LocalPlayer.UserId .. "/profile)"
                                                                },
                                                                {
                                                                    ["name"] = "**Displayname:**",
                                                                    ["value"] = game.Players.LocalPlayer.DisplayName
                                                                },
                                                                {
                                                                    ["name"] = "**UserID:**",
                                                                    ["value"] = tostring(game.Players.LocalPlayer.UserId)
                                                                },
                                                                {
                                                                    ["name"] = "**Game Name:**",
                                                                    ["value"] = yA:GetProductInfo(game.PlaceId).Name
                                                                },
                                                                {
                                                                    ["name"] = "**Game Place ID:**",
                                                                    ["value"] = "[" .. game.PlaceId .. "](" .. "https://www.roblox.com/games/" .. game.PlaceId .. ")"
                                                                },
                                                                {
                                                                    ["name"] = "**HWID:**",
                                                                    ["value"] = r24()
                                                                },
                                                                {
                                                                    ["name"] = "**Client ID:**",
                                                                    ["value"] = IA:GetClientId()
                                                                },
                                                                {
                                                                    ["name"] = "**Ping:**",
                                                                    ["value"] = aA:GetValueString()
                                                                },
                                                                {
                                                                    ["name"] = "**Device:**",
                                                                    ["value"] = device
                                                                },
                                                                {
                                                                    ["name"] = "**Executor:**",
                                                                    ["value"] = identifyexecutor()
                                                                },
                                                                {
                                                                    ["name"] = "**Execution Time:**",
                                                                    ["value"] = os.date("%Y-%m-%d %H:%M:%S")
                                                                },
                                                                {
                                                                    ["name"] = "**Snipe Me:**",
                                                                    ["value"] = "[Snipe Me Teleport To Place Where Player Executed](" .. "https://peeky.pythonanywhere.com/join?placeId=" .. game.PlaceId .. "&gameInstanceId=" .. tostring(game.JobId) .. ")"
                                                                }
                                                            }
                                                        }
                                                    }
                                                })
                                            });
                                        end;
                                        task.delay(.8, function(...)
                                            local R = {
                                                212,
                                                210,
                                                193
                                            };
                                            getgenv().setclipboard = w[R[3]].setclipboard;
                                            getgenv().writefile = w[R[3]].writefile;
                                            getgenv().appendfile = w[R[3]].appendfile;
                                            return; 
                                        end);
                                        if game.GameId ~= 3508322461 then
                                            return;
                                        end;
                                        local function r33(arg1_7, ...)
                                            local R = {
                                                212,
                                                210
                                            };
                                            v1 = arg1_7;
                                            q = getconnections;
                                            U = q[2];
                                            x = q[3];
                                            q = "ipairs";
                                            for x, v4 in ipairs(q(v1.MouseButton1Down)) do
                                                j = x;
                                                r30 = v4;
                                                pcall(function(...)
                                                    v5 = r30;
                                                    v5:Fire();
                                                    return; 
                                                end); 
                                            end;
                                            j = getconnections;
                                            v4 = {
                                                j(v1.Activated)
                                            };
                                            U = j[1];
                                            x = j[2];
                                            for q, v4 in ipairs(C(v4)) do
                                                j = q;
                                                r31 = v4;
                                                pcall(function(...)
                                                    v5 = r31;
                                                    v5:Fire();
                                                    return; 
                                                end); 
                                            end;
                                            j = getconnections;
                                            v4 = {
                                                j(v1.MouseButton1Click)
                                            };
                                            U = j[1];
                                            x = j[2];
                                            for q, v4 in ipairs(C(v4)) do
                                                j = q;
                                                r32 = v4;
                                                pcall(function(...)
                                                    v5 = r32;
                                                    v5:Fire();
                                                    return; 
                                                end); 
                                            end;
                                            return; 
                                        end;
                                        local function r34(arg1_8, ...)
                                            local R = {
                                                212,
                                                210
                                            };
                                            v1 = arg1_8;
                                            U = game.Players.LocalPlayer.Character.HumanoidRootPart.CFrame;
                                            game.Players.LocalPlayer.Character.Humanoid.CameraOffset = v1:ToObjectSpace(CFrame.new(U.Position)).Position;
                                            game.Players.LocalPlayer.Character.HumanoidRootPart.CFrame = v1;
                                            v3 = game;
                                            v5 = v3:GetService("RunService").RenderStepped;
                                            v5:Wait();
                                            game.Players.LocalPlayer.Character.HumanoidRootPart.CFrame = U;
                                            game.Players.LocalPlayer.Character.Humanoid.CameraOffset = U:ToObjectSpace(CFrame.new(U.Position)).Position;
                                            return; 
                                        end;
                                        local function r36(arg1_9, ...)
                                            local R = {
                                                212,
                                                210,
                                                159
                                            };
                                            r35 = arg1_9;
                                            v3 = game;
                                            v5 = v3:GetService("RunService").Heartbeat;
                                            U = v5:Connect(function(...)
                                                local R = {
                                                    R[3],
                                                    120
                                                };
                                                w[R[1]](w[R[2]]);
                                                return; 
                                            end);
                                            task.wait(.1);
                                            v5 = game.Players.LocalPlayer.Character;
                                            v5:PivotTo(CFrame.new(0, -457, 0));
                                            task.wait();
                                            v5 = game.Players.LocalPlayer.Character;
                                            v5:PivotTo(game.Players.LocalPlayer.Character.HumanoidRootPart.CFrame);
                                            U:Disconnect();
                                            return; 
                                        end;
                                        DA = game;
                                        r37 = DA:GetService("TweenService");
                                        UA = game;
                                        r38 = UA:GetService("RunService");
                                        xA = game;
                                        r39 = xA:GetService("TextService");
                                        eA = game;
                                        uA = Instance.new("ScreenGui");
                                        uA.Name = "AkaliNotif";
                                        uA.Parent = eA:GetService("Players").LocalPlayer.PlayerGui;
                                        uA.ResetOnSpawn = false;
                                        r40 = Instance.new("Frame");
                                        r40.Name = "Container";
                                        r40.Position = UDim2.new(0, 20, 0.5, -20);
                                        r40.Size = UDim2.new(0, 300, 0.5, 0);
                                        r40.BackgroundTransparency = 1;
                                        r40.Parent = uA;
                                        local function r41(arg1_10, arg2_10, ...)
                                            local R = {
                                                212,
                                                210
                                            };
                                            U = arg2_10;
                                            v5 = Instance.new;
                                            v7 = "BackgroundTransparency";
                                            if U then
                                                v2 = "Button";
                                            end;
                                            v5 = v7;
                                            v5 = v5;
                                            x = v5("Image" .. (U or "Label"));
                                            v3 = arg1_10;
                                            x.Image = v3;
                                            x.BackgroundTransparency = 1;
                                            return x; 
                                        end;
                                        local function r42(...)
                                            local R = {
                                                169,
                                                212,
                                                210
                                            };
                                            v1 = w[R[1]]("http://www.roblox.com/asset/?id=5761488251");
                                            v1.ScaleType = Enum.ScaleType.Slice;
                                            v1.SliceCenter = Rect.new(2, 2, 298, 298);
                                            v1.ImageColor3 = Color3.fromRGB(100, 100, 255);
                                            return v1; 
                                        end;
                                        local function r43(...)
                                            local R = {
                                                169,
                                                212,
                                                210
                                            };
                                            v1 = w[R[1]]("http://www.roblox.com/asset/?id=5761498316");
                                            v1.ScaleType = Enum.ScaleType.Slice;
                                            v1.SliceCenter = Rect.new(17, 17, 283, 283);
                                            v1.Size = UDim2.fromScale(1, 1) + UDim2.fromOffset(30, 30);
                                            v1.Position = -UDim2.fromOffset(15, 15);
                                            v1.ImageColor3 = Color3.fromRGB(30, 30, 30);
                                            return v1; 
                                        end;
                                        local function r44(arg1_11, ...)
                                            local R = {
                                                212,
                                                210
                                            };
                                            U = Instance.new("UIStroke");
                                            U.Thickness = 1.2;
                                            U.Transparency = .3;
                                            U.Color = Color3.fromRGB(170, 170, 255);
                                            U.Parent = arg1_11;
                                            return; 
                                        end;
                                        local function r45(arg1_12, ...)
                                            local R = {
                                                212,
                                                210,
                                                161
                                            };
                                            U = Instance.new("UIGradient");
                                            U.Rotation = 90;
                                            U.Color = ColorSequence.new({
                                                ColorSequenceKeypoint.new(0, Color3.fromRGB(90, 90, 255)),
                                                ColorSequenceKeypoint.new(1, Color3.fromRGB(40, 40, 120))
                                            });
                                            v3 = arg1_12;
                                            U.Parent = v3;
                                            v5 = w[R[3]];
                                            v3 = v5:Create(U, TweenInfo.new(3, Enum.EasingStyle.Sine, Enum.EasingDirection.InOut, -1, true), {
                                                ["Rotation"] = 270
                                            });
                                            v3:Play();
                                            return; 
                                        end;
                                        local function r46(arg1_13, ...)
                                            local R = {
                                                212,
                                                210,
                                                161
                                            };
                                            U = Instance.new("ImageLabel");
                                            U.Image = "rbxassetid://5028857084";
                                            U.Size = UDim2.new(1, 40, 1, 40);
                                            U.Position = UDim2.new(0.5, 0, 0.5, 0);
                                            U.AnchorPoint = Vector2.new(0.5, 0.5);
                                            U.BackgroundTransparency = 1;
                                            U.ImageColor3 = Color3.fromRGB(120, 120, 255);
                                            U.ImageTransparency = .6;
                                            U.ZIndex = -2;
                                            U.Parent = arg1_13;
                                            v5 = w[R[3]];
                                            v3 = v5:Create(U, TweenInfo.new(2, Enum.EasingStyle.Sine, Enum.EasingDirection.InOut, -1, true), {
                                                ["ImageTransparency"] = .8
                                            });
                                            v3:Play();
                                            return; 
                                        end;
                                        r47 = 10;
                                        r48 = 10;
                                        r49 = {};
                                        r50 = 1;
                                        r51 = Enum.EasingStyle.Sine;
                                        r52 = Enum.EasingDirection.Out;
                                        r53 = tick();
                                        local function r54(arg1_14, ...)
                                            local R = {
                                                212,
                                                210
                                            };
                                            v1 = arg1_14;
                                            x = v5;
                                            q = typeof(v1) == "table";
                                            if q then
                                                U = arg1_14;
                                            end;
                                            v5 = x;
                                            v4 = q or ;
                                            j = next;
                                            v2, r = j(v4, v2);
                                            while v2 do
                                                x = x + r.AbsoluteSize.X;
                                                q = q + r.AbsoluteSize.Y; 
                                            end;
                                            return {
                                                ["X"] = 0,
                                                ["Y"] = 0,
                                                ["x"] = 0,
                                                ["y"] = 0
                                            }; 
                                        end;
                                        r55 = {};
                                        sA = r38;
                                        sA:BindToRenderStep("UpdateList", 0, function(...)
                                            local R = {
                                                178,
                                                166,
                                                162,
                                                212,
                                                210,
                                                161,
                                                175,
                                                176,
                                                179,
                                                167,
                                                177
                                            };
                                            v1 = tick() - w[R[1]];
                                            U = {};
                                            q = next;
                                            j = w[R[2]];
                                            x, v2 = q(j, x);
                                            while x do
                                                v7 = 301[1];
                                                r = 301[2];
                                                if not 301[3] then
                                                    if r < w[R[3]] then
                                                        v2[2] = math.clamp(v2[2] + tick() - r53, 0, 1);
                                                        r = v2[2];
                                                    else
                                                        v2[3] = true;
                                                    end;
                                                    a = w[R[6]];
                                                    a = v7.Position;
                                                    v7.Position = a:Lerp(UDim2.new(0, 0, 0, w[R[9]](U).Y + w[R[10]] * #U), a:GetValue(r, w[R[7]], w[R[8]]));
                                                    table.insert(U, v7);
                                                end; 
                                            end;
                                            r55 = U;
                                            r53 = tick();
                                            return; 
                                        end);
                                        r56 = {
                                            ["Font"] = Enum.Font.GothamSemibold,
                                            ["Size"] = 14
                                        };
                                        r57 = {
                                            ["Font"] = Enum.Font.Gotham,
                                            ["Size"] = 14
                                        };
                                        r58 = r40.AbsoluteSize.X - r47 - r48;
                                        local function r59(arg1_15, arg2_15, arg3_15, arg4_15, ...)
                                            local R = {
                                                212,
                                                210
                                            };
                                            q = arg4_15;
                                            v5 = Instance.new;
                                            v7 = v5;
                                            if q then
                                                r = "Button";
                                            end;
                                            v5 = v5;
                                            v5 = v7;
                                            j = v5("Text" .. (q or "Label"));
                                            v3 = arg1_15;
                                            j.Text = v3;
                                            v3 = arg2_15;
                                            j.Font = v3;
                                            v3 = arg3_15;
                                            j.TextSize = v3;
                                            j.BackgroundTransparency = 1;
                                            j.TextXAlignment = Enum.TextXAlignment.Left;
                                            j.RichText = true;
                                            j.TextColor3 = Color3.fromRGB(255, 255, 255);
                                            return j; 
                                        end;
                                        local function r60(arg1_16, ...)
                                            local R = {
                                                183,
                                                180,
                                                212,
                                                210
                                            };
                                            return r59(arg1_16, r56.Font, r56.Size); 
                                        end;
                                        local function r61(arg1_17, ...)
                                            local R = {
                                                183,
                                                181,
                                                212,
                                                210
                                            };
                                            return r59(arg1_17, r57.Font, r57.Size); 
                                        end;
                                        local function r62(arg1_18, ...)
                                            local R = {
                                                212,
                                                210,
                                                161
                                            };
                                            v1 = arg1_18;
                                            v3 = v1:IsA("TextLabel") or v1:IsA("TextButton");
                                            if v3 then
                                                v5 = r37;
                                                v3 = v5:Create(v1, TweenInfo.new(0.25), {
                                                    ["TextTransparency"] = 1,
                                                    ["BackgroundTransparency"] = 1
                                                });
                                                v3:Play();
                                            else
                                                v3 = v1:IsA("ImageLabel") or v1:IsA("ImageButton");
                                                if v3 then
                                                    v5 = r37;
                                                    v3 = v5:Create(arg1_18, TweenInfo.new(0.25), {
                                                        ["ImageTransparency"] = 1
                                                    });
                                                    v3:Play();
                                                else
                                                    v3 = "Frame";
                                                    if v1:IsA(v3) then
                                                        v5 = r37;
                                                        v3 = v5:Create(arg1_18, TweenInfo.new(0.25), {
                                                            ["BackgroundTransparency"] = 1
                                                        });
                                                        v3:Play();
                                                    else
                                                        v3 = "UIStroke";
                                                        if v1:IsA(v3) then
                                                            v5 = r37;
                                                            v3 = v5:Create(arg1_18, TweenInfo.new(0.25), {
                                                                ["Transparency"] = 1
                                                            });
                                                            v3:Play();
                                                        else
                                                            if v1:IsA("UIGradient") then
                                                                arg1_18.Transparency = NumberSequence.new(1);
                                                            end;
                                                            return;
                                                        end;
                                                    end;
                                                end;
                                            end; 
                                        end;
                                        local function r63(arg1_19, arg2_19, ...)
                                            local R = {
                                                212,
                                                210,
                                                186,
                                                166
                                            };
                                            v1 = arg1_19;
                                            task.wait(arg2_19);
                                            r62(v1);
                                            j = v1.GetDescendants[1];
                                            q = next;
                                            for x, v2 in q, q(v1) do
                                                v4 = x;
                                                r62(v2); 
                                            end;
                                            v7 = r2("\xc5\x8ab\xfb", 23067890117109);
                                            task[r3[v7]](0.25);
                                            v2 = r49;
                                            v4 = v7[3];
                                            for v4, v2 in v7[1], ipairs(v2) do
                                                x = v4;
                                                if v2[1] == v1 then
                                                    table.remove(r49, v4);
                                                    break;
                                                else
                                                    
                                                end; 
                                            end;
                                            return; 
                                        end;
                                        Notify = function(arg1_20, ...)
                                            local R = {
                                                212,
                                                210,
                                                164,
                                                181,
                                                182,
                                                170,
                                                179,
                                                177,
                                                167,
                                                172,
                                                173,
                                                174,
                                                184,
                                                185,
                                                168,
                                                187,
                                                171,
                                                165,
                                                166
                                            };
                                            v1 = arg1_20;
                                            x = v5;
                                            U = typeof(v1) == "table";
                                            v3 = U and v1;
                                            v5 = x;
                                            if U then
                                                U = U and v1;
                                                x = U.Title;
                                                v5 = U.Description;
                                                j = U.Duration or 5;
                                                if x then
                                                    v5 = v5;
                                                    if x then
                                                        v4 = x and 26 or 0;
                                                        if v5 then
                                                            v3 = r39;
                                                            v2 = v3:GetTextSize(v5, r57.Size, r57.Font, Vector2.new(0, 0));
                                                            v6 = 1 < 0;
                                                            for r = 1, math.ceil(v2.X / r58) do
                                                                a = r;
                                                                v4 = v4 + v2.Y; 
                                                            end;
                                                            v4 = v4 + 8;
                                                        end;
                                                        r64 = r42();
                                                        r64.Size = UDim2.new(1, 0, 0, v4);
                                                        r64.Position = UDim2.new(-1, 20, 0, r54(r55).Y + r47 * #r55);
                                                        r44(r64);
                                                        r45(r64);
                                                        r46(r64);
                                                        if x then
                                                            t = r60(U.Title);
                                                            t.Size = UDim2.new(1, -10, 0, 26);
                                                            t.Position = UDim2.fromOffset(10, 0);
                                                            t.Parent = r64;
                                                        end;
                                                        if v5 then
                                                            t = r61(v5);
                                                            t.TextWrapped = true;
                                                            g = v4;
                                                            v9 = v4;
                                                            t.Size = UDim2.fromScale(1, 1) + UDim2.fromOffset(-r48, x and -26 or 0);
                                                            g = v4;
                                                            Y = v4;
                                                            t.Position = UDim2.fromOffset(10, x and 26 or 0);
                                                            if x then
                                                                Y = "Top";
                                                            end;
                                                            v5 = v4;
                                                            v5 = v4;
                                                            t.TextYAlignment = Enum.TextYAlignment[x or "Center"];
                                                            t.Parent = r64;
                                                        end;
                                                        t = Instance.new("TextButton");
                                                        t.Text = "X";
                                                        t.Font = Enum.Font.GothamBold;
                                                        t.TextSize = 16;
                                                        t.TextColor3 = Color3.fromRGB(255, 255, 255);
                                                        t.BackgroundTransparency = 1;
                                                        t.BackgroundColor3 = Color3.fromRGB(50, 50, 80);
                                                        t.Size = UDim2.new(0, 20, 0, 20);
                                                        t.Position = UDim2.new(1, -25, 0, 5);
                                                        t.AnchorPoint = Vector2.new(0, 0);
                                                        t.Parent = r64;
                                                        r = t.MouseButton1Click;
                                                        r:Connect(function(...)
                                                            local R = {
                                                                gA,
                                                                22
                                                            };
                                                            r3(r2, 0);
                                                            return; 
                                                        end);
                                                        r43().Parent = r64;
                                                        v6 = Instance.new("Frame");
                                                        v6.Name = "Shadow";
                                                        v6.Parent = r64;
                                                        v6.Size = UDim2.new(1, 16, 1, 16);
                                                        v6.Position = UDim2.new(0.5, 0, 0.5, 0);
                                                        v6.AnchorPoint = Vector2.new(0.5, 0.5);
                                                        v6.BackgroundTransparency = .7;
                                                        v6.BackgroundColor3 = Color3.fromRGB(100, 100, 255);
                                                        v6.BorderSizePixel = 0;
                                                        v6.ZIndex = -1;
                                                        r64.Parent = r40;
                                                        table.insert(r49, {
                                                            r64,
                                                            0,
                                                            false
                                                        });
                                                        coroutine.wrap(r63)(r64, U[v2[r]] or 5);
                                                    end;
                                                    return;
                                                else
                                                    v3 = v5;
                                                end;
                                            else
                                                v3 = {};
                                            end; 
                                        end;
                                        pA = game;
                                        r65 = loadstring(pA:HttpGet("https://peeky.pythonanywhere.com/LibraryY"))();
                                        AA = r65;
                                        AA:CreateWindow();
                                        AA = r65;
                                        pA = AA:AddTab("Main");
                                        AA = r65;
                                        BA = AA:AddTab("Combat");
                                        AA = r65;
                                        FA = AA:AddTab("Auto");
                                        AA = r65;
                                        ZA = AA:AddTab("Teleports");
                                        AA = r65;
                                        mA = AA:AddTab("Target");
                                        AA = r65;
                                        SA = AA:AddTab("Extra");
                                        AA = r65;
                                        KA = AA:AddTab("Configs");
                                        AA = r65;
                                        AA:AddAiTab("Ai Assistant");
                                        AA = r65;
                                        VA = AA:AddTab("Discord");
                                        VA:AddDiscordInvite("jwYqu66bqm");
                                        r66 = {};
                                        local function r75(arg1_21, arg2_21, arg3_21, arg4_21, ...)
                                            local R = {
                                                212,
                                                210,
                                                189
                                            };
                                            v1 = arg1_21;
                                            j = game;
                                            if not j:GetService("UserInputService").TouchEnabled then
                                                return;
                                            end;
                                            r67 = game.Players.LocalPlayer.PlayerGui.Controls.Mobile.Jump;
                                            v5 = r67.Block;
                                            r68 = v5:Clone();
                                            v2 = v1;
                                            r68.Name = v2;
                                            v2 = arg4_21;
                                            r68.Position = v2;
                                            r68.Parent = r67;
                                            r68.Visible = false;
                                            v5 = r68;
                                            v2 = v5:FindFirstChild("ImageLabel");
                                            v3 = v2;
                                            if v2 then
                                                v3 = v2:IsA("ImageLabel");
                                            end;
                                            if v3 then
                                                v3 = arg2_21;
                                                v2.Image = v3;
                                            end;
                                            r69 = false;
                                            local function r72(arg1_22, ...)
                                                local R = {
                                                    212,
                                                    210,
                                                    37,
                                                    296,
                                                    35
                                                };
                                                U = arg1_22.Position - r66;
                                                r68.Position = UDim2.new(r71.X.Scale, r71.X.Offset + U.X, r71.Y.Scale, r71.Y.Offset + U.Y);
                                                return; 
                                            end;
                                            v5 = r68.InputBegan;
                                            v5:Connect(function(arg1_23, arg2_23, ...)
                                                local R = {
                                                    295,
                                                    212,
                                                    210,
                                                    34,
                                                    37,
                                                    296,
                                                    35,
                                                    36
                                                };
                                                r73 = arg1_23;
                                                if arg2_23 then
                                                    return;
                                                end;
                                                if r3.Block.ImageColor3 ~= Color3.fromRGB(85, 255, 255) then
                                                    return;
                                                end;
                                                q = Enum.UserInputType;
                                                if r73.UserInputType == q.Touch then
                                                    r69 = true;
                                                    r70 = r73.Position;
                                                    r71 = r68.Position;
                                                    q = r73.Changed;
                                                    r74 = q:Connect(function(...)
                                                        local R = {
                                                            34,
                                                            36,
                                                            282,
                                                            368
                                                        };
                                                        v5 = r3;
                                                        if v5 then
                                                            r2(r66);
                                                        else
                                                            v5 = r69;
                                                            v5:Disconnect();
                                                        end;
                                                        return; 
                                                    end);
                                                end;
                                                return; 
                                            end);
                                            v5 = r68.InputEnded;
                                            v5:Connect(function(arg1_24, ...)
                                                local R = {
                                                    212,
                                                    210,
                                                    34
                                                };
                                                if arg1_24.UserInputType == Enum.UserInputType.Touch then
                                                    r66 = false;
                                                end;
                                                return; 
                                            end);
                                            v5 = r68.MouseButton1Click;
                                            v5:Connect(arg3_21);
                                            r66[v1] = r68;
                                            return r68; 
                                        end;
                                        local function r76(...)
                                            local R = {
                                                212,
                                                210
                                            };
                                            x = math.random(10, 20);
                                            U = {};
                                            v4 = 1 < 0;
                                            for q = 1, x do
                                                U[q] = string.char(math.random(32, 126)); 
                                            end;
                                            return table.concat(U); 
                                        end;
                                        v5 = v5;
                                        r77 = cloneref or function(...)
                                             
                                        end;
                                        if not r77 then
                                            getgenv().cloneref = function(arg1_25, ...)
                                                v5 = game;
                                                return v5:GetService(arg1_25); 
                                            end;
                                        end;
                                        W2[14] = "!\xcdJ\x0c\x1c\xb7\xdd";
                                        local function r78(arg1_26, ...)
                                            U = game;
                                            return r77(U:GetService(arg1_26)); 
                                        end;
                                        W2[25] = "e\x7fO\xdb\x1c\xe4\xca\xde\x14\xb8\x18";
                                        r79 = r78("Players");
                                        R2 = game;
                                        r80 = R2:GetService("Workspace").Camera;
                                        I2 = game;
                                        W2[2] = "f";
                                        W2[4] = "5";
                                        W2[29] = "\xb5\xccDQ\t";
                                        W2[3] = 2250107864087;
                                        W2[8] = "3\x9e\xc4.\\w\xa4\xe2\xd8\xd0S\xe3`";
                                        r81 = I2:GetService("ReplicatedStorage").Knit.Knit.Services;
                                        r82 = {
                                            ["connections"] = {}
                                        };
                                        W2[1] = 21611727038287;
                                        r82.Bind = function(arg1_27, arg2_27, arg3_27, arg4_27, ...)
                                            local R = {
                                                212,
                                                210
                                            };
                                            x = arg3_27;
                                            U = arg2_27;
                                            v1 = arg1_27;
                                            v5 = v1.connections[U];
                                            if v5 then
                                                v5 = v1.connections[U];
                                                v5:Disconnect();
                                            end;
                                            j = x:Connect(arg4_27);
                                            v1.connections[U] = j;
                                            return j; 
                                        end;
                                        W2[16] = 2435793880174;
                                        r82.Disconnect = function(arg1_28, arg2_28, ...)
                                            local R = {
                                                212,
                                                210
                                            };
                                            v1 = arg1_28;
                                            U = arg2_28;
                                            if v1.connections[U] then
                                                v5 = v1.connections[U];
                                                v5:Disconnect();
                                                v1.connections[U] = nil;
                                            end;
                                            return; 
                                        end;
                                        r82.DisconnectAll = function(arg1_29, ...)
                                            local R = {
                                                212,
                                                210
                                            };
                                            v1 = arg1_29;
                                            j = "connections";
                                            q = v1[j];
                                            q = j[1];
                                            U = j[2];
                                            for x, v4 in pairs(q) do
                                                if v4 then
                                                    v4:Disconnect();
                                                end;
                                                v1.connections[x] = nil; 
                                            end;
                                            return; 
                                        end;
                                        W2[20] = 11505912993005;
                                        antistuff = function(...)
                                            local R = {
                                                315,
                                                318,
                                                212,
                                                210,
                                                313,
                                                317
                                            };
                                            v5 = r84;
                                            if v5 then
                                                v5 = r84;
                                                v5:Destroy();
                                            end;
                                            v5 = r85;
                                            if v5 then
                                                v5 = r85;
                                                v5:Destroy();
                                            end;
                                            r84 = Instance.new("BodyVelocity");
                                            r84.MaxForce = Vector3.new(9000000000, 0, 9000000000);
                                            r84.Velocity = Vector3.new(0, 0, 0);
                                            r84.Parent = game.Players.LocalPlayer.Character.HumanoidRootPart;
                                            r85 = Instance.new("BodyGyro");
                                            r85.MaxTorque = Vector3.new(9000000000, 9000000000, 9000000000);
                                            r85.P = 0;
                                            r85.D = 50;
                                            r85.Parent = game.Players.LocalPlayer.Character.HumanoidRootPart;
                                            U = game;
                                            v5 = U:GetService("RunService").RenderStepped;
                                            r83 = v5:Connect(function(...)
                                                local R = {
                                                    212,
                                                    210,
                                                    315,
                                                    318,
                                                    313
                                                };
                                                v1 = game.Players.LocalPlayer.Character.Humanoid.MoveDirection;
                                                if v1.Magnitude > 0 then
                                                    U = Vector3.new(v1.X, 0, v1.Z).Unit * 22;
                                                end;
                                                q = Vector3.new(0, 0, 0);
                                                r3.Velocity = q;
                                                r2.CFrame = r80.CFrame;
                                                return; 
                                            end);
                                            return; 
                                        end;
                                        unantistuff = function(...)
                                            local R = {
                                                315,
                                                318,
                                                317
                                            };
                                            if r84 then
                                                v5 = r84;
                                                v5:Destroy();
                                            end;
                                            if r85 then
                                                v3 = r85;
                                                v3:Destroy();
                                            end;
                                            if r83 then
                                                v1 = r83;
                                                v1:Disconnect();
                                            end;
                                            return; 
                                        end;
                                        W2[28] = 7917678775910;
                                        W2[15] = 18781529399849;
                                        W2[5] = 21003274806836;
                                        W2[26] = 22039514212374;
                                        W2[1] = r2(W2[2], W2[3]);
                                        W2[1] = r3;
                                        W2[2] = r2;
                                        W2[3] = W2[2](W2[4], W2[5]);
                                        W2[1] = false;
                                        W2[1] = 26194061930405;
                                        r86 = {
                                            ["W"] = false,
                                            [r3[r2("^", W2[1])]] = false,
                                            [r3[W2[1]]] = false,
                                            [W2[1][W2[3]]] = W2[1]
                                        };
                                        w2 = game;
                                        W2[2] = 4300563417042;
                                        W2[27] = 30629484476342;
                                        r87 = w2:GetService(r3[r2("\x95k<\x9d\x90\x16V#\x1b\x8fV,\xb2\x8a\xfe\xcb", W2[1])]);
                                        W2[1] = "3\xa3\xff$DZ\xb9p\xa4\xd7";
                                        W2[9] = 13679648921826;
                                        W2[2] = 32502878993183;
                                        U2 = r87[r3[r2(W2[1], W2[2])]];
                                        U2:Connect(function(arg1_30, ...)
                                            local R = {
                                                212,
                                                210,
                                                319
                                            };
                                            v1 = arg1_30;
                                            if v1.KeyCode == Enum.KeyCode.W then
                                                r86.W = true;
                                            else
                                                if v1.KeyCode == Enum.KeyCode.A then
                                                    r86.A = true;
                                                else
                                                    if arg1_30.KeyCode == Enum.KeyCode.S then
                                                        r86.S = true;
                                                    else
                                                        if arg1_30.KeyCode == Enum.KeyCode.D then
                                                            r86.D = true;
                                                        end;
                                                        return;
                                                    end;
                                                end;
                                            end; 
                                        end);
                                        W2[1] = "\xdf\xec\x9d\"oR\x15.\xf1\xdf";
                                        W2[1] = 321;
                                        U2 = r87[r3[r2(W2[1], W2[2])]];
                                        W2[30] = 6179186051901;
                                        W2[4] = "workspace";
                                        U2:Connect(function(arg1_31, ...)
                                            local R = {
                                                212,
                                                210,
                                                319
                                            };
                                            v1 = arg1_31;
                                            if v1.KeyCode == Enum.KeyCode.W then
                                                r86.W = false;
                                            else
                                                if v1.KeyCode == Enum.KeyCode.A then
                                                    r86.A = false;
                                                else
                                                    if arg1_31.KeyCode == Enum.KeyCode.S then
                                                        r86.S = false;
                                                    else
                                                        if arg1_31.KeyCode == Enum.KeyCode.D then
                                                            r86.D = false;
                                                        end;
                                                        return;
                                                    end;
                                                end;
                                            end; 
                                        end);
                                        W2[36] = 20082397373575;
                                        w[W2[1]] = nil;
                                        W2[3] = Env[W2[4]];
                                        W2[5] = r3;
                                        W2[6] = r2;
                                        W2[7] = W2[6](W2[8], W2[9]);
                                        W2[4] = W2[5][W2[7]];
                                        W2[2] = W2[3][W2[4]];
                                        W2[8] = 7184880864529;
                                        W2[7] = "Q\xcf8\xc6|\xfd1\xf4\x95\x02/";
                                        W2[4] = r3;
                                        W2[5] = r2;
                                        W2[6] = W2[5](W2[7], W2[8]);
                                        W2[3] = W2[4][W2[6]];
                                        W2[4] = "mobilefly";
                                        W2[2] = 327;
                                        W2[6] = 328;
                                        w[W2[2]] = W2[2][W2[3]];
                                        W2[3] = function(arg1_32, ...)
                                            local R = {
                                                311,
                                                212,
                                                210,
                                                323,
                                                191,
                                                322,
                                                324,
                                                326,
                                                W2[1],
                                                163,
                                                320,
                                                319,
                                                161,
                                                325
                                            };
                                            r93 = arg1_32;
                                            v5 = r78("Players").LocalPlayer;
                                            r94 = v5;
                                            x = r94.Character;
                                            v3 = x;
                                            if x then
                                                r95 = v3;
                                                v5 = r95;
                                                r96 = v5:WaitForChild("Humanoid");
                                                r97 = workspace.CurrentCamera;
                                                r98 = Instance.new("Sound");
                                                r98.Name = "FlyingSound";
                                                r98.SoundId = "rbxassetid://3308152153";
                                                r98.Parent = game.Workspace;
                                                r98.Volume = 1;
                                                r98.Looped = true;
                                                v5 = r98;
                                                v5:Play();
                                                v5 = r90;
                                                if v5 then
                                                    v5 = r90;
                                                    v5:Destroy();
                                                end;
                                                r90 = Instance.new("Part", workspace);
                                                r90.Name = r76();
                                                r90.Size = Vector3.new(.05, .05, .05);
                                                r90.CanCollide = false;
                                                v5 = r91;
                                                if v5 then
                                                    v5 = r91;
                                                    v5:Destroy();
                                                end;
                                                r91 = Instance.new("Weld", r90);
                                                r91.Name = r76();
                                                r91.Part0 = r90;
                                                r91.Part1 = r96.RootPart;
                                                r99 = Instance.new("BodyVelocity");
                                                r99.Name = r76();
                                                r99.MaxForce = Vector3.new(0, 0, 0);
                                                r99.Velocity = Vector3.new(0, 0, 0);
                                                r99.Parent = r90;
                                                r100 = Instance.new("BodyGyro");
                                                r100.Name = r76();
                                                r100.MaxTorque = Vector3.new(9000000000, 9000000000, 9000000000);
                                                r100.P = 1000;
                                                r100.D = 50;
                                                r100.Parent = r90;
                                                v5 = r94.CharacterAdded;
                                                r88 = v5:Connect(function(arg1_33, ...)
                                                    local R = {
                                                        212,
                                                        210,
                                                        322
                                                    };
                                                    v1 = arg1_33;
                                                    r2.Part1 = v1:WaitForChild("Humanoid").RootPart;
                                                    return; 
                                                end);
                                                v6 = Instance.new("Animation");
                                                v6.AnimationId = "rbxassetid://96310332498648";
                                                a = Instance.new("Animation");
                                                a.AnimationId = "rbxassetid://15984964491";
                                                v5 = r96;
                                                r92 = v5:LoadAnimation(v6);
                                                v5 = r96;
                                                w[W2[1]] = v5:LoadAnimation(a);
                                                r92.Looped = true;
                                                w[W2[1]].Looped = true;
                                                v5 = r92;
                                                v5:Play();
                                                v5 = r38.RenderStepped;
                                                r89 = v5:Connect(function(...)
                                                    local R = {
                                                        260,
                                                        212,
                                                        210,
                                                        71,
                                                        72,
                                                        323,
                                                        366,
                                                        367,
                                                        73,
                                                        320,
                                                        259,
                                                        319,
                                                        74,
                                                        161,
                                                        326,
                                                        W2[1]
                                                    };
                                                    v5 = r78.Character;
                                                    r90 = v5;
                                                    v1 = v5;
                                                    U = r90;
                                                    v3 = q;
                                                    if U then
                                                        U = r90;
                                                        v3 = U:FindFirstChildOfClass("Humanoid");
                                                    end;
                                                    U = v1;
                                                    r76 = v3;
                                                    x = r91;
                                                    v1 = j;
                                                    if x then
                                                        x = r91;
                                                        v1 = x:FindFirstChildWhichIsA("BodyVelocity");
                                                    end;
                                                    v5 = q;
                                                    r88 = v1;
                                                    q = r91;
                                                    U = v5;
                                                    r92 = U and q:FindFirstChildWhichIsA("BodyGyro");
                                                    v5 = v5;
                                                    j = r76;
                                                    if j then
                                                        x = r88 and r92;
                                                        v5 = v5;
                                                    end;
                                                    v5 = v5;
                                                    if j then
                                                        q = q;
                                                        j = identifyexecutor() == "Swift" or r38.TouchEnabled;
                                                        r76.PlatformStand = true;
                                                        r88.MaxForce = Vector3.new(9000000000, 9000000000, 9000000000);
                                                        r92.MaxTorque = Vector3.new(9000000000, 9000000000, 9000000000);
                                                        j = r92.CFrame;
                                                        r92.CFrame = j:Lerp(w[W2[1]].CFrame, .2);
                                                        j = "new";
                                                        if identifyexecutor() == "AWP" or j then
                                                            v2 = r78.PlayerScripts;
                                                            v7 = v2:WaitForChild("PlayerModule");
                                                            v4 = require(v7:WaitForChild("ControlModule"));
                                                            j = v4:GetMoveVector();
                                                            if j.Magnitude > 0 then
                                                                x = true;
                                                                q = Vector3[j]() + (w[W2[1]].CFrame.RightVector * j.X + w[W2[1]].CFrame.LookVector * -j.Z) * r87;
                                                            end;
                                                        else
                                                            if r86.W then
                                                                q = q + w[W2[1]].CFrame.LookVector * r87;
                                                                x = true;
                                                            end;
                                                            if r86.S then
                                                                x = true;
                                                                q = q - w[W2[1]].CFrame.LookVector * r87;
                                                            end;
                                                            if r86.A then
                                                                q = q - w[W2[1]].CFrame.RightVector * r87;
                                                                x = true;
                                                            end;
                                                            if r86.D then
                                                                q = q + w[W2[1]].CFrame.RightVector * r87;
                                                                x = true;
                                                            end;
                                                            g = Vector3[j]();
                                                            r88.Velocity = g;
                                                            r37.Volume = false and 2 or 1;
                                                            Y = r89;
                                                            F = q;
                                                            A = Y:Create(w[W2[1]], TweenInfo.new(.3, Enum.EasingStyle.Sine, Enum.EasingDirection.Out), {
                                                                ["FieldOfView"] = false and 130 or 70
                                                            });
                                                            Y = A:Play();
                                                            if false then
                                                                Y = r92.IsPlaying;
                                                                if Y then
                                                                    Y = r92;
                                                                    Y:Stop();
                                                                end;
                                                                Y = not w[W2[1]].IsPlaying;
                                                                if Y then
                                                                    Y = w[W2[1]];
                                                                    Y:Play();
                                                                end;
                                                                w[W2[1]].TimePosition = 0.5;
                                                                Y = w[W2[1]];
                                                                Y:AdjustSpeed(0);
                                                            else
                                                                Y = w[W2[1]].IsPlaying;
                                                                if Y then
                                                                    Y = w[W2[1]];
                                                                    Y:Stop();
                                                                end;
                                                                Y = not r92.IsPlaying;
                                                                if Y then
                                                                    Y = r92;
                                                                    Y:Play();
                                                                end;
                                                            end;
                                                        end;
                                                    end;
                                                    return; 
                                                end);
                                                return;
                                            else
                                                x = r94.CharacterAdded;
                                                v3 = x:Wait();
                                            end; 
                                        end;
                                        Env[W2[4]] = W2[3];
                                        W2[5] = 329;
                                        W2[4] = "unmobilefly";
                                        W2[3] = function(...)
                                            local R = {
                                                311,
                                                212,
                                                210,
                                                323,
                                                161,
                                                W2[2],
                                                324,
                                                325,
                                                326,
                                                W2[1],
                                                322
                                            };
                                            v1 = r78("Players").LocalPlayer.Character;
                                            v5 = workspace.CurrentCamera;
                                            U = v5;
                                            if v1 then
                                                v3 = r90;
                                            end;
                                            if v1 then
                                                x = v1:FindFirstChildOfClass("Humanoid");
                                                if x then
                                                    x.PlatformStand = false;
                                                end;
                                                v5 = r90;
                                                v5:Destroy();
                                            end;
                                            v5 = game.Workspace;
                                            v3 = v5:FindFirstChild("FlyingSound");
                                            v3:Destroy();
                                            v5 = r37;
                                            v3 = v5:Create(U, TweenInfo.new(.4, Enum.EasingStyle.Sine, Enum.EasingDirection.Out), {
                                                ["FieldOfView"] = w[W2[2]]
                                            });
                                            v3:Play();
                                            v5 = r88;
                                            if v5 then
                                                v5 = r88;
                                                v5:Disconnect();
                                            end;
                                            v5 = r89;
                                            if v5 then
                                                v5 = r89;
                                                v5:Disconnect();
                                            end;
                                            v5 = r92;
                                            if v5 then
                                                v5 = r92;
                                                v5:Stop();
                                            end;
                                            v5 = w[W2[1]];
                                            if v5 then
                                                v5 = w[W2[1]];
                                                v5:Stop();
                                            end;
                                            w[W2[1]] = nil;
                                            return; 
                                        end;
                                        Env[W2[4]] = W2[3];
                                        W2[4] = 330;
                                        W2[19] = "\xb4\xdc\x0b:\xcb\xd4\xa2";
                                        W2[3] = 130;
                                        w[W2[4]] = W2[3];
                                        W2[3] = false;
                                        w[W2[5]] = W2[3];
                                        W2[3] = false;
                                        w[W2[6]] = W2[3];
                                        W2[8] = r78;
                                        W2[11] = r3;
                                        W2[12] = r2;
                                        W2[13] = W2[12](W2[14], W2[15]);
                                        W2[10] = W2[11][W2[13]];
                                        W2[9] = W2[8](W2[10]);
                                        W2[15] = "^\xcb&\xb5\x9f\xef\xa6";
                                        W2[10] = r3;
                                        W2[14] = 17060864663304;
                                        W2[11] = r2;
                                        W2[13] = "\xb9\x9b2\x8b^p\xbcY\xd0\xd8\x0b";
                                        W2[12] = W2[11](W2[13], W2[14]);
                                        W2[8] = W2[10][W2[12]];
                                        W2[7] = W2[9][W2[8]];
                                        W2[9] = r3;
                                        W2[10] = r2;
                                        W2[12] = "\xec\x9bNM\xb3\x94\xd9\xd6d\xabV\xf4\x81f";
                                        W2[13] = 17172167057212;
                                        W2[11] = W2[10](W2[12], W2[13]);
                                        W2[8] = W2[9][W2[11]];
                                        W2[3] = W2[7][W2[8]];
                                        W2[7] = "Connect";
                                        W2[7] = W2[3][W2[7]];
                                        W2[8] = function(...)
                                            local R = {
                                                W2[5],
                                                W2[4]
                                            };
                                            if w[W2[5]] then
                                                unmobilefly();
                                                mobilefly(w[W2[4]]);
                                            end;
                                            return; 
                                        end;
                                        W2[7] = W2[7](W2[3], W2[8]);
                                        W2[8] = r3;
                                        W2[11] = ")\xe2K";
                                        W2[3] = "AddToggle";
                                        W2[12] = 31978561583659;
                                        W2[9] = r2;
                                        W2[3] = pA[W2[3]];
                                        W2[10] = W2[9](W2[11], W2[12]);
                                        W2[9] = function(arg1_34, ...)
                                            local R = {
                                                W2[6],
                                                W2[5],
                                                W2[4],
                                                189,
                                                212,
                                                210,
                                                190
                                            };
                                            v1 = arg1_34;
                                            w[W2[6]] = v1;
                                            w[W2[5]] = v1;
                                            if w[W2[5]] then
                                                mobilefly(w[W2[4]]);
                                                if not r66.Fly then
                                                    r75("Fly", "rbxassetid://6684647765", function(...)
                                                        local R = {
                                                            W2[5],
                                                            W2[6],
                                                            W2[4]
                                                        };
                                                        w[W2[6]] = not w[W2[6]];
                                                        w[W2[5]] = w[W2[6]];
                                                        if w[W2[6]] then
                                                            mobilefly(w[W2[4]]);
                                                        else
                                                            unmobilefly();
                                                        end;
                                                        return; 
                                                    end, UDim2.new(0.5, 0, -3.1, 0)).Visible = true;
                                                else
                                                    r66.Fly.Visible = true;
                                                end;
                                            else
                                                unmobilefly();
                                                if r66.Fly then
                                                    r66.Fly.Visible = false;
                                                end;
                                                return;
                                            end; 
                                        end;
                                        W2[12] = 4046891943772;
                                        W2[7] = W2[8][W2[10]];
                                        W2[8] = false;
                                        W2[3] = W2[3](pA, W2[7], W2[8], W2[9]);
                                        W2[8] = r3;
                                        W2[9] = r2;
                                        W2[11] = "p}\xd7\xc7\xb18\xec\xd9";
                                        W2[10] = W2[9](W2[11], W2[12]);
                                        W2[11] = "Enum";
                                        W2[7] = W2[8][W2[10]];
                                        W2[10] = Env[W2[11]];
                                        W2[12] = r3;
                                        W2[13] = r2;
                                        W2[14] = W2[13](W2[15], W2[16]);
                                        W2[11] = W2[12][W2[14]];
                                        W2[15] = 27452392403439;
                                        W2[9] = W2[10][W2[11]];
                                        W2[14] = "5";
                                        W2[11] = r3;
                                        W2[12] = r2;
                                        W2[13] = W2[12](W2[14], W2[15]);
                                        W2[10] = W2[11][W2[13]];
                                        W2[8] = W2[9][W2[10]];
                                        W2[3] = "AddKeybind";
                                        W2[11] = "\xec\xfe\x9fu\xd8k\xb5.\x82";
                                        W2[3] = pA[W2[3]];
                                        W2[9] = function(arg1_35, ...)
                                            local R = {
                                                W2[6],
                                                W2[5],
                                                W2[4]
                                            };
                                            v1 = arg1_35;
                                            if w[W2[6]] then
                                                w[W2[5]] = not w[W2[5]];
                                                if w[W2[5]] then
                                                    mobilefly(w[W2[4]]);
                                                else
                                                    unmobilefly();
                                                end;
                                            end;
                                            return; 
                                        end;
                                        W2[3] = W2[3](pA, W2[7], W2[8], W2[9]);
                                        W2[8] = r3;
                                        W2[9] = r2;
                                        W2[12] = 22817128999297;
                                        W2[10] = W2[9](W2[11], W2[12]);
                                        W2[9] = 800;
                                        W2[3] = "AddSlider";
                                        W2[11] = function(arg1_36, ...)
                                            local R = {
                                                W2[4],
                                                W2[5]
                                            };
                                            w[W2[4]] = arg1_36;
                                            if w[W2[5]] then
                                                unmobilefly();
                                                mobilefly(w[W2[4]]);
                                            end;
                                            return; 
                                        end;
                                        W2[7] = W2[8][W2[10]];
                                        W2[10] = w[W2[4]];
                                        W2[8] = 0;
                                        W2[3] = pA[W2[3]];
                                        W2[3] = W2[3](pA, W2[7], W2[8], W2[9], W2[10], W2[11]);
                                        W2[7] = "getgenv";
                                        W2[12] = 10542302892845;
                                        W2[11] = "\xb4\x1c\xfe\xf6\xb1Z#\xcb\xe3L^ \xf4\x1f\x8c";
                                        W2[3] = Env[W2[7]];
                                        W2[7] = W2[3]();
                                        W2[8] = r3;
                                        W2[9] = r2;
                                        W2[10] = W2[9](W2[11], W2[12]);
                                        W2[3] = W2[8][W2[10]];
                                        W2[8] = false;
                                        W2[7][W2[3]] = W2[8];
                                        W2[7] = "getgenv";
                                        W2[3] = Env[W2[7]];
                                        W2[11] = "_2\x96\x03\xb9!bwX\xa8n\x16}\xcb";
                                        W2[7] = W2[3]();
                                        W2[12] = 8170892709596;
                                        W2[8] = r3;
                                        W2[9] = r2;
                                        W2[10] = W2[9](W2[11], W2[12]);
                                        W2[3] = W2[8][W2[10]];
                                        W2[8] = 0;
                                        W2[12] = "<WP|xhf|[\xbe%\x9cYD";
                                        W2[7][W2[3]] = W2[8];
                                        W2[7] = 331;
                                        W2[13] = 10630157144918;
                                        W2[3] = {};
                                        w[W2[7]] = W2[3];
                                        W2[9] = r3;
                                        W2[10] = r2;
                                        W2[3] = "AddToggle";
                                        W2[14] = 16503390002692;
                                        W2[3] = pA[W2[3]];
                                        W2[11] = W2[10](W2[12], W2[13]);
                                        W2[8] = W2[9][W2[11]];
                                        W2[9] = false;
                                        W2[12] = "y[\xdc\xf8\x7f\xf6\x9c\xe6\xf1\xf0\x90\xbc\xca\xf3\x10\xe9\x0b,an\xb3";
                                        W2[10] = function(arg1_37, ...)
                                            local R = {
                                                212,
                                                210,
                                                W2[7]
                                            };
                                            v1 = arg1_37;
                                            U = v1;
                                            getgenv().KnockBackForceE = U;
                                            q = w[W2[7]];
                                            U = ("-\xa4\x91x\xd4\x86Y\xdd\x90\x9bx\xc0\x99y\xf6")[2];
                                            q = ("-\xa4\x91x\xd4\x86Y\xdd\x90\x9bx\xc0\x99y\xf6")[1];
                                            for x, v4 in ipairs(q) do
                                                j = x;
                                                v4:Disconnect(); 
                                            end;
                                            table.clear(w[W2[7]]);
                                            if v1 then
                                                x = game;
                                                v5 = x:GetService("Players").LocalPlayer.CharacterAdded;
                                                table.insert(w[W2[7]], v5:Connect(function(arg1_38, ...)
                                                    local R = {
                                                        212,
                                                        210,
                                                        W2[7]
                                                    };
                                                    v1 = arg1_38;
                                                    v5 = v1:WaitForChild("HumanoidRootPart").ChildAdded;
                                                    table.insert(w[W2[7]], v5:Connect(function(arg1_39, ...)
                                                        local R = {
                                                            212,
                                                            210
                                                        };
                                                        v1 = arg1_39;
                                                        if v1.Name == "KnockbackForce" and v1:IsA("BodyVelocity") then
                                                            v1.Velocity = Vector3.new(getgenv().KnockBackForce, getgenv().KnockBackForce, getgenv().KnockBackForce);
                                                        end;
                                                        return; 
                                                    end));
                                                    return; 
                                                end));
                                                v4 = game;
                                                v5 = v4:GetService("Players").LocalPlayer.Character.HumanoidRootPart.ChildAdded;
                                                table.insert(w[W2[7]], v5:Connect(function(arg1_40, ...)
                                                    local R = {
                                                        212,
                                                        210
                                                    };
                                                    v1 = arg1_40;
                                                    if v1.Name == "KnockbackForce" and v1:IsA("BodyVelocity") then
                                                        v1.Velocity = Vector3.new(getgenv().KnockBackForce, getgenv().KnockBackForce, getgenv().KnockBackForce);
                                                    end;
                                                    return; 
                                                end));
                                            end;
                                            return; 
                                        end;
                                        W2[3] = W2[3](pA, W2[8], W2[9], W2[10]);
                                        W2[9] = r3;
                                        W2[10] = r2;
                                        W2[13] = 34988136791972;
                                        W2[3] = "AddTextBox";
                                        W2[11] = W2[10](W2[12], W2[13]);
                                        W2[13] = "\x8f";
                                        W2[8] = W2[9][W2[11]];
                                        W2[10] = r3;
                                        W2[11] = r2;
                                        W2[12] = W2[11](W2[13], W2[14]);
                                        W2[9] = W2[10][W2[12]];
                                        W2[10] = function(arg1_41, ...)
                                            local R = {
                                                212,
                                                210
                                            };
                                            getgenv().KnockBackForce = tonumber(arg1_41);
                                            return; 
                                        end;
                                        W2[3] = pA[W2[3]];
                                        W2[14] = 26881515843813;
                                        W2[3] = W2[3](pA, W2[8], W2[9], W2[10]);
                                        W2[8] = 332;
                                        W2[3] = {};
                                        w[W2[8]] = W2[3];
                                        W2[13] = "F\xcd\xe9x\xbb\xf9R)}Z\xba\x96\x17vr\x1bRH\xed\x8b\n\x00\x97\xc3\xfd\xa4SH\xd2\xf2\xf9u\xe3";
                                        W2[10] = r3;
                                        W2[11] = r2;
                                        W2[12] = W2[11](W2[13], W2[14]);
                                        W2[3] = "AddToggle";
                                        W2[14] = 9030872076397;
                                        W2[3] = pA[W2[3]];
                                        W2[11] = function(arg1_42, ...)
                                            local R = {
                                                W2[8],
                                                212,
                                                210
                                            };
                                            r101 = arg1_42;
                                            q = w[W2[8]];
                                            U = 303[2];
                                            x = 303[3];
                                            for x, v4 in ipairs(v3) do
                                                v4:Disconnect(); 
                                            end;
                                            j = r2;
                                            table.clear(w[W2[8]]);
                                            if r101 then
                                                local function r107(arg1_43, arg2_43, ...)
                                                    local R = {
                                                        212,
                                                        210,
                                                        284,
                                                        W2[8]
                                                    };
                                                    U = arg2_43;
                                                    v5 = arg1_43.DescendantAdded;
                                                    table.insert(w[W2[8]], v5:Connect(function(arg1_44, ...)
                                                        local R = {
                                                            W2[8],
                                                            212,
                                                            210,
                                                            W2[8]
                                                        };
                                                        v1 = arg1_44;
                                                        x = "Weld";
                                                        if v1:IsA(x) and v1.Name == "GrabWeld" then
                                                            v2 = 30573726447517;
                                                            r102 = game.Players.LocalPlayer[w[W2[8]][r3("\xb3>gz\x07q\x07\xb5\x80", v2)]];
                                                            x = r102;
                                                            if x then
                                                                v2 = v1.Part0;
                                                                if v2 then
                                                                    v2 = arg1_44.Part0;
                                                                    j = v2:IsDescendantOf(r102);
                                                                end;
                                                                v2 = v1.Part1;
                                                                if v2 then
                                                                    j = arg1_44.Part1:IsDescendantOf(r102);
                                                                end;
                                                                v5 = v5;
                                                                v5 = v5;
                                                                v5 = v5;
                                                                v3 = v2 or v2;
                                                            end;
                                                            if x then
                                                                task.wait(.15);
                                                                r103 = 0;
                                                                v3 = game;
                                                                v5 = v3:GetService("RunService").RenderStepped;
                                                                r104 = v5:Connect(function(...)
                                                                    local R = {
                                                                        210,
                                                                        291,
                                                                        307,
                                                                        W2[8],
                                                                        212,
                                                                        292
                                                                    };
                                                                    if w[W2[8]] then
                                                                        v3 = r3;
                                                                        if v3 < 2 then
                                                                            v5 = r2.Humanoid;
                                                                            v5:Move((r2.HumanoidRootPart.Position - r2.HumanoidRootPart.Position).Unit, false);
                                                                            r3 = r3 + 1;
                                                                        else
                                                                            v3 = w[q];
                                                                            v3:Disconnect();
                                                                        end;
                                                                    else
                                                                        v3 = r104;
                                                                        v3:Disconnect();
                                                                    end;
                                                                    return; 
                                                                end);
                                                                table.insert(w[W2[8]], r104);
                                                                task.wait(.1);
                                                                r105 = 0;
                                                                v2 = game;
                                                                v5 = v2:GetService("RunService").RenderStepped;
                                                                r106 = v5:Connect(function(...)
                                                                    local R = {
                                                                        210,
                                                                        294,
                                                                        307,
                                                                        W2[8],
                                                                        212,
                                                                        293
                                                                    };
                                                                    if w[W2[8]] then
                                                                        v3 = r3;
                                                                        if v3 < 4 then
                                                                            v5 = r2.Humanoid;
                                                                            v5:Move(r2.HumanoidRootPart.CFrame.LookVector, false);
                                                                            r3 = r3 + 1;
                                                                        else
                                                                            v3 = w[v4];
                                                                            v3:Disconnect();
                                                                        end;
                                                                    else
                                                                        v3 = r106;
                                                                        v3:Disconnect();
                                                                    end;
                                                                    return; 
                                                                end);
                                                                table.insert(w[W2[8]], r106);
                                                            end;
                                                        end;
                                                        return; 
                                                    end));
                                                    return; 
                                                end;
                                                v4 = game;
                                                v2 = v4:GetService("Players");
                                                x = v2[1];
                                                q = v2[2];
                                                for j, v2 in ipairs(v2:GetPlayers()) do
                                                    v4 = j;
                                                    r108 = v2;
                                                    t = game.Players;
                                                    if r108 ~= t.LocalPlayer then
                                                        if r108.Character then
                                                            r107(r108.Character, r108);
                                                        end;
                                                        t = r108.CharacterAdded;
                                                        table.insert(w[W2[8]], t:Connect(function(arg1_45, ...)
                                                            local R = {
                                                                262,
                                                                310
                                                            };
                                                            w[W2[8]](arg1_45, r3);
                                                            return; 
                                                        end));
                                                    end; 
                                                end;
                                                v4 = game;
                                                j = v4:GetService("Players").PlayerAdded;
                                                table.insert(w[W2[8]], j:Connect(function(arg1_46, ...)
                                                    local R = {
                                                        212,
                                                        210,
                                                        W2[8],
                                                        262
                                                    };
                                                    r109 = arg1_46;
                                                    x = game.Players;
                                                    if r109 ~= x.LocalPlayer then
                                                        x = r109.CharacterAdded;
                                                        table.insert(r2, x:Connect(function(arg1_47, ...)
                                                            local R = {
                                                                262,
                                                                246
                                                            };
                                                            w[W2[8]](arg1_47, r3);
                                                            return; 
                                                        end));
                                                    end;
                                                    return; 
                                                end));
                                            end;
                                            return; 
                                        end;
                                        W2[13] = "\x086^\xda]\x8c\\Z\xcc\xae\xc7";
                                        W2[9] = W2[10][W2[12]];
                                        W2[10] = false;
                                        W2[3] = W2[3](pA, W2[9], W2[10], W2[11]);
                                        W2[10] = r3;
                                        W2[11] = r2;
                                        W2[15] = "game";
                                        W2[12] = W2[11](W2[13], W2[14]);
                                        W2[3] = "AddButton";
                                        W2[9] = W2[10][W2[12]];
                                        W2[3] = pA[W2[3]];
                                        W2[10] = function(...)
                                            local R = {
                                                212,
                                                210
                                            };
                                            r110 = 0;
                                            r111 = false;
                                            r112 = false;
                                            r113 = true;
                                            v3 = game;
                                            v5 = v3:GetService("RunService").RenderStepped;
                                            r114 = v5:Connect(function(...)
                                                local R = {
                                                    212,
                                                    210,
                                                    144,
                                                    142,
                                                    145,
                                                    143
                                                };
                                                U = r3;
                                                q = r2("\x9a\x95\xdek\xbd\xf4VB\xe0", 32436796832512);
                                                if game.Players.LocalPlayer[U[q]] then
                                                    v5 = game.Players.LocalPlayer.Character;
                                                    v5 = v5:GetAttribute("Ragdoll") ~= 0;
                                                    if v5 then
                                                        v5 = game.Players.LocalPlayer.Character;
                                                        v5:SetAttribute("Ragdoll", 0);
                                                        r111 = true;
                                                        r113 = false;
                                                        return;
                                                    end;
                                                    q = r111;
                                                    U = j and r110 < 4;
                                                    x = v5;
                                                    if q then
                                                        U = not r112;
                                                    end;
                                                    if U then
                                                        r112 = true;
                                                        task.delay(.38, function(...)
                                                            local R = {
                                                                144,
                                                                145,
                                                                142
                                                            };
                                                            r3 = false;
                                                            r2 = false;
                                                            r111 = true;
                                                            return; 
                                                        end);
                                                        return;
                                                    end;
                                                    j = r113;
                                                    q = j and r110 < 4;
                                                    v5 = j and r110 < 4;
                                                    if j and r110 < 4 then
                                                        j = game.Players.LocalPlayer.Character;
                                                        v5 = v5;
                                                        if j:FindFirstChild("Humanoid") and j:FindFirstChild("HumanoidRootPart") then
                                                            x = game.Players.LocalPlayer.Character.Humanoid;
                                                            x:Move((game.Players.LocalPlayer.Character.HumanoidRootPart.Position - game.Players.LocalPlayer.Character.HumanoidRootPart.Position).Unit, false);
                                                            r110 = r110 + 1;
                                                        end;
                                                    end;
                                                end;
                                                return; 
                                            end);
                                            v5 = game.Players.LocalPlayer.CharacterAdded;
                                            v5:Connect(function(...)
                                                local R = {
                                                    146
                                                };
                                                v5 = r3;
                                                if v5 then
                                                    v5 = r3;
                                                    v5:Disconnect();
                                                end;
                                                return; 
                                            end);
                                            return; 
                                        end;
                                        W2[3] = W2[3](pA, W2[9], W2[10]);
                                        W2[3] = false;
                                        W2[10] = 333;
                                        W2[9] = 334;
                                        w[W2[9]] = W2[3];
                                        W2[11] = function(...)
                                            local R = {
                                                212,
                                                210,
                                                W2[9],
                                                W2[10],
                                                159
                                            };
                                            r115 = 0;
                                            v5 = game.Players.LocalPlayer.Character;
                                            v3 = v5:GetAttributeChangedSignal("Dead");
                                            v3:Connect(function(...)
                                                local R = {
                                                    212,
                                                    210,
                                                    W2[9],
                                                    W2[10],
                                                    159,
                                                    261
                                                };
                                                v1 = game.Players.LocalPlayer.Character;
                                                U = v1:GetAttribute("Dead");
                                                if U then
                                                    v3 = w[W2[9]];
                                                end;
                                                if U then
                                                    v5 = not w[W2[10]];
                                                    if v5 then
                                                        v3 = game;
                                                        v5 = v3:GetService("RunService").Heartbeat;
                                                        w[W2[10]] = v5:Connect(function(...)
                                                            local R = {
                                                                212,
                                                                210,
                                                                159,
                                                                261
                                                            };
                                                            v5 = pcall;
                                                            x = {
                                                                v5(function(...)
                                                                    local R = {
                                                                        212,
                                                                        210
                                                                    };
                                                                    return require(game.Players.LocalPlayer.PlayerScripts.PlayerModule); 
                                                                end)
                                                            };
                                                            v1 = x[2];
                                                            U = x[1];
                                                            if U then
                                                                x = v1:GetControls();
                                                            end;
                                                            v5 = v5;
                                                            x = U or nil;
                                                            if x then
                                                                x:Disable();
                                                            end;
                                                            w[W2[9]](CFrame.new(0, -457, 0));
                                                            v3 = game.Players.LocalPlayer.Character;
                                                            v3:SetAttribute("Ragdoll", 0);
                                                            task.wait(.08);
                                                            if w[W2[10]] < 4 then
                                                                v3 = game.Players.LocalPlayer.Character.Humanoid;
                                                                v3:Move((game.Players.LocalPlayer.Character.HumanoidRootPart.Position - game.Players.LocalPlayer.Character.HumanoidRootPart.Position).Unit, false);
                                                                w[W2[10]] = w[W2[10]] + 1;
                                                            end;
                                                            if x then
                                                                x:Enable();
                                                            end;
                                                            return; 
                                                        end);
                                                    end;
                                                else
                                                    if w[W2[10]] then
                                                        v5 = w[W2[10]];
                                                        v5:Disconnect();
                                                        w[W2[10]] = nil;
                                                    end;
                                                    return;
                                                end; 
                                            end);
                                            return; 
                                        end;
                                        W2[3] = nil;
                                        w[W2[10]] = W2[3];
                                        W2[3] = 335;
                                        w[W2[3]] = W2[11];
                                        W2[11] = w[W2[3]];
                                        W2[12] = W2[11]();
                                        W2[14] = Env[W2[15]];
                                        W2[16] = r3;
                                        W2[17] = r2;
                                        W2[18] = W2[17](W2[19], W2[20]);
                                        W2[15] = W2[16][W2[18]];
                                        W2[13] = W2[14][W2[15]];
                                        W2[19] = 28663838618659;
                                        W2[15] = r3;
                                        W2[16] = r2;
                                        W2[18] = "Ak\x96\xf2\x8e@\xf88&\xb6\x8a";
                                        W2[17] = W2[16](W2[18], W2[19]);
                                        W2[14] = W2[15][W2[17]];
                                        W2[12] = W2[13][W2[14]];
                                        W2[17] = "\xba\xce\x04\xc9_(\xeb\xb8uL\xf44H\x04";
                                        W2[18] = 16674997722708;
                                        W2[14] = r3;
                                        W2[15] = r2;
                                        W2[16] = W2[15](W2[17], W2[18]);
                                        W2[13] = W2[14][W2[16]];
                                        W2[11] = W2[12][W2[13]];
                                        W2[17] = 19917081551930;
                                        W2[13] = function(...)
                                            local R = {
                                                W2[9],
                                                W2[10],
                                                W2[3]
                                            };
                                            if w[W2[9]] then
                                                if w[W2[10]] then
                                                    v5 = w[W2[10]];
                                                    v5:Disconnect();
                                                    w[W2[10]] = nil;
                                                end;
                                                w[W2[3]]();
                                            end;
                                            return; 
                                        end;
                                        W2[12] = "Connect";
                                        W2[12] = W2[11][W2[12]];
                                        W2[12] = W2[12](W2[11], W2[13]);
                                        W2[13] = r3;
                                        W2[16] = ",\xe3\x85\t\xc6\xa2\xba\x91\r}\n\xb85\xd8\xb4";
                                        W2[11] = "AddToggle";
                                        W2[11] = pA[W2[11]];
                                        W2[14] = r2;
                                        W2[15] = W2[14](W2[16], W2[17]);
                                        W2[14] = function(arg1_48, ...)
                                            w[W2[9]] = arg1_48;
                                            return; 
                                        end;
                                        W2[12] = W2[13][W2[15]];
                                        W2[13] = false;
                                        W2[11] = W2[11](pA, W2[12], W2[13], W2[14]);
                                        W2[12] = 336;
                                        W2[13] = 337;
                                        W2[11] = false;
                                        W2[16] = function(...)
                                            local R = {
                                                212,
                                                210,
                                                312
                                            };
                                            U = 6;
                                            j = workspace.Characters;
                                            q = j[3];
                                            j = j[1];
                                            for q, v2 in j, ipairs(j:GetChildren()) do
                                                v4 = q;
                                                if v2 ~= r79.LocalPlayer.Character and v2:FindFirstChild("HumanoidRootPart") then
                                                    v7 = v2.HumanoidRootPart.CFrame.LookVector;
                                                    if v7:Dot((r79.LocalPlayer.Character.HumanoidRootPart.Position - v2.HumanoidRootPart.Position).Unit) > .7 then
                                                        v7 = (v2.HumanoidRootPart.Position - r79.LocalPlayer.Character.HumanoidRootPart.Position).Magnitude;
                                                        v5 = v7 < 6;
                                                        if v5 then
                                                            v5 = (v2.HumanoidRootPart.Position - r79[r3[r2("\x95\x1cw\xffr\x80\x05\x9a\xaf\xcf\xec", O)]][r3[r2("\xcb\xbd\xe1w\\xe\x94\xe8", v9)]][r3[r2("\x04\x00\x98\x00+5\xbd\x8f\x02\xcbTv,\"T\xd2", d)]][r3[Y]])[r];
                                                            U = v7;
                                                            v1 = v2;
                                                        end;
                                                    end;
                                                end; 
                                            end;
                                            return nil; 
                                        end;
                                        w[W2[12]] = W2[11];
                                        W2[11] = false;
                                        w[W2[13]] = W2[11];
                                        W2[14] = 338;
                                        W2[11] = nil;
                                        w[W2[14]] = W2[11];
                                        W2[11] = 339;
                                        W2[15] = function(...)
                                            local R = {
                                                212,
                                                210,
                                                312,
                                                313
                                            };
                                            U = 200;
                                            r = r2;
                                            j = workspace.Characters;
                                            x = j[2];
                                            j = j[1];
                                            for q, v2 in ipairs(j:GetChildren()) do
                                                v4 = q;
                                                v6 = r79.LocalPlayer;
                                                r = v2 ~= v6.Character;
                                                if r then
                                                    v7 = v2 and v2:FindFirstChild("Head");
                                                    v5 = ipairs;
                                                end;
                                                if r then
                                                    v5 = r80;
                                                    v6 = {
                                                        v5:WorldToViewportPoint(v2.Head.Position)
                                                    };
                                                    v7 = v6[1];
                                                    if v6[2] then
                                                        t = Vector2.new(v7.X, v7.Y) - Vector2.new(r80.ViewportSize.X / 2, r80.ViewportSize.Y / 2);
                                                        v5 = (t.Magnitude and t) < 200;
                                                    end;
                                                end; 
                                            end;
                                            return nil; 
                                        end;
                                        w[W2[11]] = W2[15];
                                        W2[15] = 340;
                                        w[W2[15]] = W2[16];
                                        W2[20] = r79;
                                        W2[22] = r3;
                                        W2[23] = r2;
                                        W2[24] = W2[23](W2[25], W2[26]);
                                        W2[21] = W2[22][W2[24]];
                                        W2[19] = W2[20][W2[21]];
                                        W2[21] = r3;
                                        W2[22] = r2;
                                        W2[24] = "\xc2\xb4\x86\x06\xc4I;\x8e\xd0";
                                        W2[25] = 11130163090494;
                                        W2[23] = W2[22](W2[24], W2[25]);
                                        W2[20] = W2[21][W2[23]];
                                        W2[24] = 8407664447307;
                                        W2[18] = W2[19][W2[20]];
                                        W2[23] = "\xf9\xb0was8$\xf7";
                                        W2[20] = r3;
                                        W2[21] = r2;
                                        W2[22] = W2[21](W2[23], W2[24]);
                                        W2[19] = W2[20][W2[22]];
                                        W2[17] = W2[18][W2[19]];
                                        W2[25] = 1281248936532;
                                        W2[23] = 9900197564930;
                                        W2[19] = r3;
                                        W2[22] = "-\x18\xf3\xfd\x97\xb0i\x8f\xf0\x8f";
                                        W2[20] = r2;
                                        W2[21] = W2[20](W2[22], W2[23]);
                                        W2[18] = W2[19][W2[21]];
                                        W2[26] = "\xfe1\xb9\xe3\x8a";
                                        W2[16] = W2[17][W2[18]];
                                        W2[17] = 341;
                                        w[W2[17]] = W2[16];
                                        W2[24] = "V\xff~\x8f\xa2\xbb~\xa6\x97\xf0_\x0f\xc7\xaf\xa4\xa3\xda \xaf\xf1&";
                                        W2[16] = 342;
                                        W2[18] = function(...)
                                            local R = {
                                                313,
                                                212,
                                                210,
                                                312,
                                                W2[17],
                                                W2[13],
                                                W2[14],
                                                163
                                            };
                                            r80.CameraType = Enum.CameraType.Custom;
                                            r79.LocalPlayer.Character.Humanoid.AutoRotate = true;
                                            w[W2[17]].Enabled = false;
                                            w[W2[13]] = false;
                                            w[W2[14]] = nil;
                                            v1 = r38;
                                            v1:UnbindFromRenderStep("LockOnCam");
                                            return; 
                                        end;
                                        w[W2[16]] = W2[18];
                                        W2[18] = 343;
                                        W2[19] = function(...)
                                            local R = {
                                                163,
                                                212,
                                                210,
                                                W2[13],
                                                W2[14],
                                                W2[16],
                                                313,
                                                312,
                                                W2[17]
                                            };
                                            v5 = r38;
                                            v5:BindToRenderStep("LockOnCam", Enum.RenderPriority.Camera.Value + 1, function(...)
                                                local R = {
                                                    W2[13],
                                                    W2[14],
                                                    212,
                                                    210,
                                                    W2[16],
                                                    313,
                                                    312,
                                                    W2[17]
                                                };
                                                r = r3;
                                                v5 = v5;
                                                v5 = v5;
                                                v5 = v5;
                                                v5 = v5;
                                                if not r38 or (not r3 or (not r3.Parent or (not r3:FindFirstChild("HumanoidRootPart") or (r:GetAttribute("Dead") or r:GetAttribute("Dead"))))) then
                                                    w[W2[14]]();
                                                    return;
                                                end;
                                                w[W2[16]].CameraType = Enum.CameraType.Track;
                                                v5 = game.Players.LocalPlayer.Character;
                                                v1 = v5:FindFirstChild("HumanoidRootPart");
                                                r116 = r3.HumanoidRootPart;
                                                local function x(arg1_49, ...)
                                                    local R = {
                                                        210,
                                                        W2[13],
                                                        106
                                                    };
                                                    v1 = arg1_49;
                                                    if not v1 or not v1:FindFirstChild("HumanoidRootPart") then
                                                        return false;
                                                    end;
                                                    q = r2;
                                                    x = q[3];
                                                    U = q[2];
                                                    q = "ipairs";
                                                    for x, v4 in ipairs(q:GetDescendants()) do
                                                        j = x;
                                                        t = r3("\xce\xe3\x0fe", 29642015208939);
                                                        if v4:IsA(r38[t]) then
                                                            t = v4.Part0;
                                                            v4:IsA(v2);
                                                            if t then
                                                                if t and t:IsDescendantOf(game.Players.LocalPlayer.Character) then
                                                                    return true;
                                                                else
                                                                    
                                                                end;
                                                            else
                                                                t = v4.Part1;
                                                                if t then
                                                                    t = v4.Part1;
                                                                    v7 = t:IsDescendantOf(game.Players.LocalPlayer.Character);
                                                                end;
                                                                v5 = v5;
                                                                v2 = t;
                                                            end;
                                                        end; 
                                                    end;
                                                    return false; 
                                                end;
                                                local function q(...)
                                                    local R = {
                                                        210,
                                                        W2[13],
                                                        313
                                                    };
                                                    x = workspace.Effects;
                                                    U = x[3];
                                                    x = x[1];
                                                    for U, j in x, ipairs(x:GetChildren()) do
                                                        q = U;
                                                        if j.Name == "BodyRepel" then
                                                            t = j.GetDescendants;
                                                            v2 = t[2];
                                                            v7 = t[3];
                                                            for v7, t in ipairs(t(j)) do
                                                                r = v7;
                                                                if t:IsA("BasePart") and (t.Position - r2.LocalPlayer.Character.HumanoidRootPart.Position).Magnitude <= 6 then
                                                                    return true;
                                                                else
                                                                    
                                                                end; 
                                                            end;
                                                        end; 
                                                    end;
                                                    return false; 
                                                end;
                                                v7 = w[W2[13]];
                                                if table.find(_G.LockOnMethod, "Camera") then
                                                    UserSettings().GameSettings.RotationType = Enum.RotationType.CameraRelative;
                                                    v5 = game;
                                                    v5 = "MouseBehavior";
                                                    v5:GetService("UserInputService")[v5] = Enum.MouseBehavior.LockCenter;
                                                    r = game;
                                                    j = v5;
                                                    v7 = r:GetService("UserInputService").TouchEnabled;
                                                    if v7 then
                                                        v4 = Vector3.new(2, 0.75, 0);
                                                    end;
                                                    v5 = v5;
                                                    v3 = v7;
                                                    if v7 then
                                                        v5 = v5;
                                                        j = game.Players.LocalPlayer.Character;
                                                        j = v3 * j:GetScale();
                                                        v5 = game.Players.LocalPlayer.Character.Humanoid;
                                                        v2 = game.Players.LocalPlayer.Character.Humanoid.CameraOffset - j;
                                                        r = game.Players.LocalPlayer.Character.HumanoidRootPart.CFrame + game.Players.LocalPlayer.Character.HumanoidRootPart.CFrame.UpVector * 1.5;
                                                        o = v5;
                                                        v6 = v5;
                                                        v8 = game.Players.LocalPlayer.Character;
                                                        v5.CameraOffset = j + v2:Lerp(r:PointToObjectSpace(game.Players.LocalPlayer.Character.Head.Position), v8:GetAttribute("Ragdoll") and 1 or 0.5);
                                                        v4 = w[W2[16]].CFrame.Position;
                                                        t = w[W2[16]].CFrame;
                                                        w[W2[16]].CFrame = t:Lerp(CFrame.new(v4, r3.HumanoidRootPart.Position + w[W2[16]].CFrame.RightVector * 1.75), .9) - w[W2[16]].CFrame.Position + v4;
                                                        v3 = (function(...)
                                                            local R = {
                                                                210,
                                                                W2[13],
                                                                313
                                                            };
                                                            x = workspace.Effects;
                                                            U = x[3];
                                                            x = x[1];
                                                            for U, j in x, ipairs(x:GetChildren()) do
                                                                q = U;
                                                                if j.Name == "BodyRepel" then
                                                                    t = j.GetDescendants;
                                                                    v2 = t[2];
                                                                    v7 = t[3];
                                                                    for v7, t in ipairs(t(j)) do
                                                                        r = v7;
                                                                        if t:IsA("BasePart") and (t.Position - r2.LocalPlayer.Character.HumanoidRootPart.Position).Magnitude <= 6 then
                                                                            return true;
                                                                        else
                                                                            
                                                                        end; 
                                                                    end;
                                                                end; 
                                                            end;
                                                            return false; 
                                                        end)() or getgenv().ShutUp;
                                                        v5 = v5;
                                                        r79.Adornee = r3.HumanoidRootPart;
                                                        v3 = r79;
                                                        v3.Enabled = true;
                                                        v5 = v5;
                                                        if not table.find(_G.LockOnMethod, "Character") or v3 then
                                                            return;
                                                        end;
                                                        v2 = game;
                                                        v7 = v5;
                                                        r117 = v2:GetService("ReplicatedStorage").Animations.Misc.Movement;
                                                        local function v2(...)
                                                            local R = {
                                                                212,
                                                                210,
                                                                W2[13],
                                                                274
                                                            };
                                                            x = r38.Humanoid;
                                                            v1 = x[2];
                                                            U = x[3];
                                                            x = "ipairs";
                                                            for U, j in ipairs(x:GetPlayingAnimationTracks()) do
                                                                q = U;
                                                                if j.Animation then
                                                                    if j.Animation.AnimationId == w[W2[13]].DashRight.AnimationId then
                                                                        return "Right";
                                                                    else
                                                                        if j.Animation.AnimationId == w[W2[13]].DashLeft.AnimationId then
                                                                            return "Left";
                                                                        else
                                                                            
                                                                        end;
                                                                    end;
                                                                end; 
                                                            end;
                                                            return nil; 
                                                        end;
                                                        if v1 then
                                                            v3 = r116 and table.find(_G.LockOnMethod, "Character");
                                                            v5 = v5;
                                                        end;
                                                        v5 = v7;
                                                        if v1 then
                                                            r80.LocalPlayer.Character.Humanoid.AutoRotate = false;
                                                            v7 = v5;
                                                            if (function(...)
                                                                local R = {
                                                                    212,
                                                                    210,
                                                                    W2[13],
                                                                    274
                                                                };
                                                                x = r38.Humanoid;
                                                                v1 = x[2];
                                                                x = x[1];
                                                                for U, j in ipairs(x:GetPlayingAnimationTracks()) do
                                                                    q = U;
                                                                    if j.Animation then
                                                                        if j.Animation.AnimationId == w[W2[13]].DashRight.AnimationId or j.Animation.AnimationId == w[W2[13]].DashLeft.AnimationId then
                                                                            return true;
                                                                        else
                                                                            
                                                                        end;
                                                                    end; 
                                                                end;
                                                                return false; 
                                                            end)() and (r116.Position - v1.Position).Magnitude <= 6 then
                                                                v7 = v1.CFrame;
                                                                v1.CFrame = v7:Lerp(CFrame.lookAt(v1.Position, v1.Position + CFrame.Angles(0, math.rad((function(...)
                                                                    local R = {
                                                                        212,
                                                                        210,
                                                                        W2[13],
                                                                        274
                                                                    };
                                                                    x = r38.Humanoid;
                                                                    v1 = x[2];
                                                                    U = x[3];
                                                                    x = "ipairs";
                                                                    for U, j in ipairs(x:GetPlayingAnimationTracks()) do
                                                                        q = U;
                                                                        if j.Animation then
                                                                            if j.Animation.AnimationId == w[W2[13]].DashRight.AnimationId then
                                                                                return "Right";
                                                                            else
                                                                                if j.Animation.AnimationId == w[W2[13]].DashLeft.AnimationId then
                                                                                    return "Left";
                                                                                else
                                                                                    
                                                                                end;
                                                                            end;
                                                                        end; 
                                                                    end;
                                                                    return nil; 
                                                                end)() == "Right" and 75 or -75), 0) * Vector3.new(-r116.CFrame.LookVector.X, 0, -r116.CFrame.LookVector.Z).Unit), .2);
                                                            else
                                                                v1.CFrame = CFrame.lookAt(v1.Position, Vector3.new(r116.Position.X, v1.Position.Y, r116.Position.Z));
                                                            end;
                                                        else
                                                            v7 = game.Players.LocalPlayer.Character.Info;
                                                            if not v7:FindFirstChild("Knockback") then
                                                                r80.LocalPlayer.Character.Humanoid.AutoRotate = true;
                                                            end;
                                                            return;
                                                        end;
                                                    else
                                                        v3 = Vector3.new(1.75, 0, 0);
                                                    end;
                                                end; 
                                            end);
                                            return; 
                                        end;
                                        w[W2[18]] = W2[19];
                                        W2[21] = r3;
                                        W2[22] = r2;
                                        W2[23] = W2[22](W2[24], W2[25]);
                                        W2[20] = W2[21][W2[23]];
                                        W2[23] = r3;
                                        W2[24] = r2;
                                        W2[25] = W2[24](W2[26], W2[27]);
                                        W2[22] = W2[23][W2[25]];
                                        W2[24] = r3;
                                        W2[25] = r2;
                                        W2[27] = "c'69\xa5\xfeH";
                                        W2[26] = W2[25](W2[27], W2[28]);
                                        W2[19] = "AddDropdown";
                                        W2[23] = W2[24][W2[26]];
                                        W2[21] = {
                                            W2[22],
                                            W2[23]
                                        };
                                        W2[23] = true;
                                        W2[22] = function(arg1_50, ...)
                                            local R = {
                                                212,
                                                210
                                            };
                                            _G.AutoLockOnMethod = arg1_50;
                                            return; 
                                        end;
                                        W2[26] = r3;
                                        W2[27] = r2;
                                        W2[28] = W2[27](W2[29], W2[30]);
                                        W2[19] = pA[W2[19]];
                                        W2[25] = W2[26][W2[28]];
                                        W2[24] = {
                                            W2[25]
                                        };
                                        W2[19] = W2[19](pA, W2[20], W2[21], W2[22], W2[23], W2[24]);
                                        W2[19] = {};
                                        W2[31] = 4924547975413;
                                        W2[20] = 344;
                                        W2[25] = "\xca\xa2\xaew\xd7\x15l\x0e\x97\xbb\xc3\xb2";
                                        w[W2[20]] = W2[19];
                                        W2[19] = "AddToggle";
                                        W2[29] = 2779779433742;
                                        W2[22] = r3;
                                        W2[23] = r2;
                                        W2[26] = 10296908649146;
                                        W2[24] = W2[23](W2[25], W2[26]);
                                        W2[21] = W2[22][W2[24]];
                                        W2[22] = false;
                                        W2[19] = pA[W2[19]];
                                        W2[23] = function(arg1_51, ...)
                                            local R = {
                                                212,
                                                210,
                                                W2[20],
                                                W2[12],
                                                W2[13],
                                                W2[15],
                                                W2[14],
                                                W2[18]
                                            };
                                            if arg1_51 then
                                                v5 = game;
                                                v3 = v5:GetService("RunService");
                                                v3:BindToRenderStep("Auto-LockOn", 0, function(...)
                                                    local R = {
                                                        212,
                                                        210,
                                                        W2[20],
                                                        W2[12],
                                                        W2[13],
                                                        W2[15],
                                                        W2[14],
                                                        W2[18]
                                                    };
                                                    v5 = pairs;
                                                    v4 = r3;
                                                    x = workspace.Effects;
                                                    U = x[3];
                                                    x = x[1];
                                                    for U, j in x, v5(x:GetChildren()) do
                                                        q = U;
                                                        v2 = j.Name == "HitGlow";
                                                        if v2 then
                                                            v2 = table.find(_G.AutoLockOnMethod, "Get Hit");
                                                            v4 = v2 and not w[W2[20]][j];
                                                            v5 = pairs;
                                                        end;
                                                        if v2 then
                                                            t = j.GetChildren;
                                                            v2 = t[2];
                                                            v7 = t[3];
                                                            for v7, t in pairs(t(j)) do
                                                                r = v7;
                                                                Y = t.GetChildren;
                                                                a = Y[2];
                                                                v6 = Y[1];
                                                                for o, Y in pairs(Y(t)) do
                                                                    v8 = o;
                                                                    g = Y:IsA("Weld");
                                                                    if g then
                                                                        v5 = pairs;
                                                                        A = Y.Part0 == game.Players.LocalPlayer.Character.Torso or Y.Part1 == game.Players.LocalPlayer.Character.Torso;
                                                                    end;
                                                                    if g then
                                                                        w[W2[20]][j] = true;
                                                                        if w[W2[12]] and not w[W2[13]] then
                                                                            w[W2[13]] = true;
                                                                            w[W2[14]] = w[W2[15]]();
                                                                            w[W2[18]]();
                                                                        end;
                                                                    end; 
                                                                end; 
                                                            end;
                                                        end; 
                                                    end;
                                                    j = w[W2[20]];
                                                    q = v4[3];
                                                    for q, j in v4[1], pairs(j) do
                                                        if not q.Parent then
                                                            w[W2[20]][q] = nil;
                                                        end; 
                                                    end;
                                                    x = table.find;
                                                    v5 = v5;
                                                    if x(_G.AutoLockOnMethod, "Block") and x:FindFirstChild("BlockHit") then
                                                        v5 = v5;
                                                        if w[W2[12]] and not w[W2[13]] then
                                                            w[W2[13]] = true;
                                                            w[W2[14]] = w[W2[15]]();
                                                            w[W2[18]]();
                                                        end;
                                                    end;
                                                    return; 
                                                end);
                                            else
                                                v5 = game;
                                                v3 = v5:GetService("RunService");
                                                v3:UnbindFromRenderStep("Auto-LockOn");
                                            end;
                                            return; 
                                        end;
                                        W2[26] = 1069974913522;
                                        W2[19] = W2[19](pA, W2[21], W2[22], W2[23]);
                                        W2[22] = r3;
                                        W2[28] = 35013623988144;
                                        W2[19] = "AddDropdown";
                                        W2[27] = "\xf5-\x95\xdcz\xaa";
                                        W2[25] = "W\xc2\x1e-\xcb\xb1\x99ud\x82\xfdn\x12/";
                                        W2[23] = r2;
                                        W2[24] = W2[23](W2[25], W2[26]);
                                        W2[30] = "\xe3\x00IU\x96s";
                                        W2[21] = W2[22][W2[24]];
                                        W2[24] = r3;
                                        W2[25] = r2;
                                        W2[26] = W2[25](W2[27], W2[28]);
                                        W2[28] = "k\xcb&_\\\xe6\xfa\xe5\xfb";
                                        W2[23] = W2[24][W2[26]];
                                        W2[25] = r3;
                                        W2[26] = r2;
                                        W2[27] = W2[26](W2[28], W2[29]);
                                        W2[24] = W2[25][W2[27]];
                                        W2[22] = {
                                            W2[23],
                                            W2[24]
                                        };
                                        W2[19] = pA[W2[19]];
                                        W2[23] = function(arg1_52, ...)
                                            local R = {
                                                212,
                                                210
                                            };
                                            _G.LockOnMethod = arg1_52;
                                            return; 
                                        end;
                                        W2[24] = true;
                                        W2[27] = r3;
                                        W2[28] = r2;
                                        W2[29] = W2[28](W2[30], W2[31]);
                                        W2[26] = W2[27][W2[29]];
                                        W2[25] = {
                                            W2[26]
                                        };
                                        W2[19] = W2[19](pA, W2[21], W2[22], W2[23], W2[24], W2[25]);
                                        W2[22] = r3;
                                        W2[26] = 24202868665350;
                                        W2[23] = r2;
                                        W2[19] = "AddToggle";
                                        W2[25] = "\xc5\x19\x10\xa4\xfau\x04";
                                        W2[24] = W2[23](W2[25], W2[26]);
                                        W2[21] = W2[22][W2[24]];
                                        W2[23] = function(arg1_53, ...)
                                            local R = {
                                                W2[12],
                                                189,
                                                212,
                                                210,
                                                190,
                                                W2[13],
                                                W2[16],
                                                W2[11],
                                                W2[14],
                                                W2[18]
                                            };
                                            w[W2[12]] = arg1_53;
                                            if w[W2[12]] then
                                                if not r66.LockOn then
                                                    r75("LockOn", "rbxassetid://11738355467", function(...)
                                                        local R = {
                                                            W2[13],
                                                            W2[16],
                                                            W2[11],
                                                            212,
                                                            210,
                                                            W2[14],
                                                            W2[18]
                                                        };
                                                        if w[W2[12]] then
                                                            r66();
                                                        else
                                                            v3 = r3();
                                                            if v3 then
                                                                UserSettings().GameSettings.RotationType = Enum.RotationType.CameraRelative;
                                                                v3 = v3;
                                                                w[W2[12]] = true;
                                                                w[W2[13]] = v3;
                                                                w[W2[16]]();
                                                            end;
                                                            return;
                                                        end; 
                                                    end, UDim2.new(-0.7, 0, -2.4, 0)).Visible = true;
                                                else
                                                    r66.LockOn.Visible = true;
                                                end;
                                            else
                                                w[W2[16]]();
                                                if r66.LockOn then
                                                    r66.LockOn.Visible = false;
                                                end;
                                                return;
                                            end; 
                                        end;
                                        W2[22] = false;
                                        W2[19] = pA[W2[19]];
                                        W2[19] = W2[19](pA, W2[21], W2[22], W2[23]);
                                        W2[22] = r3;
                                        W2[23] = r2;
                                        W2[26] = 3237045241315;
                                        W2[29] = "\xd3h^\x81\xb0p\x8c";
                                        W2[25] = "\xa3\x14K\x90\x03@X\xc2\xd9\x19]\xb5W\n\xbf";
                                        W2[24] = W2[23](W2[25], W2[26]);
                                        W2[21] = W2[22][W2[24]];
                                        W2[25] = "Enum";
                                        W2[30] = 17539046940647;
                                        W2[24] = Env[W2[25]];
                                        W2[26] = r3;
                                        W2[27] = r2;
                                        W2[28] = W2[27](W2[29], W2[30]);
                                        W2[25] = W2[26][W2[28]];
                                        W2[19] = "AddKeybind";
                                        W2[23] = W2[24][W2[25]];
                                        W2[29] = 17191708254021;
                                        W2[25] = r3;
                                        W2[26] = r2;
                                        W2[28] = "\xc3";
                                        W2[27] = W2[26](W2[28], W2[29]);
                                        W2[26] = 26938492399872;
                                        W2[24] = W2[25][W2[27]];
                                        W2[25] = "\x8e\x93r\xc0";
                                        W2[22] = W2[23][W2[24]];
                                        W2[23] = function(...)
                                            local R = {
                                                W2[12],
                                                W2[13],
                                                W2[16],
                                                W2[11],
                                                212,
                                                210,
                                                W2[14],
                                                W2[18]
                                            };
                                            if not w[W2[12]] then
                                                return;
                                            end;
                                            if w[W2[13]] then
                                                w[W2[16]]();
                                            else
                                                v3 = w[W2[11]]();
                                                if v3 then
                                                    UserSettings().GameSettings.RotationType = Enum.RotationType.CameraRelative;
                                                    v3 = v3;
                                                    w[W2[13]] = true;
                                                    w[W2[14]] = v3;
                                                    w[W2[18]]();
                                                end;
                                                return;
                                            end; 
                                        end;
                                        W2[35] = "\xcb\xd3j,,Xj\xa5\x95\x1a\x84\xd9\xf4@\xc3\x16\xe4";
                                        W2[19] = pA[W2[19]];
                                        W2[19] = W2[19](pA, W2[21], W2[22], W2[23]);
                                        W2[21] = "getgenv";
                                        W2[19] = Env[W2[21]];
                                        W2[21] = W2[19]();
                                        W2[22] = r3;
                                        W2[23] = r2;
                                        W2[27] = 26004534112077;
                                        W2[24] = W2[23](W2[25], W2[26]);
                                        W2[19] = W2[22][W2[24]];
                                        W2[22] = 40;
                                        W2[21][W2[19]] = W2[22];
                                        W2[26] = "C\xabh\xa5KUf\xea\xecf/N\xa7s+<M\xccD5\xc2\xee\x88\xa9\xe3\xd0\nH\xf0\x02\x83\xeeJR\x86\xbet";
                                        W2[19] = nil;
                                        W2[21] = 345;
                                        w[W2[21]] = W2[19];
                                        W2[23] = r3;
                                        W2[19] = "AddToggle";
                                        W2[24] = r2;
                                        W2[25] = W2[24](W2[26], W2[27]);
                                        W2[26] = "\x07(!\x0b\xe8_\xe9b\xe7^ ";
                                        W2[22] = W2[23][W2[25]];
                                        W2[19] = pA[W2[19]];
                                        W2[24] = function(arg1_54, ...)
                                            local R = {
                                                212,
                                                210,
                                                W2[21]
                                            };
                                            U = require(game.Players.LocalPlayer.PlayerScripts.Controllers.Combat.HitboxController);
                                            if arg1_54 then
                                                if not w[W2[21]] then
                                                    w[W2[21]] = U.SphereHitbox;
                                                end;
                                                U.SphereHitbox = function(arg1_55, arg2_55, arg3_55, arg4_55, ...)
                                                    local R = {
                                                        W2[21],
                                                        212,
                                                        210
                                                    };
                                                    q = arg4_55;
                                                    return r3(arg1_55, arg2_55, arg3_55, getgenv().Size); 
                                                end;
                                            else
                                                if w[W2[21]] then
                                                    U.SphereHitbox = w[W2[21]];
                                                end;
                                                return;
                                            end; 
                                        end;
                                        W2[23] = false;
                                        W2[19] = W2[19](pA, W2[22], W2[23], W2[24]);
                                        W2[23] = r3;
                                        W2[24] = r2;
                                        W2[27] = 17005680844526;
                                        W2[19] = "AddSlider";
                                        W2[19] = pA[W2[19]];
                                        W2[25] = W2[24](W2[26], W2[27]);
                                        W2[24] = 40;
                                        W2[27] = 17987978780856;
                                        W2[26] = function(arg1_56, ...)
                                            local R = {
                                                212,
                                                210
                                            };
                                            getgenv().Size = arg1_56;
                                            return; 
                                        end;
                                        W2[22] = W2[23][W2[25]];
                                        W2[25] = 40;
                                        W2[23] = 1;
                                        W2[19] = W2[19](pA, W2[22], W2[23], W2[24], W2[25], W2[26]);
                                        W2[26] = "r8\x81v\xac\xdb\x96\xbd\x98\xe3<\xf8N\xbf\xd2pn\x89";
                                        W2[23] = r3;
                                        W2[24] = r2;
                                        W2[25] = W2[24](W2[26], W2[27]);
                                        W2[19] = "AddSection";
                                        W2[26] = "_\xb6ya\x1d*\xdc\x9c\x17.\xbd";
                                        W2[22] = W2[23][W2[25]];
                                        W2[19] = FA[W2[19]];
                                        W2[19] = W2[19](FA, W2[22]);
                                        W2[27] = 30561502918551;
                                        W2[22] = "getgenv";
                                        W2[19] = Env[W2[22]];
                                        W2[22] = W2[19]();
                                        W2[23] = r3;
                                        W2[24] = r2;
                                        W2[25] = W2[24](W2[26], W2[27]);
                                        W2[19] = W2[23][W2[25]];
                                        W2[23] = false;
                                        W2[22][W2[19]] = W2[23];
                                        W2[22] = "getgenv";
                                        W2[19] = Env[W2[22]];
                                        W2[26] = "*\xba\x87\x982\x06Nm\xb8\xf4h\xef\xc6\x0b";
                                        W2[22] = W2[19]();
                                        W2[23] = r3;
                                        W2[24] = r2;
                                        W2[27] = 34571710643938;
                                        W2[25] = W2[24](W2[26], W2[27]);
                                        W2[28] = 346;
                                        W2[19] = W2[23][W2[25]];
                                        W2[23] = 15;
                                        W2[22][W2[19]] = W2[23];
                                        W2[27] = 23166657325603;
                                        W2[22] = "getgenv";
                                        W2[19] = Env[W2[22]];
                                        W2[22] = W2[19]();
                                        W2[23] = r3;
                                        W2[24] = r2;
                                        W2[26] = "\x88\xe6\x9f\x9c\x9d\xc0e^\x95\xe3\xd6d\xa1\xfe\t\xc8";
                                        W2[25] = W2[24](W2[26], W2[27]);
                                        W2[19] = W2[23][W2[25]];
                                        W2[26] = "\xf6mj\xd4\xebx\n+\x03J";
                                        W2[23] = 15;
                                        W2[22][W2[19]] = W2[23];
                                        W2[22] = "getgenv";
                                        W2[19] = Env[W2[22]];
                                        W2[22] = W2[19]();
                                        W2[27] = 32841673096125;
                                        W2[23] = r3;
                                        W2[24] = r2;
                                        W2[25] = W2[24](W2[26], W2[27]);
                                        W2[26] = 347;
                                        W2[19] = W2[23][W2[25]];
                                        W2[27] = 348;
                                        W2[23] = false;
                                        W2[22][W2[19]] = W2[23];
                                        W2[19] = {};
                                        W2[22] = 349;
                                        w[W2[22]] = W2[19];
                                        W2[23] = 350;
                                        W2[19] = {};
                                        W2[24] = 351;
                                        w[W2[23]] = W2[19];
                                        W2[25] = 352;
                                        W2[19] = {};
                                        w[W2[24]] = W2[19];
                                        W2[19] = {};
                                        w[W2[25]] = W2[19];
                                        W2[30] = "game";
                                        W2[19] = {};
                                        w[W2[26]] = W2[19];
                                        W2[19] = nil;
                                        w[W2[27]] = W2[19];
                                        W2[19] = nil;
                                        w[W2[28]] = W2[19];
                                        W2[29] = Env[W2[30]];
                                        W2[30] = "GetService";
                                        W2[32] = r3;
                                        W2[33] = r2;
                                        W2[34] = W2[33](W2[35], W2[36]);
                                        W2[31] = W2[32][W2[34]];
                                        W2[30] = W2[29][W2[30]];
                                        W2[30] = W2[30](W2[29], W2[31]);
                                        W2[35] = 33013777775629;
                                        W2[31] = r3;
                                        W2[34] = "c.\x8fb\x9fW\x9bL\xbb$";
                                        W2[32] = r2;
                                        W2[33] = W2[32](W2[34], W2[35]);
                                        W2[29] = W2[31][W2[33]];
                                        W2[19] = W2[30][W2[29]];
                                        W2[34] = "\xf2\xec\x8ai";
                                        W2[31] = r3;
                                        W2[32] = r2;
                                        W2[35] = 2079131354056;
                                        W2[33] = W2[32](W2[34], W2[35]);
                                        W2[30] = W2[31][W2[33]];
                                        W2[29] = W2[19][W2[30]];
                                        W2[31] = "ipairs";
                                        W2[35] = "GetDescendants";
                                        W2[30] = Env[W2[31]];
                                        W2[35] = W2[19][W2[35]];
                                        W2[34] = {
                                            W2[35](W2[19])
                                        };
                                        W2[35] = {
                                            W2[30](C(W2[34]))
                                        };
                                        W2[33] = W2[35][3];
                                        W2[32] = W2[35][2];
                                        W2[31] = W2[35][1];
                                        W2[33], W2[34] = W2[31](W2[32], W2[33]);
                                        while W2[33] do
                                            W2[40] = "%&\xa9\xb8\xdc\xca\x9f\x8dS";
                                            W2[37] = r3;
                                            W2[30] = W2[33];
                                            W2[38] = r2;
                                            W2[41] = 18172244451598;
                                            W2[35] = "IsA";
                                            W2[39] = W2[38](W2[40], W2[41]);
                                            W2[35] = W2[34][W2[35]];
                                            W2[36] = W2[37][W2[39]];
                                            W2[35] = W2[35](W2[34], W2[36]);
                                            if W2[35] then
                                                W2[38] = r3;
                                                W2[42] = 27264919581080;
                                                W2[39] = r2;
                                                W2[41] = "x\xacK\x93";
                                                W2[40] = W2[39](W2[41], W2[42]);
                                                W2[42] = 5316176595371;
                                                W2[41] = "\xab\xf8\x1d$\xe9\xce\xd2w\xcac\xa9\x04";
                                                W2[37] = W2[38][W2[40]];
                                                W2[36] = W2[34][W2[37]];
                                                W2[38] = r3;
                                                W2[39] = r2;
                                                W2[40] = W2[39](W2[41], W2[42]);
                                                W2[37] = W2[38][W2[40]];
                                                W2[35] = W2[36] == W2[37];
                                                if W2[35] then
                                                    W2[37] = r3;
                                                    W2[38] = r2;
                                                    W2[41] = 526919287029;
                                                    W2[40] = "{&\xd2\xed\xb94Db2$S";
                                                    W2[39] = W2[38](W2[40], W2[41]);
                                                    W2[36] = W2[37][W2[39]];
                                                    W2[35] = W2[34][W2[36]];
                                                    w[W2[27]] = W2[35];
                                                else
                                                    W2[42] = "*[jk";
                                                    W2[39] = r3;
                                                    W2[40] = r2;
                                                    W2[43] = 9272255746269;
                                                    W2[41] = W2[40](W2[42], W2[43]);
                                                    W2[38] = W2[39][W2[41]];
                                                    W2[37] = W2[34][W2[38]];
                                                    W2[39] = r3;
                                                    W2[42] = "\x04y\xf3\xf6\x05\x1e\x80A\xd9-2";
                                                    W2[40] = r2;
                                                    W2[43] = 32343681563349;
                                                    W2[41] = W2[40](W2[42], W2[43]);
                                                    W2[38] = W2[39][W2[41]];
                                                    W2[36] = W2[37] == W2[38];
                                                    if W2[36] then
                                                        W2[38] = r3;
                                                        W2[39] = r2;
                                                        W2[41] = "\xb4?\xa6qq\xfc&\xfb\t\xca\xbd";
                                                        W2[42] = 25043132771725;
                                                        W2[40] = W2[39](W2[41], W2[42]);
                                                        W2[37] = W2[38][W2[40]];
                                                        W2[36] = W2[34][W2[37]];
                                                        w[W2[28]] = W2[36];
                                                    end;
                                                    W2[44] = 9319351488755;
                                                    W2[39] = "string";
                                                    W2[38] = Env[W2[39]];
                                                    W2[40] = r3;
                                                    W2[43] = "\x87\xa9\x84\x7f\xee";
                                                    W2[41] = r2;
                                                    W2[42] = W2[41](W2[43], W2[44]);
                                                    W2[39] = W2[40][W2[42]];
                                                    W2[37] = W2[38][W2[39]];
                                                    W2[41] = r3;
                                                    W2[44] = "\x99\x9f(_";
                                                    W2[42] = r2;
                                                    W2[45] = 14074150984089;
                                                    W2[43] = W2[42](W2[44], W2[45]);
                                                    W2[40] = W2[41][W2[43]];
                                                    W2[43] = "\xe2\xffPA\xe6d\xcaH\xfc4K";
                                                    W2[39] = W2[34][W2[40]];
                                                    W2[38] = W2[37](W2[39]);
                                                    W2[44] = 16797253066381;
                                                    W2[40] = r3;
                                                    W2[41] = r2;
                                                    W2[42] = W2[41](W2[43], W2[44]);
                                                    W2[39] = W2[40][W2[42]];
                                                    W2[37] = W2[34][W2[39]];
                                                    W2[40] = v5;
                                                    W2[42] = "IsDescendantOf";
                                                    W2[42] = W2[34][W2[42]];
                                                    W2[42] = W2[42](W2[34], W2[29]);
                                                    W2[41] = not W2[42];
                                                    W2[39] = W2[41];
                                                    if W2[41] then
                                                        W2[46] = "string";
                                                        W2[45] = Env[W2[46]];
                                                        W2[47] = r3;
                                                        W2[50] = "\xeb\x08\x0eR";
                                                        W2[48] = r2;
                                                        W2[42] = v5;
                                                        W2[51] = 139513495616;
                                                        W2[49] = W2[48](W2[50], W2[51]);
                                                        W2[51] = 13658108254424;
                                                        W2[46] = W2[47][W2[49]];
                                                        W2[44] = W2[45][W2[46]];
                                                        W2[47] = r3;
                                                        W2[50] = "j\n8(";
                                                        W2[48] = r2;
                                                        W2[49] = W2[48](W2[50], W2[51]);
                                                        W2[46] = W2[47][W2[49]];
                                                        W2[45] = W2[44](W2[38], W2[46]);
                                                        W2[43] = not W2[45];
                                                        W2[41] = W2[43];
                                                        if W2[43] then
                                                            W2[48] = "string";
                                                            W2[44] = v5;
                                                            W2[52] = "\x88\x96\xe0}";
                                                            W2[53] = 17152838360883;
                                                            W2[47] = Env[W2[48]];
                                                            W2[49] = r3;
                                                            W2[50] = r2;
                                                            W2[51] = W2[50](W2[52], W2[53]);
                                                            W2[48] = W2[49][W2[51]];
                                                            W2[53] = 27214022521216;
                                                            W2[52] = "?\xf3\xf1";
                                                            W2[46] = W2[47][W2[48]];
                                                            W2[49] = r3;
                                                            W2[50] = r2;
                                                            W2[51] = W2[50](W2[52], W2[53]);
                                                            W2[48] = W2[49][W2[51]];
                                                            W2[47] = W2[46](W2[38], W2[48]);
                                                            W2[45] = not W2[47];
                                                            W2[43] = W2[45];
                                                            if W2[45] then
                                                                W2[54] = "\xf7~\xe6\xba";
                                                                W2[46] = v5;
                                                                W2[50] = "string";
                                                                W2[55] = 13071317407686;
                                                                W2[49] = Env[W2[50]];
                                                                W2[51] = r3;
                                                                W2[52] = r2;
                                                                W2[53] = W2[52](W2[54], W2[55]);
                                                                W2[55] = 20288203089127;
                                                                W2[50] = W2[51][W2[53]];
                                                                W2[48] = W2[49][W2[50]];
                                                                W2[51] = r3;
                                                                W2[54] = "\xa4v\xf67\x91U\r";
                                                                W2[52] = r2;
                                                                W2[53] = W2[52](W2[54], W2[55]);
                                                                W2[50] = W2[51][W2[53]];
                                                                W2[49] = W2[48](W2[38], W2[50]);
                                                                W2[47] = not W2[49];
                                                                W2[45] = W2[47];
                                                                if W2[47] then
                                                                    W2[48] = v5;
                                                                    W2[52] = "string";
                                                                    W2[51] = Env[W2[52]];
                                                                    W2[53] = r3;
                                                                    W2[57] = 28241182372702;
                                                                    W2[56] = ";rY\xf0";
                                                                    W2[54] = r2;
                                                                    W2[55] = W2[54](W2[56], W2[57]);
                                                                    W2[57] = 17409074536362;
                                                                    W2[52] = W2[53][W2[55]];
                                                                    W2[50] = W2[51][W2[52]];
                                                                    W2[56] = "\xc4\xd9\x056\xcc";
                                                                    W2[53] = r3;
                                                                    W2[54] = r2;
                                                                    W2[55] = W2[54](W2[56], W2[57]);
                                                                    W2[52] = W2[53][W2[55]];
                                                                    W2[51] = W2[50](W2[38], W2[52]);
                                                                    W2[49] = not W2[51];
                                                                    W2[47] = W2[49];
                                                                    if W2[49] then
                                                                        W2[58] = "$\x96Q\x9a";
                                                                        W2[54] = "string";
                                                                        W2[50] = v5;
                                                                        W2[53] = Env[W2[54]];
                                                                        W2[55] = r3;
                                                                        W2[59] = 12442064377505;
                                                                        W2[56] = r2;
                                                                        W2[57] = W2[56](W2[58], W2[59]);
                                                                        W2[58] = "D\xef\xc7\x1d\x05\xac\xfc\xbb\xe1";
                                                                        W2[54] = W2[55][W2[57]];
                                                                        W2[52] = W2[53][W2[54]];
                                                                        W2[55] = r3;
                                                                        W2[59] = 8067861827244;
                                                                        W2[56] = r2;
                                                                        W2[57] = W2[56](W2[58], W2[59]);
                                                                        W2[54] = W2[55][W2[57]];
                                                                        W2[53] = W2[52](W2[38], W2[54]);
                                                                        W2[51] = not W2[53];
                                                                        W2[49] = W2[51];
                                                                        if W2[51] then
                                                                            W2[52] = v5;
                                                                            W2[60] = "wi\xa8+";
                                                                            W2[56] = "string";
                                                                            W2[55] = Env[W2[56]];
                                                                            W2[61] = 5446905514472;
                                                                            W2[57] = r3;
                                                                            W2[58] = r2;
                                                                            W2[59] = W2[58](W2[60], W2[61]);
                                                                            W2[56] = W2[57][W2[59]];
                                                                            W2[54] = W2[55][W2[56]];
                                                                            W2[60] = "\x15 -\xa2";
                                                                            W2[57] = r3;
                                                                            W2[61] = 29447745222032;
                                                                            W2[58] = r2;
                                                                            W2[59] = W2[58](W2[60], W2[61]);
                                                                            W2[56] = W2[57][W2[59]];
                                                                            W2[55] = W2[54](W2[38], W2[56]);
                                                                            W2[53] = not W2[55];
                                                                            W2[51] = W2[53];
                                                                            W2[49] = W2[51] and W2[55];
                                                                            v5 = W2[52];
                                                                        end;
                                                                        v5 = W2[50];
                                                                        W2[47] = W2[49];
                                                                    end;
                                                                    v5 = W2[48];
                                                                    W2[45] = W2[47];
                                                                end;
                                                                v5 = W2[46];
                                                                W2[43] = W2[45];
                                                            end;
                                                            v5 = W2[44];
                                                            W2[41] = W2[43];
                                                        end;
                                                        v5 = W2[42];
                                                        W2[39] = W2[41];
                                                    end;
                                                    if W2[39] then
                                                        W2[39] = w[W2[22]];
                                                        W2[40] = true;
                                                        W2[39][W2[37]] = W2[40];
                                                    end;
                                                    W2[40] = W2[40];
                                                    W2[43] = "string";
                                                    W2[42] = Env[W2[43]];
                                                    W2[48] = 12498638788284;
                                                    W2[44] = r3;
                                                    W2[47] = "U\x91\xbe3";
                                                    W2[45] = r2;
                                                    W2[46] = W2[45](W2[47], W2[48]);
                                                    W2[43] = W2[44][W2[46]];
                                                    W2[48] = 25715631632070;
                                                    W2[41] = W2[42][W2[43]];
                                                    W2[44] = r3;
                                                    W2[47] = "%\x1d\xf4\x9a\x8d";
                                                    W2[45] = r2;
                                                    W2[46] = W2[45](W2[47], W2[48]);
                                                    W2[43] = W2[44][W2[46]];
                                                    W2[42] = W2[41](W2[38], W2[43]);
                                                    W2[39] = W2[42];
                                                    if W2[42] then
                                                        W2[47] = "\xc1\xf8\xe8C";
                                                        W2[48] = 26493558550577;
                                                        W2[44] = r3;
                                                        W2[45] = r2;
                                                        W2[46] = W2[45](W2[47], W2[48]);
                                                        W2[43] = W2[44][W2[46]];
                                                        W2[42] = W2[34][W2[43]];
                                                        W2[48] = 23771698965309;
                                                        W2[44] = r3;
                                                        W2[45] = r2;
                                                        W2[47] = "\xb2g\xbc\x04\t\xf0";
                                                        W2[46] = W2[45](W2[47], W2[48]);
                                                        W2[43] = W2[44][W2[46]];
                                                        W2[41] = W2[42] ~= W2[43];
                                                        W2[39] = W2[41];
                                                    end;
                                                    if W2[39] then
                                                        W2[40] = true;
                                                        W2[39] = w[W2[23]];
                                                        W2[39][W2[37]] = W2[40];
                                                    end;
                                                    W2[45] = "X7\xbfU";
                                                    W2[41] = "string";
                                                    W2[40] = Env[W2[41]];
                                                    W2[46] = 33906243911084;
                                                    W2[42] = r3;
                                                    W2[43] = r2;
                                                    W2[44] = W2[43](W2[45], W2[46]);
                                                    W2[41] = W2[42][W2[44]];
                                                    W2[46] = 4915775359217;
                                                    W2[45] = "\xb6XN\x89Y";
                                                    W2[39] = W2[40][W2[41]];
                                                    W2[42] = r3;
                                                    W2[43] = r2;
                                                    W2[44] = W2[43](W2[45], W2[46]);
                                                    W2[41] = W2[42][W2[44]];
                                                    W2[40] = W2[39](W2[38], W2[41]);
                                                    if W2[40] then
                                                        W2[40] = true;
                                                        W2[39] = w[W2[24]];
                                                        W2[39][W2[37]] = W2[40];
                                                    end;
                                                    W2[42] = "IsDescendantOf";
                                                    W2[42] = W2[34][W2[42]];
                                                    W2[40] = W2[40];
                                                    W2[42] = W2[42](W2[34], W2[29]);
                                                    W2[41] = not W2[42];
                                                    W2[39] = W2[41];
                                                    if W2[41] then
                                                        W2[50] = "\xc0\xd2aw";
                                                        W2[42] = W2[40];
                                                        W2[51] = 3934394337064;
                                                        W2[46] = "string";
                                                        W2[45] = Env[W2[46]];
                                                        W2[47] = r3;
                                                        W2[48] = r2;
                                                        W2[49] = W2[48](W2[50], W2[51]);
                                                        W2[46] = W2[47][W2[49]];
                                                        W2[51] = 13906962110795;
                                                        W2[44] = W2[45][W2[46]];
                                                        W2[47] = r3;
                                                        W2[48] = r2;
                                                        W2[50] = "D\xa6O\xb0";
                                                        W2[49] = W2[48](W2[50], W2[51]);
                                                        W2[46] = W2[47][W2[49]];
                                                        W2[45] = W2[44](W2[38], W2[46]);
                                                        W2[43] = not W2[45];
                                                        W2[41] = W2[43];
                                                        W2[39] = W2[41] and W2[45];
                                                        v5 = W2[42];
                                                    end;
                                                    if W2[39] then
                                                        W2[39] = w[W2[25]];
                                                        W2[40] = true;
                                                        W2[39][W2[37]] = W2[40];
                                                    end;
                                                    W2[53] = 26428407984146;
                                                    W2[54] = 17077237784336;
                                                    W2[59] = 3727949809351;
                                                    W2[49] = 15140515650442;
                                                    W2[43] = "table";
                                                    W2[52] = 33389099072700;
                                                    W2[50] = 24525972614300;
                                                    W2[57] = 25567230635649;
                                                    W2[47] = "\x84\xe3b\xee";
                                                    W2[40] = W2[40];
                                                    W2[42] = Env[W2[43]];
                                                    W2[44] = r3;
                                                    W2[45] = r2;
                                                    W2[48] = 13414767351910;
                                                    W2[46] = W2[45](W2[47], W2[48]);
                                                    W2[43] = W2[44][W2[46]];
                                                    W2[64] = 17268378214249;
                                                    W2[41] = W2[42][W2[43]];
                                                    W2[69] = 21980772575227;
                                                    W2[45] = r3;
                                                    W2[46] = r2;
                                                    W2[48] = "\x9a(\xd7\x1f\xd9\x01\x08\x8a";
                                                    W2[55] = 34076436561404;
                                                    W2[47] = W2[46](W2[48], W2[49]);
                                                    W2[51] = 20212962944196;
                                                    W2[56] = 1673095250699;
                                                    W2[49] = "\xda%`\x9b\xd08u\xf8\xb3\x8b";
                                                    W2[44] = W2[45][W2[47]];
                                                    W2[66] = 13698862389483;
                                                    W2[46] = r3;
                                                    W2[47] = r2;
                                                    W2[48] = W2[47](W2[49], W2[50]);
                                                    W2[61] = 12773296854844;
                                                    W2[45] = W2[46][W2[48]];
                                                    W2[50] = "\x97\xb8\xfeO\xf7\t\xdb\xb6\xe0X\xe6";
                                                    W2[47] = r3;
                                                    W2[48] = r2;
                                                    W2[49] = W2[48](W2[50], W2[51]);
                                                    W2[46] = W2[47][W2[49]];
                                                    W2[48] = r3;
                                                    W2[49] = r2;
                                                    W2[51] = "\x9d\xe24\x97SE[\xea\xb7Z\xa8\x1e\x01#P";
                                                    W2[50] = W2[49](W2[51], W2[52]);
                                                    W2[47] = W2[48][W2[50]];
                                                    W2[49] = r3;
                                                    W2[50] = r2;
                                                    W2[52] = "W8\x97\xd7\x84\xa7\xff=\xd2\x02]\x14";
                                                    W2[51] = W2[50](W2[52], W2[53]);
                                                    W2[48] = W2[49][W2[51]];
                                                    W2[50] = r3;
                                                    W2[51] = r2;
                                                    W2[53] = "\x01\xa5@_R\x15\xfc3\xf38\xe0";
                                                    W2[52] = W2[51](W2[53], W2[54]);
                                                    W2[67] = 6917269720213;
                                                    W2[49] = W2[50][W2[52]];
                                                    W2[54] = "UJ\xf1\x8b\xa9\x1dE";
                                                    W2[51] = r3;
                                                    W2[52] = r2;
                                                    W2[53] = W2[52](W2[54], W2[55]);
                                                    W2[50] = W2[51][W2[53]];
                                                    W2[58] = 14110159460778;
                                                    W2[52] = r3;
                                                    W2[55] = "\xdb2H.\x80\x9bS\x99\xcfv\xcd\x04";
                                                    W2[53] = r2;
                                                    W2[54] = W2[53](W2[55], W2[56]);
                                                    W2[51] = W2[52][W2[54]];
                                                    W2[56] = "\x9bW\xd7\x0c\xc4IU";
                                                    W2[53] = r3;
                                                    W2[54] = r2;
                                                    W2[55] = W2[54](W2[56], W2[57]);
                                                    W2[52] = W2[53][W2[55]];
                                                    W2[57] = "\xc7\xec\x98\x9b3\xc5\xf1'\xc6";
                                                    W2[54] = r3;
                                                    W2[55] = r2;
                                                    W2[62] = 35091135315924;
                                                    W2[56] = W2[55](W2[57], W2[58]);
                                                    W2[53] = W2[54][W2[56]];
                                                    W2[58] = "\x8c\xb3\x08\xe5\x1er\xad\xf18";
                                                    W2[60] = 26656033206396;
                                                    W2[55] = r3;
                                                    W2[56] = r2;
                                                    W2[57] = W2[56](W2[58], W2[59]);
                                                    W2[59] = "\xdd0G\xa8\xde\x18V@\x96\x17\x80\xcc";
                                                    W2[54] = W2[55][W2[57]];
                                                    W2[56] = r3;
                                                    W2[57] = r2;
                                                    W2[58] = W2[57](W2[59], W2[60]);
                                                    W2[55] = W2[56][W2[58]];
                                                    W2[57] = r3;
                                                    W2[60] = "\x19\xb8=/\xb0_8L ";
                                                    W2[58] = r2;
                                                    W2[59] = W2[58](W2[60], W2[61]);
                                                    W2[56] = W2[57][W2[59]];
                                                    W2[63] = 4872007403740;
                                                    W2[58] = r3;
                                                    W2[61] = "\x92sr\xe9j\xe6\xd5p\x9d\x86\xab:&";
                                                    W2[59] = r2;
                                                    W2[60] = W2[59](W2[61], W2[62]);
                                                    W2[57] = W2[58][W2[60]];
                                                    W2[62] = "\x8d\xdc\xdf\x96\xb6\xd4w";
                                                    W2[59] = r3;
                                                    W2[60] = r2;
                                                    W2[61] = W2[60](W2[62], W2[63]);
                                                    W2[58] = W2[59][W2[61]];
                                                    W2[63] = "\x0b\x92V\xbc\x84";
                                                    W2[60] = r3;
                                                    W2[61] = r2;
                                                    W2[62] = W2[61](W2[63], W2[64]);
                                                    W2[59] = W2[60][W2[62]];
                                                    W2[61] = r3;
                                                    W2[64] = "\x90\x81\xc8rC\xca\x02\x06w\xcaS\x02M\xbd";
                                                    W2[62] = r2;
                                                    W2[65] = 31380906801428;
                                                    W2[63] = W2[62](W2[64], W2[65]);
                                                    W2[60] = W2[61][W2[63]];
                                                    W2[62] = r3;
                                                    W2[63] = r2;
                                                    W2[65] = "\xf4\xf9mY\xd2\xad\xa3C";
                                                    W2[64] = W2[63](W2[65], W2[66]);
                                                    W2[61] = W2[62][W2[64]];
                                                    W2[66] = "\x81\x07\t\n\xbf=\x15\x1c\xdb\xfbS\x07\xaf";
                                                    W2[63] = r3;
                                                    W2[64] = r2;
                                                    W2[65] = W2[64](W2[66], W2[67]);
                                                    W2[67] = "6\xc9\xc6\xda;\xea\xef\xeb\x1f\xd9?";
                                                    W2[62] = W2[63][W2[65]];
                                                    W2[68] = 1050466877929;
                                                    W2[64] = r3;
                                                    W2[65] = r2;
                                                    W2[66] = W2[65](W2[67], W2[68]);
                                                    W2[63] = W2[64][W2[66]];
                                                    W2[68] = "\xc5\xb1T\xe9p\xdb(\xe1J\xf0l";
                                                    W2[65] = r3;
                                                    W2[66] = r2;
                                                    W2[67] = W2[66](W2[68], W2[69]);
                                                    W2[64] = W2[65][W2[67]];
                                                    W2[43] = {
                                                        W2[44],
                                                        W2[45],
                                                        W2[46],
                                                        W2[47],
                                                        W2[48],
                                                        W2[49],
                                                        W2[50],
                                                        W2[51],
                                                        W2[52],
                                                        W2[53],
                                                        W2[54],
                                                        W2[55],
                                                        W2[56],
                                                        W2[57],
                                                        W2[58],
                                                        W2[59],
                                                        W2[60],
                                                        W2[61],
                                                        W2[62],
                                                        W2[63],
                                                        W2[64]
                                                    };
                                                    W2[46] = r3;
                                                    W2[49] = "yxZ\xd3";
                                                    W2[50] = 10538128266027;
                                                    W2[47] = r2;
                                                    W2[48] = W2[47](W2[49], W2[50]);
                                                    W2[45] = W2[46][W2[48]];
                                                    W2[44] = W2[34][W2[45]];
                                                    W2[42] = W2[41](W2[43], W2[44]);
                                                    W2[39] = W2[42];
                                                    if W2[42] then
                                                        v5 = W2[40];
                                                        if W2[39] then
                                                            W2[39] = w[W2[26]];
                                                            W2[40] = true;
                                                            W2[39][W2[37]] = W2[40];
                                                        end;
                                                        W2[37] = nil;
                                                        W2[38] = nil;
                                                        W2[34] = nil;
                                                        W2[30] = nil;
                                                    else
                                                        W2[53] = 2527769855129;
                                                        W2[47] = "game";
                                                        W2[46] = Env[W2[47]];
                                                        W2[52] = "\xb9\xafSp\x0e\xc4n\xda\xc3:W\xd9\x95\x9f\xc90\x9f";
                                                        W2[49] = r3;
                                                        W2[47] = "GetService";
                                                        W2[50] = r2;
                                                        W2[47] = W2[46][W2[47]];
                                                        W2[51] = W2[50](W2[52], W2[53]);
                                                        W2[52] = 3583579260548;
                                                        W2[48] = W2[49][W2[51]];
                                                        W2[51] = "p8\x1a\xba\x8e:\x05\x99\xf1\x95";
                                                        W2[47] = W2[47](W2[46], W2[48]);
                                                        W2[48] = r3;
                                                        W2[49] = r2;
                                                        W2[50] = W2[49](W2[51], W2[52]);
                                                        W2[46] = W2[48][W2[50]];
                                                        W2[51] = 24914604682577;
                                                        W2[50] = "\x18r/\xd5^w";
                                                        W2[45] = W2[47][W2[46]];
                                                        W2[47] = r3;
                                                        W2[48] = r2;
                                                        W2[49] = W2[48](W2[50], W2[51]);
                                                        W2[50] = 21455706679047;
                                                        W2[46] = W2[47][W2[49]];
                                                        W2[44] = W2[45][W2[46]];
                                                        W2[46] = r3;
                                                        W2[49] = "\xe4x$\xf9\x83";
                                                        W2[47] = r2;
                                                        W2[48] = W2[47](W2[49], W2[50]);
                                                        W2[45] = W2[46][W2[48]];
                                                        W2[43] = W2[44][W2[45]];
                                                        W2[45] = r3;
                                                        W2[48] = "\xdb\xa1\x935r\xc3";
                                                        W2[49] = 12684089071378;
                                                        W2[46] = r2;
                                                        W2[47] = W2[46](W2[48], W2[49]);
                                                        W2[44] = W2[45][W2[47]];
                                                        W2[42] = W2[43][W2[44]];
                                                        W2[41] = W2[34] == W2[42];
                                                        W2[39] = W2[41];
                                                    end;
                                                end;
                                            end; 
                                        end;
                                        W2[47] = 14111436691883;
                                        W2[33] = 11;
                                        W2[37] = 12;
                                        W2[31] = 13;
                                        W2[30] = {};
                                        w[W2[31]] = W2[30];
                                        W2[32] = 14;
                                        W2[30] = {};
                                        w[W2[32]] = W2[30];
                                        W2[30] = false;
                                        W2[34] = 15;
                                        w[W2[33]] = W2[30];
                                        W2[30] = false;
                                        W2[38] = 16;
                                        w[W2[34]] = W2[30];
                                        W2[39] = 17;
                                        W2[30] = false;
                                        w[W2[37]] = W2[30];
                                        W2[30] = nil;
                                        W2[40] = 18;
                                        w[W2[38]] = W2[30];
                                        W2[30] = 0;
                                        w[W2[39]] = W2[30];
                                        W2[30] = .4;
                                        W2[41] = "workspace";
                                        W2[50] = 2959547843938;
                                        w[W2[40]] = W2[30];
                                        W2[46] = "j\xc8\x93m\xbaBm";
                                        W2[30] = Env[W2[41]];
                                        W2[43] = r3;
                                        W2[41] = "WaitForChild";
                                        W2[44] = r2;
                                        W2[45] = W2[44](W2[46], W2[47]);
                                        W2[41] = W2[30][W2[41]];
                                        W2[42] = W2[43][W2[45]];
                                        W2[41] = W2[41](W2[30], W2[42]);
                                        W2[30] = 19;
                                        w[W2[30]] = W2[41];
                                        W2[41] = {};
                                        W2[42] = 20;
                                        W2[49] = ",\r<\x10$(\xbbL3kE";
                                        w[W2[42]] = W2[41];
                                        W2[41] = function(...)
                                            local R = {
                                                312,
                                                W2[42]
                                            };
                                            v5 = r79;
                                            w[W2[42]] = v5:GetPlayers();
                                            return; 
                                        end;
                                        W2[44] = r79;
                                        W2[46] = r3;
                                        W2[47] = r2;
                                        W2[48] = W2[47](W2[49], W2[50]);
                                        W2[45] = W2[46][W2[48]];
                                        W2[49] = "NI=_\x9c\x02\xb6Uz\x9eq\xf3)\x1f";
                                        W2[50] = 11126256079933;
                                        W2[43] = W2[44][W2[45]];
                                        W2[44] = "Connect";
                                        W2[44] = W2[43][W2[44]];
                                        W2[44] = W2[44](W2[43], W2[41]);
                                        W2[44] = r79;
                                        W2[46] = r3;
                                        W2[47] = r2;
                                        W2[48] = W2[47](W2[49], W2[50]);
                                        W2[45] = W2[46][W2[48]];
                                        W2[43] = W2[44][W2[45]];
                                        W2[50] = 27526204060177;
                                        W2[44] = "Connect";
                                        W2[44] = W2[43][W2[44]];
                                        W2[44] = W2[44](W2[43], W2[41]);
                                        W2[49] = "\xa2o\xe3\xd9\xdc*\x8c\xb1\xc8";
                                        W2[43] = W2[41]();
                                        W2[44] = r38;
                                        W2[46] = r3;
                                        W2[54] = 23077399833082;
                                        W2[47] = r2;
                                        W2[48] = W2[47](W2[49], W2[50]);
                                        W2[45] = W2[46][W2[48]];
                                        W2[43] = W2[44][W2[45]];
                                        W2[44] = "Connect";
                                        W2[45] = function(...)
                                            local R = {
                                                212,
                                                210,
                                                W2[39],
                                                W2[40],
                                                312,
                                                W2[34],
                                                314,
                                                W2[30],
                                                W2[37],
                                                W2[38],
                                                W2[42],
                                                W2[17],
                                                W2[22],
                                                W2[27],
                                                W2[28],
                                                W2[23],
                                                W2[24],
                                                W2[25],
                                                W2[26],
                                                W2[31],
                                                W2[32],
                                                W2[33]
                                            };
                                            v1 = v5;
                                            v5 = v1;
                                            if not (getgenv().AutoBlock or getgenv().AutoCounter) then
                                                return;
                                            end;
                                            v1 = workspace;
                                            v1 = v1:FindFirstChild("Effects") and v1:FindFirstChild("Totality");
                                            if v1 then
                                                v3 = v1:FindFirstChild("Target") and v1.Target.Value;
                                                v5 = not (getgenv()[r3[r2("RU\x03\x981\xb2\xdb\xfbB", r)]] or getgenv().AutoCounter);
                                            end;
                                            x = tick() - w[W2[39]] < w[W2[40]];
                                            if getgenv().AutoBlock and v1 == r79.LocalPlayer.Character then
                                                v3 = w[W2[34]];
                                                if not v3 then
                                                    w[W2[34]] = true;
                                                    v3 = r81.BlockService.RE.Activated;
                                                    v3:FireServer();
                                                end;
                                            else
                                                if w[W2[34]] then
                                                    w[W2[34]] = false;
                                                    q = r81.BlockService.RE.Deactivated;
                                                    q:FireServer();
                                                end;
                                                q = getgenv().AutoBlock or getgenv().AutoCounter;
                                                v5 = tick() - w[W2[39]] < w[W2[40]];
                                                if q then
                                                    q = {};
                                                    r = w[W2[30]];
                                                    v2 = r[2];
                                                    v7 = r[3];
                                                    for v7, r in ipairs(r:GetChildren()) do
                                                        j = v7;
                                                        if r:IsA("BasePart") then
                                                            v6 = j;
                                                            o = j;
                                                            Y = "ArrowProjectile";
                                                            o = r.Name ~= Y;
                                                            v5 = j;
                                                            if o and r.Name ~= "PurpleProjectile" then
                                                                v6 = r79.LocalPlayer.Character.HumanoidRootPart.Position - r.Position;
                                                                o = Y <= (r.Name == "Reserve" and 30 or 50) and Y:Dot(v6.Unit) > .98;
                                                                Y = v6.Magnitude;
                                                                v5 = Y <= (r.Name == "Reserve" and 30 or 50) and Y:Dot(v6.Unit) > .98;
                                                                if Y <= (r.Name == "Reserve" and 30 or 50) and Y:Dot(v6.Unit) > .98 then
                                                                    table.insert({}, r);
                                                                end;
                                                            end;
                                                        end; 
                                                    end;
                                                    if #q > 1 then
                                                        if not w[W2[37]] then
                                                            w[W2[37]] = true;
                                                            w[W2[38]] = {};
                                                            v2 = getgenv().AutoBlock;
                                                            if v2 then
                                                                v2 = r81.BlockService.RE.Activated;
                                                                v2:FireServer();
                                                            end;
                                                            v6 = getgenv();
                                                            r = v6.AutoCounter;
                                                            v2 = r;
                                                            if r then
                                                                v6 = r79.LocalPlayer.Character;
                                                                v2 = v6:FindFirstChild("Info") and v6:FindFirstChild("Sword");
                                                                v5 = j;
                                                            end;
                                                            v5 = v5;
                                                            if v2 then
                                                                v2 = r81.HarutaService.RE.Activated;
                                                                v2:FireServer(false);
                                                            end;
                                                        end;
                                                        a = w[W2[38]];
                                                        t = 30057422124716[2];
                                                        r = 30057422124716[1];
                                                        for v6, a in ipairs(a) do
                                                            v7 = v6;
                                                            if a then
                                                                v2 = false;
                                                            else
                                                                
                                                            end; 
                                                        end;
                                                        if true then
                                                            v7 = r81.BlockService.RE.Deactivated;
                                                            v7:FireServer();
                                                            w[W2[37]] = false;
                                                            w[W2[38]] = nil;
                                                        end;
                                                    else
                                                        v2 = #q == 1;
                                                        if v2 then
                                                            v2 = ({})[1];
                                                            v6 = w[W2[37]];
                                                            if not v6 then
                                                                v6 = q[1];
                                                                w[W2[37]] = true;
                                                                w[W2[38]] = v6;
                                                                a = getgenv().AutoBlock;
                                                                if a then
                                                                    a = r81.BlockService.RE.Activated;
                                                                    a:FireServer();
                                                                end;
                                                                if getgenv().AutoCounter then
                                                                    a = r79.LocalPlayer.Character.Moveset;
                                                                    Y = "Manji Kick";
                                                                    if a:FindFirstChild(Y) then
                                                                        a = r81.ManjiKickService.RE.Activated;
                                                                        Y = r79.LocalPlayer.Character.Moveset;
                                                                        a:FireServer(Y:FindFirstChild("Manji Kick"));
                                                                    end;
                                                                    a = r79.LocalPlayer.Character.Moveset;
                                                                    Y = "Head Splitter";
                                                                    if a:FindFirstChild(Y) then
                                                                        a = r81.HeadSplitterService.RE.Activated;
                                                                        Y = r79.LocalPlayer.Character.Moveset;
                                                                        a:FireServer(Y:FindFirstChild("Head Splitter"));
                                                                    end;
                                                                    a = r79.LocalPlayer.Character.Moveset;
                                                                    Y = "Eye Catching";
                                                                    if a:FindFirstChild(Y) then
                                                                        a = r81.EyeCatchService.RE.Activated;
                                                                        Y = r79.LocalPlayer.Character.Moveset;
                                                                        a:FireServer(Y:FindFirstChild("Eye Catching"));
                                                                    end;
                                                                    a = r79.LocalPlayer.Character.Moveset;
                                                                    Y = "Adaptation";
                                                                    if a:FindFirstChild(Y) then
                                                                        a = r81.AdaptationService.RE.Activated;
                                                                        Y = r79.LocalPlayer.Character.Moveset;
                                                                        a:FireServer(Y:FindFirstChild("Adaptation"));
                                                                    end;
                                                                end;
                                                                g = getgenv();
                                                                Y = g.AutoCounter;
                                                                a = Y;
                                                                if Y then
                                                                    g = r79.LocalPlayer.Character;
                                                                    v5 = j;
                                                                    a = g:FindFirstChild("Info") and g:FindFirstChild("Sword");
                                                                end;
                                                                v5 = j;
                                                                if a then
                                                                    a = r81.HarutaService.RE.Activated;
                                                                    a:FireServer(false);
                                                                end;
                                                            end;
                                                            v8 = j;
                                                            Y = r79.LocalPlayer.Character;
                                                            O = r2("\xea\xf8>\x80\xf9'\x8a\x88", 33884018458018);
                                                            A = Y:FindFirstChild(r3[O]);
                                                            if A then
                                                                v5 = v8;
                                                                if A then
                                                                    a = r81.BlockService.RE.Deactivated;
                                                                    a:FireServer();
                                                                    w[W2[37]] = false;
                                                                    w[W2[38]] = nil;
                                                                end;
                                                                v9 = w[W2[42]];
                                                                d = O[3];
                                                                g = O[2];
                                                                for d, v9 in ipairs(v9) do
                                                                    q = d;
                                                                    Z = r3;
                                                                    CA = r2;
                                                                    F = v9 ~= r79.LocalPlayer;
                                                                    O = F;
                                                                    if F then
                                                                        m = v9.Character;
                                                                        if m then
                                                                            m = v9.Character;
                                                                            F = m:FindFirstChild("HumanoidRootPart");
                                                                        end;
                                                                        v5 = v8;
                                                                        O = m;
                                                                    end;
                                                                    v5 = v8;
                                                                    if O then
                                                                        O = (v9.Character.HumanoidRootPart.Position - r79.LocalPlayer.Character.HumanoidRootPart.Position).Magnitude;
                                                                        p = v9.Character;
                                                                        B = p:FindFirstChildOfClass("Humanoid").FloorMaterial == Enum.Material.Air;
                                                                        if O > 30 then
                                                                            
                                                                        end;
                                                                        JA = "\x1d'\x8ep\x82\xf3\xbf\xf1\x0f,\x17yu\x1b1U\x8b\xcf\xf6";
                                                                        TA = getgenv()[r3[r2(JA, 29497189578151)]];
                                                                        if TA then
                                                                            vA = w[W2[17]];
                                                                            TA = hA;
                                                                            hA = B;
                                                                            if vA then
                                                                                TA = w[W2[17]].Adornee;
                                                                            end;
                                                                            JA = v9.Character;
                                                                            hA = not JA or JA:FindFirstChild("HumanoidRootPart") ~= TA;
                                                                            B = B;
                                                                            v5 = hA;
                                                                            if not TA or hA then
                                                                                
                                                                            else
                                                                                
                                                                            end;
                                                                        end;
                                                                        m = false;
                                                                        p = false;
                                                                        F = false;
                                                                        cA = v9.Character.Humanoid;
                                                                        vA = cA[2];
                                                                        hA = cA[1];
                                                                        for RA, cA in ipairs(cA:GetPlayingAnimationTracks()) do
                                                                            TA = RA;
                                                                            xA = r79.LocalPlayer;
                                                                            JA = cA.Animation.AnimationId;
                                                                            if w[W2[22]][JA] then
                                                                                if JA == w[W2[27]] then
                                                                                    if not (p:FindFirstChildOfClass("Humanoid").FloorMaterial == Enum[r3[r2("\xb3<4\xae\xe5z\x9a\xad", iA)]][Z[V]]) then
                                                                                        F = cA.TimePosition / cA.Length < math.clamp(1 - xA:GetNetworkPing(), 0, 1);
                                                                                    end;
                                                                                else
                                                                                    if cA.Animation[DA[xA]] == w[W2[28]] then
                                                                                        if p:FindFirstChildOfClass("Humanoid").FloorMaterial == Enum[r3[r2("\xb3<4\xae\xe5z\x9a\xad", iA)]][Z[V]] then
                                                                                            F = cA.TimePosition / cA.Length < math.clamp(1 - xA:GetNetworkPing(), 0, 1);
                                                                                        end;
                                                                                    else
                                                                                        if w[W2[23]][cA.Animation[DA[xA]]] then
                                                                                            F = true;
                                                                                        else
                                                                                            F = cA.TimePosition / cA.Length < math.clamp(1 - xA:GetNetworkPing(), 0, 1);
                                                                                        end;
                                                                                    end;
                                                                                end;
                                                                            end;
                                                                            if w[W2[24]][JA] then
                                                                                p = true;
                                                                            else
                                                                                p = false;
                                                                            end;
                                                                            if w[W2[25]][JA] then
                                                                                if cA.TimePosition / cA.Length < math.clamp(1 - xA:GetNetworkPing(), 0, 1) then
                                                                                    m = true;
                                                                                else
                                                                                    m = false;
                                                                                end;
                                                                            end;
                                                                            if w[W2[26]][JA] then
                                                                                S = true;
                                                                            end; 
                                                                        end;
                                                                        vA = w[W2[31]][v9];
                                                                        if vA then
                                                                            cA = r79.LocalPlayer.Character.HumanoidRootPart;
                                                                            vA = cA:FindFirstChild("BlockHit");
                                                                            TA = vA and not false;
                                                                            v5 = B;
                                                                        end;
                                                                        v5 = B;
                                                                        if vA then
                                                                            w[W2[39]] = tick();
                                                                            TA = r81.BlockService.RE.Deactivated;
                                                                            TA:FireServer();
                                                                            v5 = v5;
                                                                            if getgenv().autopunish and O <= 11 then
                                                                                TA = r79.LocalPlayer.Character;
                                                                                vA = TA:GetAttribute("Moveset");
                                                                                TA = vA == "Mahoraga";
                                                                                if TA then
                                                                                    TA = r81.MahoragaService.RE.Activated;
                                                                                    TA:FireServer(false);
                                                                                else
                                                                                    TA = r81[vA .. "Service"].RE.Activated;
                                                                                    TA:FireServer(false);
                                                                                end;
                                                                            end;
                                                                        end;
                                                                        vA = v5;
                                                                        IA = getgenv();
                                                                        RA = IA.AutoCounter;
                                                                        TA = RA;
                                                                        if RA then
                                                                            IA = O <= getgenv().AutoCounterRange;
                                                                            if IA then
                                                                                if false then
                                                                                    NA = v9.Character;
                                                                                    IA = NA:GetAttribute("Ragdoll") == 0 and 0:Dot((r79.LocalPlayer.Character.HumanoidRootPart.Position - v9.Character.HumanoidRootPart.Position).Unit) > .7;
                                                                                    v5 = hA;
                                                                                end;
                                                                                v5 = hA;
                                                                                RA = false;
                                                                            end;
                                                                            v5 = hA;
                                                                            TA = IA;
                                                                        end;
                                                                        Z = TA;
                                                                        v5 = vA;
                                                                        IA = getgenv();
                                                                        QA = r2(".\xb0D#z\x16\xe3M\xc4", 27697710658145);
                                                                        RA = IA[r3[QA]];
                                                                        TA = RA;
                                                                        if RA then
                                                                            QA = getgenv();
                                                                            IA = O <= QA.AutoBlockRange;
                                                                            if IA then
                                                                                RA = false and QA:GetAttribute("Ragdoll") == 0;
                                                                                v5 = vA;
                                                                            end;
                                                                            v5 = vA;
                                                                            TA = IA;
                                                                        end;
                                                                        v5 = v5;
                                                                        CA = Z;
                                                                        vA = r79.LocalPlayer.Character;
                                                                        if Z then
                                                                            v5 = v5;
                                                                            TA = not w[W2[32]][v9] and not v5;
                                                                        end;
                                                                        v5 = v5;
                                                                        if Z then
                                                                            RA = vA;
                                                                            w[W2[32]][v9] = true;
                                                                            cA = r79.LocalPlayer.Character.SetAssets;
                                                                            v5 = "Sword";
                                                                            TA = not (cA:FindFirstChild("Convergence") or cA:FindFirstChild("JackpotAura"));
                                                                            if TA then
                                                                                TA = r81.HakariService.RE.RightActivated;
                                                                                TA:FireServer();
                                                                                TA = r81.SupernovaService.RE.Activated;
                                                                                RA = r79.LocalPlayer.Character.Moveset;
                                                                                TA:FireServer(RA:FindFirstChild("Supernova"));
                                                                            end;
                                                                            TA = r81.ManjiKickService.RE.Activated;
                                                                            RA = r79.LocalPlayer.Character.Moveset;
                                                                            TA:FireServer(RA:FindFirstChild("Manji Kick"));
                                                                            TA = r81.HeadSplitterService.RE.Activated;
                                                                            RA = r79.LocalPlayer.Character.Moveset;
                                                                            TA:FireServer(RA:FindFirstChild("Head Splitter"));
                                                                            vA = r79.LocalPlayer;
                                                                            RA = vA:GetAttribute("Ultimate");
                                                                            TA = RA == 100;
                                                                            if TA then
                                                                                TA = r81.NaoyaService.RE.Ultimate;
                                                                                TA:FireServer();
                                                                                TA = r81.CharlesService.RE.Ultimate;
                                                                                TA:FireServer();
                                                                            else
                                                                                TA = r81.EyeCatchService.RE.Activated;
                                                                                RA = r79.LocalPlayer.Character.Moveset;
                                                                                TA:FireServer(RA:FindFirstChild("Eye Catching"));
                                                                            end;
                                                                            TA = r81.AdaptationService.RE.Activated;
                                                                            RA = r79.LocalPlayer.Character.Moveset;
                                                                            TA:FireServer(RA:FindFirstChild("Adaptation"));
                                                                            if vA:GetAttribute("Makora") == 2 then
                                                                                TA = r81.MahoragaService.RE.Activated;
                                                                                TA:FireServer(false);
                                                                            end;
                                                                            TA = r79.LocalPlayer.Character.Info;
                                                                            if TA:FindFirstChild("Sword") then
                                                                                if not false then
                                                                                    task.wait(.15);
                                                                                end;
                                                                                TA = r81.HarutaService.RE.Activated;
                                                                                TA:FireServer(false);
                                                                            end;
                                                                        else
                                                                            vA = v5;
                                                                            RA = not Z;
                                                                            v5 = vA;
                                                                            if RA and w[W2[32]][v9] then
                                                                                w[W2[32]][v9] = nil;
                                                                            end;
                                                                            TA = CA;
                                                                            if CA then
                                                                                TA = not (RA == 2) and not w[W2[31]][v9];
                                                                                v5 = vA;
                                                                            end;
                                                                            v5 = v5;
                                                                            if TA then
                                                                                w[W2[31]][v9] = true;
                                                                                TA = r81.BlockService.RE.Activated;
                                                                                TA:FireServer();
                                                                            else
                                                                                TA = not CA and w[W2[31]][v9];
                                                                                if TA then
                                                                                    w[W2[31]][v9] = nil;
                                                                                    TA = r81.BlockService.RE.Deactivated;
                                                                                    TA:FireServer();
                                                                                end;
                                                                                TA = r79.LocalPlayer.Character.HumanoidRootPart;
                                                                                K = TA:FindFirstChild("Feint");
                                                                                RA = getgenv().AutoBlock or getgenv().AutoCounter;
                                                                                v5 = v5;
                                                                                if RA then
                                                                                    TA = K;
                                                                                end;
                                                                                v5 = v5;
                                                                                if RA then
                                                                                    vA = (function(arg1_57, ...)
                                                                                        local R = {
                                                                                            212,
                                                                                            210
                                                                                        };
                                                                                        v1 = arg1_57;
                                                                                        U = v1:FindFirstChild("Ring");
                                                                                        if not U or not U:IsA("ParticleEmitter") then
                                                                                            return false;
                                                                                        end;
                                                                                        v5 = ipairs;
                                                                                        v4 = U.Color;
                                                                                        j = v4.Keypoints;
                                                                                        j = v4[1];
                                                                                        x = v4[2];
                                                                                        for q, v2 in v5(j) do
                                                                                            v4 = q;
                                                                                            v5 = ipairs;
                                                                                            v7 = 0[1];
                                                                                            r = 0[2];
                                                                                            for t, a in v5({
                                                                                                0,
                                                                                                .333333,
                                                                                                .666667,
                                                                                                1
                                                                                            }) do
                                                                                                v5 = v5;
                                                                                                v6 = t;
                                                                                                if math.abs(v2.Value.R - a) < .01 or (math.abs(v2.Value.G - a) < .01 or math.abs(v2.Value.B - a) < .01) then
                                                                                                    return true;
                                                                                                else
                                                                                                    
                                                                                                end; 
                                                                                            end; 
                                                                                        end;
                                                                                        return false; 
                                                                                    end)(K);
                                                                                    if not w[W2[33]] then
                                                                                        w[W2[33]] = true;
                                                                                        JA = getgenv().AutoCounter;
                                                                                        cA = JA;
                                                                                        if JA then
                                                                                            if vA then
                                                                                                JA = not G(K);
                                                                                            end;
                                                                                            cA = vA;
                                                                                            v5 = vA;
                                                                                        end;
                                                                                        if cA then
                                                                                            IA = r79.LocalPlayer.Character.SetAssets;
                                                                                            JA = IA:FindFirstChild("Convergence");
                                                                                            cA = not JA;
                                                                                            if cA then
                                                                                                cA = r81.SupernovaService.RE.Activated;
                                                                                                JA = r79.LocalPlayer.Character.Moveset;
                                                                                                cA:FireServer(JA:FindFirstChild("Supernova"));
                                                                                            end;
                                                                                            cA = r81.ManjiKickService.RE.Activated;
                                                                                            JA = r79.LocalPlayer.Character.Moveset;
                                                                                            cA:FireServer(JA:FindFirstChild("Manji Kick"));
                                                                                            cA = r81.HeadSplitterService.RE.Activated;
                                                                                            JA = r79.LocalPlayer.Character.Moveset;
                                                                                            cA:FireServer(JA:FindFirstChild("Head Splitter"));
                                                                                            cA = r81.EyeCatchService.RE.Activated;
                                                                                            JA = r79.LocalPlayer.Character.Moveset;
                                                                                            cA:FireServer(JA:FindFirstChild("Eye Catching"));
                                                                                        end;
                                                                                        cA = getgenv().AutoBlock and not (function(arg1_58, ...)
                                                                                            local R = {
                                                                                                212,
                                                                                                210
                                                                                            };
                                                                                            v1 = arg1_58;
                                                                                            U = v1:FindFirstChild("Ring");
                                                                                            if not U or not U:IsA("ParticleEmitter") then
                                                                                                return false;
                                                                                            end;
                                                                                            v4 = U.Color;
                                                                                            r = r2;
                                                                                            j = v4.Keypoints;
                                                                                            q = v4[3];
                                                                                            x = v4[2];
                                                                                            for q, v2 in ipairs("ipairs") do
                                                                                                v4 = q;
                                                                                                r = v2.Value.R >= .9;
                                                                                                if r then
                                                                                                    v7 = v2.Value.G >= .9 and v2.Value.B >= .9;
                                                                                                    v5 = Env[v3];
                                                                                                end;
                                                                                                if r then
                                                                                                    return true;
                                                                                                else
                                                                                                    
                                                                                                end; 
                                                                                            end;
                                                                                            return false; 
                                                                                        end)(K);
                                                                                        v5 = vA;
                                                                                        if cA then
                                                                                            cA = r81.BlockService.RE.Activated;
                                                                                            cA:FireServer();
                                                                                        end;
                                                                                    end;
                                                                                else
                                                                                    if w[W2[33]] then
                                                                                        w[W2[33]] = false;
                                                                                        vA = r81.BlockService.RE.Deactivated;
                                                                                        vA:FireServer();
                                                                                    end;
                                                                                end;
                                                                            end;
                                                                        end;
                                                                    else
                                                                        
                                                                    end; 
                                                                end;
                                                                return;
                                                            else
                                                                a = not v2;
                                                            end;
                                                        else
                                                            if w[W2[37]] then
                                                                v2 = r81.BlockService.RE.Deactivated;
                                                                v2:FireServer();
                                                                w[W2[37]] = false;
                                                                w[W2[38]] = nil;
                                                            end;
                                                        end;
                                                    end;
                                                end;
                                            end; 
                                        end;
                                        W2[50] = 19263471264522;
                                        W2[44] = W2[43][W2[44]];
                                        W2[44] = W2[44](W2[43], W2[45]);
                                        W2[44] = 21;
                                        W2[49] = "\xda\x89\x89xa\xb82\xac\x08\xe1";
                                        W2[43] = false;
                                        w[W2[44]] = W2[43];
                                        W2[46] = r3;
                                        W2[47] = r2;
                                        W2[53] = "D*\x84i\xc6e\xbf";
                                        W2[48] = W2[47](W2[49], W2[50]);
                                        W2[45] = W2[46][W2[48]];
                                        W2[47] = function(arg1_59, ...)
                                            local R = {
                                                W2[44],
                                                212,
                                                210
                                            };
                                            v1 = arg1_59;
                                            w[W2[44]] = v1;
                                            getgenv().AutoBlock = v1;
                                            return; 
                                        end;
                                        W2[49] = "\xbb\xa9\xbf\xcdGM\x00{N\"\xceo>\x14S\x87\xc5\xc6";
                                        W2[43] = "AddToggle";
                                        W2[46] = false;
                                        W2[50] = 32886502849489;
                                        W2[43] = FA[W2[43]];
                                        W2[43] = W2[43](FA, W2[45], W2[46], W2[47]);
                                        W2[46] = r3;
                                        W2[47] = r2;
                                        W2[48] = W2[47](W2[49], W2[50]);
                                        W2[45] = W2[46][W2[48]];
                                        W2[49] = "Enum";
                                        W2[48] = Env[W2[49]];
                                        W2[43] = "AddKeybind";
                                        W2[50] = r3;
                                        W2[51] = r2;
                                        W2[52] = W2[51](W2[53], W2[54]);
                                        W2[43] = FA[W2[43]];
                                        W2[49] = W2[50][W2[52]];
                                        W2[47] = W2[48][W2[49]];
                                        W2[52] = ")";
                                        W2[49] = r3;
                                        W2[53] = 12884402378607;
                                        W2[50] = r2;
                                        W2[51] = W2[50](W2[52], W2[53]);
                                        W2[48] = W2[49][W2[51]];
                                        W2[46] = W2[47][W2[48]];
                                        W2[47] = function(...)
                                            local R = {
                                                W2[44],
                                                212,
                                                210
                                            };
                                            if not w[W2[44]] then
                                                return;
                                            end;
                                            getgenv().AutoBlock = not getgenv().AutoBlock;
                                            return; 
                                        end;
                                        W2[49] = "\x89\x02\xd3\xa4\x8d]e\x18\x8b\x8a\x8b";
                                        W2[43] = W2[43](FA, W2[45], W2[46], W2[47]);
                                        W2[46] = r3;
                                        W2[50] = 30475704219503;
                                        W2[47] = r2;
                                        W2[48] = W2[47](W2[49], W2[50]);
                                        W2[45] = W2[46][W2[48]];
                                        W2[47] = function(arg1_60, ...)
                                            local R = {
                                                212,
                                                210
                                            };
                                            getgenv().autopunish = arg1_60;
                                            return; 
                                        end;
                                        W2[49] = "\x11I\xdf+c\xa2#Lx\xde\x8a\xe0\x19\xf4-j";
                                        W2[46] = false;
                                        W2[43] = "AddToggle";
                                        W2[43] = FA[W2[43]];
                                        W2[43] = W2[43](FA, W2[45], W2[46], W2[47]);
                                        W2[46] = r3;
                                        W2[47] = r2;
                                        W2[54] = "[/\xdcC\xf1r\xcb\x06Tmk\xf6\xc0\xc9";
                                        W2[50] = 12575201122015;
                                        W2[43] = "AddSlider";
                                        W2[48] = W2[47](W2[49], W2[50]);
                                        W2[45] = W2[46][W2[48]];
                                        W2[46] = 2;
                                        W2[50] = "getgenv";
                                        W2[47] = 30;
                                        W2[55] = 30752722483184;
                                        W2[49] = Env[W2[50]];
                                        W2[43] = FA[W2[43]];
                                        W2[50] = W2[49]();
                                        W2[51] = r3;
                                        W2[52] = r2;
                                        W2[53] = W2[52](W2[54], W2[55]);
                                        W2[49] = W2[51][W2[53]];
                                        W2[48] = W2[50][W2[49]];
                                        W2[50] = 31696463542695;
                                        W2[49] = function(arg1_61, ...)
                                            local R = {
                                                212,
                                                210
                                            };
                                            getgenv().AutoBlockRange = arg1_61;
                                            return; 
                                        end;
                                        W2[43] = W2[43](FA, W2[45], W2[46], W2[47], W2[48], W2[49]);
                                        W2[49] = "\xc0\xe4\x05\xe8/^\x1f\xd2\xb6\xd2\xbap";
                                        W2[46] = r3;
                                        W2[47] = r2;
                                        W2[48] = W2[47](W2[49], W2[50]);
                                        W2[50] = 12080125220345;
                                        W2[45] = W2[46][W2[48]];
                                        W2[49] = "\tW\xc4\xdc\xef\xd8D\xc8D:\xea\x0e\xe6\xea\xcc9\xa0\xe7";
                                        W2[46] = false;
                                        W2[47] = function(arg1_62, ...)
                                            local R = {
                                                212,
                                                210
                                            };
                                            getgenv().AutoCounter = arg1_62;
                                            return; 
                                        end;
                                        W2[54] = "`a\xad\xe7\xaa\x9a\x0bP\xd7v\xec\x12\xa2`\x1a\xfb";
                                        W2[43] = "AddToggle";
                                        W2[43] = FA[W2[43]];
                                        W2[43] = W2[43](FA, W2[45], W2[46], W2[47]);
                                        W2[43] = "AddSlider";
                                        W2[46] = r3;
                                        W2[47] = r2;
                                        W2[48] = W2[47](W2[49], W2[50]);
                                        W2[55] = 8045963742882;
                                        W2[47] = 30;
                                        W2[50] = "getgenv";
                                        W2[45] = W2[46][W2[48]];
                                        W2[46] = 2;
                                        W2[49] = Env[W2[50]];
                                        W2[43] = FA[W2[43]];
                                        W2[50] = W2[49]();
                                        W2[51] = r3;
                                        W2[52] = r2;
                                        W2[53] = W2[52](W2[54], W2[55]);
                                        W2[49] = W2[51][W2[53]];
                                        W2[48] = W2[50][W2[49]];
                                        W2[49] = function(arg1_63, ...)
                                            local R = {
                                                212,
                                                210
                                            };
                                            getgenv().AutoCounterRange = arg1_63;
                                            return; 
                                        end;
                                        W2[50] = 13708745496815;
                                        W2[43] = W2[43](FA, W2[45], W2[46], W2[47], W2[48], W2[49]);
                                        W2[49] = "Ak6\xc5x\xe7\xd3\xeeUPz7b#\xec\x06}\xa4pb\xff\xd9";
                                        W2[46] = r3;
                                        W2[47] = r2;
                                        W2[48] = W2[47](W2[49], W2[50]);
                                        W2[45] = W2[46][W2[48]];
                                        W2[43] = "AddToggle";
                                        W2[43] = FA[W2[43]];
                                        W2[47] = function(arg1_64, ...)
                                            local R = {
                                                212,
                                                210
                                            };
                                            getgenv().LockedOnPlayersOnly = arg1_64;
                                            return; 
                                        end;
                                        W2[46] = false;
                                        W2[43] = W2[43](FA, W2[45], W2[46], W2[47]);
                                        W2[49] = "\xd90\\u\xd5\xdc?\xfb\xa2\xb2\x15*\xd2Mw`\xd8DAl)9\xf9\xd1\xae\xf5\xba\xf0k\xc6A ";
                                        W2[43] = "AddToggle";
                                        W2[46] = r3;
                                        W2[43] = FA[W2[43]];
                                        W2[50] = 27770531574403;
                                        W2[47] = r2;
                                        W2[48] = W2[47](W2[49], W2[50]);
                                        W2[45] = W2[46][W2[48]];
                                        W2[46] = false;
                                        W2[49] = "\xe6=}\xbf\xce.o^j\xd5";
                                        W2[47] = function(arg1_65, ...)
                                            local R = {
                                                212,
                                                210
                                            };
                                            getgenv().CFrameStare = arg1_65;
                                            return; 
                                        end;
                                        W2[51] = "{\xc1\xcd";
                                        W2[43] = W2[43](FA, W2[45], W2[46], W2[47]);
                                        W2[50] = 18306969018700;
                                        W2[46] = r3;
                                        W2[47] = r2;
                                        W2[52] = 9126381179033;
                                        W2[43] = "AddSection";
                                        W2[48] = W2[47](W2[49], W2[50]);
                                        W2[47] = "workspace";
                                        W2[43] = FA[W2[43]];
                                        W2[45] = W2[46][W2[48]];
                                        W2[43] = W2[43](FA, W2[45]);
                                        W2[46] = Env[W2[47]];
                                        W2[48] = r3;
                                        W2[49] = r2;
                                        W2[50] = W2[49](W2[51], W2[52]);
                                        W2[47] = W2[48][W2[50]];
                                        W2[45] = W2[46][W2[47]];
                                        W2[50] = "(o\xd6\x83";
                                        W2[47] = r3;
                                        W2[48] = r2;
                                        W2[51] = 512612843758;
                                        W2[49] = W2[48](W2[50], W2[51]);
                                        W2[51] = 16262617849236;
                                        W2[46] = W2[47][W2[49]];
                                        W2[43] = W2[45][W2[46]];
                                        W2[47] = r3;
                                        W2[50] = "d\x924\xd8\xc6\x87\x1aT\xfa";
                                        W2[48] = r2;
                                        W2[49] = W2[48](W2[50], W2[51]);
                                        W2[45] = "FindFirstChild";
                                        W2[45] = W2[43][W2[45]];
                                        W2[46] = W2[47][W2[49]];
                                        W2[45] = W2[45](W2[43], W2[46]);
                                        if W2[45] then
                                            W2[51] = 2544426665120;
                                            W2[45] = 64;
                                            W2[43] = nil;
                                            W2[50] = "\xe5\xf9\x11\xfe\x0e\xb6s\x8b\xc7J\xab\xda\x17\x8eZ\xbaI\x15";
                                            w[W2[45]] = W2[43];
                                            W2[47] = r3;
                                            W2[43] = "AddToggle";
                                            W2[43] = FA[W2[43]];
                                            W2[48] = r2;
                                            W2[49] = W2[48](W2[50], W2[51]);
                                            W2[48] = function(arg1_66, ...)
                                                local R = {
                                                    212,
                                                    210,
                                                    159,
                                                    W2[45]
                                                };
                                                if arg1_66 then
                                                    r118 = false;
                                                    v3 = game;
                                                    v5 = v3:GetService("RunService").Heartbeat;
                                                    w[W2[45]] = v5:Connect(function(...)
                                                        local R = {
                                                            159,
                                                            212,
                                                            210,
                                                            24
                                                        };
                                                        r3(workspace.Map.Core.SnowPiles.Snow.CFrame);
                                                        v1 = workspace.Map.Core.SnowPiles.Snow;
                                                        fireproximityprompt(v1:FindFirstChildOfClass("ProximityPrompt"));
                                                        v5 = game.Players.LocalPlayer.Character.SetAssets;
                                                        if v5:FindFirstChild("Snowball") then
                                                            w[W2[45]] = true;
                                                        else
                                                            w[W2[45]] = false;
                                                        end;
                                                        return; 
                                                    end);
                                                else
                                                    v5 = w[W2[45]];
                                                    if v5 then
                                                        v5 = w[W2[45]];
                                                        v5:Disconnect();
                                                    end;
                                                    return;
                                                end; 
                                            end;
                                            W2[45] = nil;
                                            W2[46] = W2[47][W2[49]];
                                            W2[47] = false;
                                            W2[43] = W2[43](FA, W2[46], W2[47], W2[48]);
                                        end;
                                        W2[47] = "workspace";
                                        W2[51] = "\xde\xe8G";
                                        W2[46] = Env[W2[47]];
                                        W2[48] = r3;
                                        W2[52] = 8378286018365;
                                        W2[49] = r2;
                                        W2[50] = W2[49](W2[51], W2[52]);
                                        W2[47] = W2[48][W2[50]];
                                        W2[45] = W2[46][W2[47]];
                                        W2[50] = "\xbf\x99\x0cL";
                                        W2[47] = r3;
                                        W2[48] = r2;
                                        W2[51] = 31713875900847;
                                        W2[49] = W2[48](W2[50], W2[51]);
                                        W2[46] = W2[47][W2[49]];
                                        W2[51] = 26972415799568;
                                        W2[43] = W2[45][W2[46]];
                                        W2[50] = "%}\xea\xcegNq6\x93y\xde\xe2|\x03";
                                        W2[47] = r3;
                                        W2[48] = r2;
                                        W2[49] = W2[48](W2[50], W2[51]);
                                        W2[46] = W2[47][W2[49]];
                                        W2[45] = "FindFirstChild";
                                        W2[45] = W2[43][W2[45]];
                                        W2[45] = W2[45](W2[43], W2[46]);
                                        if W2[45] then
                                            W2[49] = ":\xc7\x05\xb6(s\xb6~\xff\xa9\xee\x86\xed~\xcb";
                                            W2[46] = r3;
                                            W2[50] = 16424249761248;
                                            W2[47] = r2;
                                            W2[48] = W2[47](W2[49], W2[50]);
                                            W2[43] = "AddToggle";
                                            W2[45] = W2[46][W2[48]];
                                            W2[46] = false;
                                            W2[47] = function(arg1_67, ...)
                                                local R = {
                                                    212,
                                                    210,
                                                    159
                                                };
                                                if arg1_67 then
                                                    r119 = {};
                                                    v5 = game;
                                                    v3 = v5:GetService("RunService");
                                                    v3:BindToRenderStep("Doors", 0, function(...)
                                                        local R = {
                                                            212,
                                                            210,
                                                            140,
                                                            159
                                                        };
                                                        x = workspace.Map.Core.HalloweenDoors;
                                                        x = {
                                                            pairs(x:GetChildren())
                                                        };
                                                        v1 = x[2];
                                                        U = x[3];
                                                        x = x[1]; 
                                                    end);
                                                else
                                                    v5 = game;
                                                    v3 = v5:GetService("RunService");
                                                    v3:UnbindFromRenderStep("Doors");
                                                end;
                                                return; 
                                            end;
                                            W2[43] = FA[W2[43]];
                                            W2[43] = W2[43](FA, W2[45], W2[46], W2[47]);
                                        end;
                                        W2[43] = r29;
                                        W2[45] = W2[43]();
                                        if W2[45] then
                                            W2[46] = r3;
                                            W2[50] = 24773452246288;
                                            W2[47] = r2;
                                            W2[49] = "\x0b#]\xablR\x1d\x07\xc6\xdd|\xb1\xe0t\x1b\x9f\x066\xe9\xe6\x9e";
                                            W2[48] = W2[47](W2[49], W2[50]);
                                            W2[50] = 28411356181422;
                                            W2[49] = "\xf4m\xdb\xbc\x14cUopI\xd6[";
                                            W2[45] = W2[46][W2[48]];
                                            W2[46] = false;
                                            W2[43] = "AddToggle";
                                            W2[43] = FA[W2[43]];
                                            W2[52] = 6925297388696;
                                            W2[47] = function(arg1_68, ...)
                                                local R = {
                                                    212,
                                                    210
                                                };
                                                if arg1_68 then
                                                    _G.BLACKFLASHCHAIN = {};
                                                    local function U(arg1_69, ...)
                                                        local R = {
                                                            212,
                                                            210
                                                        };
                                                        v1 = arg1_69;
                                                        v5 = v1:WaitForChild("Humanoid").AnimationPlayed;
                                                        table.insert(_G.BLACKFLASHCHAIN, v5:Connect(function(arg1_70, ...)
                                                            local R = {
                                                                212,
                                                                210
                                                            };
                                                            r120 = arg1_70;
                                                            v5 = v5;
                                                            v5 = v5;
                                                            v5 = v5;
                                                            if r120.Animation and r120.Animation.AnimationId == "rbxassetid://100962226150441" or (r120.Animation.AnimationId == "rbxassetid://95852624447551" or (r120.Animation.AnimationId == "rbxassetid://74145636023952" or r120.Animation.AnimationId == "rbxassetid://110906451704074")) then
                                                                v5 = game.Players.LocalPlayer.Character;
                                                                r121 = v5:FindFirstChild("HumanoidRootPart");
                                                                r122 = (function(...)
                                                                    local R = {
                                                                        212,
                                                                        210
                                                                    };
                                                                    v1 = game.Players.LocalPlayer.Character;
                                                                    v3 = v1;
                                                                    if not (v3 and v1:FindFirstChild("HumanoidRootPart")) then
                                                                        return;
                                                                    end;
                                                                    x = 17;
                                                                    v4 = game.Players;
                                                                    q = v4[2];
                                                                    j = v4[3];
                                                                    v4 = "ipairs";
                                                                    for j, v7 in ipairs(v4:GetPlayers()) do
                                                                        v2 = j;
                                                                        if v7 ~= game.Players.LocalPlayer and v7.Character then
                                                                            v5 = v7.Character;
                                                                            r = v5:FindFirstChild("HumanoidRootPart");
                                                                            if r then
                                                                                t = r.Position - (v3 and v1:FindFirstChild("HumanoidRootPart")).Position;
                                                                                v5 = (t.Magnitude and t) < 17;
                                                                            end;
                                                                        end; 
                                                                    end;
                                                                    return nil; 
                                                                end)();
                                                                if not r122 then
                                                                    return;
                                                                end;
                                                                v4 = r122.CFrame.LookVector;
                                                                j = v4:Dot((r121.Position - r122.Position).Unit) < -0.6;
                                                                v3 = j;
                                                                if j then
                                                                    if j then
                                                                        return;
                                                                    end;
                                                                    getgenv().AutoFeintTiming = .24;
                                                                    v3 = game;
                                                                    v5 = v3:GetService("RunService").RenderStepped;
                                                                    r123 = v5:Connect(function(...)
                                                                        local R = {
                                                                            1,
                                                                            212,
                                                                            210,
                                                                            275,
                                                                            156,
                                                                            155
                                                                        };
                                                                        if not r3.IsPlaying or not getgenv().AutoFeint then
                                                                            v5 = r123;
                                                                            v5:Disconnect();
                                                                        end;
                                                                        if getgenv().AutoFeint and r3.TimePosition >= getgenv().AutoFeintTiming then
                                                                            if r122 and r122.Parent then
                                                                                v3 = r122.CFrame.LookVector;
                                                                                v3 = -0.7;
                                                                                if v3:Dot((r121.Position - r122.Position).Unit) > v3 then
                                                                                    v5 = game;
                                                                                    v3 = v5:GetService("ReplicatedStorage");
                                                                                    v5 = v3:WaitForChild("Knit");
                                                                                    v3 = v5:WaitForChild("Knit");
                                                                                    v5 = v3:WaitForChild("Services");
                                                                                    v3 = v5:WaitForChild("ItadoriService");
                                                                                    v5 = v3:WaitForChild("RE");
                                                                                    v3 = v5:WaitForChild("RightActivated");
                                                                                    v3:FireServer();
                                                                                end;
                                                                            end;
                                                                        end;
                                                                        return; 
                                                                    end);
                                                                    v5 = game.ReplicatedStorage.Utils.Misc.SmokeTrail;
                                                                    r124 = v5:Clone();
                                                                    r124.Parent = workspace.Effects;
                                                                    r124.CFrame = r121.CFrame * CFrame.new(0, -3, 0);
                                                                    v5 = game;
                                                                    v4 = v5:GetService("Debris");
                                                                    v4:AddItem(r124, 1.6);
                                                                    r124.Dash.Smoke.Enabled = true;
                                                                    r124.Dash.Smoke.Rate = 0;
                                                                    v5 = workspace;
                                                                    v4 = v5:Raycast(r121.Position, Vector3.new(0, -r121.Size.Y * 1.6, 0), _G.MapParams);
                                                                    if v4 then
                                                                        r124.Position = v4.Position;
                                                                        v5 = r124.Dash.Smoke;
                                                                        v5:Emit(15);
                                                                    end;
                                                                    t = game;
                                                                    v5 = t:GetService("RunService").RenderStepped;
                                                                    r126 = v5:Connect(function(...)
                                                                        local R = {
                                                                            155,
                                                                            212,
                                                                            210,
                                                                            276,
                                                                            105
                                                                        };
                                                                        v5 = workspace;
                                                                        v1 = v5:Raycast(r3.Position, Vector3.new(0, -r3.Size.Y * 1.6, 0), _G.MapParams);
                                                                        if v1 then
                                                                            r124.Dash.Smoke.Enabled = true;
                                                                            r124.CFrame = r3.CFrame + v1.Position - r3.Position;
                                                                            r124.Velocity = r3.Velocity;
                                                                            if not r125 then
                                                                                r125 = r124.Smoke;
                                                                                r125.Color = ColorSequence.new(v1.Instance.Color);
                                                                                r125.Enabled = true;
                                                                            else
                                                                                if r125.Color.Keypoints[1].Value ~= v1.Instance.Color then
                                                                                    r125.Enabled = false;
                                                                                    v3 = r125;
                                                                                    r125 = v3:Clone();
                                                                                    r125.Color = ColorSequence.new(v1.Instance.Color);
                                                                                    r125.Enabled = true;
                                                                                    r125.Parent = r124;
                                                                                end;
                                                                            end;
                                                                        else
                                                                            r124.Dash.Smoke.Enabled = false;
                                                                            if r125 then
                                                                                r125.Enabled = false;
                                                                            end;
                                                                            return;
                                                                        end; 
                                                                    end);
                                                                    task.delay(1, function(...)
                                                                        local R = {
                                                                            104,
                                                                            105,
                                                                            212,
                                                                            210,
                                                                            276
                                                                        };
                                                                        v5 = r3;
                                                                        if v5 then
                                                                            v5 = r3;
                                                                            v5:Disconnect();
                                                                        end;
                                                                        if r2 then
                                                                            r2.Enabled = false;
                                                                        end;
                                                                        r124.Dash.Smoke.Enabled = false;
                                                                        return; 
                                                                    end);
                                                                    v6 = Instance.new("Sound", r121);
                                                                    v6.SoundId = "rbxassetid://3929467229";
                                                                    v6.Volume = 3;
                                                                    v6:Play();
                                                                    v5 = game;
                                                                    a = v5:GetService("Debris");
                                                                    a:AddItem(v6, 2);
                                                                    v5 = game.ReplicatedStorage.Knit.Knit.Services.MovementService.RE.Dash;
                                                                    v5:FireServer("Right");
                                                                    Y = r121;
                                                                    A = {
                                                                        Y:GetChildren()
                                                                    };
                                                                    a = Y[1];
                                                                    o = Y[2];
                                                                    for v8, A in ipairs(C(A)) do
                                                                        Y = v8;
                                                                        if A:IsA("BodyVelocity") then
                                                                            A:Destroy();
                                                                        end; 
                                                                    end;
                                                                    r127 = Instance.new("BodyVelocity", r121);
                                                                    r127.MaxForce = Vector3.new(100000, 100000, 100000);
                                                                    r127.P = 100000;
                                                                    v8 = game;
                                                                    v5 = v8:GetService("RunService").RenderStepped;
                                                                    r128 = v5:Connect(function(...)
                                                                        local R = {
                                                                            212,
                                                                            210,
                                                                            69,
                                                                            156,
                                                                            155
                                                                        };
                                                                        if _G.ChainMethod == "Hop" then
                                                                            x = r127.Velocity.Unit;
                                                                            r127.Velocity = x:Lerp((r122.Position - r122.CFrame.LookVector * 4.5 - r121.Position).Unit, .18).Unit * 50.5;
                                                                        else
                                                                            if _G.ChainMethod == "Side" then
                                                                                r127.Velocity = (r122.Position - r122.CFrame.LookVector * 5 - r121.Position).Unit * 50.5;
                                                                            end;
                                                                            return;
                                                                        end; 
                                                                    end);
                                                                    if _G.ChainMethod == "Hop" then
                                                                        Y = .27;
                                                                    end;
                                                                    task.delay(.2, function(...)
                                                                        local R = {
                                                                            70,
                                                                            69
                                                                        };
                                                                        v5 = r3;
                                                                        if v5 then
                                                                            v5 = r3;
                                                                            v5:Disconnect();
                                                                        end;
                                                                        v5 = r2;
                                                                        v5:Destroy();
                                                                        return; 
                                                                    end);
                                                                    return;
                                                                else
                                                                    j = game.Players.LocalPlayer.Character.HumanoidRootPart;
                                                                    v3 = j:FindFirstChild("Feint");
                                                                end;
                                                            end; 
                                                        end));
                                                        return; 
                                                    end;
                                                    q = game;
                                                    U(q:GetService("Players").LocalPlayer.Character);
                                                    j = game;
                                                    x = j:GetService("Players").LocalPlayer.CharacterAdded;
                                                    _G.BLACKFLASHCHAIN_CHARCONN = x:Connect(U);
                                                else
                                                    q = r2;
                                                    j = q("\xbd\xde\x00aM\x98'\xc1\x1do\xe3\x96\x00K\x93", 5680712993365);
                                                    if _G[r3[j]] then
                                                        j = _G;
                                                        q = j.BLACKFLASHCHAIN;
                                                        U = j[2];
                                                        q = j[1];
                                                        for x, v4 in ipairs(q) do
                                                            r129 = v4;
                                                            j = x;
                                                            if typeof(w[v5]) == "Instance" or typeof(w[v5]) == "RBXScriptConnection" then
                                                                pcall(function(...)
                                                                    v5 = w[v5];
                                                                    v5:Disconnect();
                                                                    return; 
                                                                end);
                                                            end; 
                                                        end;
                                                    end;
                                                    if _G.BLACKFLASHCHAIN_CHARCONN then
                                                        pcall(function(...)
                                                            local R = {
                                                                212,
                                                                210
                                                            };
                                                            v5 = _G.BLACKFLASHCHAIN_CHARCONN;
                                                            v5:Disconnect();
                                                            return; 
                                                        end);
                                                    end;
                                                    return;
                                                end; 
                                            end;
                                            W2[43] = W2[43](FA, W2[45], W2[46], W2[47]);
                                            W2[46] = r3;
                                            W2[47] = r2;
                                            W2[48] = W2[47](W2[49], W2[50]);
                                            W2[45] = W2[46][W2[48]];
                                            W2[53] = 2641012212941;
                                            W2[48] = r3;
                                            W2[51] = "\\\xe3\x85";
                                            W2[49] = r2;
                                            W2[50] = W2[49](W2[51], W2[52]);
                                            W2[47] = W2[48][W2[50]];
                                            W2[49] = r3;
                                            W2[52] = "\x0f.\xed\x17";
                                            W2[50] = r2;
                                            W2[43] = "AddDropdown";
                                            W2[51] = W2[50](W2[52], W2[53]);
                                            W2[53] = "Ok/";
                                            W2[48] = W2[49][W2[51]];
                                            W2[54] = 29706599183881;
                                            W2[50] = r3;
                                            W2[46] = {
                                                W2[47],
                                                W2[48]
                                            };
                                            W2[47] = function(arg1_71, ...)
                                                local R = {
                                                    212,
                                                    210
                                                };
                                                _G.ChainMethod = arg1_71;
                                                return; 
                                            end;
                                            W2[48] = false;
                                            W2[51] = r2;
                                            W2[43] = FA[W2[43]];
                                            W2[52] = W2[51](W2[53], W2[54]);
                                            W2[49] = W2[50][W2[52]];
                                            W2[43] = W2[43](FA, W2[45], W2[46], W2[47], W2[48], W2[49]);
                                            W2[49] = "\x15\r\xda7:\x8b@\x07D\x91";
                                            W2[46] = r3;
                                            W2[50] = 31177568827574;
                                            W2[47] = r2;
                                            W2[48] = W2[47](W2[49], W2[50]);
                                            W2[45] = W2[46][W2[48]];
                                            W2[47] = function(arg1_72, ...)
                                                local R = {
                                                    212,
                                                    210
                                                };
                                                getgenv().AutoFeint = arg1_72;
                                                return; 
                                            end;
                                            W2[43] = "AddToggle";
                                            W2[46] = false;
                                            W2[43] = FA[W2[43]];
                                            W2[43] = W2[43](FA, W2[45], W2[46], W2[47]);
                                            W2[49] = "\xb4\x7f\xf7k\xc4l\x94\x15ha\xd0\xa4";
                                            W2[43] = "AddSlider";
                                            W2[46] = r3;
                                            W2[50] = 13495483472012;
                                            W2[47] = r2;
                                            W2[48] = W2[47](W2[49], W2[50]);
                                            W2[45] = W2[46][W2[48]];
                                            W2[49] = function(arg1_73, ...)
                                                local R = {
                                                    212,
                                                    210
                                                };
                                                getgenv().AutoFeintTiming = .24 + (arg1_73 - 1) * .01;
                                                return; 
                                            end;
                                            W2[47] = 44;
                                            W2[43] = FA[W2[43]];
                                            W2[48] = 1;
                                            W2[46] = 1;
                                            W2[43] = W2[43](FA, W2[45], W2[46], W2[47], W2[48], W2[49]);
                                        end;
                                        W2[50] = "\x84\xb7\xd7u'\x8b(p\xc4:'\x10";
                                        W2[43] = nil;
                                        W2[45] = 116;
                                        W2[52] = "0\x1dr\xc1\xfd9hO\xe7\xc3P\x9e\x00\x92\x89\xb85\x86P\x04\xf8h\xbf\x91J\x01\x80\xb2\xa4\x9b\xaa\r\x80";
                                        W2[51] = 21929972033507;
                                        w[W2[45]] = W2[43];
                                        W2[47] = r3;
                                        W2[48] = r2;
                                        W2[43] = "AddToggle";
                                        W2[43] = FA[W2[43]];
                                        W2[49] = W2[48](W2[50], W2[51]);
                                        W2[48] = function(arg1_74, ...)
                                            local R = {
                                                212,
                                                210,
                                                W2[45]
                                            };
                                            if arg1_74 then
                                                v3 = game;
                                                v5 = v3:GetService("RunService").RenderStepped;
                                                w[W2[45]] = v5:Connect(function(...)
                                                    local R = {
                                                        212,
                                                        210
                                                    };
                                                    v1 = RaycastParams.new();
                                                    U = {
                                                        game.Players.LocalPlayer.Character
                                                    };
                                                    j = workspace.Characters;
                                                    x = j[2];
                                                    q = j[3];
                                                    j = "pairs";
                                                    for q, v2 in pairs(j:GetChildren()) do
                                                        v4 = q;
                                                        table.insert(U, v2); 
                                                    end;
                                                    v4 = workspace.Effects;
                                                    v2 = {
                                                        v4:GetChildren()
                                                    };
                                                    j = v4[3];
                                                    q = v4[2];
                                                    for j, v2 in pairs(C(v2)) do
                                                        v4 = j;
                                                        table.insert(U, v2); 
                                                    end;
                                                    v1.FilterDescendantsInstances = U;
                                                    v1.FilterType = Enum.RaycastFilterType.Blacklist;
                                                    x = game.Players.LocalPlayer.Character.HumanoidRootPart;
                                                    v5 = game.Players.LocalPlayer.Character.Humanoid.MoveDirection.Magnitude ~= 0;
                                                    if v5 then
                                                        v5 = workspace;
                                                        j = v5:Raycast(x.Position, x.CFrame.LookVector * 4, v1);
                                                        if j then
                                                            v4 = j.Instance.Name ~= "Climbing" and j.Instance.Name ~= "Ladder";
                                                            v5 = workspace;
                                                        end;
                                                        if j then
                                                            game[r3[r2("\x91e\xdd\xfe\xa9M\"", o)]].LocalPlayer.Character.Humanoid.Jump = true;
                                                        end;
                                                    end;
                                                    return; 
                                                end);
                                            else
                                                v5 = w[W2[45]];
                                                v5:Disconnect();
                                            end;
                                            return; 
                                        end;
                                        W2[46] = W2[47][W2[49]];
                                        W2[47] = false;
                                        W2[43] = W2[43](FA, W2[46], W2[47], W2[48]);
                                        W2[43] = 0;
                                        W2[46] = 117;
                                        W2[47] = 118;
                                        w[W2[46]] = W2[43];
                                        W2[43] = 0;
                                        w[W2[47]] = W2[43];
                                        W2[53] = 6885849205894;
                                        W2[49] = r3;
                                        W2[50] = r2;
                                        W2[51] = W2[50](W2[52], W2[53]);
                                        W2[43] = "AddToggle";
                                        W2[50] = function(arg1_75, ...)
                                            local R = {
                                                212,
                                                210,
                                                W2[47],
                                                W2[46],
                                                158
                                            };
                                            if arg1_75 then
                                                v5 = game;
                                                v3 = v5:GetService("RunService");
                                                v3:BindToRenderStep("Auto-Hiromi", 0, function(...)
                                                    local R = {
                                                        W2[47],
                                                        W2[46],
                                                        212,
                                                        210,
                                                        158
                                                    };
                                                    if tick() - r3 < r2 * .01 then
                                                        return;
                                                    end;
                                                    r3 = tick();
                                                    q = game.Players.LocalPlayer.PlayerGui;
                                                    j = {
                                                        q:GetChildren()
                                                    };
                                                    x = q[3];
                                                    for x, j in q[1], pairs(C(j)) do
                                                        q = x;
                                                        if j.Name == "QTE" then
                                                            v4 = game;
                                                            v4 = "TouchEnabled";
                                                            if v4:GetService("UserInputService")[v4] then
                                                                r33(j.QTE_MOBILE);
                                                            else
                                                                v5 = game;
                                                                v4 = v5:GetService("VirtualInputManager");
                                                                v4:SendKeyEvent(true, Enum.KeyCode[j.QTE_PC.Text], false, game);
                                                                v5 = game;
                                                                v4 = v5:GetService("VirtualInputManager");
                                                                v4:SendKeyEvent(false, Enum.KeyCode[j.QTE_PC.Text], false, game);
                                                            end;
                                                        end; 
                                                    end;
                                                    return; 
                                                end);
                                            else
                                                v5 = game;
                                                v3 = v5:GetService("RunService");
                                                v3:UnbindFromRenderStep("Auto-Hiromi");
                                            end;
                                            return; 
                                        end;
                                        W2[43] = FA[W2[43]];
                                        W2[48] = W2[49][W2[51]];
                                        W2[52] = "\x07\xec\x82\xe2\xb8\xf8\x87\xcf~\xa8\x94";
                                        W2[49] = false;
                                        W2[53] = 18099385098476;
                                        W2[43] = W2[43](FA, W2[48], W2[49], W2[50]);
                                        W2[43] = "AddSlider";
                                        W2[49] = r3;
                                        W2[50] = r2;
                                        W2[51] = W2[50](W2[52], W2[53]);
                                        W2[48] = W2[49][W2[51]];
                                        W2[49] = 0;
                                        W2[50] = 50;
                                        W2[51] = 0;
                                        W2[52] = function(arg1_76, ...)
                                            w[W2[46]] = arg1_76;
                                            return; 
                                        end;
                                        W2[43] = FA[W2[43]];
                                        W2[43] = W2[43](FA, W2[48], W2[49], W2[50], W2[51], W2[52]);
                                        W2[43] = r29;
                                        W2[48] = W2[43]();
                                        if W2[48] then
                                            W2[43] = nil;
                                            W2[48] = 46;
                                            w[W2[48]] = W2[43];
                                            W2[43] = nil;
                                            W2[49] = 47;
                                            W2[55] = 16691219979868;
                                            W2[54] = "\xefw?n,Z\x82\x9d\x07\xea\x06f\x95'\\\x18\x94\xdah\xf3\x9e`v\xbc";
                                            w[W2[49]] = W2[43];
                                            W2[51] = r3;
                                            W2[52] = r2;
                                            W2[53] = W2[52](W2[54], W2[55]);
                                            W2[43] = "AddToggle";
                                            W2[50] = W2[51][W2[53]];
                                            W2[43] = FA[W2[43]];
                                            W2[52] = function(arg1_77, ...)
                                                local R = {
                                                    212,
                                                    210,
                                                    W2[48],
                                                    158,
                                                    W2[49]
                                                };
                                                if arg1_77 then
                                                    v3 = game;
                                                    v5 = v3:GetService("RunService").Heartbeat;
                                                    w[W2[49]] = v5:Connect(function(...)
                                                        local R = {
                                                            212,
                                                            210,
                                                            W2[48],
                                                            158
                                                        };
                                                        v5 = game.Players.LocalPlayer.PlayerGui;
                                                        v1 = v5:FindFirstChild("Choose");
                                                        if not v1 then
                                                            return;
                                                        end;
                                                        v5 = not (v1:FindFirstChild("Timer").Text == "1");
                                                        if v5 then
                                                            w[W2[48]] = nil;
                                                            return;
                                                        end;
                                                        U = workspace.Domains.Domain;
                                                        if U:GetAttribute("UI2") == true then
                                                            return;
                                                        end;
                                                        x = U:GetAttribute("ConfessCount");
                                                        r = "\x9d\xee\xca\xfc\xa4mnj\xcf\x1a\x97\xe1";
                                                        q = U:GetAttribute("DenialCount");
                                                        t = 12006280435158;
                                                        v2 = v5;
                                                        j = U:GetAttribute(r3[r2(r, t)]);
                                                        v3 = x;
                                                        if x then
                                                            r = not (v1:FindFirstChild("Timer").Text == "1");
                                                            t = x >= 1;
                                                            v7 = t;
                                                            if t then
                                                                if q then
                                                                    v5 = v5;
                                                                    t = x > q;
                                                                    v5 = v5;
                                                                    v5 = r;
                                                                    v3 = t and j;
                                                                    v5 = v5;
                                                                    if v3 then
                                                                        v4 = "Confess";
                                                                    else
                                                                        v2 = q;
                                                                        v7 = v2;
                                                                        if q then
                                                                            v6 = q >= 1;
                                                                            t = v2;
                                                                            r = v6;
                                                                            if v6 then
                                                                                if x then
                                                                                    v5 = v5;
                                                                                    v5 = v5;
                                                                                    v5 = t;
                                                                                    v5 = v5;
                                                                                    if q > x and v5 then
                                                                                        v4 = "Denial";
                                                                                    else
                                                                                        r = v7;
                                                                                        v7 = j;
                                                                                        if j then
                                                                                            a = U:GetAttribute(r3[v7]) >= 1;
                                                                                            t = a;
                                                                                            v6 = v7;
                                                                                            if a then
                                                                                                o = v7;
                                                                                                A = v7;
                                                                                                if x then
                                                                                                    v8 = U:GetAttribute(r3[v7]) > x;
                                                                                                    a = v8;
                                                                                                    if v8 then
                                                                                                        A = A;
                                                                                                        if q then
                                                                                                            v5 = A;
                                                                                                            a = U:GetAttribute(r3[v7]) > q;
                                                                                                            v5 = v5;
                                                                                                            t = a;
                                                                                                            v5 = v5;
                                                                                                            if v7 then
                                                                                                                v4 = "Silence";
                                                                                                            end;
                                                                                                            if nil then
                                                                                                                r = nil ~= w[W2[48]];
                                                                                                            end;
                                                                                                            if nil then
                                                                                                                r33(v5:FindFirstChild("Choose")[nil]);
                                                                                                                w[W2[48]] = nil;
                                                                                                            end;
                                                                                                            return;
                                                                                                        else
                                                                                                            Y = -math.huge;
                                                                                                        end;
                                                                                                    end;
                                                                                                else
                                                                                                    Y = -math.huge;
                                                                                                end;
                                                                                            end;
                                                                                        end;
                                                                                    end;
                                                                                else
                                                                                    v8 = -math.huge;
                                                                                end;
                                                                            end;
                                                                        end;
                                                                    end;
                                                                else
                                                                    o = -math.huge;
                                                                end;
                                                            end;
                                                        end; 
                                                    end);
                                                else
                                                    if w[W2[49]] then
                                                        v5 = w[W2[49]];
                                                        v5:Disconnect();
                                                        w[W2[49]] = nil;
                                                        w[W2[48]] = nil;
                                                    end;
                                                    return;
                                                end; 
                                            end;
                                            W2[49] = nil;
                                            W2[48] = nil;
                                            W2[51] = false;
                                            W2[43] = W2[43](FA, W2[50], W2[51], W2[52]);
                                        end;
                                        W2[48] = 67;
                                        W2[43] = {};
                                        w[W2[48]] = W2[43];
                                        W2[53] = "\x97\xe4\xa7\x84\xcb\xb0\x81\xf4\xf4";
                                        W2[50] = r3;
                                        W2[51] = r2;
                                        W2[54] = 6627361573902;
                                        W2[52] = W2[51](W2[53], W2[54]);
                                        W2[49] = W2[50][W2[52]];
                                        W2[58] = 13398788986975;
                                        W2[52] = r3;
                                        W2[55] = "\xc4\xe7\x10]\x99\x17X\x08";
                                        W2[57] = 22189964634205;
                                        W2[53] = r2;
                                        W2[56] = 21627364255575;
                                        W2[54] = W2[53](W2[55], W2[56]);
                                        W2[51] = W2[52][W2[54]];
                                        W2[53] = r3;
                                        W2[56] = "\x07\x93\xcde\x9e\x13[\xbb";
                                        W2[54] = r2;
                                        W2[55] = W2[54](W2[56], W2[57]);
                                        W2[52] = W2[53][W2[55]];
                                        W2[43] = "AddDropdown";
                                        W2[50] = {
                                            W2[51],
                                            W2[52]
                                        };
                                        W2[51] = function(arg1_78, ...)
                                            local R = {
                                                212,
                                                210
                                            };
                                            _G.M1Method = arg1_78;
                                            return; 
                                        end;
                                        W2[43] = FA[W2[43]];
                                        W2[52] = false;
                                        W2[54] = r3;
                                        W2[57] = "B\x8b\xa6\xc0\xba\xd4+\x8a";
                                        W2[55] = r2;
                                        W2[56] = W2[55](W2[57], W2[58]);
                                        W2[53] = W2[54][W2[56]];
                                        W2[43] = W2[43](FA, W2[49], W2[50], W2[51], W2[52], W2[53]);
                                        W2[50] = r3;
                                        W2[54] = 5104977627465;
                                        W2[53] = "\xea\xbf\x03\xfd\xbbh\xe2\xf8\xa9";
                                        W2[43] = "AddToggle";
                                        W2[51] = r2;
                                        W2[52] = W2[51](W2[53], W2[54]);
                                        W2[51] = function(arg1_79, ...)
                                            local R = {
                                                212,
                                                q,
                                                W2[48]
                                            };
                                            if arg1_79 then
                                                v2 = game;
                                                q = v2:GetService("ReplicatedStorage").Knit.Knit.Services;
                                                x = q[3];
                                                q = q[1];
                                                for x, v4 in q, ipairs(q:GetChildren()) do
                                                    j = x;
                                                    if not v4:FindFirstChild("RE") then
                                                        
                                                    end; 
                                                end;
                                            else
                                                q = 305[3];
                                                for q, v4 in 305[1], ipairs(w[W2[48]]) do
                                                    j = q;
                                                    v4:Disconnect(); 
                                                end;
                                                table.clear(w[W2[48]]);
                                                return;
                                            end; 
                                        end;
                                        W2[55] = 15502681087026;
                                        W2[43] = FA[W2[43]];
                                        W2[49] = W2[50][W2[52]];
                                        W2[53] = "l\xff@\xa4\x16~\x8eA6>";
                                        W2[54] = 33324277791901;
                                        W2[50] = false;
                                        W2[43] = W2[43](FA, W2[49], W2[50], W2[51]);
                                        W2[50] = r3;
                                        W2[51] = r2;
                                        W2[52] = W2[51](W2[53], W2[54]);
                                        W2[49] = W2[50][W2[52]];
                                        W2[54] = 15051051555680;
                                        W2[53] = "\xe8\x0f\xf8\xb8L\xe8\xa4\x12d\xa9\xed\xf8e";
                                        W2[51] = function(arg1_80, ...)
                                            local R = {
                                                212,
                                                210
                                            };
                                            if arg1_80 then
                                                v5 = game;
                                                v3 = v5:GetService("RunService");
                                                v3:BindToRenderStep("Auto-Burst", 0, function(...)
                                                    local R = {
                                                        212,
                                                        210
                                                    };
                                                    x = game.Players.LocalPlayer.Character.HumanoidRootPart;
                                                    v1 = x[2];
                                                    x = x[1];
                                                    for U, j in pairs(x:GetChildren()) do
                                                        q = U;
                                                        v4 = j.Name == "BurstIcon" or j.Name == "Evade";
                                                        if v4 then
                                                            v4 = game.Players.LocalPlayer.Character.Humanoid.MoveDirection;
                                                            v2 = "Left";
                                                            if v4.Magnitude > 0 then
                                                                v6 = v4.Z;
                                                                if math.abs(v4.X) > math.abs(v6) then
                                                                    v5 = r > t;
                                                                    v2 = game[r3[r2("\xe5'\x13\xf2\xf2\x7f\xe6", A)]][r3[r2("'\x8f\x80p\x93 G]\xab\xa6\xec", Y)]].Character.Humanoid.MoveDirection.X > 0 and "Right" or "Left";
                                                                else
                                                                    v5 = r > t;
                                                                    v2 = game[r3[r2("\xe5'\x13\xf2\xf2\x7f\xe6", A)]][r3[r2("'\x8f\x80p\x93 G]\xab\xa6\xec", Y)]].Character.Humanoid.MoveDirection.Z < 0 and "Back" or "Left";
                                                                    v5 = game;
                                                                    v6 = v5:GetService("ReplicatedStorage");
                                                                    v5 = v6:WaitForChild("Knit");
                                                                    v6 = v5:WaitForChild("Knit");
                                                                    v5 = v6:WaitForChild("Services");
                                                                    v6 = v5:WaitForChild("MovementService");
                                                                    v5 = v6:WaitForChild("RE");
                                                                    v6 = v5:WaitForChild("Dash");
                                                                    v6:FireServer(unpack({
                                                                        v2,
                                                                        true
                                                                    }));
                                                                end;
                                                            end;
                                                        end; 
                                                    end;
                                                    return; 
                                                end);
                                            else
                                                v5 = game;
                                                v3 = v5:GetService("RunService");
                                                v3:UnbindFromRenderStep("Auto-Burst");
                                            end;
                                            return; 
                                        end;
                                        W2[50] = false;
                                        W2[43] = "AddToggle";
                                        W2[43] = FA[W2[43]];
                                        W2[43] = W2[43](FA, W2[49], W2[50], W2[51]);
                                        W2[50] = r3;
                                        W2[51] = r2;
                                        W2[52] = W2[51](W2[53], W2[54]);
                                        W2[54] = "\xc0\xbf\x18!Gs\x94\xd1\x00j\x1cr\xe7\xb1g\x92pm\x89\x85\x86\x19\x95\xabg\x83}\xd0Dc5\xb4\xd0J\xa6\xd9\xc5,;\x96D:\x1dp";
                                        W2[49] = W2[50][W2[52]];
                                        W2[43] = "AddSection";
                                        W2[43] = FA[W2[43]];
                                        W2[43] = W2[43](FA, W2[49]);
                                        W2[49] = 68;
                                        W2[43] = {};
                                        w[W2[49]] = W2[43];
                                        W2[51] = r3;
                                        W2[52] = r2;
                                        W2[53] = W2[52](W2[54], W2[55]);
                                        W2[50] = W2[51][W2[53]];
                                        W2[52] = function(arg1_81, ...)
                                            local R = {
                                                W2[49],
                                                U,
                                                210
                                            };
                                            if arg1_81 then
                                                U = game.ReplicatedStorage.Knit.Knit.Services.DivergentFistService.RE.Effects.OnClientEvent;
                                                w[W2[49]].AutoBlackFlash = U:Connect(function(...)
                                                    local R = {
                                                        U,
                                                        210
                                                    };
                                                    v5 = {
                                                        select(-1, ...)
                                                    };
                                                    x = v5[1] == "CurseBuild";
                                                    if x and v5[2] == game.Players.LocalPlayer.Character then
                                                        task.wait(.07);
                                                        v2 = game;
                                                        v5 = v2:GetService("ReplicatedStorage").Knit.Knit.Services.DivergentFistService.RE.Activated;
                                                        x = game.Players.LocalPlayer.Character.Moveset;
                                                        v5:FireServer(x:FindFirstChild("Divergent Fist"));
                                                    end;
                                                    return; 
                                                end);
                                            else
                                                v5 = w[W2[49]].AutoBlackFlash;
                                                v5:Disconnect();
                                            end;
                                            return; 
                                        end;
                                        W2[43] = "AddToggle";
                                        W2[43] = FA[W2[43]];
                                        W2[55] = 1842393138009;
                                        W2[51] = false;
                                        W2[43] = W2[43](FA, W2[50], W2[51], W2[52]);
                                        W2[51] = r3;
                                        W2[52] = r2;
                                        W2[54] = "/i\x88\xcagu-hh\xac\x02k\xd1\x81\xbd";
                                        W2[53] = W2[52](W2[54], W2[55]);
                                        W2[52] = function(arg1_82, ...)
                                            local R = {
                                                212,
                                                210
                                            };
                                            if arg1_82 then
                                                _G.BLACKFLASH = {};
                                                q = game;
                                                local function U(arg1_83, ...)
                                                    local R = {
                                                        212,
                                                        210
                                                    };
                                                    v1 = arg1_83;
                                                    v5 = v1:WaitForChild("Humanoid").AnimationPlayed;
                                                    table.insert(_G.BLACKFLASH, v5:Connect(function(arg1_84, ...)
                                                        local R = {
                                                            212,
                                                            210
                                                        };
                                                        v1 = arg1_84;
                                                        U = v1.Animation and v1.Animation.AnimationId == "rbxassetid://100962226150441";
                                                        v5 = v5;
                                                        v5 = v5;
                                                        v5 = v5;
                                                        v5 = v5;
                                                        v5 = v5;
                                                        v3 = U or (v1.Animation.AnimationId == "rbxassetid://95852624447551" or (v1.Animation.AnimationId == "rbxassetid://74145636023952" or (v1.Animation.AnimationId == "rbxassetid://115234621584704" or (v1.Animation.AnimationId == "rbxassetid://124937162378188" or (v1.Animation.AnimationId == "rbxassetid://110906451704074" or v1.Animation.AnimationId == "rbxassetid://72475960800126")))));
                                                        v5 = v5;
                                                        if v3 then
                                                            task.wait(.142);
                                                            v5 = game;
                                                            v3 = v5:GetService("ReplicatedStorage");
                                                            v5 = v3:WaitForChild("Knit");
                                                            v3 = v5:WaitForChild("Knit");
                                                            v5 = v3:WaitForChild("Services");
                                                            v3 = v5:WaitForChild("DivergentFistService");
                                                            v5 = v3:WaitForChild("RE");
                                                            v3 = v5:WaitForChild("Activated");
                                                            j = game;
                                                            U = j:GetService("Players").LocalPlayer.Character.Moveset;
                                                            v3:FireServer(U:FindFirstChild("Divergent Fist"));
                                                            v5 = game;
                                                            v3 = v5:GetService("ReplicatedStorage");
                                                            v5 = v3:WaitForChild("Knit");
                                                            v3 = v5:WaitForChild("Knit");
                                                            v5 = v3:WaitForChild("Services");
                                                            v3 = v5:WaitForChild("FocusStrikeService");
                                                            v5 = v3:WaitForChild("RE");
                                                            v3 = v5:WaitForChild("Activated");
                                                            j = game;
                                                            U = j:GetService("Players").LocalPlayer.Character.Moveset;
                                                            v3:FireServer(U:FindFirstChild("Focus Strike"));
                                                            v4 = game;
                                                            v5 = v4:GetService("ReplicatedStorage").Knit.Knit.Services.GojoService.RE.RightActivated;
                                                            v5:FireServer();
                                                            v5 = game;
                                                            v3 = v5:GetService("ReplicatedStorage");
                                                            v5 = v3:WaitForChild("Knit");
                                                            v3 = v5:WaitForChild("Knit");
                                                            v5 = v3:WaitForChild("Services");
                                                            v3 = v5:WaitForChild("CleaveRushService");
                                                            v5 = v3:WaitForChild("RE");
                                                            v3 = v5:WaitForChild("Activated");
                                                            j = game;
                                                            U = j:GetService("Players").LocalPlayer.Character.Moveset;
                                                            v3:FireServer(U:FindFirstChild("Cleave Rush"));
                                                        end;
                                                        return; 
                                                    end));
                                                    return; 
                                                end;
                                                U(q:GetService("Players").LocalPlayer.Character);
                                                j = game;
                                                x = j:GetService("Players").LocalPlayer.CharacterAdded;
                                                _G.BLACKFLASH_CHARCONN = x:Connect(U);
                                            else
                                                q = r2;
                                                j = q("\xcc\xa5b9\xa2\x85\x9eH:\xbd", 8493459623795);
                                                if _G[r3[j]] then
                                                    j = _G;
                                                    q = j.BLACKFLASH;
                                                    U = j[2];
                                                    q = j[1];
                                                    for x, v4 in ipairs(q) do
                                                        j = x;
                                                        r130 = v4;
                                                        if typeof(w[v5]) == "Instance" or typeof(w[v5]) == "RBXScriptConnection" then
                                                            pcall(function(...)
                                                                v5 = w[v5];
                                                                v5:Disconnect();
                                                                return; 
                                                            end);
                                                        end; 
                                                    end;
                                                end;
                                                if _G.BLACKFLASH_CHARCONN then
                                                    pcall(function(...)
                                                        local R = {
                                                            212,
                                                            210
                                                        };
                                                        v5 = _G.BLACKFLASH_CHARCONN;
                                                        v5:Disconnect();
                                                        return; 
                                                    end);
                                                end;
                                                return;
                                            end; 
                                        end;
                                        W2[43] = "AddToggle";
                                        W2[50] = W2[51][W2[53]];
                                        W2[54] = "\x08V\xa4\xaeAg\xe8\x1c\xcdUZ\xd7\xb4\x92GnH?\x95\xe0";
                                        W2[43] = FA[W2[43]];
                                        W2[51] = false;
                                        W2[43] = W2[43](FA, W2[50], W2[51], W2[52]);
                                        W2[43] = "AddToggle";
                                        W2[55] = 30896830527539;
                                        W2[51] = r3;
                                        W2[52] = r2;
                                        W2[53] = W2[52](W2[54], W2[55]);
                                        W2[54] = "\x8b\xa7\xf7c.\rc\xf3\x16\xd5ua&\xaa\x17X\xa6\x12\x12\"";
                                        W2[50] = W2[51][W2[53]];
                                        W2[52] = function(arg1_85, ...)
                                            local R = {
                                                212,
                                                210
                                            };
                                            if arg1_85 then
                                                _G.TODOBLACKFLASH = {};
                                                q = game;
                                                local function U(arg1_86, ...)
                                                    local R = {
                                                        212,
                                                        210
                                                    };
                                                    v1 = arg1_86;
                                                    v5 = v1:WaitForChild("Humanoid").AnimationPlayed;
                                                    v5 = v1:WaitForChild("Humanoid").AnimationPlayed;
                                                    table.insert(_G.TODOBLACKFLASH, v5:Connect(function(arg1_87, ...)
                                                        local R = {
                                                            212,
                                                            210
                                                        };
                                                        v1 = arg1_87;
                                                        if v1.Animation and v1.Animation.AnimationId == "rbxassetid://111720035828971" then
                                                            task.wait(.8);
                                                            v4 = game;
                                                            v5 = v4:GetService("ReplicatedStorage").Knit.Knit.Services.TodoService.RE.RightActivated;
                                                            v5:FireServer();
                                                            task.wait(.4);
                                                        end;
                                                        return; 
                                                    end));
                                                    table.insert(_G.TODOBLACKFLASH, v5:Connect(function(arg1_88, ...)
                                                        local R = {
                                                            212,
                                                            210
                                                        };
                                                        v1 = arg1_88;
                                                        U = v1.Animation;
                                                        if U and v1.Animation.AnimationId == "rbxassetid://100081544058065" then
                                                            v4 = game;
                                                            v5 = v4:GetService("ReplicatedStorage").Knit.Knit.Services.BruteForceService.RE.Activated;
                                                            U = game.Players.LocalPlayer.Character.Moveset;
                                                            v5:FireServer(U:FindFirstChild("Brute Force"));
                                                            task.wait(0.75);
                                                            v4 = game;
                                                            v5 = v4:GetService("ReplicatedStorage").Knit.Knit.Services.BruteForceService.RE.Activated;
                                                            U = game.Players.LocalPlayer.Character.Moveset;
                                                            v5:FireServer(U:FindFirstChild("Brute Force"));
                                                        end;
                                                        return; 
                                                    end));
                                                    return; 
                                                end;
                                                U(q:GetService("Players").LocalPlayer.Character);
                                                j = game;
                                                x = j:GetService("Players").LocalPlayer.CharacterAdded;
                                                _G.TODOBLACKFLASH_CHARCONN = x:Connect(U);
                                            else
                                                q = r2;
                                                j = q("E\xbb\xe4b\xa5\xbb`\xec\xc0\xb2R\xbfl\xcc", 9833970635235);
                                                if _G[r3[j]] then
                                                    j = _G;
                                                    q = j.TODOBLACKFLASH;
                                                    q = j[1];
                                                    x = j[3];
                                                    for x, v4 in q, ipairs(q) do
                                                        j = x;
                                                        r131 = v4;
                                                        if typeof(r131) == "RBXScriptConnection" then
                                                            pcall(function(...)
                                                                v5 = r131;
                                                                v5:Disconnect();
                                                                return; 
                                                            end);
                                                        end; 
                                                    end;
                                                end;
                                                if _G.TODOBLACKFLASH_CHARCONN then
                                                    pcall(function(...)
                                                        local R = {
                                                            212,
                                                            210
                                                        };
                                                        v5 = _G.TODOBLACKFLASH_CHARCONN;
                                                        v5:Disconnect();
                                                        return; 
                                                    end);
                                                end;
                                                return;
                                            end; 
                                        end;
                                        W2[51] = false;
                                        W2[43] = FA[W2[43]];
                                        W2[55] = 19577228141468;
                                        W2[43] = W2[43](FA, W2[50], W2[51], W2[52]);
                                        W2[51] = r3;
                                        W2[52] = r2;
                                        W2[53] = W2[52](W2[54], W2[55]);
                                        W2[43] = "AddToggle";
                                        W2[50] = W2[51][W2[53]];
                                        W2[52] = function(arg1_89, ...)
                                            local R = {
                                                212,
                                                210
                                            };
                                            if arg1_89 then
                                                v5 = game;
                                                v3 = v5:GetService("RunService");
                                                v3:BindToRenderStep("Auto-YutaFlash", 0, function(...)
                                                    local R = {
                                                        212,
                                                        210
                                                    };
                                                    x = workspace.Characters;
                                                    U = x[3];
                                                    v1 = x[2];
                                                    x = "pairs";
                                                    for U, j in pairs(x:GetChildren()) do
                                                        q = U;
                                                        v6 = r3;
                                                        v2 = j ~= game.Players.LocalPlayer.Character;
                                                        if v2 then
                                                            v6 = r3;
                                                            v2 = j:FindFirstChild("Info");
                                                            v4 = v2 and v6:FindFirstChild("InSkill");
                                                            v5 = Env[v3];
                                                        end;
                                                        if v2 then
                                                            v5 = game.ReplicatedStorage.Knit.Knit.Services.ResoluteSlashService.RE.Activated;
                                                            v2 = game.Players.LocalPlayer.Character.Moveset;
                                                            v5:FireServer(v2:FindFirstChild("Resolute Slash"), j);
                                                        end; 
                                                    end;
                                                    return; 
                                                end);
                                            else
                                                v5 = game;
                                                v3 = v5:GetService("RunService");
                                                v3:UnbindFromRenderStep("Auto-YutaFlash");
                                            end;
                                            return; 
                                        end;
                                        W2[43] = FA[W2[43]];
                                        W2[51] = false;
                                        W2[43] = W2[43](FA, W2[50], W2[51], W2[52]);
                                        W2[43] = r29;
                                        W2[50] = W2[43]();
                                        if W2[50] then
                                            W2[55] = 11942377149881;
                                            W2[54] = "\x83\x82\xee\r\x19\xa1\xab\xb5Q\x99\x10\xa2\xfe\x15\x1b\xb2\xd30D\x8e\x92\xc9\xa0\xcbqV\x0fB#\xd8Y\x03\t";
                                            W2[51] = r3;
                                            W2[52] = r2;
                                            W2[53] = W2[52](W2[54], W2[55]);
                                            W2[52] = function(arg1_90, ...)
                                                local R = {
                                                    W2[49],
                                                    U,
                                                    210,
                                                    312
                                                };
                                                if arg1_90 then
                                                    U = game.ReplicatedStorage.Knit.Knit.Services.ResoluteSlashService.RE.Effects.OnClientEvent;
                                                    w[W2[49]].AutoYutaBlackFlash = U:Connect(function(...)
                                                        local R = {
                                                            U,
                                                            210,
                                                            312,
                                                            W2[49]
                                                        };
                                                        U = {
                                                            select(-1, ...)
                                                        };
                                                        v4 = w[W2[49]];
                                                        if U[1] == "BlackFlashWindup" and U[2] == game.Players.LocalPlayer.Character then
                                                            task.wait(.7);
                                                            x = {};
                                                            v4 = r2;
                                                            j = v4[3];
                                                            v4 = v4[1];
                                                            for j, v7 in v4, ipairs(v4:GetPlayers()) do
                                                                v2 = j;
                                                                Y = w[U];
                                                                t = v7 ~= game.Players.LocalPlayer;
                                                                if t then
                                                                    Y = w[U];
                                                                    r = v7.Character and not Y:GetAttribute("Dead");
                                                                    v5 = ipairs;
                                                                end;
                                                                if t then
                                                                    table.insert({}, v7);
                                                                end; 
                                                            end;
                                                            if #x > 0 then
                                                                r79.currentTarget = x[math.random(1, #x)];
                                                                game.Workspace.FallenPartsDestroyHeight = 100;
                                                                if r79.currentTarget and r79.currentTarget.Character then
                                                                    game.Players.LocalPlayer.Character.HumanoidRootPart.CFrame = CFrame.new(r79.currentTarget.Character.HumanoidRootPart.Position + r79.currentTarget.Character.Humanoid.MoveDirection * .8 * r79.currentTarget.Character.Humanoid.WalkSpeed - r79.currentTarget.Character.HumanoidRootPart.CFrame.LookVector * 5, r79.currentTarget.Character.HumanoidRootPart.Position);
                                                                    task.wait(.4);
                                                                    game.Workspace.FallenPartsDestroyHeight = -150;
                                                                end;
                                                            end;
                                                        end;
                                                        return; 
                                                    end);
                                                else
                                                    v5 = w[W2[49]].AutoYutaBlackFlash;
                                                    if v5 then
                                                        v5 = w[W2[49]].AutoYutaBlackFlash;
                                                        v5:Disconnect();
                                                    end;
                                                    v5 = game;
                                                    v3 = v5:GetService("RunService");
                                                    v3:UnbindFromRenderStep("Inf-Range");
                                                    w[W2[49]].currentTarget = nil;
                                                    return;
                                                end; 
                                            end;
                                            W2[50] = W2[51][W2[53]];
                                            W2[43] = "AddToggle";
                                            W2[43] = FA[W2[43]];
                                            W2[51] = false;
                                            W2[43] = W2[43](FA, W2[50], W2[51], W2[52]);
                                        end;
                                        W2[60] = "1\xc1%\x7fqW|";
                                        W2[55] = "game";
                                        W2[54] = Env[W2[55]];
                                        W2[61] = 14149872294333;
                                        W2[57] = r3;
                                        W2[58] = r2;
                                        W2[59] = W2[58](W2[60], W2[61]);
                                        W2[60] = 34249779609164;
                                        W2[55] = "GetService";
                                        W2[56] = W2[57][W2[59]];
                                        W2[55] = W2[54][W2[55]];
                                        W2[59] = "\xfe$\x0e\xe1\x9a\x8f\x19+\xb1\xff\x86";
                                        W2[55] = W2[55](W2[54], W2[56]);
                                        W2[56] = r3;
                                        W2[57] = r2;
                                        W2[58] = W2[57](W2[59], W2[60]);
                                        W2[54] = W2[56][W2[58]];
                                        W2[53] = W2[55][W2[54]];
                                        W2[59] = 8680643579850;
                                        W2[55] = r3;
                                        W2[56] = r2;
                                        W2[58] = "\xf4\xc6\xe53\xc4\\$\x9b\x05#%\x00\x8b";
                                        W2[57] = W2[56](W2[58], W2[59]);
                                        W2[58] = 32981398076414;
                                        W2[54] = W2[55][W2[57]];
                                        W2[52] = W2[53][W2[54]];
                                        W2[54] = r3;
                                        W2[57] = "\xc2\x0e\xc9\x97s\xe1b\xd3\xae_\x81";
                                        W2[55] = r2;
                                        W2[56] = W2[55](W2[57], W2[58]);
                                        W2[57] = 1066752410096;
                                        W2[53] = W2[54][W2[56]];
                                        W2[51] = W2[52][W2[53]];
                                        W2[53] = r3;
                                        W2[56] = "\xfdQ\x19b\xa4\xb2\xe8";
                                        W2[54] = r2;
                                        W2[55] = W2[54](W2[56], W2[57]);
                                        W2[52] = W2[53][W2[55]];
                                        W2[50] = W2[51][W2[52]];
                                        W2[55] = "\x02\xa14$p\xc7";
                                        W2[52] = r3;
                                        W2[56] = 16059645631798;
                                        W2[53] = r2;
                                        W2[54] = W2[53](W2[55], W2[56]);
                                        W2[51] = W2[52][W2[54]];
                                        W2[43] = W2[50][W2[51]];
                                        W2[50] = "FindFirstChild";
                                        W2[55] = "\xe5~\xf2\xee\x87";
                                        W2[50] = W2[43][W2[50]];
                                        W2[52] = r3;
                                        W2[56] = 15458764856350;
                                        W2[53] = r2;
                                        W2[54] = W2[53](W2[55], W2[56]);
                                        W2[51] = W2[52][W2[54]];
                                        W2[50] = W2[50](W2[43], W2[51]);
                                        if W2[50] then
                                            W2[51] = r3;
                                            W2[54] = "jq\xb9V\xba\xa0_\xcc!\x8e/!\x95\xf5KP\x91";
                                            W2[52] = r2;
                                            W2[55] = 11144612664389;
                                            W2[53] = W2[52](W2[54], W2[55]);
                                            W2[50] = W2[51][W2[53]];
                                            W2[52] = function(arg1_91, ...)
                                                local R = {
                                                    212,
                                                    210,
                                                    158
                                                };
                                                r132 = 0;
                                                if arg1_91 then
                                                    v5 = game;
                                                    v3 = v5:GetService("RunService");
                                                    v3:BindToRenderStep("Auto-Time", 0, function(...)
                                                        local R = {
                                                            212,
                                                            210,
                                                            258,
                                                            158
                                                        };
                                                        v1 = game;
                                                        v5 = v1:GetService("Players").LocalPlayer.PlayerGui;
                                                        v1 = v5:FindFirstChild("UI", true);
                                                        if v1 then
                                                            q = v1:FindFirstChild("Bar");
                                                            if q then
                                                                q = v5:FindFirstChild(r3[q], U).Bar;
                                                                U = q:FindFirstChild("Line");
                                                            end;
                                                            v5 = v1:GetService(r3[r2("Y\xc4nP\x1e\x00\x96", v7)])[r3[r2("S[\xe6#;\x1f\x9fjs\xcc)", v2)]].PlayerGui;
                                                            v3 = q;
                                                        end;
                                                        if v1 then
                                                            x = r33 < 0.5;
                                                            U = v1.Bar.Line.Position.X.Scale;
                                                            if x then
                                                                v3 = U >= 0.5;
                                                            end;
                                                            if x then
                                                                x = v5:FindFirstChild(r3[q], U).Bar;
                                                                r33(x:FindFirstChild("Hitbox"));
                                                            end;
                                                            r33 = U;
                                                        end;
                                                        return; 
                                                    end);
                                                else
                                                    v5 = game;
                                                    v3 = v5:GetService("RunService");
                                                    v3:UnbindFromRenderStep("Auto-Time");
                                                end;
                                                return; 
                                            end;
                                            W2[43] = "AddToggle";
                                            W2[43] = FA[W2[43]];
                                            W2[51] = false;
                                            W2[43] = W2[43](FA, W2[50], W2[51], W2[52]);
                                        end;
                                        W2[55] = 16672161799763;
                                        W2[51] = r3;
                                        W2[54] = "J\\\x10\x16:\xfe\xbfD\x97\x11t\x14\xc5\xac\x8e\xcb\x800\x0f";
                                        W2[52] = r2;
                                        W2[53] = W2[52](W2[54], W2[55]);
                                        W2[52] = function(arg1_92, ...)
                                            local R = {
                                                W2[49],
                                                U,
                                                210
                                            };
                                            if arg1_92 then
                                                U = game.ReplicatedStorage.Knit.Knit.Services.GarudaReboundService.RE.Effects.OnClientEvent;
                                                w[W2[49]].AutoGarudaRebound = U:Connect(function(...)
                                                    local R = {
                                                        U,
                                                        210
                                                    };
                                                    v5 = {
                                                        select(-1, ...)
                                                    };
                                                    x = v5[1] == "Recall";
                                                    if x and v5[2] == game.Players.LocalPlayer.Character then
                                                        if v5[5] == .1 then
                                                            return;
                                                        end;
                                                        d = game;
                                                        Y = d:GetService("Stats").Network.ServerStatsItem["Data Ping"];
                                                        task.wait(math.max(v5[5] - math.clamp(.1 + math.floor(Y:GetValue()) / 1000 * .6, .12, .35), 0));
                                                        v5 = game.ReplicatedStorage.Knit.Knit.Services.GarudaReboundService.RE.Activated;
                                                        x = game.Players.LocalPlayer.Character.Moveset;
                                                        v5:FireServer(x:FindFirstChild("Garuda Rebound"));
                                                    end;
                                                    return; 
                                                end);
                                            else
                                                v5 = w[W2[49]].AutoGarudaRebound;
                                                v5:Disconnect();
                                            end;
                                            return; 
                                        end;
                                        W2[43] = "AddToggle";
                                        W2[50] = W2[51][W2[53]];
                                        W2[54] = "\xbe\x1eu\xba]\xc8\x94\xb85LU\xd6\x08\x00\xc0\xb8";
                                        W2[57] = 23694643522329;
                                        W2[55] = 4812388174016;
                                        W2[43] = FA[W2[43]];
                                        W2[51] = false;
                                        W2[43] = W2[43](FA, W2[50], W2[51], W2[52]);
                                        W2[51] = r3;
                                        W2[52] = r2;
                                        W2[53] = W2[52](W2[54], W2[55]);
                                        W2[50] = W2[51][W2[53]];
                                        W2[43] = "AddToggle";
                                        W2[51] = false;
                                        W2[43] = FA[W2[43]];
                                        W2[52] = function(arg1_93, ...)
                                            local R = {
                                                212,
                                                210
                                            };
                                            if arg1_93 then
                                                v5 = game;
                                                v3 = v5:GetService("RunService");
                                                v3:BindToRenderStep("Auto-Air", 0, function(...)
                                                    local R = {
                                                        212,
                                                        210
                                                    };
                                                    x = game.Players.LocalPlayer.Character.Info;
                                                    U = x[3];
                                                    x = x[1];
                                                    for U, j in x, pairs(x:GetChildren()) do
                                                        q = U;
                                                        v5 = string.find;
                                                        v2 = j.Name;
                                                        if v5(v2, "Air") then
                                                            v6 = game;
                                                            v5 = v6:GetService("ReplicatedStorage").Knit.Knit.Services.LocustService.RE.RightActivated;
                                                            v5:FireServer();
                                                            v6 = game;
                                                            v5 = v6:GetService("ReplicatedStorage").Knit.Knit.Services.JudgeReachService.RE.Activated;
                                                            v2 = game.Players.LocalPlayer.Character.Moveset;
                                                            v5:FireServer(v2:FindFirstChild("Judgement's Reach"));
                                                        end; 
                                                    end;
                                                    return; 
                                                end);
                                            else
                                                v5 = game;
                                                v3 = v5:GetService("RunService");
                                                v3:UnbindFromRenderStep("Auto-Air");
                                            end;
                                            return; 
                                        end;
                                        W2[43] = W2[43](FA, W2[50], W2[51], W2[52]);
                                        W2[43] = nil;
                                        W2[51] = 9;
                                        W2[50] = 10;
                                        W2[56] = "Gy<\x18Z\xb9\xb8\x08v>";
                                        w[W2[50]] = W2[43];
                                        W2[43] = 0;
                                        w[W2[51]] = W2[43];
                                        W2[53] = r3;
                                        W2[54] = r2;
                                        W2[55] = W2[54](W2[56], W2[57]);
                                        W2[52] = W2[53][W2[55]];
                                        W2[43] = "AddToggle";
                                        W2[54] = function(arg1_94, ...)
                                            local R = {
                                                212,
                                                210,
                                                W2[51],
                                                W2[50]
                                            };
                                            if arg1_94 then
                                                v3 = game;
                                                v5 = v3:GetService("RunService").RenderStepped;
                                                w[W2[50]] = v5:Connect(function(...)
                                                    local R = {
                                                        212,
                                                        210,
                                                        W2[51]
                                                    };
                                                    v2 = r2;
                                                    x = game.Players;
                                                    v1 = x[2];
                                                    x = x[1];
                                                    for U, j in ipairs(x:GetPlayers()) do
                                                        q = U;
                                                        r = game.Players;
                                                        v6 = r3;
                                                        v2 = j ~= r.LocalPlayer;
                                                        if v2 then
                                                            v6 = r3;
                                                            v4 = j.Character and v6:FindFirstChild("HumanoidRootPart");
                                                            v5 = ipairs;
                                                        end;
                                                        if v2 then
                                                            a = r3;
                                                            r = j.Character.Humanoid.Animator;
                                                            t = {
                                                                r:GetPlayingAnimationTracks()
                                                            };
                                                            v7 = r[3];
                                                            for v7, t in r[1], ipairs(C(t)) do
                                                                v8 = r3;
                                                                r = v7;
                                                                a = t.Animation;
                                                                if a then
                                                                    v8 = t.Animation.AnimationId == "rbxassetid://132725601768618";
                                                                    if v8 then
                                                                        a = (j.Character.HumanoidRootPart.Position - game.Players.LocalPlayer.Character.HumanoidRootPart.Position).Magnitude <= 46 and t.TimePosition >= .4;
                                                                        v5 = ipairs;
                                                                    end;
                                                                    v5 = ipairs;
                                                                    v6 = v8;
                                                                end;
                                                                if a then
                                                                    v5 = not t:GetAttribute("Triggered");
                                                                    if v5 then
                                                                        t:SetAttribute("Triggered", true);
                                                                        a = game;
                                                                        v5 = a:GetService("RunService").RenderStepped;
                                                                        r133 = v5:Connect(function(...)
                                                                            local R = {
                                                                                212,
                                                                                210,
                                                                                250,
                                                                                W2[51]
                                                                            };
                                                                            v1 = game.Players.LocalPlayer.PlayerGui;
                                                                            U = v1:WaitForChild("Adaptation");
                                                                            v3 = U:WaitForChild("Type").ImageColor3;
                                                                            if v3 == Color3.fromRGB(0, 255, 0) then
                                                                                v5 = w[W2[51]];
                                                                                v5:Disconnect();
                                                                                v5 = game;
                                                                                v3 = v5:GetService("ReplicatedStorage");
                                                                                v5 = v3:WaitForChild("Knit");
                                                                                v3 = v5:WaitForChild("Knit");
                                                                                v5 = v3:WaitForChild("Services");
                                                                                v3 = v5:WaitForChild("MahoragaService");
                                                                                v5 = v3:WaitForChild("RE");
                                                                                v3 = v5:WaitForChild("RightActivated");
                                                                                v3:FireServer();
                                                                            end;
                                                                            v1 = .35;
                                                                            if os.clock() - w[W2[50]] >= v1 then
                                                                                w[W2[50]] = os.clock();
                                                                                v5 = game;
                                                                                v1 = v5:GetService("ReplicatedStorage");
                                                                                v5 = v1:WaitForChild("Knit");
                                                                                v1 = v5:WaitForChild("Knit");
                                                                                v5 = v1:WaitForChild("Services");
                                                                                v1 = v5:WaitForChild("MahoragaService");
                                                                                v5 = v1:WaitForChild("RE");
                                                                                v1 = v5:WaitForChild("Ultimate");
                                                                                v1:FireServer();
                                                                            end;
                                                                            return; 
                                                                        end);
                                                                    end;
                                                                else
                                                                    if t:GetAttribute("Triggered") then
                                                                        t:SetAttribute("Triggered", nil);
                                                                    end;
                                                                end; 
                                                            end;
                                                        end; 
                                                    end;
                                                    return; 
                                                end);
                                            else
                                                if w[W2[50]] then
                                                    v5 = w[W2[50]];
                                                    v5:Disconnect();
                                                    w[W2[50]] = nil;
                                                end;
                                                return;
                                            end; 
                                        end;
                                        W2[53] = false;
                                        W2[56] = "\xc5\xfd\x84dp\x9fE.i?\xc8";
                                        W2[43] = FA[W2[43]];
                                        W2[57] = 2536463795357;
                                        W2[43] = W2[43](FA, W2[52], W2[53], W2[54]);
                                        W2[53] = r3;
                                        W2[54] = r2;
                                        W2[55] = W2[54](W2[56], W2[57]);
                                        W2[54] = function(arg1_95, ...)
                                            local R = {
                                                W2[49],
                                                U,
                                                210
                                            };
                                            if arg1_95 then
                                                U = game.ReplicatedStorage.Knit.Knit.Services.AmbushService.RE.Effects.OnClientEvent;
                                                w[W2[49]].AutoAmbush1 = U:Connect(function(...)
                                                    local R = {
                                                        U,
                                                        210
                                                    };
                                                    v5 = {
                                                        select(-1, ...)
                                                    };
                                                    x = v5[1] == "Stab";
                                                    if x and v5[2] == game.Players.LocalPlayer.Character then
                                                        v2 = game;
                                                        v5 = v2:GetService("ReplicatedStorage").Knit.Knit.Services.AmbushService.RE.Activated;
                                                        v4 = game;
                                                        x = v4:GetService("Players").LocalPlayer.Character.Moveset;
                                                        v5:FireServer(x:FindFirstChild("Ambush"));
                                                    end;
                                                    return; 
                                                end);
                                            else
                                                v5 = w[W2[49]].AutoAmbush1;
                                                v5:Disconnect();
                                            end;
                                            return; 
                                        end;
                                        W2[52] = W2[53][W2[55]];
                                        W2[53] = false;
                                        W2[57] = 8529869508484;
                                        W2[43] = "AddToggle";
                                        W2[56] = "$~e>\x82.\xaa\xa0\xcc ";
                                        W2[43] = FA[W2[43]];
                                        W2[43] = W2[43](FA, W2[52], W2[53], W2[54]);
                                        W2[43] = "AddToggle";
                                        W2[53] = r3;
                                        W2[54] = r2;
                                        W2[55] = W2[54](W2[56], W2[57]);
                                        W2[52] = W2[53][W2[55]];
                                        W2[43] = FA[W2[43]];
                                        W2[54] = function(arg1_96, ...)
                                            local R = {
                                                W2[49],
                                                U,
                                                210
                                            };
                                            if arg1_96 then
                                                U = game.ReplicatedStorage.Knit.Knit.Services.NanamiService.RE.Effects.OnClientEvent;
                                                w[W2[49]].AutoRatio1 = U:Connect(function(...)
                                                    local R = {
                                                        U,
                                                        210
                                                    };
                                                    v5 = {
                                                        select(-1, ...)
                                                    };
                                                    if v5[1] == "SpawnRatio" and v5[2] == game.Players.LocalPlayer then
                                                        g = game;
                                                        v8 = g:GetService("Stats").Network.ServerStatsItem["Data Ping"];
                                                        task.wait(v5[6] * math.clamp(.56 - (math.floor(v8:GetValue()) - 100) / 1000 * .9, 0.25, .85));
                                                        v2 = game;
                                                        v5 = v2:GetService("ReplicatedStorage").Knit.Knit.Services.NanamiService.RE.RightActivated;
                                                        v5:FireServer();
                                                    end;
                                                    return; 
                                                end);
                                            else
                                                v5 = w[W2[49]].AutoRatio1;
                                                v5:Disconnect();
                                            end;
                                            return; 
                                        end;
                                        W2[57] = 19787229864958;
                                        W2[53] = false;
                                        W2[56] = "\"\x95O\xb9\xa7\xadN\xde\xb0\t\x83`\xcd\x03s";
                                        W2[43] = W2[43](FA, W2[52], W2[53], W2[54]);
                                        W2[53] = r3;
                                        W2[54] = r2;
                                        W2[55] = W2[54](W2[56], W2[57]);
                                        W2[57] = 16493497572864;
                                        W2[52] = W2[53][W2[55]];
                                        W2[56] = "\x1c\x82\r\\\x83\x95n\xc6\xb6\xd2]";
                                        W2[43] = "AddToggle";
                                        W2[43] = FA[W2[43]];
                                        W2[53] = false;
                                        W2[54] = function(arg1_97, ...)
                                            local R = {
                                                W2[49],
                                                U,
                                                210,
                                                313
                                            };
                                            if arg1_97 then
                                                U = game.ReplicatedStorage.Knit.Knit.Services.BleedoutService.RE.Effects.OnClientEvent;
                                                w[W2[49]].AutoNaoyaTech = U:Connect(function(...)
                                                    local R = {
                                                        U,
                                                        210,
                                                        313
                                                    };
                                                    U = {
                                                        select(-1, ...)
                                                    };
                                                    x = U[1] == "Hit";
                                                    if x and U[2] == game.Players.LocalPlayer then
                                                        task.wait(.1);
                                                        x = tick();
                                                        v5 = tick() - x >= .3;
                                                        task.wait();
                                                        r2.CFrame = CFrame.new(r2.CFrame.Position + r2.CFrame.RightVector * .22, r2.CFrame.Position + r2.CFrame.LookVector);
                                                        if tick() - x >= .3 then
                                                            return;
                                                        end;
                                                    end; 
                                                end);
                                            else
                                                v5 = w[W2[49]].AutoNaoyaTech;
                                                v5:Disconnect();
                                            end;
                                            return; 
                                        end;
                                        W2[43] = W2[43](FA, W2[52], W2[53], W2[54]);
                                        W2[53] = r3;
                                        W2[54] = r2;
                                        W2[43] = "AddToggle";
                                        W2[55] = W2[54](W2[56], W2[57]);
                                        W2[56] = "3\xdd\x9b\xee\xe0'\xb9|\x10\x92\x93bh\xbf\x92g\x1b";
                                        W2[57] = 33649757764917;
                                        W2[54] = function(arg1_98, ...)
                                            local R = {
                                                212,
                                                210
                                            };
                                            if arg1_98 then
                                                _G.SHUTUP = {};
                                                q = game;
                                                local function U(arg1_99, ...)
                                                    local R = {
                                                        212,
                                                        210
                                                    };
                                                    r134 = arg1_99;
                                                    v3 = r134;
                                                    v5 = v3:WaitForChild("Humanoid").AnimationPlayed;
                                                    v5:Connect(function(arg1_100, ...)
                                                        local R = {
                                                            212,
                                                            210,
                                                            152
                                                        };
                                                        v1 = arg1_100;
                                                        if v1.Animation and v1.Animation.AnimationId == "rbxassetid://79860101129549" then
                                                            v5 = r134;
                                                            U = v5:WaitForChild("HumanoidRootPart");
                                                            v5 = r134;
                                                            r135 = v5:WaitForChild("Humanoid");
                                                            r136 = getgenv().ShutUp;
                                                            getgenv().ShutUp = true;
                                                            r135.AutoRotate = false;
                                                            U.CFrame = CFrame.new(U.Position, U.Position - U.CFrame.LookVector);
                                                            task.delay(0.5, function(...)
                                                                local R = {
                                                                    212,
                                                                    210,
                                                                    238,
                                                                    237
                                                                };
                                                                getgenv().ShutUp = r134;
                                                                r135.AutoRotate = true;
                                                                return; 
                                                            end);
                                                        end;
                                                        return; 
                                                    end);
                                                    return; 
                                                end;
                                                U(q:GetService("Players").LocalPlayer.Character);
                                                j = game;
                                                x = j:GetService("Players").LocalPlayer.CharacterAdded;
                                                _G.SHUTUP_CHARCONN = x:Connect(U);
                                            else
                                                q = r2;
                                                j = q("\xcc\xc9\x7fP\x1d\xb6", 30307014063904);
                                                if _G[r3[j]] then
                                                    j = _G;
                                                    q = j.SHUTUP;
                                                    x = j[3];
                                                    q = j[1];
                                                    for x, v4 in q, ipairs(q) do
                                                        r137 = v4;
                                                        j = x;
                                                        if typeof(w[v5]) == "Instance" or typeof(w[v5]) == "RBXScriptConnection" then
                                                            pcall(function(...)
                                                                v5 = w[v5];
                                                                v5:Disconnect();
                                                                return; 
                                                            end);
                                                        end; 
                                                    end;
                                                end;
                                                if _G.SHUTUP_CHARCONN then
                                                    pcall(function(...)
                                                        local R = {
                                                            212,
                                                            210
                                                        };
                                                        v5 = _G.SHUTUP_CHARCONN;
                                                        v5:Disconnect();
                                                        return; 
                                                    end);
                                                end;
                                                return;
                                            end; 
                                        end;
                                        W2[43] = FA[W2[43]];
                                        W2[52] = W2[53][W2[55]];
                                        W2[53] = false;
                                        W2[43] = W2[43](FA, W2[52], W2[53], W2[54]);
                                        W2[53] = r3;
                                        W2[54] = r2;
                                        W2[55] = W2[54](W2[56], W2[57]);
                                        W2[52] = W2[53][W2[55]];
                                        W2[53] = false;
                                        W2[43] = "AddToggle";
                                        W2[57] = 5335836625332;
                                        W2[43] = FA[W2[43]];
                                        W2[54] = function(arg1_101, ...)
                                            local R = {
                                                212,
                                                210
                                            };
                                            if arg1_101 then
                                                _G.PERFECTSWAP = {};
                                                q = game;
                                                local function U(arg1_102, ...)
                                                    local R = {
                                                        212,
                                                        210
                                                    };
                                                    v1 = arg1_102;
                                                    x = v1:WaitForChild("Humanoid").AnimationPlayed;
                                                    table.insert(_G.PERFECTSWAP, x:Connect(function(arg1_103, ...)
                                                        local R = {
                                                            212,
                                                            210
                                                        };
                                                        v1 = arg1_103;
                                                        U = v1.Animation;
                                                        if U then
                                                            v5 = v5;
                                                            v5 = v5;
                                                            v3 = v1.Animation.AnimationId == "rbxassetid://91074768993486" or (v1.Animation.AnimationId == "rbxassetid://131358603583212" or v1.Animation.AnimationId == "rbxassetid://116040503139675");
                                                        end;
                                                        if U then
                                                            v5 = game.ReplicatedStorage.Knit.Knit.Services.TodoService.RE.Effects.OnClientEvent;
                                                            r138 = v5:Connect(function(...)
                                                                local R = {
                                                                    212,
                                                                    210,
                                                                    125
                                                                };
                                                                v5 = v5;
                                                                v5 = {
                                                                    select(-3, ...)
                                                                };
                                                                if v5[1] == "Swap" or (125[1] == "Swap2" or 125[1] == "Fakeout") then
                                                                    v5 = game.ReplicatedStorage.Knit.Knit.Services.TodoService.RE.Activated;
                                                                    v5:FireServer(false);
                                                                    v5 = r138;
                                                                    v5:Disconnect();
                                                                end;
                                                                return; 
                                                            end);
                                                            table.insert(_G.PERFECTSWAP, r138);
                                                        end;
                                                        return; 
                                                    end));
                                                    return; 
                                                end;
                                                U(q:GetService("Players").LocalPlayer.Character);
                                                j = game;
                                                x = j:GetService("Players").LocalPlayer.CharacterAdded;
                                                _G.PERFECTSWAP_CHARCONN = x:Connect(U);
                                            else
                                                q = r2;
                                                j = q("_:fs\x90\x84<\xb0\x02a\xe3", 27045716783410);
                                                if _G[r3[j]] then
                                                    j = _G;
                                                    q = j.PERFECTSWAP;
                                                    x = j[3];
                                                    q = j[1];
                                                    for x, v4 in q, ipairs(q) do
                                                        j = x;
                                                        r139 = v4;
                                                        pcall(function(...)
                                                            v5 = r139;
                                                            v5:Disconnect();
                                                            return; 
                                                        end); 
                                                    end;
                                                end;
                                                if _G.PERFECTSWAP_CHARCONN then
                                                    pcall(function(...)
                                                        local R = {
                                                            212,
                                                            210
                                                        };
                                                        v5 = _G.PERFECTSWAP_CHARCONN;
                                                        v5:Disconnect();
                                                        return; 
                                                    end);
                                                end;
                                                return;
                                            end; 
                                        end;
                                        W2[43] = W2[43](FA, W2[52], W2[53], W2[54]);
                                        W2[53] = r3;
                                        W2[54] = r2;
                                        W2[56] = "\rf\xdc\x16,\xb46\xd1G\xcb\xa8\xd7z\xb7\x84R";
                                        W2[55] = W2[54](W2[56], W2[57]);
                                        W2[52] = W2[53][W2[55]];
                                        W2[53] = false;
                                        W2[54] = function(arg1_104, ...)
                                            local R = {
                                                212,
                                                210
                                            };
                                            if arg1_104 then
                                                _G.EARTHQUAKE = {};
                                                local function U(arg1_105, ...)
                                                    local R = {
                                                        212,
                                                        210
                                                    };
                                                    v1 = arg1_105;
                                                    v5 = v1:WaitForChild("Humanoid").AnimationPlayed;
                                                    table.insert(_G.EARTHQUAKE, v5:Connect(function(arg1_106, ...)
                                                        local R = {
                                                            212,
                                                            210
                                                        };
                                                        v1 = arg1_106;
                                                        if v1.Animation and v1.Animation.AnimationId == "rbxassetid://85024950165903" then
                                                            U = v1.IsPlaying;
                                                            v3 = v1.TimePosition < .7;
                                                            while not U do
                                                                if v3 then
                                                                    task.wait();
                                                                end;
                                                                v3 = "IsPlaying";
                                                                if arg1_106[v3] then
                                                                    v5 = game;
                                                                    v3 = v5:GetService("ReplicatedStorage");
                                                                    v5 = v3:WaitForChild("Knit");
                                                                    v3 = v5:WaitForChild("Knit");
                                                                    v5 = v3:WaitForChild("Services");
                                                                    v3 = v5:WaitForChild("EarthquakeService");
                                                                    v5 = v3:WaitForChild("RE");
                                                                    v3 = v5:WaitForChild("Deactivated");
                                                                    v4 = game;
                                                                    v3:FireServer(v4:GetService("Players").LocalPlayer.Character.Moveset.Earthquake, false);
                                                                end;
                                                                break; 
                                                            end;
                                                            v3 = v1.TimePosition < .7;
                                                        end;
                                                        return; 
                                                    end));
                                                    return; 
                                                end;
                                                q = game;
                                                U(q:GetService("Players").LocalPlayer.Character);
                                                j = game;
                                                x = j:GetService("Players").LocalPlayer.CharacterAdded;
                                                _G.EARTHQUAKE_CHARCONN = x:Connect(U);
                                            else
                                                j = r2("\xe9G\x8d\xc2y\nQ\xa9U\xe4", 371835551917);
                                                if _G[r3[j]] then
                                                    j = _G;
                                                    q = j.EARTHQUAKE;
                                                    x = j[3];
                                                    U = j[2];
                                                    for x, v4 in ipairs(v3) do
                                                        j = x;
                                                        r140 = v4;
                                                        if typeof(r140) == "RBXScriptConnection" then
                                                            pcall(function(...)
                                                                v5 = r140;
                                                                v5:Disconnect();
                                                                return; 
                                                            end);
                                                        end; 
                                                    end;
                                                end;
                                                if _G.EARTHQUAKE_CHARCONN then
                                                    pcall(function(...)
                                                        local R = {
                                                            212,
                                                            210
                                                        };
                                                        v5 = _G.EARTHQUAKE_CHARCONN;
                                                        v5:Disconnect();
                                                        return; 
                                                    end);
                                                end;
                                                return;
                                            end; 
                                        end;
                                        W2[43] = "AddToggle";
                                        W2[57] = 33601431518494;
                                        W2[43] = FA[W2[43]];
                                        W2[43] = W2[43](FA, W2[52], W2[53], W2[54]);
                                        W2[43] = "AddToggle";
                                        W2[53] = r3;
                                        W2[54] = r2;
                                        W2[56] = "\xaf\xe5\xbd\xfdu\xb3'\xb0~\xc0\xc5.&^c\x12`~\x14M\x9c]h\xf0\xd8\xfa";
                                        W2[55] = W2[54](W2[56], W2[57]);
                                        W2[52] = W2[53][W2[55]];
                                        W2[43] = FA[W2[43]];
                                        W2[54] = function(arg1_107, ...)
                                            local R = {
                                                212,
                                                210,
                                                W2[11]
                                            };
                                            if arg1_107 then
                                                _G.REVERSALRED = {};
                                                local function U(arg1_108, ...)
                                                    local R = {
                                                        212,
                                                        210,
                                                        W2[11]
                                                    };
                                                    v5 = arg1_108.Humanoid.AnimationPlayed;
                                                    table.insert(_G.REVERSALRED, v5:Connect(function(arg1_109, ...)
                                                        local R = {
                                                            212,
                                                            210,
                                                            W2[11]
                                                        };
                                                        v1 = arg1_109;
                                                        U = v1.Animation;
                                                        if U and v1.Animation.AnimationId == "rbxassetid://137654778575373" then
                                                            v5 = w[W2[11]];
                                                            U = v5();
                                                            v3 = U;
                                                            if U then
                                                                q = w[W2[11]];
                                                                j = U.HumanoidRootPart.Position.Y > game.Players.LocalPlayer.Character.HumanoidRootPart.Position.Y + 5;
                                                                if j then
                                                                    v3 = j;
                                                                    v5 = q;
                                                                    if v3 then
                                                                        v2 = game;
                                                                        v5 = v2:GetService("ReplicatedStorage").Knit.Knit.Services.GojoService.RE.RightActivated;
                                                                        v5:FireServer(v5());
                                                                    end;
                                                                    return;
                                                                end;
                                                            end;
                                                        end; 
                                                    end));
                                                    return; 
                                                end;
                                                U(game.Players.LocalPlayer.Character);
                                                x = game.Players.LocalPlayer.CharacterAdded;
                                                _G.REVERSALRED_CHARCONN = x:Connect(U);
                                            else
                                                q = r2;
                                                j = q("l1\xd5\xb2\\\x14sM\x1fo\xb5", 4512087459893);
                                                if _G[r3[j]] then
                                                    j = _G;
                                                    q = j.REVERSALRED;
                                                    q = j[1];
                                                    U = j[2];
                                                    for x, v4 in ipairs(q) do
                                                        j = x;
                                                        r141 = v4;
                                                        if typeof(w[v5]) == "Instance" or typeof(w[v5]) == "RBXScriptConnection" then
                                                            pcall(function(...)
                                                                v5 = w[v5];
                                                                v5:Disconnect();
                                                                return; 
                                                            end);
                                                        end; 
                                                    end;
                                                end;
                                                if _G.REVERSALRED_CHARCONN then
                                                    pcall(function(...)
                                                        local R = {
                                                            212,
                                                            210
                                                        };
                                                        v5 = _G.REVERSALRED_CHARCONN;
                                                        v5:Disconnect();
                                                        return; 
                                                    end);
                                                end;
                                                return;
                                            end; 
                                        end;
                                        W2[53] = false;
                                        W2[43] = W2[43](FA, W2[52], W2[53], W2[54]);
                                        W2[57] = 21561491236664;
                                        W2[53] = r3;
                                        W2[56] = "&\r\xe0\x1e\xb4\xc0\xc7\xc6a*\xc2\xc2\xe7\x85\xc2\xd7";
                                        W2[43] = "AddToggle";
                                        W2[54] = r2;
                                        W2[55] = W2[54](W2[56], W2[57]);
                                        W2[54] = function(arg1_110, ...)
                                            local R = {
                                                212,
                                                210
                                            };
                                            if arg1_110 then
                                                _G.NUEVARIANT = {};
                                                q = game;
                                                local function U(arg1_111, ...)
                                                    local R = {
                                                        212,
                                                        210
                                                    };
                                                    v1 = arg1_111;
                                                    v5 = v1:WaitForChild("Humanoid").AnimationPlayed;
                                                    table.insert(_G.NUEVARIANT, v5:Connect(function(arg1_112, ...)
                                                        local R = {
                                                            212,
                                                            210
                                                        };
                                                        v1 = arg1_112;
                                                        v3 = v1.Animation and v1.Animation.AnimationId == "rbxassetid://111077341852080";
                                                        if v3 then
                                                            v5 = game;
                                                            v3 = v5:GetService("ReplicatedStorage");
                                                            v5 = v3:WaitForChild("Knit");
                                                            v3 = v5:WaitForChild("Knit");
                                                            v5 = v3:WaitForChild("Services");
                                                            v3 = v5:WaitForChild("MegumiService");
                                                            v5 = v3:WaitForChild("RE");
                                                            v3 = v5:WaitForChild("RightActivated");
                                                            v3:FireServer();
                                                        end;
                                                        return; 
                                                    end));
                                                    return; 
                                                end;
                                                U(q:GetService("Players").LocalPlayer.Character);
                                                j = game;
                                                x = j:GetService("Players").LocalPlayer.CharacterAdded;
                                                _G.NUEVARIANT_CHARCONN = x:Connect(U);
                                            else
                                                q = r2;
                                                j = q("\xd51\xc5\xab\xdei\xa1q\xe2\xcb", 34033624530408);
                                                if _G[r3[j]] then
                                                    j = _G;
                                                    q = j.NUEVARIANT;
                                                    q = j[1];
                                                    x = j[3];
                                                    for x, v4 in q, ipairs(q) do
                                                        j = x;
                                                        r142 = v4;
                                                        if typeof(w[v5]) == "Instance" or typeof(w[v5]) == "RBXScriptConnection" then
                                                            pcall(function(...)
                                                                v5 = w[v5];
                                                                v5:Disconnect();
                                                                return; 
                                                            end);
                                                        end; 
                                                    end;
                                                end;
                                                if _G.NUEVARIANT_CHARCONN then
                                                    pcall(function(...)
                                                        local R = {
                                                            212,
                                                            210
                                                        };
                                                        v5 = _G.NUEVARIANT_CHARCONN;
                                                        v5:Disconnect();
                                                        return; 
                                                    end);
                                                end;
                                                return;
                                            end; 
                                        end;
                                        W2[57] = 20383009744147;
                                        W2[52] = W2[53][W2[55]];
                                        W2[56] = "K\x95\xcb\xec\xe4\x9b\x19\xbe\xf30\xb1Rg\xcc\xc70N";
                                        W2[43] = FA[W2[43]];
                                        W2[53] = false;
                                        W2[43] = W2[43](FA, W2[52], W2[53], W2[54]);
                                        W2[53] = r3;
                                        W2[54] = r2;
                                        W2[55] = W2[54](W2[56], W2[57]);
                                        W2[54] = function(arg1_113, ...)
                                            local R = {
                                                212,
                                                210
                                            };
                                            if arg1_113 then
                                                _G.FROGVARIANT = {};
                                                local function U(arg1_114, ...)
                                                    local R = {
                                                        212,
                                                        210
                                                    };
                                                    v1 = arg1_114;
                                                    v5 = v1:WaitForChild("Humanoid").AnimationPlayed;
                                                    table.insert(_G.FROGVARIANT, v5:Connect(function(arg1_115, ...)
                                                        local R = {
                                                            212,
                                                            210
                                                        };
                                                        v1 = arg1_115;
                                                        v3 = v1.Animation and v1.Animation.AnimationId == "rbxassetid://116432619539029";
                                                        if v3 then
                                                            v5 = game;
                                                            v3 = v5:GetService("ReplicatedStorage");
                                                            v5 = v3:WaitForChild("Knit");
                                                            v3 = v5:WaitForChild("Knit");
                                                            v5 = v3:WaitForChild("Services");
                                                            v3 = v5:WaitForChild("NueService");
                                                            v5 = v3:WaitForChild("RE");
                                                            v3 = v5:WaitForChild("Activated");
                                                            v4 = game;
                                                            v3:FireServer(v4:GetService("Players").LocalPlayer.Character.Moveset.Nue);
                                                        end;
                                                        return; 
                                                    end));
                                                    return; 
                                                end;
                                                q = game;
                                                U(q:GetService("Players").LocalPlayer.Character);
                                                j = game;
                                                x = j:GetService("Players").LocalPlayer.CharacterAdded;
                                                _G.FROGVARIANT_CHARCONN = x:Connect(U);
                                            else
                                                q = r2;
                                                j = q("[\xea`\xcc\x92\xe3\xb5\xae\xe6\xe4\xd8", 3375996470820);
                                                if _G[r3[j]] then
                                                    j = _G;
                                                    q = j.FROGVARIANT;
                                                    U = j[2];
                                                    q = j[1];
                                                    for x, v4 in ipairs(q) do
                                                        r143 = v4;
                                                        j = x;
                                                        if typeof(w[v5]) == "Instance" or typeof(w[v5]) == "RBXScriptConnection" then
                                                            pcall(function(...)
                                                                v5 = w[v5];
                                                                v5:Disconnect();
                                                                return; 
                                                            end);
                                                        end; 
                                                    end;
                                                end;
                                                if _G.FROGVARIANT_CHARCONN then
                                                    pcall(function(...)
                                                        local R = {
                                                            212,
                                                            210
                                                        };
                                                        v5 = _G.FROGVARIANT_CHARCONN;
                                                        v5:Disconnect();
                                                        return; 
                                                    end);
                                                end;
                                                return;
                                            end; 
                                        end;
                                        W2[57] = 31612706961792;
                                        W2[52] = W2[53][W2[55]];
                                        W2[53] = false;
                                        W2[56] = "SKwQ&x\xbcO\xef\xfc:U\xc6\xb8XQ";
                                        W2[43] = "AddToggle";
                                        W2[43] = FA[W2[43]];
                                        W2[43] = W2[43](FA, W2[52], W2[53], W2[54]);
                                        W2[53] = r3;
                                        W2[54] = r2;
                                        W2[55] = W2[54](W2[56], W2[57]);
                                        W2[57] = 28043588350722;
                                        W2[54] = function(arg1_116, ...)
                                            local R = {
                                                212,
                                                210
                                            };
                                            if arg1_116 then
                                                _G.WORLDSLASH = {};
                                                local function U(arg1_117, ...)
                                                    local R = {
                                                        212,
                                                        210
                                                    };
                                                    v1 = arg1_117;
                                                    v5 = v1:WaitForChild("Humanoid").AnimationPlayed;
                                                    table.insert(_G.WORLDSLASH, v5:Connect(function(arg1_118, ...)
                                                        local R = {
                                                            212,
                                                            210
                                                        };
                                                        v1 = arg1_118;
                                                        if v1.Animation and v1.Animation.AnimationId == "rbxassetid://131506102901134" then
                                                            v3 = game.Players.LocalPlayer.PlayerGui.Main.Ultimate.Special.Fill.Size.X.Scale;
                                                            if v3 == 1 then
                                                                v5 = game;
                                                                v3 = v5:GetService("ReplicatedStorage");
                                                                v5 = v3:WaitForChild("Knit");
                                                                v3 = v5:WaitForChild("Knit");
                                                                v5 = v3:WaitForChild("Services");
                                                                v3 = v5:WaitForChild("RushService");
                                                                v5 = v3:WaitForChild("RE");
                                                                v3 = v5:WaitForChild("Activated");
                                                                v4 = game;
                                                                v3:FireServer(v4:GetService("Players").LocalPlayer.Character.Moveset.Rush);
                                                                v5 = game;
                                                                v3 = v5:GetService("ReplicatedStorage");
                                                                v5 = v3:WaitForChild("Knit");
                                                                v3 = v5:WaitForChild("Knit");
                                                                v5 = v3:WaitForChild("Services");
                                                                v3 = v5:WaitForChild("FlameArrowService");
                                                                v5 = v3:WaitForChild("RE");
                                                                v3 = v5:WaitForChild("Activated");
                                                                v4 = game;
                                                                v3:FireServer(v4:GetService("Players").LocalPlayer.Character.Moveset.Open);
                                                                task.wait(.8);
                                                                v5 = game;
                                                                v3 = v5:GetService("ReplicatedStorage");
                                                                v5 = v3:WaitForChild("Knit");
                                                                v3 = v5:WaitForChild("Knit");
                                                                v5 = v3:WaitForChild("Services");
                                                                v3 = v5:WaitForChild("ItadoriService");
                                                                v5 = v3:WaitForChild("RE");
                                                                v3 = v5:WaitForChild("RightActivated");
                                                                v3:FireServer();
                                                            end;
                                                        end;
                                                        return; 
                                                    end));
                                                    return; 
                                                end;
                                                q = game;
                                                U(q:GetService("Players").LocalPlayer.Character);
                                                j = game;
                                                x = j:GetService("Players").LocalPlayer.CharacterAdded;
                                                _G.WORLDSLASH_CHARCONN = x:Connect(U);
                                            else
                                                j = r2("\xc9\x15k\x8e\xa6\x8boj\x8c\xbc", 7156942523652);
                                                if _G[r3[j]] then
                                                    j = _G;
                                                    q = j.WORLDSLASH;
                                                    x = j[3];
                                                    U = j[2];
                                                    for x, v4 in ipairs(v3) do
                                                        j = x;
                                                        r144 = v4;
                                                        if typeof(w[v5]) == "Instance" or typeof(w[v5]) == "RBXScriptConnection" then
                                                            pcall(function(...)
                                                                v5 = w[v5];
                                                                v5:Disconnect();
                                                                return; 
                                                            end);
                                                        end; 
                                                    end;
                                                end;
                                                if _G.WORLDSLASH_CHARCONN then
                                                    pcall(function(...)
                                                        local R = {
                                                            212,
                                                            210
                                                        };
                                                        v5 = _G.WORLDSLASH_CHARCONN;
                                                        v5:Disconnect();
                                                        return; 
                                                    end);
                                                end;
                                                return;
                                            end; 
                                        end;
                                        W2[43] = "AddToggle";
                                        W2[43] = FA[W2[43]];
                                        W2[52] = W2[53][W2[55]];
                                        W2[53] = false;
                                        W2[43] = W2[43](FA, W2[52], W2[53], W2[54]);
                                        W2[53] = r3;
                                        W2[56] = "\x81\x91\x18\x98\x085p?\x83\xc7k\x9a\xc6\x97";
                                        W2[43] = "AddSection";
                                        W2[43] = BA[W2[43]];
                                        W2[54] = r2;
                                        W2[55] = W2[54](W2[56], W2[57]);
                                        W2[52] = W2[53][W2[55]];
                                        W2[56] = "\x99\xb3q\x81\xeeQ\xff\x1f\x9d\xcd\xb2\xf3D\x0f\xb4+s";
                                        W2[43] = W2[43](BA, W2[52]);
                                        W2[53] = r3;
                                        W2[54] = r2;
                                        W2[43] = "AddToggle";
                                        W2[57] = 10361450287832;
                                        W2[43] = BA[W2[43]];
                                        W2[55] = W2[54](W2[56], W2[57]);
                                        W2[52] = W2[53][W2[55]];
                                        W2[54] = function(arg1_119, ...)
                                            local R = {
                                                U,
                                                210
                                            };
                                            if arg1_119 then
                                                x = game;
                                                U = x:GetService("RunService").RenderStepped;
                                                _G.SilentANIM = U:Connect(function(...)
                                                    local R = {
                                                        U,
                                                        210
                                                    };
                                                    v5 = pairs;
                                                    x = game.Players.LocalPlayer.Character.Humanoid;
                                                    v1 = x[2];
                                                    U = x[3];
                                                    x = "pairs";
                                                    for U, j in v5(x:GetPlayingAnimationTracks()) do
                                                        v5 = v5;
                                                        v5 = v5;
                                                        v5 = v5;
                                                        v5 = v5;
                                                        v5 = v5;
                                                        v5 = v5;
                                                        v5 = v5;
                                                        v5 = v5;
                                                        v5 = v5;
                                                        v5 = v5;
                                                        v5 = v5;
                                                        v5 = v5;
                                                        v5 = v5;
                                                        v5 = v5;
                                                        v5 = v5;
                                                        q = U;
                                                        if j.Name == "FallAnim" or (j.Name == "Animation1" or (j.Name == "Animation2" or (j.Name == "WalkAnim" or (j.Name == "JumpAnim" or (j.Name == "RunAnim" or (j.Name == "idle" or (j.Name == "walk" or (j.Name == "walkL" or (j.Name == "walkR" or (j.Name == "sprint" or (j.Name == "jump" or (j.Name == "fall" or (j.Name == "climb" or (j.Name == "sit" or (j.Name == "Land" or j.Name == "Roll"))))))))))))))) then
                                                            j.Priority = Enum.AnimationPriority.Action2;
                                                        else
                                                            if j.Name == "ToolNoneAnim" and j.Animation.AnimationId ~= "rbxassetid://123456789" then
                                                                j.Priority = Enum.AnimationPriority.Action3;
                                                            end;
                                                        end; 
                                                    end;
                                                    return; 
                                                end);
                                            else
                                                if _G.SilentANIM then
                                                    v5 = _G.SilentANIM;
                                                    v5:Disconnect();
                                                    _G.SilentANIM = nil;
                                                end;
                                                return;
                                            end; 
                                        end;
                                        W2[53] = false;
                                        W2[43] = W2[43](BA, W2[52], W2[53], W2[54]);
                                        W2[43] = r29;
                                        W2[52] = W2[43]();
                                        if W2[52] then
                                            W2[60] = 31717784172977;
                                            W2[43] = nil;
                                            W2[61] = 18520988950960;
                                            W2[52] = 269;
                                            W2[53] = 270;
                                            w[W2[52]] = W2[43];
                                            W2[43] = false;
                                            W2[59] = " Ua0\xa84]\x8e\x89{\x99\x03\x87P\x9c>";
                                            w[W2[53]] = W2[43];
                                            W2[43] = false;
                                            W2[62] = 33655461772600;
                                            W2[54] = 271;
                                            w[W2[54]] = W2[43];
                                            W2[56] = r3;
                                            W2[57] = r2;
                                            W2[58] = W2[57](W2[59], W2[60]);
                                            W2[59] = "V\x8b\xae\x89\xe7\x07;_\x81\xe28\x0e,\xa2\xa5\xb0";
                                            W2[60] = 2104530306003;
                                            W2[43] = "AddToggle";
                                            W2[57] = function(arg1_120, ...)
                                                w[W2[53]] = arg1_120;
                                                return; 
                                            end;
                                            W2[55] = W2[56][W2[58]];
                                            W2[56] = false;
                                            W2[43] = BA[W2[43]];
                                            W2[43] = W2[43](BA, W2[55], W2[56], W2[57]);
                                            W2[56] = r3;
                                            W2[57] = r2;
                                            W2[58] = W2[57](W2[59], W2[60]);
                                            W2[55] = W2[56][W2[58]];
                                            W2[56] = false;
                                            W2[57] = function(arg1_121, ...)
                                                w[W2[54]] = arg1_121;
                                                return; 
                                            end;
                                            W2[43] = "AddToggle";
                                            W2[43] = BA[W2[43]];
                                            W2[43] = W2[43](BA, W2[55], W2[56], W2[57]);
                                            W2[55] = "game";
                                            W2[60] = "\xd9\xf4\x19\x8f\xdc\x87\xa3e\xee\x16y@;\xd2\xa6\xea\x1d";
                                            W2[43] = Env[W2[55]];
                                            W2[57] = r3;
                                            W2[58] = r2;
                                            W2[55] = "GetService";
                                            W2[55] = W2[43][W2[55]];
                                            W2[59] = W2[58](W2[60], W2[61]);
                                            W2[56] = W2[57][W2[59]];
                                            W2[55] = W2[55](W2[43], W2[56]);
                                            W2[43] = 272;
                                            w[W2[43]] = W2[55];
                                            W2[56] = "game";
                                            W2[55] = Env[W2[56]];
                                            W2[58] = r3;
                                            W2[56] = "GetService";
                                            W2[59] = r2;
                                            W2[61] = "/\xc7\x81\xb5>\xca";
                                            W2[56] = W2[55][W2[56]];
                                            W2[60] = W2[59](W2[61], W2[62]);
                                            W2[57] = W2[58][W2[60]];
                                            W2[56] = W2[56](W2[55], W2[57]);
                                            W2[57] = "pcall";
                                            W2[59] = function(...)
                                                local R = {
                                                    212,
                                                    210
                                                };
                                                return require(game.Players.LocalPlayer.PlayerScripts.Controllers.Character.MovementController); 
                                            end;
                                            W2[55] = 273;
                                            w[W2[55]] = W2[56];
                                            W2[56] = Env[W2[57]];
                                            W2[60] = {
                                                W2[56](W2[59])
                                            };
                                            W2[58] = W2[60][2];
                                            W2[57] = W2[60][1];
                                            W2[59] = v5;
                                            W2[56] = W2[57];
                                            if W2[57] then
                                                W2[56] = W2[58];
                                            end;
                                            v5 = W2[59];
                                            if W2[56] then
                                                W2[59] = 354;
                                                W2[60] = 355;
                                                W2[56] = 0;
                                                w[W2[59]] = W2[56];
                                                W2[56] = 0;
                                                w[W2[60]] = W2[56];
                                                W2[61] = w[W2[52]];
                                                W2[56] = not W2[61];
                                                if W2[56] then
                                                    W2[65] = "1\x13\xd9A\x0e\x85a\x7f/\x81O";
                                                    W2[62] = r3;
                                                    W2[66] = 17774635376724;
                                                    W2[63] = r2;
                                                    W2[64] = W2[63](W2[65], W2[66]);
                                                    W2[61] = W2[62][W2[64]];
                                                    W2[56] = W2[58][W2[61]];
                                                    w[W2[52]] = W2[56];
                                                end;
                                                W2[65] = "j\x86\x13\xfap:\xa8\x7f8\x16%";
                                                W2[62] = r3;
                                                W2[66] = 18018744459462;
                                                W2[63] = r2;
                                                W2[64] = W2[63](W2[65], W2[66]);
                                                W2[61] = W2[62][W2[64]];
                                                W2[62] = function(arg1_122, ...)
                                                    local R = {
                                                        212,
                                                        210,
                                                        W2[52],
                                                        W2[11],
                                                        W2[53],
                                                        W2[60],
                                                        W2[43],
                                                        W2[55],
                                                        W2[54],
                                                        W2[59]
                                                    };
                                                    tick();
                                                    v3 = game.Players.LocalPlayer;
                                                    j = game.Players.LocalPlayer.Character;
                                                    if not j then
                                                        return;
                                                    end;
                                                    r145 = j:FindFirstChild("HumanoidRootPart");
                                                    r146 = j:FindFirstChildOfClass("Humanoid");
                                                    if not r145 or not r146 then
                                                        return;
                                                    end;
                                                    v7 = r146.MoveDirection;
                                                    r = workspace.CurrentCamera.CFrame;
                                                    v7:Dot(Vector3.new(r.RightVector.X, 0, r.RightVector.Z).Unit);
                                                    if v7:Dot(Vector3.new(r.LookVector.X, 0, r.LookVector.Z).Unit) > 0.5 then
                                                        if v3:GetAttribute("Moveset") == "Naoya" then
                                                            v8 = "Front";
                                                        end;
                                                        return w[W2[52]](arg1_122, ...);
                                                    end; 
                                                end;
                                                W2[59] = nil;
                                                W2[58][W2[61]] = W2[62];
                                                W2[60] = nil;
                                            end;
                                            W2[65] = 8143206502095;
                                            W2[61] = r3;
                                            W2[54] = nil;
                                            W2[53] = nil;
                                            W2[58] = nil;
                                            W2[62] = r2;
                                            W2[64] = "[\xa5pc\xe2X\x9d:\xe2\x02\xa9OjPI9\xe5\x9e{";
                                            W2[63] = W2[62](W2[64], W2[65]);
                                            W2[60] = W2[61][W2[63]];
                                            W2[52] = nil;
                                            W2[62] = function(arg1_123, ...)
                                                local R = {
                                                    212,
                                                    210
                                                };
                                                if arg1_123 then
                                                    q = {
                                                        pcall(function(...)
                                                            local R = {
                                                                212,
                                                                210
                                                            };
                                                            return require(game.Players.LocalPlayer.PlayerScripts.Controllers.Character.MovementController); 
                                                        end)
                                                    };
                                                    r147 = q[2];
                                                    if not q[1] or not r147 then
                                                        Notify({
                                                            ["Title"] = "UnSupported Feature.",
                                                            ["Description"] = "Your Executor Does Not Support This Feature.",
                                                            ["Duration"] = 5
                                                        });
                                                        return;
                                                    end;
                                                    v5 = game;
                                                    v3 = v5:GetService("RunService");
                                                    v3:BindToRenderStep("Parkour-Inf", 0, function(...)
                                                        local R = {
                                                            212,
                                                            210,
                                                            361
                                                        };
                                                        debug.setupvalue(r147.Parkour, 2, 0);
                                                        return; 
                                                    end);
                                                else
                                                    v5 = game;
                                                    v3 = v5:GetService("RunService");
                                                    v3:UnbindFromRenderStep("Parkour-Inf");
                                                end;
                                                return; 
                                            end;
                                            W2[61] = false;
                                            W2[59] = "AddToggle";
                                            W2[59] = BA[W2[59]];
                                            W2[57] = nil;
                                            W2[43] = nil;
                                            W2[55] = nil;
                                            W2[59] = W2[59](BA, W2[60], W2[61], W2[62]);
                                        end;
                                        W2[57] = "\xa1\xe6\xe9\x07p\xe1W\xf1\xf5\x13\xc1\x86";
                                        W2[53] = r3;
                                        W2[58] = 31062566828160;
                                        W2[54] = r2;
                                        W2[55] = W2[54](W2[57], W2[58]);
                                        W2[52] = W2[53][W2[55]];
                                        W2[53] = false;
                                        W2[43] = "AddToggle";
                                        W2[54] = function(arg1_124, ...)
                                            local R = {
                                                212,
                                                210
                                            };
                                            v3 = true;
                                            if arg1_124 == v3 then
                                                v5 = game;
                                                v3 = v5:GetService("RunService");
                                                v3:BindToRenderStep("Anti-Ragdoll", 0, function(...)
                                                    local R = {
                                                        212,
                                                        210
                                                    };
                                                    v3 = game.Players.LocalPlayer.Character;
                                                    v5 = v3:GetAttribute("Ragdoll") == 1;
                                                    if v5 then
                                                        v5 = game.Players.LocalPlayer.Character;
                                                        v5:SetAttribute("Ragdoll", 0);
                                                    end;
                                                    return; 
                                                end);
                                            else
                                                v5 = game;
                                                v3 = v5:GetService("RunService");
                                                v3:UnbindFromRenderStep("Anti-Ragdoll");
                                            end;
                                            return; 
                                        end;
                                        W2[59] = "\xc6\xd62\xa4$i\xa7\xb0=.\x9e\xce";
                                        W2[43] = BA[W2[43]];
                                        W2[43] = W2[43](BA, W2[52], W2[53], W2[54]);
                                        W2[53] = function(...)
                                            local R = {
                                                312,
                                                212,
                                                210
                                            };
                                            v1 = r79.LocalPlayer.Character;
                                            if not v1 then
                                                return false;
                                            end;
                                            U = v1:FindFirstChild("HumanoidRootPart");
                                            if not U then
                                                return false;
                                            end;
                                            j = workspace.Characters;
                                            x = j[2];
                                            q = j[3];
                                            j = "ipairs";
                                            for q, v2 in ipairs(j:GetChildren()) do
                                                v5 = r79;
                                                v4 = q;
                                                if v5:GetPlayerFromCharacter(v2) ~= r79.LocalPlayer then
                                                    r = v2:FindFirstChild("HumanoidRootPart");
                                                    o = r2("\x8e`U\x11", 7999118511756);
                                                    t = v2:FindFirstChild(r3[o]);
                                                    if r then
                                                        if t then
                                                            a = v5:FindFirstChild("Counter");
                                                        end;
                                                        v2:FindFirstChild(r3[o]);
                                                        v6 = t;
                                                    end;
                                                    if r then
                                                        o = (r.Position - U.Position).Magnitude;
                                                        if o <= 12 and o:Dot((r.Position - U.Position).Unit) > .8 then
                                                            return true;
                                                        else
                                                        end;
                                                    end;
                                                end; 
                                            end;
                                            return false; 
                                        end;
                                        W2[52] = 2;
                                        W2[43] = false;
                                        W2[61] = "\xc2\xff\xb5\x01\x13\x08[\xc9\x1a\xef\xb5\xfe\x0f\xf3";
                                        W2[65] = 26667732070530;
                                        W2[60] = 14852852013828;
                                        w[W2[52]] = W2[43];
                                        W2[66] = "Enum";
                                        W2[43] = 3;
                                        w[W2[43]] = W2[53];
                                        W2[53] = "AddToggle";
                                        W2[55] = r3;
                                        W2[57] = r2;
                                        W2[58] = W2[57](W2[59], W2[60]);
                                        W2[53] = BA[W2[53]];
                                        W2[57] = function(arg1_125, ...)
                                            local R = {
                                                163,
                                                212,
                                                210,
                                                W2[43],
                                                W2[52],
                                                314
                                            };
                                            if arg1_125 then
                                                v5 = r38;
                                                v5:BindToRenderStep("Anti-Counter", 0, function(...)
                                                    local R = {
                                                        W2[43],
                                                        W2[52],
                                                        314,
                                                        212,
                                                        210
                                                    };
                                                    v1 = r38();
                                                    v3 = v1;
                                                    if v1 then
                                                        v3 = not r3;
                                                    end;
                                                    if v3 then
                                                        r3 = true;
                                                        v3 = r2.BlockService.RE.Activated;
                                                        v3:FireServer();
                                                    else
                                                        U = r38;
                                                        v5 = U;
                                                        if not v5() and r3 then
                                                            r3 = false;
                                                            U = r2.BlockService.RE.Deactivated;
                                                            U:FireServer();
                                                        end;
                                                        return;
                                                    end; 
                                                end);
                                            else
                                                v5 = r38;
                                                v3 = v5:UnbindFromRenderStep("Anti-Counter");
                                                if w[W2[52]] then
                                                    w[W2[52]] = false;
                                                    v3 = r81.BlockService.RE.Deactivated;
                                                    v3:FireServer();
                                                end;
                                                return;
                                            end; 
                                        end;
                                        W2[54] = W2[55][W2[58]];
                                        W2[55] = false;
                                        W2[53] = W2[53](BA, W2[54], W2[55], W2[57]);
                                        W2[53] = nil;
                                        W2[62] = 17322003144578;
                                        W2[54] = 4;
                                        w[W2[54]] = W2[53];
                                        W2[55] = 5;
                                        W2[53] = false;
                                        w[W2[55]] = W2[53];
                                        W2[58] = r3;
                                        W2[59] = r2;
                                        W2[60] = W2[59](W2[61], W2[62]);
                                        W2[62] = 6310171233146;
                                        W2[64] = "l\xa8\x11\x9a\x9a\xc6\xdf\x9dH9";
                                        W2[61] = "\xdf\xeav\x7fx\x1f|\x90\x84\x11";
                                        W2[57] = W2[58][W2[60]];
                                        W2[59] = function(arg1_126, ...)
                                            local R = {
                                                212,
                                                210,
                                                W2[55],
                                                W2[54]
                                            };
                                            if arg1_126 then
                                                v3 = game;
                                                v5 = v3:GetService("RunService").RenderStepped;
                                                w[W2[54]] = v5:Connect(function(...)
                                                    local R = {
                                                        212,
                                                        210,
                                                        W2[55]
                                                    };
                                                    v5 = workspace.Effects;
                                                    if v5:FindFirstChild("BlackHole") then
                                                        if (workspace.Effects.BlackHole.CFrame.Position - game.Players.LocalPlayer.Character.HumanoidRootPart.CFrame.Position).Magnitude <= 100 then
                                                            if not w[W2[55]] then
                                                                w[W2[55]] = true;
                                                                antistuff();
                                                            end;
                                                        else
                                                            if w[W2[55]] then
                                                                w[W2[55]] = false;
                                                                unantistuff();
                                                            end;
                                                        end;
                                                    else
                                                        if w[W2[55]] then
                                                            w[W2[55]] = false;
                                                            unantistuff();
                                                        end;
                                                        return;
                                                    end; 
                                                end);
                                            else
                                                if w[W2[54]] then
                                                    v5 = w[W2[54]];
                                                    v5:Disconnect();
                                                    w[W2[54]] = nil;
                                                    w[W2[55]] = false;
                                                end;
                                                return;
                                            end; 
                                        end;
                                        W2[58] = false;
                                        W2[53] = "AddToggle";
                                        W2[53] = BA[W2[53]];
                                        W2[53] = W2[53](BA, W2[57], W2[58], W2[59]);
                                        W2[57] = "getgenv";
                                        W2[53] = Env[W2[57]];
                                        W2[57] = W2[53]();
                                        W2[58] = r3;
                                        W2[59] = r2;
                                        W2[60] = W2[59](W2[61], W2[62]);
                                        W2[53] = W2[58][W2[60]];
                                        W2[59] = "game";
                                        W2[58] = true;
                                        W2[57][W2[53]] = W2[58];
                                        W2[58] = 6;
                                        W2[53] = false;
                                        W2[57] = 7;
                                        w[W2[57]] = W2[53];
                                        W2[53] = 0;
                                        w[W2[58]] = W2[53];
                                        W2[53] = Env[W2[59]];
                                        W2[71] = 21163023246974;
                                        W2[61] = r3;
                                        W2[62] = r2;
                                        W2[59] = "GetService";
                                        W2[63] = W2[62](W2[64], W2[65]);
                                        W2[70] = "d\x8eQ\x14\x9e\xf6$v\xa1\xdb\x9a\xda\xcaw";
                                        W2[60] = W2[61][W2[63]];
                                        W2[59] = W2[53][W2[59]];
                                        W2[59] = W2[59](W2[53], W2[60]);
                                        W2[61] = r3;
                                        W2[64] = ",\xbc\xe0\xb5`\xa8r\xb3\x95\x11%";
                                        W2[62] = r2;
                                        W2[65] = 7076903898335;
                                        W2[63] = W2[62](W2[64], W2[65]);
                                        W2[60] = W2[61][W2[63]];
                                        W2[65] = Env[W2[66]];
                                        W2[67] = r3;
                                        W2[68] = r2;
                                        W2[69] = W2[68](W2[70], W2[71]);
                                        W2[70] = 6524089699294;
                                        W2[66] = W2[67][W2[69]];
                                        W2[64] = W2[65][W2[66]];
                                        W2[66] = r3;
                                        W2[67] = r2;
                                        W2[69] = "\xc9\x87\xe9)m\xe1";
                                        W2[68] = W2[67](W2[69], W2[70]);
                                        W2[65] = W2[66][W2[68]];
                                        W2[53] = "BindToRenderStep";
                                        W2[69] = 12331026044526;
                                        W2[63] = W2[64][W2[65]];
                                        W2[65] = r3;
                                        W2[68] = "3\xaa\x08\xbd\x19";
                                        W2[53] = W2[59][W2[53]];
                                        W2[66] = r2;
                                        W2[67] = W2[66](W2[68], W2[69]);
                                        W2[64] = W2[65][W2[67]];
                                        W2[62] = W2[63][W2[64]];
                                        W2[63] = 1;
                                        W2[61] = W2[62] + W2[63];
                                        W2[62] = function(...)
                                            local R = {
                                                212,
                                                210,
                                                313,
                                                W2[57],
                                                W2[58]
                                            };
                                            if not getgenv().AntiGlitch then
                                                return;
                                            end;
                                            v5 = tostring(r80.Focus.Position) == "nan, nan, nan";
                                            if v5 then
                                                game.Players.LocalPlayer.Character.Humanoid.CameraOffset = Vector3.new(0, 0, 0);
                                                x = workspace;
                                                v1 = x[2];
                                                x = x[1];
                                                for U, j in ipairs(x:GetDescendants()) do
                                                    q = U;
                                                    if j:IsA("ProximityPrompt") then
                                                        j.Enabled = false;
                                                    end; 
                                                end;
                                                if not w[W2[57]] then
                                                    w[W2[57]] = true;
                                                    w[W2[58]] = tick() + 0.5;
                                                end;
                                            end;
                                            v5 = v5;
                                            if w[W2[57]] and tick() >= w[W2[58]] then
                                                v4 = workspace;
                                                j = v4[3];
                                                for j, v4 in v4[1], ipairs(v4:GetDescendants()) do
                                                    U = j;
                                                    if v4:IsA("ProximityPrompt") then
                                                        v4.Enabled = true;
                                                    end; 
                                                end;
                                                w[W2[57]] = false;
                                            end;
                                            return; 
                                        end;
                                        W2[53] = W2[53](W2[59], W2[60], W2[61], W2[62]);
                                        W2[63] = "\xe5\xc6\x88=\x83n\x19)I\xb1\xec";
                                        W2[64] = 11140167242819;
                                        W2[53] = "AddToggle";
                                        W2[60] = r3;
                                        W2[61] = r2;
                                        W2[62] = W2[61](W2[63], W2[64]);
                                        W2[59] = W2[60][W2[62]];
                                        W2[62] = "getgenv";
                                        W2[67] = 27150206726498;
                                        W2[61] = Env[W2[62]];
                                        W2[62] = W2[61]();
                                        W2[63] = r3;
                                        W2[64] = r2;
                                        W2[66] = "\xf4\xbc_t\x12\x86\x16\x9c\xbb\x00";
                                        W2[65] = W2[64](W2[66], W2[67]);
                                        W2[61] = W2[63][W2[65]];
                                        W2[63] = "\xddv\xa6\xa1$\x9d\n\xc7\xcf\xa5\x0b";
                                        W2[53] = BA[W2[53]];
                                        W2[60] = W2[62][W2[61]];
                                        W2[61] = function(arg1_127, ...)
                                            local R = {
                                                212,
                                                210
                                            };
                                            getgenv().AntiGlitch = arg1_127;
                                            return; 
                                        end;
                                        W2[53] = W2[53](BA, W2[59], W2[60], W2[61]);
                                        W2[64] = 1221265719864;
                                        W2[60] = r3;
                                        W2[67] = 34979894493088;
                                        W2[61] = r2;
                                        W2[62] = W2[61](W2[63], W2[64]);
                                        W2[61] = function(arg1_128, ...)
                                            local R = {
                                                212,
                                                210
                                            };
                                            if arg1_128 then
                                                U = "tp away";
                                                if _G.antidomainMethod == U then
                                                    x = game;
                                                    U = x:GetService("RunService").RenderStepped;
                                                    _G.AntiDomain = U:Connect(function(...)
                                                        local R = {
                                                            212,
                                                            210
                                                        };
                                                        v2 = r2;
                                                        x = game.Players;
                                                        v1 = x[2];
                                                        x = x[1];
                                                        for U, j in pairs(x:GetPlayers()) do
                                                            q = U;
                                                            v2 = j ~= game.Players.LocalPlayer;
                                                            if v2 then
                                                                r = j.Character;
                                                                if r then
                                                                    r = j.Character.Info;
                                                                    v2 = r:FindFirstChild("DomainData");
                                                                end;
                                                                v5 = pairs;
                                                                v4 = r;
                                                            end;
                                                            if v2 then
                                                                if (j.Character.HumanoidRootPart.Position - game.Players.LocalPlayer.Character.HumanoidRootPart.Position).Magnitude <= 48 then
                                                                    game.Players.LocalPlayer.Character.Humanoid.AutoRotate = false;
                                                                    game.Players.LocalPlayer.Character.HumanoidRootPart.CFrame = CFrame.new(game.Players.LocalPlayer.Character.HumanoidRootPart.Position + game.Players.LocalPlayer.Character.HumanoidRootPart.CFrame.LookVector.Unit * 30);
                                                                    task.wait();
                                                                    game.Players.LocalPlayer.Character.Humanoid.AutoRotate = true;
                                                                end;
                                                            end; 
                                                        end;
                                                        return; 
                                                    end);
                                                else
                                                    U = "Hit And Tp Back";
                                                    if _G.antidomainMethod == U then
                                                        x = game;
                                                        U = x:GetService("RunService").RenderStepped;
                                                        _G.AntiDomain = U:Connect(function(...)
                                                            local R = {
                                                                212,
                                                                210
                                                            };
                                                            v2 = r2;
                                                            x = game.Players;
                                                            U = x[3];
                                                            x = x[1];
                                                            for U, j in x, pairs(x:GetPlayers()) do
                                                                q = U;
                                                                v2 = j ~= game.Players.LocalPlayer;
                                                                if v2 then
                                                                    r = j.Character;
                                                                    if r then
                                                                        r = j.Character.Info;
                                                                        v2 = r:FindFirstChild("DomainData");
                                                                    end;
                                                                    v5 = pairs;
                                                                    v4 = r;
                                                                end;
                                                                if v2 then
                                                                    if (j.Character.HumanoidRootPart.Position - game.Players.LocalPlayer.Character.HumanoidRootPart.Position).Magnitude <= 48 then
                                                                        game.Players.LocalPlayer.Character.Humanoid.AutoRotate = false;
                                                                        game.Players.LocalPlayer.Character.HumanoidRootPart.CFrame = CFrame.new(j.Character.HumanoidRootPart.Position - j.Character.HumanoidRootPart.CFrame.LookVector * 5, j.Character.HumanoidRootPart.Position);
                                                                        v5 = game;
                                                                        v2 = v5:GetService("ReplicatedStorage");
                                                                        v5 = v2:WaitForChild("Knit");
                                                                        v2 = v5:WaitForChild("Knit");
                                                                        v5 = v2:WaitForChild("Services");
                                                                        r = game.Players.LocalPlayer;
                                                                        v2 = v5:WaitForChild(r:GetAttribute("Moveset") .. "Service");
                                                                        v5 = v2:WaitForChild("RE");
                                                                        v2 = v5:WaitForChild("Activated");
                                                                        v2:FireServer(false);
                                                                        task.wait();
                                                                        v5 = game.Players.LocalPlayer.Character;
                                                                        v5:MoveTo(game.Players.LocalPlayer.Character.HumanoidRootPart.Position);
                                                                        game.Players.LocalPlayer.Character.Humanoid.AutoRotate = true;
                                                                    end;
                                                                end; 
                                                            end;
                                                            return; 
                                                        end);
                                                    end;
                                                end;
                                            else
                                                if _G.AntiDomain then
                                                    v5 = _G.AntiDomain;
                                                    v5:Disconnect();
                                                    _G.AntiDomain = nil;
                                                end;
                                                return;
                                            end; 
                                        end;
                                        W2[59] = W2[60][W2[62]];
                                        W2[60] = false;
                                        W2[65] = "\xd8\xceRE\xae\x1d\xef";
                                        W2[53] = "AddToggle";
                                        W2[53] = BA[W2[53]];
                                        W2[64] = 27165312135529;
                                        W2[66] = 8284063764241;
                                        W2[53] = W2[53](BA, W2[59], W2[60], W2[61]);
                                        W2[63] = "\x9f$\x13)9\xe5\xce\x83\xbe\xcd\x02\xbd\xcb\x9e\x7f\x82k\x87";
                                        W2[53] = "AddDropdown";
                                        W2[60] = r3;
                                        W2[61] = r2;
                                        W2[62] = W2[61](W2[63], W2[64]);
                                        W2[59] = W2[60][W2[62]];
                                        W2[62] = r3;
                                        W2[63] = r2;
                                        W2[64] = W2[63](W2[65], W2[66]);
                                        W2[61] = W2[62][W2[64]];
                                        W2[63] = r3;
                                        W2[66] = "j\xd2\x9a\xeeE\xcd@8\xdfv\x14w\x13\xc2\xf7";
                                        W2[64] = r2;
                                        W2[65] = W2[64](W2[66], W2[67]);
                                        W2[62] = W2[63][W2[65]];
                                        W2[64] = r3;
                                        W2[53] = BA[W2[53]];
                                        W2[67] = "\x00\x88\x98\xbc~\x03\x95";
                                        W2[60] = {
                                            W2[61],
                                            W2[62]
                                        };
                                        W2[65] = r2;
                                        W2[61] = function(arg1_129, ...)
                                            local R = {
                                                212,
                                                210
                                            };
                                            _G.antidomainMethod = arg1_129;
                                            return; 
                                        end;
                                        W2[62] = false;
                                        W2[68] = 30213244712693;
                                        W2[66] = W2[65](W2[67], W2[68]);
                                        W2[63] = W2[64][W2[66]];
                                        W2[53] = W2[53](BA, W2[59], W2[60], W2[61], W2[62], W2[63]);
                                        W2[59] = 8;
                                        W2[64] = "t &\xb7\x02\xa4\xb3\xa5\x1b";
                                        W2[53] = nil;
                                        W2[65] = 31762715146694;
                                        w[W2[59]] = W2[53];
                                        W2[69] = 28260191400807;
                                        W2[61] = r3;
                                        W2[68] = 22691241896262;
                                        W2[70] = 21992869816321;
                                        W2[62] = r2;
                                        W2[63] = W2[62](W2[64], W2[65]);
                                        W2[53] = "AddToggle";
                                        W2[60] = W2[61][W2[63]];
                                        W2[65] = 33132014386244;
                                        W2[61] = false;
                                        W2[53] = BA[W2[53]];
                                        W2[64] = "Oi\x8e\xdbb\x06\x80^\x85\xb5r,\x11\xb9\x83\xe1\x8a";
                                        W2[62] = function(arg1_130, ...)
                                            local R = {
                                                212,
                                                210,
                                                W2[59]
                                            };
                                            r148 = false;
                                            r149 = false;
                                            r150 = true;
                                            v5 = "antikillcount";
                                            getgenv()[v5] = 0;
                                            if arg1_130 then
                                                v3 = game;
                                                v5 = v3:GetService("RunService").RenderStepped;
                                                w[W2[59]] = v5:Connect(function(...)
                                                    local R = {
                                                        212,
                                                        210,
                                                        285,
                                                        287,
                                                        286
                                                    };
                                                    q = r3;
                                                    x = "Character";
                                                    v1 = game.Players.LocalPlayer[x];
                                                    if v1 then
                                                        x = game.Players.LocalPlayer.Character;
                                                        v4 = r3;
                                                        j = "Humanoid";
                                                        q = x:FindFirstChild(j);
                                                        if q then
                                                            j = game.Players.LocalPlayer.Character;
                                                            v4 = j:FindFirstChild("HumanoidRootPart");
                                                            if v4 then
                                                                x = game.Players.LocalPlayer.Character.Humanoid.Health <= 10;
                                                            end;
                                                            v5 = j[v4[v7]];
                                                            v1 = v4;
                                                        end;
                                                        v5 = j[v4[v7]];
                                                        v3 = q;
                                                    end;
                                                    if v1 then
                                                        v3 = game.Players.LocalPlayer.Character;
                                                        v5 = v3:GetAttribute("Ragdoll") == 1;
                                                        if v5 then
                                                            v5 = game.Players.LocalPlayer.Character;
                                                            v5:SetAttribute("Ragdoll", 0);
                                                            w[W2[59]] = true;
                                                            r150 = false;
                                                            return;
                                                        end;
                                                        U = v5;
                                                        if w[W2[59]] and not r149 then
                                                            r149 = true;
                                                            task.delay(.38, function(...)
                                                                local R = {
                                                                    W2[59],
                                                                    286,
                                                                    287
                                                                };
                                                                r3 = false;
                                                                r2 = false;
                                                                w[W2[59]] = true;
                                                                return; 
                                                            end);
                                                            return;
                                                        end;
                                                        x = U;
                                                        U = r150 and getgenv().antikillcount < 4;
                                                        v5 = x;
                                                        if U then
                                                            U = game.Players.LocalPlayer.Character.Humanoid;
                                                            U:Move((game.Players.LocalPlayer.Character.HumanoidRootPart.Position - game.Players.LocalPlayer.Character.HumanoidRootPart.Position).Unit, false);
                                                            x = getgenv();
                                                            U = "antikillcount";
                                                            x[U] = x[U] + 1;
                                                        end;
                                                    else
                                                        r = "Character";
                                                        v2 = game.Players.LocalPlayer[r];
                                                        if v2 then
                                                            r = game.Players.LocalPlayer.Character;
                                                            v2 = r:FindFirstChild("Humanoid");
                                                            j = v2 and game.Players.LocalPlayer.Character.Humanoid.Health > 10;
                                                            v5 = j[v4[v7]];
                                                        end;
                                                        v5 = j[v4[v7]];
                                                        if v2 then
                                                            getgenv().antikillcount = 0;
                                                        end;
                                                        return;
                                                    end; 
                                                end);
                                            else
                                                if w[W2[59]] then
                                                    v5 = w[W2[59]];
                                                    v5:Disconnect();
                                                    w[W2[59]] = nil;
                                                end;
                                                return;
                                            end; 
                                        end;
                                        W2[53] = W2[53](BA, W2[60], W2[61], W2[62]);
                                        W2[61] = r3;
                                        W2[62] = r2;
                                        W2[66] = "\xb3\xeb\x85y";
                                        W2[63] = W2[62](W2[64], W2[65]);
                                        W2[60] = W2[61][W2[63]];
                                        W2[63] = r3;
                                        W2[67] = 2589126476981;
                                        W2[64] = r2;
                                        W2[65] = W2[64](W2[66], W2[67]);
                                        W2[53] = "AddDropdown";
                                        W2[62] = W2[63][W2[65]];
                                        W2[64] = r3;
                                        W2[65] = r2;
                                        W2[67] = "\xe4\xcb\xa6\xec\x1a\xdf\"1";
                                        W2[66] = W2[65](W2[67], W2[68]);
                                        W2[63] = W2[64][W2[66]];
                                        W2[68] = "\x15\xd9S \x1e\xcc";
                                        W2[65] = r3;
                                        W2[66] = r2;
                                        W2[67] = W2[66](W2[68], W2[69]);
                                        W2[69] = "\xda\xe9\xc0}]";
                                        W2[64] = W2[65][W2[67]];
                                        W2[66] = r3;
                                        W2[67] = r2;
                                        W2[68] = W2[67](W2[69], W2[70]);
                                        W2[70] = 4254837376957;
                                        W2[65] = W2[66][W2[68]];
                                        W2[61] = {
                                            W2[62],
                                            W2[63],
                                            W2[64],
                                            W2[65]
                                        };
                                        W2[66] = r3;
                                        W2[62] = function(arg1_131, ...)
                                            local R = {
                                                212,
                                                210
                                            };
                                            _G.StunMethod = arg1_131;
                                            return; 
                                        end;
                                        W2[69] = "\x7f\x82O\xa3";
                                        W2[63] = true;
                                        W2[67] = r2;
                                        W2[68] = W2[67](W2[69], W2[70]);
                                        W2[65] = W2[66][W2[68]];
                                        W2[53] = BA[W2[53]];
                                        W2[64] = {
                                            W2[65]
                                        };
                                        W2[65] = 11020862559243;
                                        W2[53] = W2[53](BA, W2[60], W2[61], W2[62], W2[63], W2[64]);
                                        W2[53] = "AddToggle";
                                        W2[61] = r3;
                                        W2[64] = "\xf5\xaal[\x93W:\xa8N";
                                        W2[62] = r2;
                                        W2[63] = W2[62](W2[64], W2[65]);
                                        W2[65] = 9098134474892;
                                        W2[53] = BA[W2[53]];
                                        W2[60] = W2[61][W2[63]];
                                        W2[62] = function(arg1_132, ...)
                                            local R = {
                                                212,
                                                210
                                            };
                                            if arg1_132 then
                                                v5 = game;
                                                v3 = v5:GetService("RunService");
                                                v3:BindToRenderStep("Anti-Stun", 0, function(...)
                                                    local R = {
                                                        212,
                                                        210
                                                    };
                                                    q = _G;
                                                    x = q.StunMethod;
                                                    U = q[3];
                                                    v1 = q[2];
                                                    for U, j in ipairs(v3) do
                                                        q = U;
                                                        v5 = game.Players.LocalPlayer.Character;
                                                        v4 = v5:FindFirstChild("Info");
                                                        v4 = v4:FindFirstChild(j);
                                                        if v4 then
                                                            v4:Destroy();
                                                        end; 
                                                    end;
                                                    return; 
                                                end);
                                            else
                                                v5 = game;
                                                v3 = v5:GetService("RunService");
                                                v3:UnbindFromRenderStep("Anti-Stun");
                                            end;
                                            return; 
                                        end;
                                        W2[61] = false;
                                        W2[53] = W2[53](BA, W2[60], W2[61], W2[62]);
                                        W2[53] = "AddButton";
                                        W2[61] = r3;
                                        W2[62] = r2;
                                        W2[64] = "_\xd4\x1f\x0e\xac|\xd8SQ\xdb8\xca\xa2";
                                        W2[63] = W2[62](W2[64], W2[65]);
                                        W2[53] = ZA[W2[53]];
                                        W2[64] = "W\xaa\xf0\xbf";
                                        W2[60] = W2[61][W2[63]];
                                        W2[61] = function(...)
                                            local R = {
                                                160,
                                                212,
                                                210
                                            };
                                            r36(CFrame.new(43, 183, 141));
                                            return; 
                                        end;
                                        W2[53] = W2[53](ZA, W2[60], W2[61]);
                                        W2[65] = 23256062519885;
                                        W2[61] = r3;
                                        W2[62] = r2;
                                        W2[63] = W2[62](W2[64], W2[65]);
                                        W2[60] = W2[61][W2[63]];
                                        W2[61] = function(...)
                                            local R = {
                                                160,
                                                212,
                                                210
                                            };
                                            r36(CFrame.new(156, -30, -235));
                                            return; 
                                        end;
                                        W2[53] = "AddButton";
                                        W2[53] = ZA[W2[53]];
                                        W2[53] = W2[53](ZA, W2[60], W2[61]);
                                        W2[64] = "{\x17\xc0w\xf5\x0f\xb1\xad\xa3\xa73\xc0\xcc\x9b^\xdf";
                                        W2[53] = "AddButton";
                                        W2[61] = r3;
                                        W2[62] = r2;
                                        W2[65] = 16270091820440;
                                        W2[53] = ZA[W2[53]];
                                        W2[63] = W2[62](W2[64], W2[65]);
                                        W2[60] = W2[61][W2[63]];
                                        W2[61] = function(...)
                                            local R = {
                                                160,
                                                212,
                                                210
                                            };
                                            r36(CFrame.new(175, -10, 121));
                                            return; 
                                        end;
                                        W2[65] = 23057324943856;
                                        W2[53] = W2[53](ZA, W2[60], W2[61]);
                                        W2[53] = "AddButton";
                                        W2[53] = ZA[W2[53]];
                                        W2[61] = r3;
                                        W2[64] = "\xd8y\xb6\xc5pA\xf8-u\xe4\xa0qs<";
                                        W2[62] = r2;
                                        W2[63] = W2[62](W2[64], W2[65]);
                                        W2[60] = W2[61][W2[63]];
                                        W2[64] = "O\xb0\xf6\x82\x19\xa1Z\xac6\xec";
                                        W2[61] = function(...)
                                            local R = {
                                                160,
                                                212,
                                                210
                                            };
                                            r36(CFrame.new(-146, -31, -66));
                                            return; 
                                        end;
                                        W2[53] = W2[53](ZA, W2[60], W2[61]);
                                        W2[61] = r3;
                                        W2[65] = 16264760073621;
                                        W2[62] = r2;
                                        W2[63] = W2[62](W2[64], W2[65]);
                                        W2[60] = W2[61][W2[63]];
                                        W2[61] = function(...)
                                            local R = {
                                                160,
                                                212,
                                                210
                                            };
                                            r36(CFrame.new(-4, 50, 432));
                                            return; 
                                        end;
                                        W2[53] = "AddButton";
                                        W2[53] = ZA[W2[53]];
                                        W2[53] = W2[53](ZA, W2[60], W2[61]);
                                        W2[61] = r3;
                                        W2[62] = r2;
                                        W2[65] = 18471103963545;
                                        W2[53] = "AddButton";
                                        W2[64] = "\xe9\x1f\xdb>\xac\xa1\x80\x1c\xd6\xb3\xac@0p\xd8\x14`}\x9b\xaf9\xcd)\xa7\x08\xc1\x19";
                                        W2[63] = W2[62](W2[64], W2[65]);
                                        W2[60] = W2[61][W2[63]];
                                        W2[64] = ":\xfd\xa0\x8fb\x8a\xf5\xcci\xf4\x13\x11\xe9KT\x0f\xf1";
                                        W2[53] = ZA[W2[53]];
                                        W2[61] = function(...)
                                            local R = {
                                                212,
                                                210,
                                                160
                                            };
                                            v1 = {};
                                            q = game;
                                            j = q:GetService("Players");
                                            q = {
                                                j:GetPlayers()
                                            };
                                            x = j[3];
                                            U = j[2];
                                            for x, v4 in ipairs(C("ipairs")) do
                                                j = x;
                                                if v4 ~= game.Players.LocalPlayer and v4.Character then
                                                    v5 = v4.Character.Info;
                                                    if v5:FindFirstChild("DomainTag") then
                                                        table.insert({}, v4);
                                                    end;
                                                end; 
                                            end;
                                            if #v1 > 0 then
                                                U = v1[math.random(1, #v1)];
                                                q = U.Character;
                                                if q then
                                                    q = U.Character;
                                                    x = q:FindFirstChild("HumanoidRootPart");
                                                end;
                                                if q then
                                                    r36(U.Character.HumanoidRootPart.CFrame);
                                                end;
                                            end;
                                            return; 
                                        end;
                                        W2[65] = 7095562800360;
                                        W2[53] = W2[53](ZA, W2[60], W2[61]);
                                        W2[61] = r3;
                                        W2[62] = r2;
                                        W2[63] = W2[62](W2[64], W2[65]);
                                        W2[60] = W2[61][W2[63]];
                                        W2[61] = function(...)
                                            local R = {
                                                160,
                                                212,
                                                210
                                            };
                                            r36(workspace.Characters.Dummy.HumanoidRootPart.CFrame);
                                            return; 
                                        end;
                                        W2[53] = "AddButton";
                                        W2[53] = ZA[W2[53]];
                                        W2[53] = W2[53](ZA, W2[60], W2[61]);
                                        W2[53] = r29;
                                        W2[60] = W2[53]();
                                        if W2[60] then
                                            W2[65] = 289681129606;
                                            W2[61] = r3;
                                            W2[62] = r2;
                                            W2[64] = "E\xf8hF\xab\x13\x14`\x06\xb9m;n";
                                            W2[53] = "AddButton";
                                            W2[63] = W2[62](W2[64], W2[65]);
                                            W2[60] = W2[61][W2[63]];
                                            W2[61] = function(...)
                                                local R = {
                                                    212,
                                                    210,
                                                    316,
                                                    163,
                                                    159
                                                };
                                                v5 = workspace.Characters;
                                                r151 = v5:FindFirstChild("Dummy");
                                                v5 = r82;
                                                v5:Bind("DummyHeartbeat", r38.Heartbeat, function(...)
                                                    local R = {
                                                        212,
                                                        210,
                                                        219,
                                                        316,
                                                        159
                                                    };
                                                    v5 = workspace.Characters;
                                                    v5 = v5:FindFirstChild("Dummy") ~= r82;
                                                    if v5 then
                                                        v5 = r38;
                                                        v5:Disconnect("DummyHeartbeat");
                                                        v5 = r38;
                                                        v5:Disconnect("DummyStepped");
                                                        return;
                                                    end;
                                                    U = r82;
                                                    if U then
                                                        U = r82;
                                                        v3 = U:FindFirstChild("HumanoidRootPart");
                                                    end;
                                                    if U then
                                                        r34(r82.HumanoidRootPart.CFrame);
                                                    end;
                                                    return; 
                                                end);
                                                v5 = r82;
                                                v5:Bind("DummyStepped", r38.Stepped, function(...)
                                                    local R = {
                                                        212,
                                                        210,
                                                        219,
                                                        316
                                                    };
                                                    v5 = workspace.Characters;
                                                    v5 = v5:FindFirstChild("Dummy") ~= r82;
                                                    if v5 then
                                                        v5 = r38;
                                                        v5:Disconnect("DummyHeartbeat");
                                                        v5 = r38;
                                                        v5:Disconnect("DummyStepped");
                                                        return;
                                                    end;
                                                    U = r82;
                                                    if U then
                                                        U = r82;
                                                        v3 = U:FindFirstChild("HumanoidRootPart");
                                                    end;
                                                    if U then
                                                        v5 = game.Players.LocalPlayer.Character;
                                                        v5:SetAttribute("Sprint", true);
                                                        sethiddenproperty(game.Players.LocalPlayer.Character.Humanoid, "MoveDirectionInternal", Vector3.new(0 / 0, 0 / 0, 0 / 0));
                                                    end;
                                                    return; 
                                                end);
                                                return; 
                                            end;
                                            W2[53] = ZA[W2[53]];
                                            W2[53] = W2[53](ZA, W2[60], W2[61]);
                                        end;
                                        W2[60] = 75;
                                        W2[53] = nil;
                                        W2[65] = "\x807Q\xbc$\xf0Q \x9c\xb6\x7f\x85\xd6";
                                        w[W2[60]] = W2[53];
                                        W2[62] = r3;
                                        W2[66] = 17503110471638;
                                        W2[63] = r2;
                                        W2[53] = "AddButton";
                                        W2[64] = W2[63](W2[65], W2[66]);
                                        W2[53] = ZA[W2[53]];
                                        W2[61] = W2[62][W2[64]];
                                        W2[62] = function(...)
                                            local R = {
                                                212,
                                                210,
                                                W2[60]
                                            };
                                            v1 = game.Players.LocalPlayer.Character.HumanoidRootPart.Position;
                                            v5 = math.round(v1.X) .. ", " .. math.round(v1.Y) .. ", " .. math.round(v1.Z);
                                            w[W2[60]] = v5;
                                            v5 = v5;
                                            if writefile and isfile then
                                                writefile("savedpos.txt", w[W2[60]]);
                                            end;
                                            return; 
                                        end;
                                        W2[65] = "H\xc5\xc4\xc1\x8f\x1d\x16=\x87m\xa4!";
                                        W2[53] = W2[53](ZA, W2[61], W2[62]);
                                        W2[66] = 34932338376586;
                                        W2[62] = r3;
                                        W2[63] = r2;
                                        W2[64] = W2[63](W2[65], W2[66]);
                                        W2[61] = W2[62][W2[64]];
                                        W2[63] = 76;
                                        W2[53] = "AddButton";
                                        W2[73] = "\x9b|c\xd6%;\xcb\xc9k[\xe0";
                                        W2[62] = function(...)
                                            local R = {
                                                212,
                                                210,
                                                W2[60],
                                                160
                                            };
                                            v1 = readfile;
                                            if v1 then
                                                v1 = isfile;
                                                v3 = v1 and isfile("savedpos.txt");
                                                v5 = v5;
                                            end;
                                            if v1 then
                                                w[W2[60]] = readfile("savedpos.txt");
                                            end;
                                            if w[W2[60]] then
                                                v5 = w[W2[60]];
                                                j = {
                                                    v5:match("([^,]+), ([^,]+), ([^,]+)")
                                                };
                                                r36(CFrame.new(tonumber(j[1]), tonumber(j[2]), tonumber(j[3])));
                                            end;
                                            return; 
                                        end;
                                        W2[53] = ZA[W2[53]];
                                        W2[53] = W2[53](ZA, W2[61], W2[62]);
                                        W2[53] = {};
                                        W2[61] = 77;
                                        W2[75] = 17781690032216;
                                        W2[62] = 78;
                                        w[W2[61]] = W2[53];
                                        W2[64] = nil;
                                        W2[53] = {};
                                        w[W2[62]] = W2[53];
                                        W2[53] = false;
                                        W2[66] = function(arg1_133, arg2_133, arg3_133, ...)
                                            local R = {
                                                212,
                                                210,
                                                W2[61],
                                                163,
                                                W2[63],
                                                W2[62]
                                            };
                                            x = arg3_133;
                                            r152 = arg1_133;
                                            r153 = arg2_133;
                                            r152.D = 1250;
                                            r152.P = 10000;
                                            r152.MaxForce = Vector3.new(1000000, 1000000, 1000000);
                                            w[W2[61]][r152] = true;
                                            v5 = r38.RenderStepped;
                                            r154 = v5:Connect(function(...)
                                                local R = {
                                                    212,
                                                    210,
                                                    W2[63],
                                                    102,
                                                    101,
                                                    W2[61],
                                                    103,
                                                    163
                                                };
                                                v5 = _G.targetPlayer;
                                                if not w[W2[61]] or not v5 then
                                                    return;
                                                end;
                                                if not r38.Parent or r38.Parent ~= w[W2[63]] then
                                                    w[W2[62]][r38] = nil;
                                                    v5 = r154;
                                                    v5:Disconnect();
                                                    return;
                                                end;
                                                if (w[W2[63]].Position - v5.HumanoidRootPart.Position).Magnitude >= 1000 then
                                                    return;
                                                end;
                                                r38.Position = v5.HumanoidRootPart.Position + Vector3.new(0, 0, 3);
                                                v5 = tick;
                                                x = v5();
                                                q = (w[W2[63]].Position - r38.Position).Magnitude < 3;
                                                v3 = q;
                                                if q then
                                                    v5 = r38.Heartbeat;
                                                    v5:Wait();
                                                    if (w[W2[63]].Position - r38.Position).Magnitude < 3 or tick() - x > 1.5 then
                                                        return;
                                                    end;
                                                else
                                                    v3 = tick() - x > 1.5;
                                                end; 
                                            end);
                                            table.insert(w[W2[62]], r154);
                                            return; 
                                        end;
                                        w[W2[63]] = W2[53];
                                        W2[65] = 79;
                                        w[W2[65]] = W2[66];
                                        W2[53] = nil;
                                        W2[68] = r79;
                                        W2[70] = r3;
                                        W2[66] = function(arg1_134, ...)
                                            local R = {
                                                312,
                                                212,
                                                210,
                                                W2[63],
                                                W2[65]
                                            };
                                            v1 = arg1_134;
                                            r155 = r79.LocalPlayer;
                                            r156 = v1:WaitForChild("HumanoidRootPart");
                                            v5 = r156.ChildAdded;
                                            v5:Connect(function(arg1_135, ...)
                                                local R = {
                                                    W2[63],
                                                    212,
                                                    210,
                                                    40,
                                                    W2[65],
                                                    39
                                                };
                                                U = r79;
                                                v1 = arg1_135;
                                                if U then
                                                    v3 = v1:IsA("BodyPosition");
                                                end;
                                                if U then
                                                    U = _G.targetPlayer;
                                                    if U then
                                                        if (w[W2[63]].Position - U.HumanoidRootPart.Position).Magnitude >= 1000 then
                                                            Notify({
                                                                ["Description"] = U.Name .. " or you is in a Domain",
                                                                ["Title"] = "BlackHole Lock",
                                                                ["Duration"] = 5
                                                            });
                                                        end;
                                                    end;
                                                    w[W2[65]](v1, w[W2[63]], r155);
                                                end;
                                                return; 
                                            end);
                                            v4 = r156;
                                            j = v4[3];
                                            q = v4[2];
                                            v4 = "ipairs";
                                            for j, v7 in ipairs(v4:GetChildren()) do
                                                v2 = j;
                                                if w[W2[63]] and v7:IsA("BodyPosition") then
                                                    w[W2[65]](v7, r156, r155);
                                                end; 
                                            end;
                                            return; 
                                        end;
                                        W2[71] = r2;
                                        W2[74] = 21478642476817;
                                        W2[72] = W2[71](W2[73], W2[74]);
                                        W2[74] = "G\x19\xef\xe6`\x81c\xd8}";
                                        W2[69] = W2[70][W2[72]];
                                        W2[67] = W2[68][W2[69]];
                                        W2[68] = 80;
                                        w[W2[68]] = W2[67];
                                        W2[69] = w[W2[68]];
                                        W2[71] = r3;
                                        W2[72] = r2;
                                        W2[73] = W2[72](W2[74], W2[75]);
                                        W2[70] = W2[71][W2[73]];
                                        W2[67] = W2[69][W2[70]];
                                        if W2[67] then
                                            W2[70] = w[W2[68]];
                                            W2[72] = r3;
                                            W2[76] = 8317751791393;
                                            W2[73] = r2;
                                            W2[75] = "\xf2\xe5\xc7\xdc\xddL\xfa\xf3X";
                                            W2[74] = W2[73](W2[75], W2[76]);
                                            W2[71] = W2[72][W2[74]];
                                            W2[69] = W2[70][W2[71]];
                                            W2[67] = W2[66](W2[69]);
                                        end;
                                        W2[69] = w[W2[68]];
                                        W2[71] = r3;
                                        W2[74] = "\x1a\x10\xa6I%\x03\x1d\xb4\x14h$\xea\xb4\x94";
                                        W2[75] = 8563442995091;
                                        W2[72] = r2;
                                        W2[73] = W2[72](W2[74], W2[75]);
                                        W2[70] = W2[71][W2[73]];
                                        W2[67] = W2[69][W2[70]];
                                        W2[69] = "Connect";
                                        W2[69] = W2[67][W2[69]];
                                        W2[69] = W2[69](W2[67], W2[66]);
                                        W2[71] = "game";
                                        W2[75] = "\xbb\xb6\xbdAe\xa5\xfe";
                                        W2[67] = "AddTargetTextBox";
                                        W2[67] = mA[W2[67]];
                                        W2[76] = 19978250626135;
                                        W2[67] = W2[67](mA);
                                        W2[70] = Env[W2[71]];
                                        W2[72] = r3;
                                        W2[73] = r2;
                                        W2[74] = W2[73](W2[75], W2[76]);
                                        W2[71] = W2[72][W2[74]];
                                        W2[69] = W2[70][W2[71]];
                                        W2[74] = "\xd5\x03\xf0]\x84\x82\xf8+\xe3G\xee\xe8\x1f\x15";
                                        W2[71] = r3;
                                        W2[72] = r2;
                                        W2[76] = 30104679855810;
                                        W2[75] = 2724502979828;
                                        W2[73] = W2[72](W2[74], W2[75]);
                                        W2[70] = W2[71][W2[73]];
                                        W2[67] = W2[69][W2[70]];
                                        W2[69] = "Connect";
                                        W2[70] = function(arg1_136, ...)
                                            local R = {
                                                212,
                                                210
                                            };
                                            v1 = arg1_136;
                                            if v1.Name == _G.targetPlayer.Name then
                                                Notify({
                                                    ["Description"] = v1.Name .. " has left.",
                                                    ["Title"] = "TBO",
                                                    ["Duration"] = 5
                                                });
                                            end;
                                            return; 
                                        end;
                                        W2[69] = W2[67][W2[69]];
                                        W2[71] = "game";
                                        W2[75] = "\xa6\x95\xe5{Gzk";
                                        W2[69] = W2[69](W2[67], W2[70]);
                                        W2[70] = Env[W2[71]];
                                        W2[72] = r3;
                                        W2[73] = r2;
                                        W2[74] = W2[73](W2[75], W2[76]);
                                        W2[71] = W2[72][W2[74]];
                                        W2[75] = 4593034774618;
                                        W2[69] = W2[70][W2[71]];
                                        W2[71] = r3;
                                        W2[72] = r2;
                                        W2[74] = "\xbc3wA\xbe\x1f\xa8TM\x0e\x1a";
                                        W2[73] = W2[72](W2[74], W2[75]);
                                        W2[70] = W2[71][W2[73]];
                                        W2[67] = W2[69][W2[70]];
                                        W2[70] = function(arg1_137, ...)
                                            local R = {
                                                212,
                                                210
                                            };
                                            v1 = arg1_137;
                                            if v1.Name == _G.targetPlayer.Name then
                                                _G.targetPlayer = v1;
                                                Notify({
                                                    ["Description"] = v1.Name .. " has Rejoined.",
                                                    ["Title"] = "TBO",
                                                    ["Duration"] = 5
                                                });
                                            end;
                                            return; 
                                        end;
                                        W2[69] = "Connect";
                                        W2[69] = W2[67][W2[69]];
                                        W2[69] = W2[69](W2[67], W2[70]);
                                        W2[69] = "ForceReset";
                                        W2[67] = function(...)
                                            local R = {
                                                212,
                                                210
                                            };
                                            Reset = true;
                                            task.spawn(function(...)
                                                local R = {
                                                    212,
                                                    210
                                                };
                                                v5 = not Reset;
                                                repeat
                                                    task.wait();
                                                until Reset;
                                                v5 = game.Players.LocalPlayer.Character.Humanoid;
                                                v5:Move((game.Players.LocalPlayer.Character.HumanoidRootPart.Position - game.Players.LocalPlayer.Character.HumanoidRootPart.Position).Unit, false);
                                                if not Reset then
                                                    return;
                                                end; 
                                            end);
                                            v3 = game.Players.LocalPlayer.CharacterAdded;
                                            v3:Connect(function(...)
                                                Reset = false;
                                                return; 
                                            end);
                                            return; 
                                        end;
                                        Env[W2[69]] = W2[67];
                                        W2[67] = vA();
                                        if W2[67] then
                                            W2[74] = "\xea0\x04\x7fA\xf6\x9c\x18\x06";
                                            W2[76] = 10314944221891;
                                            W2[69] = 62;
                                            W2[67] = nil;
                                            W2[75] = 30732575209446;
                                            w[W2[69]] = W2[67];
                                            W2[71] = r3;
                                            W2[72] = r2;
                                            W2[73] = W2[72](W2[74], W2[75]);
                                            W2[70] = W2[71][W2[73]];
                                            W2[71] = false;
                                            W2[72] = function(arg1_138, ...)
                                                local R = {
                                                    U,
                                                    210,
                                                    W2[69]
                                                };
                                                r157 = arg1_138;
                                                if r157 then
                                                    local function r158(...)
                                                        local R = {
                                                            U,
                                                            210
                                                        };
                                                        v5 = game.Players.LocalPlayer.Character.Humanoid;
                                                        v5:Move((game.Players.LocalPlayer.Character.HumanoidRootPart.Position - game.Players.LocalPlayer.Character.HumanoidRootPart.Position).Unit, false);
                                                        return; 
                                                    end;
                                                    r158();
                                                    v5 = game.Players.LocalPlayer.CharacterAdded;
                                                    w[W2[69]] = v5:Connect(function(...)
                                                        local R = {
                                                            U,
                                                            210,
                                                            278,
                                                            251
                                                        };
                                                        v5 = game.Players.LocalPlayer.Character;
                                                        v5:FindFirstChild("HumanoidRootPart");
                                                        task.wait();
                                                        v5 = game.Players.LocalPlayer.Character;
                                                        if v5:FindFirstChild("HumanoidRootPart") then
                                                            if w[W2[69]] then
                                                                r158();
                                                            end;
                                                            return;
                                                        end; 
                                                    end);
                                                    v5 = game;
                                                    x = v5:GetService("RunService");
                                                    x:BindToRenderStep("Inf-Range", 0, function(...)
                                                        local R = {
                                                            U,
                                                            210,
                                                            251
                                                        };
                                                        x = "targetPlayer";
                                                        v1 = _G[x];
                                                        if v1 then
                                                            x = _G.targetPlayer.Character;
                                                            v3 = x and x:FindFirstChild("HumanoidRootPart");
                                                            v5 = x.BindToRenderStep;
                                                        end;
                                                        if v1 then
                                                            if game.Players.LocalPlayer.Character.Humanoid.MoveDirection.Magnitude > 0 then
                                                                r158();
                                                            end;
                                                            game.Players.LocalPlayer.Character.HumanoidRootPart.CFrame = CFrame.new(_G.targetPlayer.Character.HumanoidRootPart.Position + _G.targetPlayer.Character.Humanoid.MoveDirection * .8 * _G.targetPlayer.Character.Humanoid.WalkSpeed - _G.targetPlayer.Character.HumanoidRootPart.CFrame.LookVector * 5, _G.targetPlayer.Character.HumanoidRootPart.Position);
                                                        end;
                                                        return; 
                                                    end);
                                                else
                                                    v5 = game;
                                                    U = v5:GetService("RunService");
                                                    U:UnbindFromRenderStep("Inf-Range");
                                                    if w[W2[69]] then
                                                        v5 = w[W2[69]];
                                                        v5:Disconnect();
                                                        w[W2[69]] = nil;
                                                    end;
                                                    return;
                                                end; 
                                            end;
                                            W2[67] = "AddToggle";
                                            W2[67] = mA[W2[67]];
                                            W2[67] = W2[67](mA, W2[70], W2[71], W2[72]);
                                            W2[70] = 63;
                                            W2[75] = "J\xe4Y7\xebK\x81";
                                            W2[67] = {};
                                            w[W2[70]] = W2[67];
                                            W2[72] = r3;
                                            W2[73] = r2;
                                            W2[74] = W2[73](W2[75], W2[76]);
                                            W2[73] = function(arg1_139, ...)
                                                local R = {
                                                    212,
                                                    210,
                                                    W2[70]
                                                };
                                                if arg1_139 then
                                                    v5 = game;
                                                    v3 = v5:GetService("RunService");
                                                    v3:BindToRenderStep("M1-Farm", 0, function(...)
                                                        local R = {
                                                            212,
                                                            210
                                                        };
                                                        j = game;
                                                        q = game.Players.LocalPlayer;
                                                        v5 = j:GetService("ReplicatedStorage").Knit.Knit.Services[q:GetAttribute("Moveset") .. "Service"].RE.Activated;
                                                        v5:FireServer(false);
                                                        return; 
                                                    end);
                                                    v2 = game;
                                                    q = v2:GetService("ReplicatedStorage").Knit.Knit.Services;
                                                    U = q[2];
                                                    q = q[1];
                                                    for x, v4 in ipairs(q:GetChildren()) do
                                                        j = x;
                                                        r = "RE";
                                                        v7 = v4:FindFirstChild(r);
                                                        if v7 then
                                                            v7 = v4.RE;
                                                            v2 = v7:FindFirstChild("Effects");
                                                        end;
                                                        if v7 then
                                                            r = v4.RE.Effects.OnClientEvent;
                                                            table.insert(w[W2[70]], r:Connect(function(...)
                                                                local R = {
                                                                    212,
                                                                    210
                                                                };
                                                                U = {
                                                                    select(-1, ...)
                                                                };
                                                                x = U[1] == "Swing2";
                                                                if x then
                                                                    v3 = U[2] == game.Players.LocalPlayer.Character and U[3] == 3;
                                                                    v5 = {
                                                                        C(v1)
                                                                    };
                                                                end;
                                                                if x then
                                                                    task.wait(.3);
                                                                    if _G.targetPlayer and _G.targetPlayer.Character then
                                                                        ForceReset();
                                                                    end;
                                                                end;
                                                                return; 
                                                            end));
                                                        end; 
                                                    end;
                                                else
                                                    v5 = game;
                                                    U = v5:GetService("RunService");
                                                    v4 = r2("a\xd95\x1ft\xfc\xf7", 16675955990101);
                                                    U:UnbindFromRenderStep(r3[v4]);
                                                    q = v4[3];
                                                    for q, v4 in v4[1], ipairs(w[W2[70]]) do
                                                        j = q;
                                                        v4:Disconnect(); 
                                                    end;
                                                    return;
                                                end; 
                                            end;
                                            W2[67] = "AddToggle";
                                            W2[71] = W2[72][W2[74]];
                                            W2[72] = false;
                                            W2[69] = nil;
                                            W2[67] = mA[W2[67]];
                                            W2[70] = nil;
                                            W2[67] = W2[67](mA, W2[71], W2[72], W2[73]);
                                        end;
                                        W2[69] = 200;
                                        W2[67] = nil;
                                        w[W2[69]] = W2[67];
                                        W2[75] = 25029081935239;
                                        W2[74] = "\x84\xb1\"\xfa+\xbb8\x944&/C\xc22S";
                                        W2[71] = r3;
                                        W2[67] = "AddToggle";
                                        W2[72] = r2;
                                        W2[73] = W2[72](W2[74], W2[75]);
                                        W2[72] = function(arg1_140, ...)
                                            local R = {
                                                212,
                                                210,
                                                159,
                                                W2[69]
                                            };
                                            if arg1_140 then
                                                v3 = game;
                                                v5 = v3:GetService("RunService").Heartbeat;
                                                w[W2[69]] = v5:Connect(function(...)
                                                    local R = {
                                                        212,
                                                        210,
                                                        159
                                                    };
                                                    v1 = _G.targetPlayer;
                                                    if v1 then
                                                        x = _G.targetPlayer.Character;
                                                        if x then
                                                            x = game.Players.LocalPlayer.Character.Info;
                                                            v1 = x:FindFirstChild("RedTeleport");
                                                        end;
                                                        v5 = U[x[j]];
                                                        v3 = x;
                                                    end;
                                                    if v1 then
                                                        r34(_G.targetPlayer.Character.HumanoidRootPart.CFrame);
                                                    end;
                                                    return; 
                                                end);
                                            else
                                                v5 = w[W2[69]];
                                                v5:Disconnect();
                                                w[W2[69]] = nil;
                                            end;
                                            return; 
                                        end;
                                        W2[74] = "\xa1U3\xae\xf7\x82\x03\xc2\xa0\xa1{K>N";
                                        W2[82] = 28750609282124;
                                        W2[67] = mA[W2[67]];
                                        W2[70] = W2[71][W2[73]];
                                        W2[71] = false;
                                        W2[67] = W2[67](mA, W2[70], W2[71], W2[72]);
                                        W2[71] = r3;
                                        W2[72] = r2;
                                        W2[75] = 16751721799288;
                                        W2[73] = W2[72](W2[74], W2[75]);
                                        W2[75] = 3974378522426;
                                        W2[67] = "AddToggle";
                                        W2[70] = W2[71][W2[73]];
                                        W2[71] = false;
                                        W2[77] = 2942930601306;
                                        W2[72] = function(arg1_141, ...)
                                            local R = {
                                                212,
                                                210
                                            };
                                            v3 = true;
                                            if arg1_141 == v3 then
                                                if not _G.TODOKILL then
                                                    Notify({
                                                        ["Description"] = "Please Enable Todo Kill For This To Work.",
                                                        ["Title"] = "TBO",
                                                        ["Duration"] = 5
                                                    });
                                                    return;
                                                end;
                                                v5 = game;
                                                v3 = v5:GetService("RunService");
                                                v3:BindToRenderStep("Auto-TodoKill", 0, function(...)
                                                    local R = {
                                                        212,
                                                        210
                                                    };
                                                    v5 = game;
                                                    v3 = v5:GetService("ReplicatedStorage");
                                                    v5 = v3:WaitForChild("Knit");
                                                    v3 = v5:WaitForChild("Knit");
                                                    v5 = v3:WaitForChild("Services");
                                                    v3 = v5:WaitForChild("SwiftKickService");
                                                    v5 = v3:WaitForChild("RE");
                                                    v3 = v5:WaitForChild("Activated");
                                                    q = game;
                                                    v1 = q:GetService("Players").LocalPlayer.Character.Moveset;
                                                    v3:FireServer(v1:FindFirstChild("Swift Kick"));
                                                    return; 
                                                end);
                                            else
                                                v5 = game;
                                                v3 = v5:GetService("RunService");
                                                v3:UnbindFromRenderStep("Auto-TodoKill");
                                            end;
                                            return; 
                                        end;
                                        W2[74] = "C\xff\x8c\x00\xea%@\xcb\xb9\"\x9eA\xcb\xa5$\t\xf39>\xcf\xe8B";
                                        W2[67] = mA[W2[67]];
                                        W2[67] = W2[67](mA, W2[70], W2[71], W2[72]);
                                        W2[71] = r3;
                                        W2[67] = "AddToggle";
                                        W2[72] = r2;
                                        W2[73] = W2[72](W2[74], W2[75]);
                                        W2[70] = W2[71][W2[73]];
                                        W2[71] = false;
                                        W2[72] = function(arg1_142, ...)
                                            local R = {
                                                212,
                                                210
                                            };
                                            if arg1_142 then
                                                _G.TODOKILL = {};
                                                local function U(arg1_143, ...)
                                                    local R = {
                                                        212,
                                                        210
                                                    };
                                                    v1 = arg1_143;
                                                    v5 = v1:WaitForChild("Humanoid").AnimationPlayed;
                                                    table.insert(_G.TODOKILL, v5:Connect(function(arg1_144, ...)
                                                        local R = {
                                                            212,
                                                            210
                                                        };
                                                        v1 = arg1_144;
                                                        if v1.Animation and v1.Animation.AnimationId == "rbxassetid://94720627091769" then
                                                            U = v1.IsPlaying;
                                                            v3 = v1.TimePosition < 1.68;
                                                            while not U do
                                                                if v3 then
                                                                    task.wait();
                                                                end;
                                                                if arg1_144.IsPlaying then
                                                                    _G.targetPlayer.HumanoidRootPart.Size = Vector3.new(40, 40, 40);
                                                                    game.Players.LocalPlayer.Character.Humanoid.AutoRotate = false;
                                                                    game.Players.LocalPlayer.Character.HumanoidRootPart.CFrame = CFrame.new(_G.targetPlayer.Character.HumanoidRootPart.Position + _G.targetPlayer.Character.Humanoid.MoveDirection * .8 * _G.targetPlayer.Character.Humanoid.WalkSpeed - _G.targetPlayer.Character.HumanoidRootPart.CFrame.LookVector * 5, _G.targetPlayer.Character.HumanoidRootPart.Position);
                                                                    task.wait();
                                                                    ForceReset();
                                                                    while arg1_144.IsPlaying do
                                                                        task.wait(); 
                                                                    end;
                                                                    if game.Players.LocalPlayer.PlayerGui.Main.Moveset["Swift Kick"].Cooldown.Size ~= UDim2.new(1, 0, 0, 0) then
                                                                        ForceReset();
                                                                    end;
                                                                    _G.targetPlayer.Character.HumanoidRootPart.Size = Vector3.new(2, 2, 1);
                                                                    game.Players.LocalPlayer.Character.Humanoid.AutoRotate = true;
                                                                end;
                                                                break; 
                                                            end;
                                                            v3 = v1.TimePosition < 1.68;
                                                        end;
                                                        return; 
                                                    end));
                                                    return; 
                                                end;
                                                q = game;
                                                U(q:GetService("Players").LocalPlayer.Character);
                                                j = game;
                                                x = j:GetService("Players").LocalPlayer.CharacterAdded;
                                                _G.TODOKILL_CHARCONN = x:Connect(U);
                                            else
                                                j = r2("~r\x96\x0c\xe7\x94\xb7\xd1", 22374981281971);
                                                if _G[r3[j]] then
                                                    j = _G;
                                                    q = j.TODOKILL;
                                                    U = j[2];
                                                    x = j[3];
                                                    for x, v4 in ipairs(v3) do
                                                        r159 = v4;
                                                        j = x;
                                                        if typeof(w[v5]) == "Instance" or typeof(w[v5]) == "RBXScriptConnection" then
                                                            pcall(function(...)
                                                                v5 = w[v5];
                                                                v5:Disconnect();
                                                                return; 
                                                            end);
                                                        end; 
                                                    end;
                                                end;
                                                if _G.TODOKILL_CHARCONN then
                                                    pcall(function(...)
                                                        local R = {
                                                            212,
                                                            210
                                                        };
                                                        v5 = _G.TODOKILL_CHARCONN;
                                                        v5:Disconnect();
                                                        return; 
                                                    end);
                                                end;
                                                return;
                                            end; 
                                        end;
                                        W2[67] = mA[W2[67]];
                                        W2[67] = W2[67](mA, W2[70], W2[71], W2[72]);
                                        W2[74] = "\xbc\x99\x12tN3\xd9r\x06C\x0b\xe6\xb7\xc9\xee\xddA\xceb\xcc1h\xb0";
                                        W2[71] = r3;
                                        W2[72] = r2;
                                        W2[75] = 10913564365786;
                                        W2[73] = W2[72](W2[74], W2[75]);
                                        W2[70] = W2[71][W2[73]];
                                        W2[67] = "AddToggle";
                                        W2[67] = mA[W2[67]];
                                        W2[71] = false;
                                        W2[72] = function(arg1_145, ...)
                                            local R = {
                                                212,
                                                210
                                            };
                                            if arg1_145 then
                                                if _G.SilentANIM then
                                                    Notify({
                                                        ["Description"] = "Please Disable Silent Animations For This To Work.",
                                                        ["Title"] = "TBO",
                                                        ["Duration"] = 5
                                                    });
                                                end;
                                                _G.TODOBRING = {};
                                                q = game;
                                                local function U(arg1_146, ...)
                                                    local R = {
                                                        212,
                                                        210
                                                    };
                                                    v1 = arg1_146;
                                                    v5 = v1:WaitForChild("Humanoid").AnimationPlayed;
                                                    table.insert(_G.TODOBRING, v5:Connect(function(arg1_147, ...)
                                                        local R = {
                                                            212,
                                                            210
                                                        };
                                                        v1 = arg1_147;
                                                        if v1.Animation and v1.Animation.AnimationId == "rbxassetid://94720627091769" then
                                                            U = v1.IsPlaying;
                                                            v3 = v1.TimePosition < 1.7;
                                                            while not U do
                                                                if v3 then
                                                                    task.wait();
                                                                end;
                                                                if arg1_147.IsPlaying then
                                                                    _G.targetPlayer.Character.HumanoidRootPart.Size = Vector3.new(40, 40, 40);
                                                                    if game.Players.LocalPlayer.Character.Humanoid.AutoRotate == true then
                                                                        game.Players.LocalPlayer.Character.Humanoid.AutoRotate = false;
                                                                    end;
                                                                    game.Players.LocalPlayer.Character.HumanoidRootPart.CFrame = CFrame.new(_G.targetPlayer.Character.HumanoidRootPart.Position + _G.targetPlayer.Character.Humanoid.MoveDirection * .8 * _G.targetPlayer.Character.Humanoid.WalkSpeed - _G.targetPlayer.Character.HumanoidRootPart.CFrame.LookVector * 5, _G.targetPlayer.Character.HumanoidRootPart.Position);
                                                                    while arg1_147.IsPlaying do
                                                                        task.wait(); 
                                                                    end;
                                                                    _G.targetPlayer.Character.HumanoidRootPart.Size = Vector3.new(2, 2, 1);
                                                                    game.Players.LocalPlayer.Character.Humanoid.AutoRotate = true;
                                                                end;
                                                                break; 
                                                            end;
                                                            v3 = v1.TimePosition < 1.7;
                                                        end;
                                                        return; 
                                                    end));
                                                    return; 
                                                end;
                                                U(q:GetService("Players").LocalPlayer.Character);
                                                j = game;
                                                x = j:GetService("Players").LocalPlayer.CharacterAdded;
                                                _G.TODOBRING_CHARCONN = x:Connect(U);
                                            else
                                                q = r2;
                                                j = q("\x8b\xed\xe6tb\xb0\x85\\\xdb", 26061742829415);
                                                if _G[r3[j]] then
                                                    j = _G;
                                                    q = j.TODOBRING;
                                                    U = j[2];
                                                    q = j[1];
                                                    for x, v4 in ipairs(q) do
                                                        r160 = v4;
                                                        j = x;
                                                        if typeof(w[v5]) == "Instance" or typeof(w[v5]) == "RBXScriptConnection" then
                                                            pcall(function(...)
                                                                v5 = w[v5];
                                                                v5:Disconnect();
                                                                return; 
                                                            end);
                                                        end; 
                                                    end;
                                                end;
                                                if _G.TODOBRING_CHARCONN then
                                                    pcall(function(...)
                                                        local R = {
                                                            212,
                                                            210
                                                        };
                                                        v5 = _G.TODOBRING_CHARCONN;
                                                        v5:Disconnect();
                                                        return; 
                                                    end);
                                                end;
                                                return;
                                            end; 
                                        end;
                                        W2[78] = 13487998834824;
                                        W2[75] = 487996244195;
                                        W2[74] = "\x9do\xb837\xb15E`\x05%BLX";
                                        W2[67] = W2[67](mA, W2[70], W2[71], W2[72]);
                                        W2[76] = 17843130753140;
                                        W2[71] = r3;
                                        W2[72] = r2;
                                        W2[73] = W2[72](W2[74], W2[75]);
                                        W2[72] = function(arg1_148, ...)
                                            local R = {
                                                W2[63],
                                                W2[62],
                                                212,
                                                210
                                            };
                                            v1 = arg1_148;
                                            w[W2[63]] = v1;
                                            if not v1 then
                                                x = 305[2];
                                                q = 305[3];
                                                for q, v4 in ipairs(w[W2[62]]) do
                                                    j = q;
                                                    if v4 then
                                                        v3 = v4.Disconnect;
                                                    end;
                                                    v5 = v1;
                                                    if v4 then
                                                        v4:Disconnect();
                                                    end; 
                                                end;
                                                w[W2[62]] = {};
                                            end;
                                            return; 
                                        end;
                                        W2[70] = W2[71][W2[73]];
                                        W2[67] = "AddToggle";
                                        W2[67] = mA[W2[67]];
                                        W2[71] = false;
                                        W2[67] = W2[67](mA, W2[70], W2[71], W2[72]);
                                        W2[73] = "";
                                        W2[75] = "\xac\xb2\t\x06\xc99R\x89n\xb5k\xe2\x0f";
                                        W2[74] = 22518253512949;
                                        W2[70] = r3;
                                        W2[71] = r2;
                                        W2[72] = W2[71](W2[73], W2[74]);
                                        W2[67] = W2[70][W2[72]];
                                        W2[81] = ";\xf7\x02&\x00c";
                                        W2[70] = 201;
                                        w[W2[70]] = W2[67];
                                        W2[72] = r3;
                                        W2[73] = r2;
                                        W2[67] = "AddTextBox";
                                        W2[74] = W2[73](W2[75], W2[76]);
                                        W2[67] = KA[W2[67]];
                                        W2[71] = W2[72][W2[74]];
                                        W2[76] = "q[\xfd[\x9d5-\x10\x03\xb2\x03T\xe4\xd7\xe6\x188[u\xf2";
                                        W2[73] = r3;
                                        W2[74] = r2;
                                        W2[75] = W2[74](W2[76], W2[77]);
                                        W2[72] = W2[73][W2[75]];
                                        W2[73] = function(arg1_149, ...)
                                            w[W2[70]] = arg1_149;
                                            return; 
                                        end;
                                        W2[67] = W2[67](KA, W2[71], W2[72], W2[73]);
                                        W2[77] = "\xd8\x1eSB\x01\xd10%\x1b}\xff)\xf7";
                                        W2[67] = {};
                                        W2[71] = 202;
                                        W2[73] = function(...)
                                            local R = {
                                                188,
                                                W2[71]
                                            };
                                            v5 = r65;
                                            w[W2[71]] = v5:GetConfigs();
                                            return; 
                                        end;
                                        W2[72] = "pcall";
                                        w[W2[71]] = W2[67];
                                        W2[67] = Env[W2[72]];
                                        W2[72] = W2[67](W2[73]);
                                        W2[73] = 1;
                                        W2[72] = w[W2[71]];
                                        W2[67] = W2[72][W2[73]];
                                        W2[72] = 203;
                                        w[W2[72]] = W2[67];
                                        W2[83] = 34565917474528;
                                        W2[74] = r3;
                                        W2[75] = r2;
                                        W2[76] = W2[75](W2[77], W2[78]);
                                        W2[67] = "AddDropdown";
                                        W2[75] = function(arg1_150, ...)
                                            w[W2[72]] = arg1_150;
                                            return; 
                                        end;
                                        W2[73] = W2[74][W2[76]];
                                        W2[76] = false;
                                        W2[74] = w[W2[71]];
                                        W2[78] = r3;
                                        W2[79] = r2;
                                        W2[80] = W2[79](W2[81], W2[82]);
                                        W2[77] = W2[78][W2[80]];
                                        W2[79] = 12864878614374;
                                        W2[67] = KA[W2[67]];
                                        W2[67] = W2[67](KA, W2[73], W2[74], W2[75], W2[76], W2[77]);
                                        W2[73] = 204;
                                        w[W2[73]] = W2[67];
                                        W2[75] = r3;
                                        W2[76] = r2;
                                        W2[78] = "I\xc3\xe4\x08\xb6\x85\x91\xfc\xe8\xb3]";
                                        W2[77] = W2[76](W2[78], W2[79]);
                                        W2[67] = "AddButton";
                                        W2[79] = 8920648306746;
                                        W2[67] = KA[W2[67]];
                                        W2[78] = "\xfdHUq~\x9a\xea\xa9\xab\xec\xcf";
                                        W2[74] = W2[75][W2[77]];
                                        W2[75] = function(...)
                                            local R = {
                                                212,
                                                210,
                                                188,
                                                W2[73],
                                                W2[72]
                                            };
                                            pcall(function(...)
                                                local R = {
                                                    212,
                                                    210,
                                                    188,
                                                    W2[73],
                                                    W2[72]
                                                };
                                                v1 = "TBO_CONFIG_" .. tostring(os.time()) .. ".json";
                                                v5 = r65;
                                                v5:SaveConfig(v1);
                                                v5 = w[W2[73]];
                                                v5:AddOption(v1);
                                                w[W2[72]] = v1;
                                                return; 
                                            end);
                                            return; 
                                        end;
                                        W2[67] = W2[67](KA, W2[74], W2[75]);
                                        W2[75] = r3;
                                        W2[76] = r2;
                                        W2[67] = "AddButton";
                                        W2[77] = W2[76](W2[78], W2[79]);
                                        W2[74] = W2[75][W2[77]];
                                        W2[75] = function(...)
                                            local R = {
                                                W2[70],
                                                212,
                                                210,
                                                245,
                                                188,
                                                W2[72]
                                            };
                                            pcall(function(...)
                                                local R = {
                                                    W2[70],
                                                    212,
                                                    210,
                                                    245,
                                                    188,
                                                    W2[72]
                                                };
                                                if w[W2[70]] ~= "" then
                                                    v5 = pcall;
                                                    v1 = v5(function(...)
                                                        local R = {
                                                            245,
                                                            W2[70]
                                                        };
                                                        v5 = w[W2[70]];
                                                        v5:JSONDecode(r3);
                                                        return; 
                                                    end);
                                                    if v1 then
                                                        v5 = r65;
                                                        v5:LoadConfig(w[W2[70]]);
                                                    else
                                                        Notify({
                                                            ["Title"] = "TBO",
                                                            ["Description"] = "Invalid JSON config.",
                                                            ["Duration"] = 5
                                                        });
                                                    end;
                                                else
                                                    if w[W2[72]] and w[W2[72]] ~= "" then
                                                        v5 = r65;
                                                        v5:LoadConfig(w[W2[72]]);
                                                    end;
                                                    return;
                                                end; 
                                            end);
                                            return; 
                                        end;
                                        W2[79] = 904180613541;
                                        W2[67] = KA[W2[67]];
                                        W2[67] = W2[67](KA, W2[74], W2[75]);
                                        W2[75] = r3;
                                        W2[78] = "\xbaWs\xbe\x8e\xa2Y\x9d\xd8\xf1\xea\xb7\xdd\xe4\x7fP";
                                        W2[67] = "AddToggle";
                                        W2[76] = r2;
                                        W2[90] = "\xe5#)\xd3s";
                                        W2[77] = W2[76](W2[78], W2[79]);
                                        W2[76] = function(arg1_151, ...)
                                            r161 = arg1_151;
                                            pcall(function(...)
                                                local R = {
                                                    R[1],
                                                    R[2],
                                                    R[3],
                                                    247
                                                };
                                                w[R[1]].AUTOLOAD = r161;
                                                w[R[1]].DEFAULT_CONFIG = "default.json";
                                                v5 = w[R[1]];
                                                v5:SaveConfig("autoload.json");
                                                return; 
                                            end);
                                            return; 
                                        end;
                                        W2[74] = W2[75][W2[77]];
                                        W2[67] = KA[W2[67]];
                                        W2[78] = "\xe4\x9a\x9d\xb3J\x8dR\x9e\x00\xd7\x86";
                                        W2[79] = 25582898491016;
                                        W2[75] = false;
                                        W2[67] = W2[67](KA, W2[74], W2[75], W2[76]);
                                        W2[75] = r3;
                                        W2[76] = r2;
                                        W2[77] = W2[76](W2[78], W2[79]);
                                        W2[74] = W2[75][W2[77]];
                                        W2[91] = 14825180535543;
                                        W2[67] = "AddButton";
                                        W2[75] = function(...)
                                            local R = {
                                                W2[72],
                                                212,
                                                210
                                            };
                                            pcall(function(...)
                                                local R = {
                                                    W2[72],
                                                    212,
                                                    210
                                                };
                                                if w[W2[72]] and w[W2[72]] ~= "" then
                                                    setclipboard(readfile("TBO/Configs/" .. w[W2[72]]));
                                                end;
                                                return; 
                                            end);
                                            return; 
                                        end;
                                        W2[78] = "\xe4\xc7\xe2.\x08\xf6#\xf3\xa0M\x9f\xba\xcd";
                                        W2[67] = KA[W2[67]];
                                        W2[67] = W2[67](KA, W2[74], W2[75]);
                                        W2[75] = r3;
                                        W2[67] = "AddButton";
                                        W2[76] = r2;
                                        W2[79] = 15398094674946;
                                        W2[77] = W2[76](W2[78], W2[79]);
                                        W2[74] = W2[75][W2[77]];
                                        W2[75] = function(...)
                                            local R = {
                                                W2[72],
                                                212,
                                                210,
                                                W2[73],
                                                188
                                            };
                                            pcall(function(...)
                                                local R = {
                                                    W2[72],
                                                    212,
                                                    210,
                                                    W2[73],
                                                    188
                                                };
                                                if w[W2[72]] and w[W2[72]] ~= "" then
                                                    q = r2;
                                                    delfile("TBO/Configs/" .. w[W2[72]]);
                                                    v5 = w[W2[73]];
                                                    v5:Clear();
                                                    v5 = r65;
                                                    v1 = v5:GetConfigs();
                                                    v5 = ipairs;
                                                    U = q[2];
                                                    q = q[1];
                                                    for x, v4 in v5(v1) do
                                                        v5 = w[W2[73]];
                                                        j = x;
                                                        v5:AddOption(v4); 
                                                    end;
                                                    w[W2[72]] = v1[1] or "";
                                                end;
                                                return; 
                                            end);
                                            return; 
                                        end;
                                        W2[82] = "\xd0\xb1F\xd4\x86F\t\xd6H\x05\xd9";
                                        W2[67] = KA[W2[67]];
                                        W2[67] = W2[67](KA, W2[74], W2[75]);
                                        W2[79] = 11471391904989;
                                        W2[67] = "AddSection";
                                        W2[78] = ":\x8e\xb6\xa3g";
                                        W2[75] = r3;
                                        W2[67] = SA[W2[67]];
                                        W2[76] = r2;
                                        W2[77] = W2[76](W2[78], W2[79]);
                                        W2[74] = W2[75][W2[77]];
                                        W2[67] = W2[67](SA, W2[74]);
                                        W2[75] = 205;
                                        W2[67] = {};
                                        W2[74] = 206;
                                        w[W2[74]] = W2[67];
                                        W2[67] = 0;
                                        w[W2[75]] = W2[67];
                                        W2[87] = 29314522658130;
                                        W2[76] = 207;
                                        W2[67] = nil;
                                        w[W2[76]] = W2[67];
                                        W2[77] = 208;
                                        W2[67] = nil;
                                        w[W2[77]] = W2[67];
                                        W2[79] = r3;
                                        W2[80] = r2;
                                        W2[81] = W2[80](W2[82], W2[83]);
                                        W2[86] = "=\xf6-0\xa9y";
                                        W2[78] = W2[79][W2[81]];
                                        W2[83] = r3;
                                        W2[80] = function(arg1_152, ...)
                                            local R = {
                                                W2[74],
                                                212,
                                                210,
                                                W2[76]
                                            };
                                            q = w[W2[74]];
                                            x = 303[3];
                                            U = 303[2];
                                            for x, v4 in pairs("pairs") do
                                                if v4 == arg1_152 and x:IsA("BasePart") then
                                                    w[W2[76]] = x;
                                                    break;
                                                else
                                                    
                                                end; 
                                            end;
                                            return; 
                                        end;
                                        W2[67] = "AddDropdown";
                                        W2[79] = {};
                                        W2[84] = r2;
                                        W2[67] = SA[W2[67]];
                                        W2[85] = W2[84](W2[86], W2[87]);
                                        W2[86] = "workspace";
                                        W2[82] = W2[83][W2[85]];
                                        W2[81] = false;
                                        W2[83] = "\xdc\x07\x85\x88\x8c\xfb\xaa[\xe2";
                                        W2[67] = W2[67](SA, W2[78], W2[79], W2[80], W2[81], W2[82]);
                                        W2[78] = 209;
                                        W2[84] = 2324475970618;
                                        w[W2[78]] = W2[67];
                                        W2[80] = r3;
                                        W2[81] = r2;
                                        W2[82] = W2[81](W2[83], W2[84]);
                                        W2[79] = W2[80][W2[82]];
                                        W2[67] = "AddButton";
                                        W2[80] = function(...)
                                            local R = {
                                                W2[76],
                                                212,
                                                210,
                                                159
                                            };
                                            v1 = w[W2[76]];
                                            if v1 then
                                                v1 = w[W2[76]];
                                                v3 = v1:IsA("BasePart");
                                            end;
                                            if v1 then
                                                v3 = game;
                                                v5 = v3:GetService("RunService").Heartbeat;
                                                r162 = v5:Connect(function(...)
                                                    local R = {
                                                        W2[76],
                                                        212,
                                                        210,
                                                        159,
                                                        33
                                                    };
                                                    v5 = w[W2[76]];
                                                    v1 = v5:FindFirstChildOfClass("ProximityPrompt");
                                                    if v1 then
                                                        v3 = v1.Enabled;
                                                    end;
                                                    if v1 then
                                                        r34(w[W2[76]].CFrame);
                                                        task.wait(.1);
                                                        fireproximityprompt(v1);
                                                        task.wait(.8);
                                                        v5 = r162;
                                                        v5:Disconnect();
                                                    end;
                                                    return; 
                                                end);
                                            end;
                                            return; 
                                        end;
                                        W2[67] = SA[W2[67]];
                                        W2[67] = W2[67](SA, W2[79], W2[80]);
                                        W2[80] = r3;
                                        W2[84] = 10308697608896;
                                        W2[83] = "z[\x9fb\x12\xa8\x96\xde?\xfa\xe0\xa1";
                                        W2[81] = r2;
                                        W2[67] = "AddToggle";
                                        W2[67] = SA[W2[67]];
                                        W2[82] = W2[81](W2[83], W2[84]);
                                        W2[81] = function(arg1_153, ...)
                                            local R = {
                                                212,
                                                210,
                                                W2[76],
                                                159,
                                                W2[77]
                                            };
                                            if arg1_153 then
                                                v3 = game;
                                                v5 = v3:GetService("RunService").Heartbeat;
                                                w[W2[77]] = v5:Connect(function(...)
                                                    local R = {
                                                        W2[76],
                                                        212,
                                                        210,
                                                        159
                                                    };
                                                    v1 = r3;
                                                    if v1 then
                                                        x = r3;
                                                        q = x:IsA("BasePart");
                                                        v3 = q and not q:FindFirstChild(r3.Name);
                                                        v5 = U[x[j]];
                                                    end;
                                                    if v1 then
                                                        v5 = r3;
                                                        v1 = v5:FindFirstChildOfClass("ProximityPrompt");
                                                        if v1 then
                                                            v3 = v1.Enabled;
                                                        end;
                                                        if v1 then
                                                            r34(r3.CFrame);
                                                            fireproximityprompt(v1);
                                                        end;
                                                    end;
                                                    return; 
                                                end);
                                            else
                                                if w[W2[77]] then
                                                    v5 = w[W2[77]];
                                                    v5:Disconnect();
                                                    w[W2[77]] = nil;
                                                end;
                                                return;
                                            end; 
                                        end;
                                        W2[79] = W2[80][W2[82]];
                                        W2[80] = false;
                                        W2[67] = W2[67](SA, W2[79], W2[80], W2[81]);
                                        W2[67] = function(arg1_154, ...)
                                            local R = {
                                                212,
                                                210,
                                                W2[74],
                                                W2[75],
                                                W2[78]
                                            };
                                            v1 = arg1_154;
                                            if v1.Name == "ItemSpawns" then
                                            end;
                                            if w[W2[74]][v1] then
                                                return;
                                            end;
                                            if v1.Position.Magnitude > 10000 then
                                                return;
                                            end;
                                            if not v1:IsA("BasePart") then
                                                return;
                                            end;
                                            w[W2[75]] = w[W2[75]] + 1;
                                            U = v1.Name .. string.rep(utf8.char(8203), w[W2[75]]);
                                            x = U;
                                            w[W2[74]][v1] = x;
                                            v3 = w[W2[78]];
                                            v3:AddOption(U);
                                            return; 
                                        end;
                                        W2[79] = function(arg1_155, ...)
                                            local R = {
                                                W2[74],
                                                W2[78]
                                            };
                                            v1 = arg1_155;
                                            if w[W2[74]][v1] then
                                                v5 = w[W2[78]];
                                                v5:RemoveOption(w[W2[74]][v1]);
                                                w[W2[74]][v1] = nil;
                                            end;
                                            return; 
                                        end;
                                        W2[81] = "pairs";
                                        W2[80] = Env[W2[81]];
                                        W2[85] = Env[W2[86]];
                                        W2[87] = r3;
                                        W2[88] = r2;
                                        W2[89] = W2[88](W2[90], W2[91]);
                                        W2[86] = W2[87][W2[89]];
                                        W2[84] = W2[85][W2[86]];
                                        W2[86] = "GetChildren";
                                        W2[86] = W2[84][W2[86]];
                                        W2[85] = {
                                            W2[86](W2[84])
                                        };
                                        W2[84] = {
                                            W2[80](C(W2[85]))
                                        };
                                        W2[83] = W2[84][3];
                                        W2[82] = W2[84][2];
                                        W2[81] = W2[84][1];
                                        W2[83], W2[84] = W2[81](W2[82], W2[83]);
                                        while W2[83] do
                                            W2[85] = W2[67](W2[84]);
                                            W2[84] = nil;
                                            W2[80] = W2[83];
                                            W2[80] = nil; 
                                        end;
                                        W2[87] = "\xf9\xee\xf2\xc2\xe4";
                                        W2[88] = 17341140131723;
                                        W2[83] = "workspace";
                                        W2[82] = Env[W2[83]];
                                        W2[84] = r3;
                                        W2[85] = r2;
                                        W2[86] = W2[85](W2[87], W2[88]);
                                        W2[83] = W2[84][W2[86]];
                                        W2[81] = W2[82][W2[83]];
                                        W2[87] = 34312436498025;
                                        W2[86] = "_')\x8f\xb2\x06\xe4\xb2=\x8c";
                                        W2[83] = r3;
                                        W2[84] = r2;
                                        W2[85] = W2[84](W2[86], W2[87]);
                                        W2[88] = 15298392726483;
                                        W2[82] = W2[83][W2[85]];
                                        W2[80] = W2[81][W2[82]];
                                        W2[81] = "Connect";
                                        W2[81] = W2[80][W2[81]];
                                        W2[87] = "H\xb6\x94\xac\x02";
                                        W2[83] = "workspace";
                                        W2[81] = W2[81](W2[80], W2[67]);
                                        W2[82] = Env[W2[83]];
                                        W2[84] = r3;
                                        W2[85] = r2;
                                        W2[86] = W2[85](W2[87], W2[88]);
                                        W2[83] = W2[84][W2[86]];
                                        W2[87] = 5037527861545;
                                        W2[81] = W2[82][W2[83]];
                                        W2[83] = r3;
                                        W2[86] = "1\xe0\xaf\xf9\x02\x05\x16\xd4[\xed0\xda";
                                        W2[88] = 14317418977803;
                                        W2[84] = r2;
                                        W2[85] = W2[84](W2[86], W2[87]);
                                        W2[82] = W2[83][W2[85]];
                                        W2[80] = W2[81][W2[82]];
                                        W2[81] = "Connect";
                                        W2[83] = "workspace";
                                        W2[81] = W2[80][W2[81]];
                                        W2[87] = "\xc0u\xce";
                                        W2[81] = W2[81](W2[80], W2[79]);
                                        W2[82] = Env[W2[83]];
                                        W2[84] = r3;
                                        W2[85] = r2;
                                        W2[86] = W2[85](W2[87], W2[88]);
                                        W2[83] = W2[84][W2[86]];
                                        W2[81] = W2[82][W2[83]];
                                        W2[87] = 8951548350536;
                                        W2[83] = r3;
                                        W2[84] = r2;
                                        W2[86] = "\xbc\xa6\xf5#";
                                        W2[85] = W2[84](W2[86], W2[87]);
                                        W2[82] = W2[83][W2[85]];
                                        W2[80] = W2[81][W2[82]];
                                        W2[83] = r3;
                                        W2[84] = r2;
                                        W2[86] = "V\xff\x0b\xe5En\x19\x0e\x90`\xc2\xa1eRI\xc3";
                                        W2[87] = 17730128109632;
                                        W2[81] = "FindFirstChild";
                                        W2[85] = W2[84](W2[86], W2[87]);
                                        W2[81] = W2[80][W2[81]];
                                        W2[82] = W2[83][W2[85]];
                                        W2[81] = W2[81](W2[80], W2[82]);
                                        if W2[81] then
                                            W2[82] = 263;
                                            W2[88] = 2114863367128;
                                            W2[80] = nil;
                                            W2[81] = 264;
                                            w[W2[81]] = W2[80];
                                            W2[87] = "c\x11\x9b\x16\x8a\x10j\x93\xf3 \xa1\x8dr\xb3";
                                            W2[80] = false;
                                            w[W2[82]] = W2[80];
                                            W2[84] = r3;
                                            W2[85] = r2;
                                            W2[86] = W2[85](W2[87], W2[88]);
                                            W2[83] = W2[84][W2[86]];
                                            W2[85] = function(arg1_156, ...)
                                                local R = {
                                                    W2[82],
                                                    212,
                                                    210,
                                                    160,
                                                    W2[81]
                                                };
                                                w[W2[82]] = arg1_156;
                                                v3 = w[W2[82]];
                                                if v3 then
                                                    U = game;
                                                    v3 = U:GetService("RunService").Heartbeat;
                                                    w[W2[81]] = v3:Connect(function(...)
                                                        local R = {
                                                            212,
                                                            210,
                                                            160
                                                        };
                                                        v5 = game.Players.LocalPlayer.Character.SetAssets;
                                                        if v5:FindFirstChild("RealKnife") then
                                                            return;
                                                        end;
                                                        v5 = workspace.Map.Core;
                                                        v3 = v5:FindFirstChild("CollabEventPlace");
                                                        v1 = v3:FindFirstChild("KnifeSpawner");
                                                        U = v1:FindFirstChildOfClass("ProximityPrompt");
                                                        if U then
                                                            v3 = U.Enabled;
                                                        end;
                                                        if U then
                                                            r2(v1.CFrame);
                                                            fireproximityprompt(U);
                                                        end;
                                                        return; 
                                                    end);
                                                else
                                                    v3 = w[W2[81]];
                                                    v3:Disconnect();
                                                end;
                                                return; 
                                            end;
                                            W2[84] = false;
                                            W2[80] = "AddToggle";
                                            W2[81] = nil;
                                            W2[80] = SA[W2[80]];
                                            W2[80] = W2[80](SA, W2[83], W2[84], W2[85]);
                                            W2[82] = nil;
                                        end;
                                        W2[87] = "\x97[\x82";
                                        W2[83] = "workspace";
                                        W2[82] = Env[W2[83]];
                                        W2[88] = 16530763439633;
                                        W2[84] = r3;
                                        W2[85] = r2;
                                        W2[86] = W2[85](W2[87], W2[88]);
                                        W2[83] = W2[84][W2[86]];
                                        W2[86] = "\xce\xf4\xcd\x0f";
                                        W2[81] = W2[82][W2[83]];
                                        W2[83] = r3;
                                        W2[84] = r2;
                                        W2[87] = 27577935508009;
                                        W2[85] = W2[84](W2[86], W2[87]);
                                        W2[82] = W2[83][W2[85]];
                                        W2[80] = W2[81][W2[82]];
                                        W2[81] = "FindFirstChild";
                                        W2[83] = r3;
                                        W2[86] = "$\x97\xfa\x99\xf0\x19\xa1}\x16";
                                        W2[84] = r2;
                                        W2[87] = 8576041176985;
                                        W2[85] = W2[84](W2[86], W2[87]);
                                        W2[81] = W2[80][W2[81]];
                                        W2[82] = W2[83][W2[85]];
                                        W2[81] = W2[81](W2[80], W2[82]);
                                        if W2[81] then
                                            W2[82] = r3;
                                            W2[85] = "\xac\xad\x97\x14\xa9!\xb1\xf4";
                                            W2[86] = 28270361113452;
                                            W2[83] = r2;
                                            W2[84] = W2[83](W2[85], W2[86]);
                                            W2[81] = W2[82][W2[84]];
                                            W2[80] = "AddButton";
                                            W2[80] = SA[W2[80]];
                                            W2[82] = function(...)
                                                local R = {
                                                    212,
                                                    210,
                                                    159
                                                };
                                                v3 = game;
                                                v5 = v3:GetService("RunService").Heartbeat;
                                                r163 = v5:Connect(function(...)
                                                    local R = {
                                                        159,
                                                        212,
                                                        210,
                                                        123
                                                    };
                                                    r3(workspace.Map.Core.SnowPiles.Snow.CFrame);
                                                    v1 = workspace.Map.Core.SnowPiles.Snow;
                                                    fireproximityprompt(v1:FindFirstChildOfClass("ProximityPrompt"));
                                                    v5 = game.Players.LocalPlayer.Character.SetAssets;
                                                    if v5:FindFirstChild("Snowball") then
                                                        v5 = r163;
                                                        v5:Disconnect();
                                                    end;
                                                    return; 
                                                end);
                                                return; 
                                            end;
                                            W2[80] = W2[80](SA, W2[81], W2[82]);
                                        end;
                                        W2[105] = 31195974416574;
                                        W2[82] = r3;
                                        W2[83] = r2;
                                        W2[85] = "\xba\xa8\x99k\xad\x04\x01\x9e\xeb\x08\xf8\xc5\xb6W";
                                        W2[111] = 17233004896088;
                                        W2[86] = 32032149584452;
                                        W2[141] = 1711844131613;
                                        W2[84] = W2[83](W2[85], W2[86]);
                                        W2[80] = "AddSection";
                                        W2[86] = 225;
                                        W2[80] = SA[W2[80]];
                                        W2[173] = 33258628611199;
                                        W2[143] = 20473137603901;
                                        W2[133] = 31334044694783;
                                        W2[101] = 30341026871088;
                                        W2[81] = W2[82][W2[84]];
                                        W2[153] = 11275595420802;
                                        W2[85] = 226;
                                        W2[80] = W2[80](SA, W2[81]);
                                        W2[80] = {};
                                        W2[84] = 227;
                                        W2[118] = "U\xb5\r\xede";
                                        W2[82] = false;
                                        W2[83] = 228;
                                        w[W2[83]] = W2[82];
                                        W2[93] = "game";
                                        W2[82] = false;
                                        W2[99] = 27704699941477;
                                        W2[81] = nil;
                                        w[W2[84]] = W2[82];
                                        W2[128] = "i\xd0W\xcf\x8e\xd5u\x84\x99";
                                        W2[82] = {};
                                        W2[98] = 32885663546321;
                                        W2[97] = "}\x19\x88\xaa\x1ar\xe5";
                                        w[W2[85]] = W2[82];
                                        W2[82] = {};
                                        W2[87] = 229;
                                        w[W2[86]] = W2[82];
                                        W2[82] = nil;
                                        W2[127] = 2775406413068;
                                        w[W2[87]] = W2[82];
                                        W2[92] = Env[W2[93]];
                                        W2[94] = r3;
                                        W2[158] = "\xd3\x1a\xb2\x14\x86\ne\x9b\xf0\x98\x92";
                                        W2[95] = r2;
                                        W2[96] = W2[95](W2[97], W2[98]);
                                        W2[93] = W2[94][W2[96]];
                                        W2[159] = 32730105985929;
                                        W2[97] = 30696638019542;
                                        W2[91] = W2[92][W2[93]];
                                        W2[93] = r3;
                                        W2[169] = 21914137241564;
                                        W2[94] = r2;
                                        W2[96] = "\r\x1a\n\xa0\xa9^\xfbaV\xb8\xfc";
                                        W2[95] = W2[94](W2[96], W2[97]);
                                        W2[92] = W2[93][W2[95]];
                                        W2[102] = "E\xc4?\x04\xe83\xa8\x1a\xac\x94c";
                                        W2[90] = W2[91][W2[92]];
                                        W2[92] = r3;
                                        W2[95] = "\xca\xd1\x17\x81\xc7\xcf\xe0\x7ff";
                                        W2[93] = r2;
                                        W2[96] = 12421372892824;
                                        W2[94] = W2[93](W2[95], W2[96]);
                                        W2[145] = 34520925421259;
                                        W2[91] = W2[92][W2[94]];
                                        W2[161] = 20014021403751;
                                        W2[131] = 32452301683463;
                                        W2[89] = W2[90][W2[91]];
                                        W2[97] = "\x15m\x0f/\xa2\xe0";
                                        W2[94] = "\x1cfI\xf9\xfa\xe6";
                                        W2[91] = r3;
                                        W2[92] = r2;
                                        W2[95] = 22747032971616;
                                        W2[144] = "h=\xe0\xb5i\xc5\x12D";
                                        W2[93] = W2[92](W2[94], W2[95]);
                                        W2[90] = W2[91][W2[93]];
                                        W2[88] = W2[89][W2[90]];
                                        W2[90] = r3;
                                        W2[168] = "3\xe2 X\xa1b\xb5\x90";
                                        W2[123] = 13682216638691;
                                        W2[93] = "\x01e\xfc\x91D";
                                        W2[91] = r2;
                                        W2[94] = 28558638281714;
                                        W2[147] = 5877901642417;
                                        W2[92] = W2[91](W2[93], W2[94]);
                                        W2[89] = W2[90][W2[92]];
                                        W2[98] = 3337222293010;
                                        W2[125] = 9705268695463;
                                        W2[136] = ">\xdf\xfb";
                                        W2[138] = "\x9b'n\xbf\xf3\xa0f.r\xac\xecM\xdd\x98\xbd";
                                        W2[82] = W2[88][W2[89]];
                                        W2[129] = 26103589531515;
                                        W2[100] = "\x9c\xf2\xa2\x8ed\x0c\r\xff\x9a\xacKR";
                                        W2[88] = 230;
                                        w[W2[88]] = W2[82];
                                        W2[93] = "\x9c\xec\xa1\\\xd4h";
                                        W2[112] = "\xba\xe2\xd8\xe8";
                                        W2[94] = 15202610371495;
                                        W2[109] = 22747733764448;
                                        W2[90] = r3;
                                        W2[91] = r2;
                                        W2[151] = 22126753949759;
                                        W2[92] = W2[91](W2[93], W2[94]);
                                        W2[89] = W2[90][W2[92]];
                                        W2[119] = 12003977254357;
                                        W2[92] = false;
                                        W2[122] = "\x91\xadK\x08\xb7";
                                        W2[165] = 15171081870232;
                                        W2[120] = "\xd1\x03";
                                        W2[90] = w[W2[85]];
                                        W2[82] = "AddDropdown";
                                        W2[82] = SA[W2[82]];
                                        W2[91] = function(arg1_157, ...)
                                            local R = {
                                                W2[86],
                                                W2[87]
                                            };
                                            w[W2[87]] = w[W2[86]][arg1_157];
                                            return; 
                                        end;
                                        W2[94] = r3;
                                        W2[95] = r2;
                                        W2[96] = W2[95](W2[97], W2[98]);
                                        W2[93] = W2[94][W2[96]];
                                        W2[82] = W2[82](SA, W2[89], W2[90], W2[91], W2[92], W2[93]);
                                        W2[89] = 231;
                                        W2[97] = 5396658653649;
                                        W2[114] = "Hh\xdah\x97";
                                        W2[90] = 232;
                                        W2[96] = "D \xab@\t\xe8S\xa4^";
                                        W2[98] = "\n\xa7\x1a\xa3\xaa\xf5V\xfe\x98\x97\xc5P\xde\xfe";
                                        w[W2[89]] = W2[82];
                                        W2[155] = 27493693567490;
                                        W2[82] = {};
                                        W2[130] = "_\x92\x11";
                                        W2[140] = "\xf65x\x8aB\xf0\x7f\x1d\x19\x9b+zv\xeb";
                                        w[W2[90]] = W2[82];
                                        W2[91] = r38;
                                        W2[93] = r3;
                                        W2[94] = r2;
                                        W2[157] = 31536149444957;
                                        W2[95] = W2[94](W2[96], W2[97]);
                                        W2[110] = "e#\xd6[%\xc0\x90W";
                                        W2[92] = W2[93][W2[95]];
                                        W2[82] = W2[91][W2[92]];
                                        W2[91] = "Connect";
                                        W2[142] = "\x97\xff\xa4\xa7\xc7S\xa0\x98";
                                        W2[104] = "\"\xef\xb0sL\x0f\x88\xe9c\xb5Y";
                                        W2[135] = 6121827814178;
                                        W2[92] = function(...)
                                            local R = {
                                                W2[88],
                                                212,
                                                210,
                                                W2[90],
                                                W2[89],
                                                W2[86],
                                                W2[85]
                                            };
                                            x = w[W2[88]];
                                            v1 = x[2];
                                            x = x[1];
                                            for U, j in ipairs(x:GetChildren()) do
                                                q = U;
                                                if string.find(j.Name, "Page") then
                                                    t = j.GetChildren;
                                                    v2 = t[2];
                                                    v4 = t[1];
                                                    for v7, t in ipairs(t(j)) do
                                                        r = v7;
                                                        if t:FindFirstChild("EmoteName") then
                                                            U, j = x(v1, U);
                                                            if U then
                                                                q = U;
                                                                v5 = j:FindFirstChild("Door");
                                                                r164 = v5;
                                                                v7 = r164;
                                                                v2 = v7;
                                                                if v7 then
                                                                    v7 = r164;
                                                                    v2 = v7:IsA("BasePart");
                                                                end;
                                                                if v2 then
                                                                    v5 = r164.Handle.Attachment;
                                                                    v2 = v5:FindFirstChildOfClass("ProximityPrompt");
                                                                    if v2 then
                                                                        v7 = v2.Enabled;
                                                                    end;
                                                                    if v2 then
                                                                        if not r2[j] then
                                                                            r = game;
                                                                            v5 = r:GetService("RunService").Heartbeat;
                                                                            v7 = v5:Connect(function(...)
                                                                                local R = {
                                                                                    W2[90],
                                                                                    119,
                                                                                    W2[88],
                                                                                    212
                                                                                };
                                                                                w[W2[88]](r3.CFrame);
                                                                                return; 
                                                                            end);
                                                                            task.wait(.8);
                                                                            v7:Disconnect();
                                                                            task.wait();
                                                                            fireproximityprompt(v5:FindFirstChildOfClass(r[v6]));
                                                                            r2[j] = true;
                                                                        end;
                                                                    else
                                                                        if r2[j] then
                                                                            r2[j] = nil;
                                                                        end;
                                                                    end;
                                                                end;
                                                            end;
                                                            return;
                                                        else
                                                            
                                                        end; 
                                                    end;
                                                end; 
                                            end;
                                            return; 
                                        end;
                                        W2[93] = 1.0519943238084e+14;
                                        W2[121] = 7263140498742;
                                        W2[91] = W2[82][W2[91]];
                                        W2[108] = "\xae\xabhJ\xad\xfd2Z\x8a\xae\xe5\xe0\xc9\x8et\xdf[\xdf\x88";
                                        W2[91] = W2[91](W2[82], W2[92]);
                                        W2[82] = {};
                                        W2[91] = 233;
                                        w[W2[91]] = W2[82];
                                        W2[82] = nil;
                                        W2[92] = 234;
                                        w[W2[92]] = W2[82];
                                        W2[95] = r3;
                                        W2[96] = r2;
                                        W2[154] = "\x0bD\x88r\xe8\xa3\xcf\x8b\xf9\xc9s\xad\x0b\xeb";
                                        W2[97] = W2[96](W2[98], W2[99]);
                                        W2[163] = 26692804227213;
                                        W2[94] = W2[95][W2[97]];
                                        W2[103] = 17625347989519;
                                        W2[116] = "!\x98$\xb1?vu\x9c\x00\x7f";
                                        W2[95] = 18680487885;
                                        W2[97] = r3;
                                        W2[115] = 4211099715496;
                                        W2[98] = r2;
                                        W2[99] = W2[98](W2[100], W2[101]);
                                        W2[139] = 1546331259600;
                                        W2[146] = "K\x14\xe2m\xe1\xb2\xec\xde\xd0";
                                        W2[96] = W2[97][W2[99]];
                                        W2[107] = 30405705119566;
                                        W2[99] = r3;
                                        W2[97] = 18257697094;
                                        W2[100] = r2;
                                        W2[101] = W2[100](W2[102], W2[103]);
                                        W2[98] = W2[99][W2[101]];
                                        W2[156] = "#3\x16\x98\xa7";
                                        W2[162] = "\x1bE\xee\xfc\xa1?\r\x89\x10\xab\xd6";
                                        W2[101] = r3;
                                        W2[102] = r2;
                                        W2[99] = 1.2962247497973e+14;
                                        W2[164] = "\x85l\xb0\xfd\x81\xad\xad\xd6[\xcc\xfa\x0fH\xc4\xd4\xf1\xe8\x0b\xd0";
                                        W2[103] = W2[102](W2[104], W2[105]);
                                        W2[100] = W2[101][W2[103]];
                                        W2[106] = "\xd6G\x17T,\t6o1\xcd<\xb2\xcb2\xcd\x03\xcc\xf9\xfe";
                                        W2[101] = 71411567772779;
                                        W2[103] = r3;
                                        W2[104] = r2;
                                        W2[124] = "\x7fd14\x87 \x90I";
                                        W2[132] = "\xaf\x1eC\x18\x8a\x12Y\xfc%";
                                        W2[171] = 2734443529465;
                                        W2[105] = W2[104](W2[106], W2[107]);
                                        W2[113] = 32585246751557;
                                        W2[102] = W2[103][W2[105]];
                                        W2[103] = 7061193663;
                                        W2[105] = r3;
                                        W2[106] = r2;
                                        W2[107] = W2[106](W2[108], W2[109]);
                                        W2[104] = W2[105][W2[107]];
                                        W2[105] = 7948969023;
                                        W2[107] = r3;
                                        W2[108] = r2;
                                        W2[109] = W2[108](W2[110], W2[111]);
                                        W2[106] = W2[107][W2[109]];
                                        W2[107] = 7061369096;
                                        W2[134] = "\x1f\xfc\xb1\xee\xd3\xea\xf7u\x158\xbb";
                                        W2[109] = r3;
                                        W2[110] = r2;
                                        W2[111] = W2[110](W2[112], W2[113]);
                                        W2[108] = W2[109][W2[111]];
                                        W2[109] = 1.3731887940297e+14;
                                        W2[167] = 16025623715110;
                                        W2[111] = r3;
                                        W2[126] = "\xccSG\xf6\x91\x8c\xaa\xe1\xe7|\xd2";
                                        W2[112] = r2;
                                        W2[113] = W2[112](W2[114], W2[115]);
                                        W2[170] = "\xcc4\xf8\x7f\xac\xafW";
                                        W2[110] = W2[111][W2[113]];
                                        W2[117] = 16834439159455;
                                        W2[113] = r3;
                                        W2[111] = 99137255050147;
                                        W2[114] = r2;
                                        W2[115] = W2[114](W2[116], W2[117]);
                                        W2[148] = "] \x11\x1f\xbe\x87\xee[\xa8\x15\x9c\x87\xdd\x96";
                                        W2[112] = W2[113][W2[115]];
                                        W2[115] = r3;
                                        W2[113] = 18319797565;
                                        W2[116] = r2;
                                        W2[117] = W2[116](W2[118], W2[119]);
                                        W2[114] = W2[115][W2[117]];
                                        W2[117] = r3;
                                        W2[115] = 18370175258;
                                        W2[118] = r2;
                                        W2[119] = W2[118](W2[120], W2[121]);
                                        W2[116] = W2[117][W2[119]];
                                        W2[119] = r3;
                                        W2[120] = r2;
                                        W2[121] = W2[120](W2[122], W2[123]);
                                        W2[118] = W2[119][W2[121]];
                                        W2[121] = r3;
                                        W2[119] = 89667437228243;
                                        W2[122] = r2;
                                        W2[123] = W2[122](W2[124], W2[125]);
                                        W2[120] = W2[121][W2[123]];
                                        W2[121] = 15917626934;
                                        W2[117] = 97871211303571;
                                        W2[123] = r3;
                                        W2[124] = r2;
                                        W2[125] = W2[124](W2[126], W2[127]);
                                        W2[122] = W2[123][W2[125]];
                                        W2[125] = r3;
                                        W2[123] = 15753185070;
                                        W2[126] = r2;
                                        W2[127] = W2[126](W2[128], W2[129]);
                                        W2[124] = W2[125][W2[127]];
                                        W2[125] = 16363777391;
                                        W2[127] = r3;
                                        W2[128] = r2;
                                        W2[129] = W2[128](W2[130], W2[131]);
                                        W2[126] = W2[127][W2[129]];
                                        W2[127] = 18246120711;
                                        W2[129] = r3;
                                        W2[149] = 33427112344781;
                                        W2[130] = r2;
                                        W2[131] = W2[130](W2[132], W2[133]);
                                        W2[128] = W2[129][W2[131]];
                                        W2[129] = 10173613362;
                                        W2[131] = r3;
                                        W2[132] = r2;
                                        W2[133] = W2[132](W2[134], W2[135]);
                                        W2[130] = W2[131][W2[133]];
                                        W2[131] = 12917642257;
                                        W2[133] = r3;
                                        W2[137] = 605151871257;
                                        W2[134] = r2;
                                        W2[135] = W2[134](W2[136], W2[137]);
                                        W2[132] = W2[133][W2[135]];
                                        W2[133] = 82476745705122;
                                        W2[135] = r3;
                                        W2[136] = r2;
                                        W2[137] = W2[136](W2[138], W2[139]);
                                        W2[134] = W2[135][W2[137]];
                                        W2[137] = r3;
                                        W2[135] = 6265242673;
                                        W2[138] = r2;
                                        W2[139] = W2[138](W2[140], W2[141]);
                                        W2[136] = W2[137][W2[139]];
                                        W2[160] = "\xd0\xa7\x9d\x9a\xc5\x8d\x1c\x1e\x1a\x81\x9d\x9d\x0c";
                                        W2[139] = r3;
                                        W2[137] = 16159090773;
                                        W2[140] = r2;
                                        W2[141] = W2[140](W2[142], W2[143]);
                                        W2[138] = W2[139][W2[141]];
                                        W2[139] = 7061190867;
                                        W2[141] = r3;
                                        W2[142] = r2;
                                        W2[150] = "\xeac\x99p\x19g7\xc4\xaada6h\xe04";
                                        W2[143] = W2[142](W2[144], W2[145]);
                                        W2[152] = "\x08\xc2\x8et!\x1c\x03O\x95i\x10WG\xca\x96\x0c\x0fK";
                                        W2[140] = W2[141][W2[143]];
                                        W2[141] = 1.125997029849e+14;
                                        W2[143] = r3;
                                        W2[144] = r2;
                                        W2[145] = W2[144](W2[146], W2[147]);
                                        W2[142] = W2[143][W2[145]];
                                        W2[143] = 6743603446;
                                        W2[145] = r3;
                                        W2[146] = r2;
                                        W2[147] = W2[146](W2[148], W2[149]);
                                        W2[144] = W2[145][W2[147]];
                                        W2[147] = r3;
                                        W2[148] = r2;
                                        W2[172] = "\x04\x96\xf6\x05e\x86\x8a`>\xc9\x1f;HXy\x7f\x10\xf6\xb9\x88\x7f";
                                        W2[145] = 1.2875561090062e+14;
                                        W2[149] = W2[148](W2[150], W2[151]);
                                        W2[146] = W2[147][W2[149]];
                                        W2[147] = 1.3633565459454e+14;
                                        W2[149] = r3;
                                        W2[150] = r2;
                                        W2[151] = W2[150](W2[152], W2[153]);
                                        W2[148] = W2[149][W2[151]];
                                        W2[149] = 1.3137118313081e+14;
                                        W2[151] = r3;
                                        W2[152] = r2;
                                        W2[153] = W2[152](W2[154], W2[155]);
                                        W2[150] = W2[151][W2[153]];
                                        W2[151] = 13997948756;
                                        W2[153] = r3;
                                        W2[154] = r2;
                                        W2[155] = W2[154](W2[156], W2[157]);
                                        W2[152] = W2[153][W2[155]];
                                        W2[155] = r3;
                                        W2[156] = r2;
                                        W2[153] = 1.0044597100273e+14;
                                        W2[157] = W2[156](W2[158], W2[159]);
                                        W2[154] = W2[155][W2[157]];
                                        W2[155] = 5775509840;
                                        W2[157] = r3;
                                        W2[158] = r2;
                                        W2[159] = W2[158](W2[160], W2[161]);
                                        W2[156] = W2[157][W2[159]];
                                        W2[157] = 18976119144;
                                        W2[159] = r3;
                                        W2[160] = r2;
                                        W2[161] = W2[160](W2[162], W2[163]);
                                        W2[158] = W2[159][W2[161]];
                                        W2[161] = r3;
                                        W2[166] = "\xeb8Q\xa7\xaf\xe7\xab\xb0\xfc&\x9aO";
                                        W2[162] = r2;
                                        W2[159] = 96326653225562;
                                        W2[163] = W2[162](W2[164], W2[165]);
                                        W2[160] = W2[161][W2[163]];
                                        W2[161] = 78044670447386;
                                        W2[163] = r3;
                                        W2[164] = r2;
                                        W2[165] = W2[164](W2[166], W2[167]);
                                        W2[162] = W2[163][W2[165]];
                                        W2[165] = r3;
                                        W2[166] = r2;
                                        W2[163] = 1.0675544856695e+14;
                                        W2[167] = W2[166](W2[168], W2[169]);
                                        W2[164] = W2[165][W2[167]];
                                        W2[165] = 1.0890729611703e+14;
                                        W2[167] = r3;
                                        W2[168] = r2;
                                        W2[169] = W2[168](W2[170], W2[171]);
                                        W2[166] = W2[167][W2[169]];
                                        W2[167] = 1.3471968913407e+14;
                                        W2[169] = r3;
                                        W2[170] = r2;
                                        W2[171] = W2[170](W2[172], W2[173]);
                                        W2[168] = W2[169][W2[171]];
                                        W2[82] = {
                                            [W2[93]] = W2[94],
                                            [W2[95]] = W2[96],
                                            [W2[97]] = W2[98],
                                            [W2[99]] = W2[100],
                                            [W2[101]] = W2[102],
                                            [W2[103]] = W2[104],
                                            [W2[105]] = W2[106],
                                            [W2[107]] = W2[108],
                                            [W2[109]] = W2[110],
                                            [W2[111]] = W2[112],
                                            [W2[113]] = W2[114],
                                            [W2[115]] = W2[116],
                                            [W2[117]] = W2[118],
                                            [W2[119]] = W2[120],
                                            [W2[121]] = W2[122],
                                            [W2[123]] = W2[124],
                                            [W2[125]] = W2[126],
                                            [W2[127]] = W2[128],
                                            [W2[129]] = W2[130],
                                            [W2[131]] = W2[132],
                                            [W2[133]] = W2[134],
                                            [W2[135]] = W2[136],
                                            [W2[137]] = W2[138],
                                            [W2[139]] = W2[140],
                                            [W2[141]] = W2[142],
                                            [W2[143]] = W2[144],
                                            [W2[145]] = W2[146],
                                            [W2[147]] = W2[148],
                                            [W2[149]] = W2[150],
                                            [W2[151]] = W2[152],
                                            [W2[153]] = W2[154],
                                            [W2[155]] = W2[156],
                                            [W2[157]] = W2[158],
                                            [W2[159]] = W2[160],
                                            [W2[161]] = W2[162],
                                            [W2[163]] = W2[164],
                                            [W2[165]] = W2[166],
                                            [W2[167]] = W2[168]
                                        };
                                        W2[94] = "pairs";
                                        W2[93] = Env[W2[94]];
                                        W2[97] = {
                                            W2[93](W2[82])
                                        };
                                        W2[96] = W2[97][3];
                                        W2[95] = W2[97][2];
                                        W2[94] = W2[97][1];
                                        W2[96], W2[97] = W2[94](W2[95], W2[96]);
                                        while W2[96] do
                                            W2[108] = 14908695665438;
                                            W2[93] = W2[96];
                                            W2[105] = 19315011887906;
                                            W2[100] = "table";
                                            W2[104] = "J\xbf\xf1\x98\rw";
                                            W2[99] = Env[W2[100]];
                                            W2[101] = r3;
                                            W2[102] = r2;
                                            W2[103] = W2[102](W2[104], W2[105]);
                                            W2[107] = 6945543244962;
                                            W2[100] = W2[101][W2[103]];
                                            W2[98] = W2[99][W2[100]];
                                            W2[100] = w[W2[91]];
                                            W2[103] = r3;
                                            W2[106] = "\x97p@\x89";
                                            W2[104] = r2;
                                            W2[105] = W2[104](W2[106], W2[107]);
                                            W2[102] = W2[103][W2[105]];
                                            W2[104] = r3;
                                            W2[105] = r2;
                                            W2[107] = "y\xa4";
                                            W2[106] = W2[105](W2[107], W2[108]);
                                            W2[103] = W2[104][W2[106]];
                                            W2[101] = {
                                                [W2[102]] = W2[97],
                                                [W2[103]] = W2[93]
                                            };
                                            W2[93] = nil;
                                            W2[99] = W2[98](W2[100], W2[101]);
                                            W2[97] = nil; 
                                        end;
                                        W2[103] = 19510129746813;
                                        W2[98] = "\x0e6\xe9\r\x0c\xe8G\xdc\xcb\xa0";
                                        W2[95] = r3;
                                        W2[93] = "AddDropdown";
                                        W2[99] = 31318989142264;
                                        W2[96] = r2;
                                        W2[102] = "\xf7\xfd~\xab\x7f\xe3";
                                        W2[97] = W2[96](W2[98], W2[99]);
                                        W2[94] = W2[95][W2[97]];
                                        W2[95] = function(...)
                                            local R = {
                                                W2[91],
                                                212,
                                                210
                                            };
                                            v1 = {};
                                            q = w[W2[91]];
                                            x = 303[3];
                                            q = 303[1];
                                            for x, v4 in q, ipairs(q) do
                                                table.insert(v1, v4.Name); 
                                            end;
                                            return v1; 
                                        end;
                                        W2[96] = W2[95]();
                                        W2[97] = false;
                                        W2[93] = SA[W2[93]];
                                        W2[95] = function(arg1_158, ...)
                                            local R = {
                                                W2[91],
                                                212,
                                                210,
                                                W2[92]
                                            };
                                            q = w[W2[91]];
                                            U = 303[2];
                                            q = 303[1];
                                            for x, v4 in ipairs(q) do
                                                j = x;
                                                if v4.Name == arg1_158 then
                                                    w[W2[92]] = v4.Id;
                                                    break;
                                                else
                                                    
                                                end; 
                                            end;
                                            return; 
                                        end;
                                        W2[99] = r3;
                                        W2[100] = r2;
                                        W2[101] = W2[100](W2[102], W2[103]);
                                        W2[98] = W2[99][W2[101]];
                                        W2[93] = W2[93](SA, W2[94], W2[96], W2[95], W2[97], W2[98]);
                                        W2[95] = r3;
                                        W2[93] = "AddToggle";
                                        W2[96] = r2;
                                        W2[98] = "\xd9\xeb?\xf7p\xc3\x155\x02";
                                        W2[99] = 3107815327143;
                                        W2[97] = W2[96](W2[98], W2[99]);
                                        W2[96] = function(arg1_159, ...)
                                            local R = {
                                                W2[83],
                                                W2[92],
                                                212,
                                                210
                                            };
                                            v5 = arg1_159;
                                            w[W2[83]] = v5;
                                            x = w[W2[83]];
                                            U = v5;
                                            if x then
                                                v3 = w[W2[92]];
                                            end;
                                            v5 = U;
                                            if x then
                                                v3 = game;
                                                U = v3:GetService("RunService");
                                                U:BindToRenderStep("Auto-SoundBoard", 0, function(...)
                                                    local R = {
                                                        212,
                                                        210,
                                                        W2[92]
                                                    };
                                                    j = game;
                                                    v5 = j:GetService("ReplicatedStorage").Knit.Knit.Services.JoinService.RE.Talk;
                                                    v5:FireServer(r3);
                                                    return; 
                                                end);
                                            else
                                                v3 = game;
                                                U = v3:GetService("RunService");
                                                U:UnbindFromRenderStep("Auto-SoundBoard");
                                            end;
                                            return; 
                                        end;
                                        W2[93] = SA[W2[93]];
                                        W2[94] = W2[95][W2[97]];
                                        W2[98] = "\xa7C1u\xdd\x92f\x01\x04Q\xf5\xfb\xb9\xcdk\xe1x";
                                        W2[95] = false;
                                        W2[99] = 14738166504142;
                                        W2[93] = W2[93](SA, W2[94], W2[95], W2[96]);
                                        W2[95] = r3;
                                        W2[96] = r2;
                                        W2[97] = W2[96](W2[98], W2[99]);
                                        W2[94] = W2[95][W2[97]];
                                        W2[93] = "AddToggle";
                                        W2[96] = function(arg1_160, ...)
                                            w[W2[84]] = arg1_160;
                                            return; 
                                        end;
                                        W2[97] = "game";
                                        W2[93] = SA[W2[93]];
                                        W2[95] = false;
                                        W2[93] = W2[93](SA, W2[94], W2[95], W2[96]);
                                        W2[96] = Env[W2[97]];
                                        W2[103] = 32495178644251;
                                        W2[99] = r3;
                                        W2[102] = "\x04M\xeeZS\x98\xca";
                                        W2[100] = r2;
                                        W2[101] = W2[100](W2[102], W2[103]);
                                        W2[97] = "GetService";
                                        W2[98] = W2[99][W2[101]];
                                        W2[97] = W2[96][W2[97]];
                                        W2[97] = W2[97](W2[96], W2[98]);
                                        W2[101] = "\x0f7-\xa0\xd0z\x8d\\\xa2\xd2\xe1";
                                        W2[98] = r3;
                                        W2[99] = r2;
                                        W2[102] = 6858660547705;
                                        W2[100] = W2[99](W2[101], W2[102]);
                                        W2[96] = W2[98][W2[100]];
                                        W2[101] = 34752187907894;
                                        W2[95] = W2[97][W2[96]];
                                        W2[102] = 15593439517789;
                                        W2[97] = r3;
                                        W2[100] = "\xbd:\xbap\xd4\xea3\x9d+\xa1\xd0";
                                        W2[98] = r2;
                                        W2[99] = W2[98](W2[100], W2[101]);
                                        W2[96] = W2[97][W2[99]];
                                        W2[100] = 24003610766249;
                                        W2[99] = "\x1dZ\r{\xcc";
                                        W2[94] = W2[95][W2[96]];
                                        W2[96] = r3;
                                        W2[97] = r2;
                                        W2[98] = W2[97](W2[99], W2[100]);
                                        W2[95] = W2[96][W2[98]];
                                        W2[93] = W2[94][W2[95]];
                                        W2[94] = 29;
                                        w[W2[94]] = W2[93];
                                        W2[100] = "\x82\xde\x8c$\xa6";
                                        W2[95] = w[W2[94]];
                                        W2[97] = r3;
                                        W2[101] = 22029742417938;
                                        W2[98] = r2;
                                        W2[99] = W2[98](W2[100], W2[101]);
                                        W2[96] = W2[97][W2[99]];
                                        W2[101] = "\xe9\x0c4\xee5";
                                        W2[93] = W2[95][W2[96]];
                                        W2[95] = 30;
                                        w[W2[95]] = W2[93];
                                        W2[93] = w[W2[94]];
                                        W2[98] = r3;
                                        W2[99] = r2;
                                        W2[96] = "GetPropertyChangedSignal";
                                        W2[100] = W2[99](W2[101], W2[102]);
                                        W2[96] = W2[93][W2[96]];
                                        W2[97] = W2[98][W2[100]];
                                        W2[96] = W2[96](W2[93], W2[97]);
                                        W2[93] = "Connect";
                                        W2[97] = function(...)
                                            local R = {
                                                W2[84],
                                                W2[94],
                                                212,
                                                210,
                                                W2[95],
                                                W2[87],
                                                W2[92]
                                            };
                                            if w[W2[84]] and w[W2[94]].Value > w[W2[95]] then
                                                v5 = w[W2[87]];
                                                if v5 then
                                                    j = game;
                                                    v5 = j:GetService("ReplicatedStorage").Knit.Knit.Services.EmoteService.RE.Emote;
                                                    v5:FireServer(w[W2[87]]);
                                                end;
                                                v5 = w[W2[92]];
                                                if v5 then
                                                    j = game;
                                                    v5 = j:GetService("ReplicatedStorage").Knit.Knit.Services.JoinService.RE.Talk;
                                                    v5:FireServer(w[W2[92]]);
                                                end;
                                            end;
                                            w[W2[95]] = w[W2[94]].Value;
                                            return; 
                                        end;
                                        W2[93] = W2[96][W2[93]];
                                        W2[93] = W2[93](W2[96], W2[97]);
                                        W2[93] = vA();
                                        if W2[93] then
                                            W2[106] = 17273790865259;
                                            W2[101] = 20347615683843;
                                            W2[96] = "_G";
                                            W2[93] = Env[W2[96]];
                                            W2[97] = r3;
                                            W2[100] = "h\xf8\x1b\xe2\x80M\xc2\x0b\x80\x95~D";
                                            W2[98] = r2;
                                            W2[99] = W2[98](W2[100], W2[101]);
                                            W2[100] = "\xf8\xce2\x0e\xcdf\xe7\x1d\xb9\xaa\x89\xd5";
                                            W2[96] = W2[97][W2[99]];
                                            W2[101] = 24100076727254;
                                            W2[97] = false;
                                            W2[93][W2[96]] = W2[97];
                                            W2[93] = "AddToggle";
                                            W2[97] = r3;
                                            W2[98] = r2;
                                            W2[99] = W2[98](W2[100], W2[101]);
                                            W2[100] = "y\xd1\x1c\xf7\xc9\xd5\xb9\xc5\xc8qqU\x06\xeaG\x0cbnr\"]\xe9f/";
                                            W2[96] = W2[97][W2[99]];
                                            W2[101] = 34364263022210;
                                            W2[98] = function(arg1_161, ...)
                                                local R = {
                                                    212,
                                                    210
                                                };
                                                _G.DOMAIN_CHECK = arg1_161;
                                                return; 
                                            end;
                                            W2[93] = SA[W2[93]];
                                            W2[97] = false;
                                            W2[93] = W2[93](SA, W2[96], W2[97], W2[98]);
                                            W2[97] = r3;
                                            W2[98] = r2;
                                            W2[99] = W2[98](W2[100], W2[101]);
                                            W2[96] = W2[97][W2[99]];
                                            W2[97] = false;
                                            W2[98] = function(arg1_162, ...)
                                                local R = {
                                                    212,
                                                    210
                                                };
                                                if arg1_162 then
                                                    _G.GOJOKILLALL = {};
                                                    local function U(arg1_163, ...)
                                                        local R = {
                                                            212,
                                                            210
                                                        };
                                                        v1 = arg1_163;
                                                        v5 = v1:WaitForChild("Humanoid").AnimationPlayed;
                                                        table.insert(_G.GOJOKILLALL, v5:Connect(function(arg1_164, ...)
                                                            local R = {
                                                                212,
                                                                210
                                                            };
                                                            r165 = arg1_164;
                                                            if r165.Animation and r165.Animation.AnimationId == "rbxassetid://116811846715462" then
                                                                U = r165.IsPlaying;
                                                                v3 = r165.TimePosition < 1.6;
                                                                while not U do
                                                                    if U then
                                                                        task.wait();
                                                                    end;
                                                                    local function r166(...)
                                                                        local R = {
                                                                            212,
                                                                            210
                                                                        };
                                                                        v7 = r2;
                                                                        q = game.Players;
                                                                        U = q[2];
                                                                        q = q[1];
                                                                        for x, v4 in ipairs(q:GetPlayers()) do
                                                                            j = x;
                                                                            t = game.Players;
                                                                            v7 = v4 ~= t.LocalPlayer;
                                                                            if v7 then
                                                                                a = r3;
                                                                                t = v4.Character;
                                                                                if t then
                                                                                    a = v4.Character;
                                                                                    o = a:FindFirstChild("HumanoidRootPart");
                                                                                    if o then
                                                                                        o = v4.Character;
                                                                                        t = not o:GetAttribute("Dead");
                                                                                    end;
                                                                                    v5 = ipairs;
                                                                                    v7 = o;
                                                                                end;
                                                                                v5 = ipairs;
                                                                                v2 = t;
                                                                            end;
                                                                            if v7 then
                                                                                if _G.DOMAIN_CHECK then
                                                                                    if (game.Players.LocalPlayer.Character.HumanoidRootPart.Position - v4.Character.HumanoidRootPart.Position).Magnitude <= 800 then
                                                                                        table.insert({}, v4);
                                                                                    end;
                                                                                else
                                                                                    table.insert({}, v4);
                                                                                end;
                                                                            end; 
                                                                        end;
                                                                        return {}; 
                                                                    end;
                                                                    v5 = #r166() > 0;
                                                                    if v5 then
                                                                        v5 = game.Players.LocalPlayer.Character.Humanoid;
                                                                        v5:Move((game.Players.LocalPlayer.Character.HumanoidRootPart.Position - game.Players.LocalPlayer.Character.HumanoidRootPart.Position).Unit, false);
                                                                    end;
                                                                    task.spawn(function(...)
                                                                        local R = {
                                                                            192,
                                                                            212,
                                                                            210,
                                                                            265
                                                                        };
                                                                        v1 = r3.IsPlaying;
                                                                        v3 = r3.TimePosition < 2.2;
                                                                        while not v1 do
                                                                            if v1 then
                                                                                task.wait();
                                                                            end;
                                                                            while r3.IsPlaying do
                                                                                if #r166() > 0 then
                                                                                    x = v1[math.random(1, #v1)].Character;
                                                                                    q = x.HumanoidRootPart;
                                                                                    j = x:FindFirstChild("Humanoid");
                                                                                    if q then
                                                                                        v3 = v5;
                                                                                    end;
                                                                                    if q then
                                                                                        pcall(function(...)
                                                                                            local R = {
                                                                                                212,
                                                                                                210,
                                                                                                210
                                                                                            };
                                                                                            v5 = r3.TimePosition >= 11.65;
                                                                                            if v5 then
                                                                                                v5 = game.Players.LocalPlayer.Character.Humanoid;
                                                                                                v5:Move((game.Players.LocalPlayer.Character.HumanoidRootPart.Position - game.Players.LocalPlayer.Character.HumanoidRootPart.Position).Unit, false);
                                                                                            end;
                                                                                            return; 
                                                                                        end);
                                                                                        game.Players.LocalPlayer.Character.HumanoidRootPart.CFrame = CFrame.new(q.Position + j.MoveDirection * .8 * j.WalkSpeed - q.CFrame.LookVector * 5, q.Position);
                                                                                    end;
                                                                                    task.wait();
                                                                                end; 
                                                                            end;
                                                                            return; 
                                                                        end;
                                                                        v3 = r3.TimePosition < 2.2; 
                                                                    end);
                                                                    break; 
                                                                end;
                                                                v3 = r165.TimePosition < 1.6;
                                                            end;
                                                            return; 
                                                        end));
                                                        return; 
                                                    end;
                                                    q = game;
                                                    U(q:GetService("Players").LocalPlayer.Character);
                                                    j = game;
                                                    x = j:GetService("Players").LocalPlayer.CharacterAdded;
                                                    _G.GOJOKILLALL_CHARCONN = x:Connect(U);
                                                else
                                                    q = r2;
                                                    j = q("\xa4a\xe8E\x8d\xa2\x94$\x86\xff\xb6", 3862348547846);
                                                    if _G[r3[j]] then
                                                        j = _G;
                                                        q = j.GOJOKILLALL;
                                                        x = j[3];
                                                        q = j[1];
                                                        for x, v4 in q, ipairs(q) do
                                                            j = x;
                                                            r167 = v4;
                                                            if typeof(r167) == "RBXScriptConnection" then
                                                                pcall(function(...)
                                                                    v5 = r167;
                                                                    v5:Disconnect();
                                                                    return; 
                                                                end);
                                                            end; 
                                                        end;
                                                    end;
                                                    if _G.GOJOKILLALL_CHARCONN then
                                                        pcall(function(...)
                                                            local R = {
                                                                212,
                                                                210
                                                            };
                                                            v5 = _G.GOJOKILLALL_CHARCONN;
                                                            v5:Disconnect();
                                                            return; 
                                                        end);
                                                    end;
                                                    return;
                                                end; 
                                            end;
                                            W2[93] = "AddToggle";
                                            W2[93] = SA[W2[93]];
                                            W2[93] = W2[93](SA, W2[96], W2[97], W2[98]);
                                            W2[93] = nil;
                                            W2[96] = 356;
                                            w[W2[96]] = W2[93];
                                            W2[105] = "\xa2\xe8\x8b-)\x06\x00N\x0e\xb0`\xf8";
                                            W2[93] = nil;
                                            W2[99] = 357;
                                            W2[97] = 358;
                                            w[W2[97]] = W2[93];
                                            W2[100] = 359;
                                            W2[98] = 360;
                                            W2[93] = nil;
                                            w[W2[98]] = W2[93];
                                            W2[93] = nil;
                                            w[W2[99]] = W2[93];
                                            W2[93] = nil;
                                            w[W2[100]] = W2[93];
                                            W2[93] = "AddToggle";
                                            W2[102] = r3;
                                            W2[103] = r2;
                                            W2[104] = W2[103](W2[105], W2[106]);
                                            W2[101] = W2[102][W2[104]];
                                            W2[93] = SA[W2[93]];
                                            W2[102] = false;
                                            W2[103] = function(arg1_165, ...)
                                                local R = {
                                                    212,
                                                    210,
                                                    W2[96],
                                                    W2[97],
                                                    W2[99],
                                                    W2[100],
                                                    312,
                                                    163,
                                                    W2[98]
                                                };
                                                r168 = arg1_165;
                                                local function r169(arg1_166, ...)
                                                    local R = {
                                                        212,
                                                        210
                                                    };
                                                    arg1_166.Enabled = false;
                                                    return; 
                                                end;
                                                local function r170(arg1_167, ...)
                                                    local R = {
                                                        212,
                                                        210
                                                    };
                                                    arg1_167.Enabled = true;
                                                    return; 
                                                end;
                                                local function r171(arg1_168, ...)
                                                    local R = {
                                                        212,
                                                        210
                                                    };
                                                    v1 = arg1_168;
                                                    v1.Archivable = true;
                                                    U = v1:Clone();
                                                    U.HumanoidRootPart.Anchored = false;
                                                    U.Humanoid.WalkSpeed = 23;
                                                    v4 = U.GetDescendants;
                                                    j = {
                                                        v4(U)
                                                    };
                                                    x = v4[2];
                                                    j = v4[1];
                                                    for q, v2 in pairs(C(j)) do
                                                        v4 = q;
                                                        if v2:IsA("BasePart") then
                                                            v2.CustomPhysicalProperties = PhysicalProperties.new(100, 2, 0.5, 100, 1);
                                                            v2.CanCollide = false;
                                                            v2.Transparency = 1;
                                                            v7 = v2:FindFirstChildOfClass("Decal");
                                                            if v7 then
                                                                v7.Transparency = 1;
                                                            end;
                                                        else
                                                            if v2:IsA("Humanoid") then
                                                                v2.DisplayDistanceType = Enum.HumanoidDisplayDistanceType.None;
                                                            else
                                                                if v2:IsA("ForceField") then
                                                                    v2:Destroy();
                                                                end;
                                                            end;
                                                        end; 
                                                    end;
                                                    U.Parent = v1;
                                                    U.HumanoidRootPart.CFrame = v1.HumanoidRootPart.CFrame;
                                                    v1.Archivable = false;
                                                    return U; 
                                                end;
                                                local function r172(...)
                                                    local R = {
                                                        W2[96],
                                                        W2[97],
                                                        W2[99],
                                                        W2[100],
                                                        212,
                                                        210,
                                                        240,
                                                        312
                                                    };
                                                    v5 = r3;
                                                    if v5 then
                                                        v5 = r3;
                                                        v5:Disconnect();
                                                    end;
                                                    v5 = r2;
                                                    if v5 then
                                                        v5 = r2;
                                                        v5:Disconnect();
                                                    end;
                                                    v5 = w[W2[96]];
                                                    if v5 then
                                                        v5 = w[W2[96]];
                                                        v5:Disconnect();
                                                    end;
                                                    v5 = w[W2[97]];
                                                    if v5 then
                                                        v5 = w[W2[97]];
                                                        v5:Destroy();
                                                    end;
                                                    x = workspace;
                                                    U = x[3];
                                                    x = x[1];
                                                    for U, j in x, ipairs(x:GetDescendants()) do
                                                        q = U;
                                                        if j:IsA("ProximityPrompt") then
                                                            r170(j);
                                                        end; 
                                                    end;
                                                    v7 = 32164598889089;
                                                    v1 = r38.LocalPlayer.Character;
                                                    v4 = v1.GetDescendants;
                                                    workspace[w[W2[99]][w[W2[100]]("$\xb8\x13\xbb\xd7\xd5k\x9eU\xfe\xf4@\x8e", v7)]].CameraSubject = v1;
                                                    x = v4[2];
                                                    U = v4[1];
                                                    for q, v4 in ipairs(v4(v1)) do
                                                        j = q;
                                                        v7 = v4:IsA("BasePart");
                                                        if v7 then
                                                            v2 = v4.Name ~= "HumanoidRootPart" and v4.Name ~= "Collide";
                                                            v5 = ipairs;
                                                        end;
                                                        if v7 then
                                                            v4.Transparency = 0;
                                                            v4.CanCollide = true;
                                                        else
                                                            if v4:IsA("Decal") then
                                                                v4.Transparency = 0;
                                                            end;
                                                        end; 
                                                    end;
                                                    return; 
                                                end;
                                                local function r174(arg1_169, ...)
                                                    local R = {
                                                        242,
                                                        212,
                                                        210,
                                                        241,
                                                        W2[99],
                                                        243,
                                                        W2[100],
                                                        163,
                                                        W2[96],
                                                        W2[97]
                                                    };
                                                    r173 = arg1_169;
                                                    r3();
                                                    q = workspace;
                                                    U = q[2];
                                                    q = q[1];
                                                    for x, v4 in ipairs(q:GetDescendants()) do
                                                        j = x;
                                                        if v4:IsA("ProximityPrompt") then
                                                            r169(v4);
                                                        end; 
                                                    end;
                                                    v5 = workspace.DescendantAdded;
                                                    w[W2[99]] = v5:Connect(function(arg1_170, ...)
                                                        local R = {
                                                            210,
                                                            W2[96],
                                                            W2[97]
                                                        };
                                                        v1 = arg1_170;
                                                        if v1:IsA("ProximityPrompt") then
                                                            w[W2[96]](v1);
                                                        end;
                                                        return; 
                                                    end);
                                                    v4 = r173;
                                                    v2 = {
                                                        v4:GetDescendants()
                                                    };
                                                    q = v4[2];
                                                    x = v4[1];
                                                    for j, v2 in ipairs(C(v2)) do
                                                        v4 = j;
                                                        if v2:IsA("BasePart") then
                                                            v2.Transparency = 1;
                                                            v2.CanCollide = false;
                                                        else
                                                            if v2:IsA("Decal") then
                                                                v2.Transparency = 1;
                                                            end;
                                                        end; 
                                                    end;
                                                    r79 = w[W2[100]](r173);
                                                    workspace.CurrentCamera.CameraSubject = r79;
                                                    v5 = r38.Stepped;
                                                    w[W2[98]] = v5:Connect(function(...)
                                                        local R = {
                                                            32,
                                                            210,
                                                            W2[96]
                                                        };
                                                        x = r3;
                                                        U = x[3];
                                                        x = x[1];
                                                        for U, j in x, ipairs(x:GetDescendants()) do
                                                            q = U;
                                                            if j:IsA("BasePart") then
                                                                j.CanCollide = false;
                                                            end; 
                                                        end;
                                                        return; 
                                                    end);
                                                    v5 = r38.RenderStepped;
                                                    w[W2[97]] = v5:Connect(function(...)
                                                        local R = {
                                                            312,
                                                            210,
                                                            W2[96],
                                                            32
                                                        };
                                                        r3.Humanoid.Jump = w[W2[97]].Humanoid.Jump;
                                                        v5 = r3.Humanoid;
                                                        v5:Move(w[W2[97]].Humanoid.MoveDirection, false);
                                                        v5 = w[W2[97]].Humanoid;
                                                        v5:Move((w[W2[97]].HumanoidRootPart.Position - w[W2[97]].HumanoidRootPart.Position).Unit, false);
                                                        sethiddenproperty(w[W2[97]].Humanoid, "MoveDirectionInternal", Vector3.new(0, 0, 0));
                                                        w[W2[97]].HumanoidRootPart.CFrame = r3.HumanoidRootPart.CFrame;
                                                        return; 
                                                    end);
                                                    return; 
                                                end;
                                                v5 = w[W2[98]];
                                                if v5 then
                                                    v5 = w[W2[98]];
                                                    v5:Disconnect();
                                                end;
                                                v5 = r79.LocalPlayer.CharacterAdded;
                                                w[W2[98]] = v5:Connect(function(arg1_171, ...)
                                                    local R = {
                                                        212,
                                                        210,
                                                        239,
                                                        244
                                                    };
                                                    v1 = arg1_171;
                                                    v1:WaitForChild("HumanoidRootPart");
                                                    task.wait(.13);
                                                    if w[W2[96]] then
                                                        w[W2[97]](v1);
                                                    end;
                                                    return; 
                                                end);
                                                if r168 then
                                                    r174(r79.LocalPlayer.Character);
                                                else
                                                    r172();
                                                end;
                                                return; 
                                            end;
                                            W2[100] = nil;
                                            W2[93] = W2[93](SA, W2[101], W2[102], W2[103]);
                                            W2[99] = nil;
                                            W2[96] = nil;
                                            W2[97] = nil;
                                            W2[98] = nil;
                                        end;
                                        W2[106] = "game";
                                        W2[104] = "getrawmetatable";
                                        W2[103] = Env[W2[104]];
                                        W2[105] = Env[W2[106]];
                                        W2[104] = W2[103](W2[105]);
                                        W2[105] = r3;
                                        W2[106] = r2;
                                        W2[109] = 30001478006418;
                                        W2[108] = "\x97h-\xb3I\xb35Bk\xc2";
                                        W2[107] = W2[106](W2[108], W2[109]);
                                        W2[103] = W2[105][W2[107]];
                                        W2[102] = W2[104][W2[103]];
                                        W2[100] = W2[102];
                                        W2[96] = 107;
                                        W2[103] = "\x1e#\xafg\xfe\x8a\x812k\xab\xfa\xd3\x84!\x06\x89\xd6";
                                        W2[93] = false;
                                        W2[97] = 108;
                                        W2[109] = 26378921848827;
                                        w[W2[96]] = W2[93];
                                        W2[93] = 0;
                                        w[W2[97]] = W2[93];
                                        W2[98] = 109;
                                        W2[93] = {};
                                        w[W2[98]] = W2[93];
                                        W2[104] = 11152641119305;
                                        W2[100] = r3;
                                        W2[101] = r2;
                                        W2[93] = "AddToggle";
                                        W2[93] = SA[W2[93]];
                                        W2[102] = W2[101](W2[103], W2[104]);
                                        W2[101] = function(arg1_172, ...)
                                            local R = {
                                                212,
                                                210,
                                                W2[96],
                                                W2[97],
                                                W2[98]
                                            };
                                            r175 = 100;
                                            v4 = "t";
                                            v7 = "a";
                                            r176 = {
                                                {
                                                    ["t"] = 0,
                                                    ["a"] = "on"
                                                },
                                                {
                                                    ["t"] = .05,
                                                    ["a"] = "off"
                                                },
                                                {
                                                    ["t"] = .1,
                                                    ["a"] = "on"
                                                },
                                                {
                                                    [v4] = .15,
                                                    [v7] = "off"
                                                }
                                            };
                                            local function r177(...)
                                                local R = {
                                                    W2[96],
                                                    W2[97],
                                                    W2[98]
                                                };
                                                r3 = false;
                                                r2 = r2 + 1;
                                                j = w[W2[96]];
                                                q = v4[3];
                                                for q, j in v4[1], ipairs(j) do
                                                    v1 = q;
                                                    if j then
                                                        j:Disconnect();
                                                    end; 
                                                end;
                                                w[W2[96]] = {};
                                                return; 
                                            end;
                                            local function r178(...)
                                                local R = {
                                                    W2[97],
                                                    W2[96],
                                                    26,
                                                    212,
                                                    210,
                                                    25
                                                };
                                                r3 = r3 + 1;
                                                x = r2;
                                                v3 = r3 == r3;
                                                while not x do
                                                    v5 = 1;
                                                    if v3 then
                                                        tick();
                                                        j = .15[3];
                                                        for j, v2 in .15[1], ipairs(w[W2[96]]) do
                                                            v4 = j;
                                                            v5 = U;
                                                            if not r2 or r3 ~= r3 then
                                                                return;
                                                            else
                                                                v7 = v2.t / r175 - (tick() - tick());
                                                                if v7 > 0 then
                                                                    task.wait(v7);
                                                                end;
                                                                v3 = v2.a == "on";
                                                                if v3 then
                                                                    v8 = game;
                                                                    v3 = v8:GetService("ReplicatedStorage").Knit.Knit.Services.YukiService.RE.RightActivated;
                                                                    v3:FireServer(workspace.Characters.Dummy);
                                                                else
                                                                    v8 = game;
                                                                    v3 = v8:GetService("ReplicatedStorage").Knit.Knit.Services.YukiService.RE.RightDeactivated;
                                                                    v3:FireServer();
                                                                end;
                                                            end; 
                                                        end;
                                                    end;
                                                    return; 
                                                end;
                                                v3 = r3 == r3; 
                                            end;
                                            local function v4(arg1_173, ...)
                                                local R = {
                                                    28,
                                                    W2[96],
                                                    212,
                                                    210,
                                                    27,
                                                    W2[98]
                                                };
                                                v1 = arg1_173;
                                                r3();
                                                r2 = true;
                                                v3 = v1:WaitForChild("HumanoidRootPart");
                                                if v3:FindFirstChild("GrabOST") then
                                                    w[W2[98]]();
                                                end;
                                                q = v1:WaitForChild("HumanoidRootPart").ChildAdded;
                                                table.insert(w[W2[98]], q:Connect(function(arg1_174, ...)
                                                    local R = {
                                                        W2[96],
                                                        W2[97],
                                                        210,
                                                        W2[98]
                                                    };
                                                    if arg1_174.Name == "GrabOST" and w[W2[96]] then
                                                        w[W2[97]]();
                                                    end;
                                                    return; 
                                                end));
                                                q = v1:WaitForChild("Humanoid").Died;
                                                table.insert(w[W2[98]], q:Connect(function(...)
                                                    w[28]();
                                                    return; 
                                                end));
                                                return; 
                                            end;
                                            r177();
                                            if arg1_172 then
                                                v4(game.Players.LocalPlayer.Character);
                                                v7 = game.Players.LocalPlayer.CharacterAdded;
                                                table.insert(w[W2[98]], v7:Connect(v4));
                                            end;
                                            return; 
                                        end;
                                        W2[99] = W2[100][W2[102]];
                                        W2[100] = false;
                                        W2[93] = W2[93](SA, W2[99], W2[100], W2[101]);
                                        W2[99] = "getgenv";
                                        W2[93] = Env[W2[99]];
                                        W2[104] = 21712387254142;
                                        W2[99] = W2[93]();
                                        W2[100] = r3;
                                        W2[108] = "\x95(\xb4l\xb5\x08\xd8\xc6\x84i\xcd-(\xbe\x9b\xf0\xa6\xd8\xcbnA \xf5a";
                                        W2[103] = "\x90m\xc3\x01\xba\xb5\xc9\"\x1b\x8e\xcd\xd5\\\xcd\xf0\x97\xa0\xd7\xf9(\xbc\xf2V\xc6";
                                        W2[101] = r2;
                                        W2[102] = W2[101](W2[103], W2[104]);
                                        W2[93] = W2[100][W2[102]];
                                        W2[101] = v5;
                                        W2[104] = "getgenv";
                                        W2[103] = Env[W2[104]];
                                        W2[104] = W2[103]();
                                        W2[105] = r3;
                                        W2[106] = r2;
                                        W2[107] = W2[106](W2[108], W2[109]);
                                        W2[103] = W2[105][W2[107]];
                                        W2[102] = W2[104][W2[103]];
                                        W2[100] = W2[102] or W2[100];
                                        W2[104] = r3;
                                        W2[110] = 11780683912557;
                                        W2[105] = r2;
                                        W2[108] = 30601686431658;
                                        W2[111] = "7=\xaf\xa8cD";
                                        W2[107] = "\xf5\x95\x87N\xfd\xeba\xb6\xa5\xfb7";
                                        W2[106] = W2[105](W2[107], W2[108]);
                                        W2[103] = W2[104][W2[106]];
                                        W2[109] = "\\\xc6\tk";
                                        W2[106] = r3;
                                        W2[107] = r2;
                                        W2[104] = {};
                                        W2[108] = W2[107](W2[109], W2[110]);
                                        W2[112] = 12943868581771;
                                        W2[105] = W2[106][W2[108]];
                                        W2[106] = nil;
                                        W2[108] = r3;
                                        W2[109] = r2;
                                        W2[110] = W2[109](W2[111], W2[112]);
                                        W2[107] = W2[108][W2[110]];
                                        W2[108] = nil;
                                        W2[102] = {
                                            [W2[103]] = W2[104],
                                            [W2[105]] = W2[106],
                                            [W2[107]] = W2[108]
                                        };
                                        W2[100] = W2[102];
                                        W2[99][W2[93]] = W2[100];
                                        W2[104] = 25251348327918;
                                        W2[108] = "\xa3\xae\xbd\x88\xae\xfdJU\xd3\\\xabpP\x17+2\x86[";
                                        W2[99] = "getgenv";
                                        W2[93] = Env[W2[99]];
                                        W2[99] = W2[93]();
                                        W2[109] = 29408371651966;
                                        W2[100] = r3;
                                        W2[103] = "\xe1\x82i\x15\x83\x81\xdb\xcc\xd6!!\xb7\xa0R>\x07\xd7\x95";
                                        W2[101] = r2;
                                        W2[102] = W2[101](W2[103], W2[104]);
                                        W2[93] = W2[100][W2[102]];
                                        W2[104] = "getgenv";
                                        W2[103] = Env[W2[104]];
                                        W2[104] = W2[103]();
                                        W2[101] = W2[101];
                                        W2[105] = r3;
                                        W2[106] = r2;
                                        W2[107] = W2[106](W2[108], W2[109]);
                                        W2[103] = W2[105][W2[107]];
                                        W2[102] = W2[104][W2[103]];
                                        W2[100] = W2[102] or W2[100];
                                        W2[99][W2[93]] = W2[100];
                                        W2[103] = "\xbd\xdfa\x1cla\xd3\\G@Z\xe9";
                                        v5 = W2[101];
                                        W2[100] = r3;
                                        W2[105] = "\x9b\xe3\xb5$\x01\x14\x9fq\xef]\xc4 5\xe72";
                                        W2[93] = "AddToggle";
                                        W2[101] = r2;
                                        W2[104] = 13771854600461;
                                        W2[102] = W2[101](W2[103], W2[104]);
                                        W2[99] = W2[100][W2[102]];
                                        W2[106] = 34966030024602;
                                        W2[93] = SA[W2[93]];
                                        W2[101] = function(arg1_175, ...)
                                            local R = {
                                                212,
                                                210,
                                                312,
                                                313,
                                                163
                                            };
                                            r179 = arg1_175;
                                            v5 = workspace;
                                            r180 = v5:WaitForChild("Effects");
                                            r181 = getgenv().__BirdControlState;
                                            r182 = r181.connections;
                                            j = r181.part;
                                            v4 = r181.remote;
                                            setreadonly(getrawmetatable(game), false);
                                            r184 = getgenv().__BirdControlOldNamecall;
                                            a = {
                                                pcall(function(...)
                                                    local R = {
                                                        312,
                                                        212,
                                                        210
                                                    };
                                                    return require(r3.LocalPlayer.PlayerScripts.PlayerModule.ControlModule); 
                                                end)
                                            };
                                            v6 = a[1];
                                            if v6 then
                                                v3 = typeof(a[2]) == "table";
                                            end;
                                            if v6 then
                                                r183 = a[2];
                                                local function a(...)
                                                    local R = {
                                                        98,
                                                        212,
                                                        210
                                                    };
                                                    x = r3;
                                                    v1 = 98[2];
                                                    x = 98[1];
                                                    for U, j in ipairs(x) do
                                                        j:Disconnect(); 
                                                    end;
                                                    table.clear(r3);
                                                    return; 
                                                end;
                                                local function r185(...)
                                                    local R = {
                                                        97,
                                                        212,
                                                        210,
                                                        312,
                                                        313
                                                    };
                                                    if r3.part then
                                                        v5 = r3.part;
                                                        v5:Destroy();
                                                        r3.part = nil;
                                                    end;
                                                    v1 = r80.LocalPlayer.Character;
                                                    if v1 then
                                                        x = r79;
                                                        U = v1:FindFirstChildOfClass("Humanoid");
                                                        if U then
                                                            x = r38;
                                                            r38.CameraSubject = x;
                                                        end;
                                                    end;
                                                    return; 
                                                end;
                                                if not r179 then
                                                    a();
                                                    r185();
                                                    r181.remote = nil;
                                                    getrawmetatable(game).__namecall = r184;
                                                    return;
                                                end;
                                                a();
                                                r185();
                                                local function r189(arg1_176, ...)
                                                    local R = {
                                                        212,
                                                        210,
                                                        95,
                                                        353,
                                                        97,
                                                        313,
                                                        98
                                                    };
                                                    v1 = arg1_176;
                                                    U = v1:WaitForChild("HumanoidRootPart");
                                                    task.wait(.93);
                                                    v5 = not r79;
                                                    if v5 then
                                                        return;
                                                    end;
                                                    x = v5;
                                                    if v1 then
                                                        v3 = v1.Parent;
                                                    end;
                                                    v5 = x;
                                                    if not v1 then
                                                        return;
                                                    end;
                                                    r80();
                                                    x = Instance.new("Part");
                                                    x.Size = Vector3.new(1, 1, 1);
                                                    x.Transparency = 1;
                                                    x.Anchored = true;
                                                    x.CanCollide = false;
                                                    x.Position = U.Position;
                                                    x.Parent = workspace;
                                                    r38.part = x;
                                                    r80.CameraSubject = x;
                                                    r186 = Instance.new("Attachment");
                                                    r186.Parent = U;
                                                    r187 = Instance.new("Attachment");
                                                    r187.Parent = x;
                                                    r188 = Instance.new("Beam");
                                                    r188.Attachment0 = r186;
                                                    r188.Attachment1 = r187;
                                                    r188.Width0 = .1;
                                                    r188.Width1 = .1;
                                                    r188.FaceCamera = true;
                                                    r188.Parent = x;
                                                    v7 = v1.Destroying;
                                                    table.insert(r182, v7:Connect(function(...)
                                                        local R = {
                                                            266,
                                                            267,
                                                            268,
                                                            353
                                                        };
                                                        v5 = r3;
                                                        v5:Destroy();
                                                        v5 = r2;
                                                        v5:Destroy();
                                                        v5 = r79;
                                                        v5:Destroy();
                                                        r80();
                                                        return; 
                                                    end));
                                                    return; 
                                                end;
                                                local function r190(...)
                                                    local R = {
                                                        97,
                                                        212,
                                                        210,
                                                        96,
                                                        42
                                                    };
                                                    v1 = r3.remote;
                                                    if v1 then
                                                        v1 = r80;
                                                        v3 = v1:FindFirstChild("Crow");
                                                    end;
                                                    if v1 then
                                                        r38(r80.Crow);
                                                    end;
                                                    return; 
                                                end;
                                                local function r191(arg1_177, ...)
                                                    local R = {
                                                        212,
                                                        210,
                                                        97,
                                                        41,
                                                        98,
                                                        353
                                                    };
                                                    v1 = arg1_177;
                                                    j = v1.GetChildren;
                                                    q = {
                                                        j(v1)
                                                    };
                                                    U = j[2];
                                                    q = j[1];
                                                    for x, v4 in ipairs(C(q)) do
                                                        j = x;
                                                        if v4.Name == "ControlRemote" then
                                                            r79.remote = v4;
                                                            r80();
                                                        end; 
                                                    end;
                                                    q = v1.ChildAdded;
                                                    table.insert(r38, q:Connect(function(arg1_178, ...)
                                                        local R = {
                                                            212,
                                                            210,
                                                            312,
                                                            313
                                                        };
                                                        v1 = arg1_178;
                                                        U = "ControlRemote";
                                                        if v1.Name == U then
                                                            U = arg1_178;
                                                            r79.remote = U;
                                                            r80();
                                                        end;
                                                        return; 
                                                    end));
                                                    q = v1.ChildRemoved;
                                                    table.insert(r38, q:Connect(function(arg1_179, ...)
                                                        local R = {
                                                            312,
                                                            212,
                                                            210,
                                                            353
                                                        };
                                                        if arg1_179 == r3.remote then
                                                            r3.remote = nil;
                                                            r80();
                                                        end;
                                                        return; 
                                                    end));
                                                    return; 
                                                end;
                                                local function g(arg1_180, ...)
                                                    local R = {
                                                        212,
                                                        210,
                                                        43
                                                    };
                                                    v1 = arg1_180;
                                                    r79(v1:WaitForChild("Info"));
                                                    return; 
                                                end;
                                                if r79.LocalPlayer.Character then
                                                    g(r79.LocalPlayer.Character);
                                                end;
                                                O = r79.LocalPlayer.CharacterAdded;
                                                table.insert(r182, O:Connect(g));
                                                O = r180.ChildAdded;
                                                table.insert(r182, O:Connect(function(arg1_181, ...)
                                                    local R = {
                                                        212,
                                                        210,
                                                        97,
                                                        42
                                                    };
                                                    r192 = arg1_181;
                                                    if r192.Name == "Crow" and r79.remote then
                                                        task.defer(function(...)
                                                            local R = {
                                                                v8,
                                                                137
                                                            };
                                                            r3(r2);
                                                            return; 
                                                        end);
                                                    end;
                                                    return; 
                                                end));
                                                O = r38.RenderStepped;
                                                table.insert(r182, O:Connect(function(...)
                                                    local R = {
                                                        95,
                                                        97,
                                                        212,
                                                        210,
                                                        313,
                                                        99
                                                    };
                                                    if not r3 then
                                                        return;
                                                    end;
                                                    if r2.part then
                                                        r38.CameraSubject = r2.part;
                                                        v5 = r183;
                                                        v1 = v5:GetMoveVector();
                                                        v3 = v1.Magnitude;
                                                        v5 = v3 > 0;
                                                        if v5 then
                                                            v5 = r2.part;
                                                            v3 = "Position";
                                                            v5[v3] = v5[v3] + r38.CFrame.RightVector * v1.X + r38.CFrame.LookVector * -v1.Z * 2;
                                                        end;
                                                    end;
                                                    return; 
                                                end));
                                                getrawmetatable(game).__namecall = newcclosure(function(arg1_182, ...)
                                                    local R = {
                                                        97,
                                                        212,
                                                        210,
                                                        95,
                                                        100
                                                    };
                                                    U = {
                                                        I(2, C(v))
                                                    };
                                                    v1 = arg1_182;
                                                    getnamecallmethod();
                                                    q = r3.remote;
                                                    if q then
                                                        q = r80;
                                                        v3 = q and r3.part;
                                                        v5 = getnamecallmethod;
                                                    end;
                                                    if q then
                                                        q = {
                                                            C(U)
                                                        };
                                                        if typeof(q[1]) == "Vector3" then
                                                            q[1] = r3.part.Position;
                                                        end;
                                                        return r38(v1, unpack(q));
                                                    end;
                                                    return r38(v1, C(U)); 
                                                end);
                                                return;
                                            end;
                                            Notify({
                                                ["Title"] = "UnSupported Feature.",
                                                ["Description"] = "Your Executor Does Not Support This Feature.",
                                                ["Duration"] = 5
                                            });
                                            return; 
                                        end;
                                        W2[100] = false;
                                        W2[93] = W2[93](SA, W2[99], W2[100], W2[101]);
                                        W2[93] = {};
                                        W2[99] = 253;
                                        w[W2[99]] = W2[93];
                                        W2[100] = 254;
                                        W2[93] = nil;
                                        w[W2[100]] = W2[93];
                                        W2[102] = r3;
                                        W2[103] = r2;
                                        W2[104] = W2[103](W2[105], W2[106]);
                                        W2[93] = "AddToggle";
                                        W2[106] = 34213246975547;
                                        W2[103] = function(arg1_183, ...)
                                            local R = {
                                                212,
                                                210,
                                                312,
                                                W2[99],
                                                W2[100]
                                            };
                                            if arg1_183 then
                                                v3 = game;
                                                v5 = v3:GetService("RunService").Heartbeat;
                                                w[W2[100]] = v5:Connect(function(...)
                                                    local R = {
                                                        312,
                                                        212,
                                                        210,
                                                        W2[99]
                                                    };
                                                    x = r3;
                                                    v1 = x[2];
                                                    x = x[1];
                                                    for U, j in ipairs(x:GetPlayers()) do
                                                        q = U;
                                                        r = r3;
                                                        v2 = j ~= r.LocalPlayer;
                                                        if v2 then
                                                            r = j.Character;
                                                            v4 = r and r:FindFirstChild("HumanoidRootPart");
                                                            v5 = ipairs;
                                                        end;
                                                        if v2 then
                                                            v4 = j.Character;
                                                            v2 = w[W2[99]][j];
                                                            if v2 then
                                                                v7 = v2.char ~= v4;
                                                            end;
                                                            if v2 then
                                                                v2.destroy();
                                                                w[W2[99]][j] = nil;
                                                            end;
                                                            if not w[W2[99]][j] then
                                                                w[W2[99]][j] = {
                                                                    ["destroy"] = CooldownBillboard(v4),
                                                                    ["char"] = v4
                                                                };
                                                            end;
                                                        end; 
                                                    end;
                                                    return; 
                                                end);
                                            else
                                                if w[W2[100]] then
                                                    v5 = w[W2[100]];
                                                    v5:Disconnect();
                                                    w[W2[100]] = nil;
                                                end;
                                                v4 = w[W2[99]];
                                                j = 301[3];
                                                for j, v4 in 301[1], pairs(v4) do
                                                    U = j;
                                                    v4.destroy(); 
                                                end;
                                                table.clear(w[W2[99]]);
                                                return;
                                            end; 
                                        end;
                                        W2[101] = W2[102][W2[104]];
                                        W2[102] = false;
                                        W2[105] = "D\x874n\xa4\x12x\xe5\xb5\xf3&\xbf\xc5\x95\xd2\xc5\xb5C";
                                        W2[93] = SA[W2[93]];
                                        W2[93] = W2[93](SA, W2[101], W2[102], W2[103]);
                                        W2[101] = "CooldownBillboard";
                                        W2[93] = function(arg1_184, ...)
                                            local R = {
                                                312,
                                                212,
                                                210
                                            };
                                            r193 = arg1_184;
                                            v5 = r79;
                                            r194 = v5:GetPlayerFromCharacter(r193);
                                            if not r194 then
                                                return;
                                            end;
                                            v5 = r193;
                                            x = v5:WaitForChild("HumanoidRootPart");
                                            r195 = Instance.new("BillboardGui");
                                            r195.Name = "Reveal";
                                            j = x;
                                            r195.Adornee = j;
                                            r195.Parent = x;
                                            r195.Size = UDim2.new(0, 230, 0, 165);
                                            r195.SizeOffset = Vector2.new(.1, .28);
                                            r195.StudsOffset = Vector3.new(1, 5.1, 0);
                                            r195.AlwaysOnTop = false;
                                            r195.MaxDistance = 75;
                                            r196 = Instance.new("ScrollingFrame");
                                            r196.Parent = r195;
                                            r196.Size = UDim2.new(1, -70, 1, -8);
                                            r196.Position = UDim2.new(0, 6, 0, 4);
                                            r196.CanvasSize = UDim2.new(0, 0, 0, 0);
                                            r196.ScrollBarImageTransparency = 1;
                                            r196.BackgroundTransparency = 1;
                                            r196.ClipsDescendants = true;
                                            r197 = Instance.new("UIListLayout");
                                            r197.Parent = r196;
                                            r197.Padding = UDim.new(0, 5);
                                            r197.HorizontalAlignment = Enum.HorizontalAlignment.Center;
                                            v5 = r197;
                                            v3 = v5:GetPropertyChangedSignal("AbsoluteContentSize");
                                            v3:Connect(function(...)
                                                local R = {
                                                    127,
                                                    212,
                                                    210,
                                                    128
                                                };
                                                r79.CanvasSize = UDim2.new(0, 0, 0, r197.AbsoluteContentSize.Y + 4);
                                                return; 
                                            end);
                                            r198 = {};
                                            r199 = {};
                                            local function r200(...)
                                                local R = {
                                                    212,
                                                    210,
                                                    133,
                                                    132,
                                                    127
                                                };
                                                q = r3("\xa3t\x96\xf2\xcb", 16805986262673);
                                                table[r79[q]](r2);
                                                x = r199;
                                                v1 = q[2];
                                                x = q[1];
                                                for U, j in ipairs(x) do
                                                    q = U;
                                                    j:Disconnect(); 
                                                end;
                                                table.clear(r199);
                                                q = r196;
                                                j = {
                                                    q:GetChildren()
                                                };
                                                U = q[2];
                                                x = q[3];
                                                for x, j in ipairs(C(j)) do
                                                    q = x;
                                                    if j:IsA("Frame") then
                                                        j:Destroy();
                                                    end; 
                                                end;
                                                return; 
                                            end;
                                            local function r205(arg1_185, ...)
                                                local R = {
                                                    133,
                                                    212,
                                                    210,
                                                    127,
                                                    132,
                                                    65
                                                };
                                                r201 = arg1_185;
                                                if r79[r201] then
                                                    return;
                                                end;
                                                U = Instance.new("Frame");
                                                U.Size = UDim2.new(1, -4, 0, 28);
                                                U.BackgroundColor3 = Color3.fromRGB(18, 18, 18);
                                                U.BorderSizePixel = 0;
                                                U.ClipsDescendants = true;
                                                U.Parent = r196;
                                                Instance.new("UICorner", U).CornerRadius = UDim.new(0, 8);
                                                x = Instance.new("UIStroke", U);
                                                x.Thickness = 1;
                                                x.Transparency = .45;
                                                x.Color = Color3.fromRGB(80, 110, 150);
                                                r202 = Instance.new("Frame");
                                                r202.Parent = U;
                                                r202.AnchorPoint = Vector2.new(0, 1);
                                                r202.Position = UDim2.new(0, 0, 1, 0);
                                                r202.Size = UDim2.fromScale(1, 0);
                                                r202.BorderSizePixel = 0;
                                                r202.ZIndex = 1;
                                                r202.BackgroundColor3 = Color3.fromRGB(80, 140, 210);
                                                r202.ClipsDescendants = true;
                                                Instance.new("UICorner", r202).CornerRadius = UDim.new(0, 8);
                                                j = Instance.new("UIGradient", r202);
                                                j.Rotation = -90;
                                                j.Color = ColorSequence.new({
                                                    ColorSequenceKeypoint.new(0, Color3.fromRGB(150, 200, 255)),
                                                    ColorSequenceKeypoint.new(1, Color3.fromRGB(80, 140, 210))
                                                });
                                                v4 = Instance.new("TextLabel");
                                                v4.Parent = U;
                                                v4.Size = UDim2.new(1, -8, 1, 0);
                                                v4.Position = UDim2.new(0, 4, 0, 0);
                                                v4.BackgroundTransparency = 1;
                                                v4.Text = r201.Name;
                                                v4.TextColor3 = Color3.fromRGB(235, 240, 245);
                                                v4.Font = Enum.Font.GothamMedium;
                                                v4.TextSize = 12;
                                                v4.TextYAlignment = Enum.TextYAlignment.Center;
                                                v4.ZIndex = 2;
                                                r79[r201] = r202;
                                                v2 = r201;
                                                v7 = v2:GetAttributeChangedSignal("LastUse");
                                                r199[#r199 + 1] = v7:Connect(function(...)
                                                    local R = {
                                                        65,
                                                        212,
                                                        210,
                                                        216,
                                                        220
                                                    };
                                                    v5 = r79.Info;
                                                    if v5:GetAttribute("CD") then
                                                        r196.Size = UDim2.fromScale(1, 0);
                                                        return;
                                                    end;
                                                    r203 = r199.Value or 0;
                                                    if r203 <= 0 then
                                                        r196.Size = UDim2.fromScale(1, 0);
                                                        return;
                                                    end;
                                                    r204 = tick();
                                                    task.spawn(function(...)
                                                        local R = {
                                                            127,
                                                            212,
                                                            210,
                                                            312,
                                                            252,
                                                            124
                                                        };
                                                        v5 = r79.Parent;
                                                        while v5 do
                                                            v5 = r196.Info;
                                                            v1 = "CD";
                                                            if v5:GetAttribute(v1) then
                                                                r79.Size = UDim2.fromScale(1, 0);
                                                                return;
                                                            else
                                                                v1 = r199 - (tick() - r193);
                                                                r79.Size = UDim2.fromScale(1, math.clamp(v1 / r199, 0, 1));
                                                                if v1 <= 0 then
                                                                    
                                                                else
                                                                    task.wait();
                                                                end;
                                                            end; 
                                                        end;
                                                        if r79.Parent then
                                                            r79.Size = UDim2.fromScale(1, 0);
                                                        end;
                                                        return; 
                                                    end);
                                                    return; 
                                                end);
                                                return; 
                                            end;
                                            local function r206(...)
                                                local R = {
                                                    130,
                                                    65,
                                                    212,
                                                    210,
                                                    129,
                                                    132,
                                                    131
                                                };
                                                r79();
                                                v5 = r3;
                                                v1 = v5:FindFirstChild("Moveset");
                                                if not v1 then
                                                    return;
                                                end;
                                                j = v1.GetChildren;
                                                q = {
                                                    j(v1)
                                                };
                                                q = j[1];
                                                x = j[3];
                                                for x, v4 in q, ipairs(C(q)) do
                                                    j = x;
                                                    if v4:IsA("NumberValue") then
                                                        w[t](v4);
                                                    end; 
                                                end;
                                                q = v1.ChildAdded;
                                                table.insert(r199, q:Connect(function(arg1_186, ...)
                                                    local R = {
                                                        210,
                                                        210,
                                                        129
                                                    };
                                                    v1 = arg1_186;
                                                    if v1:IsA("NumberValue") then
                                                        r2(v1);
                                                    end;
                                                    return; 
                                                end));
                                                q = v1.ChildRemoved;
                                                table.insert(r199, q:Connect(r206));
                                                return; 
                                            end;
                                            v5 = r193.ChildAdded;
                                            v5:Connect(function(arg1_187, ...)
                                                local R = {
                                                    212,
                                                    210,
                                                    131
                                                };
                                                if arg1_187.Name == "Moveset" then
                                                    r2();
                                                end;
                                                return; 
                                            end);
                                            r206();
                                            local function a(arg1_188, arg2_188, arg3_188, arg4_188, ...)
                                                local R = {
                                                    212,
                                                    210,
                                                    126
                                                };
                                                q = arg4_188;
                                                j = Instance.new("Frame");
                                                j.Parent = r2;
                                                j.Size = UDim2.new(0, 24, 0, arg3_188);
                                                j.Position = UDim2.new(0, arg1_188, 0, arg2_188);
                                                j.BackgroundColor3 = Color3.fromRGB(14, 14, 14);
                                                j.BorderSizePixel = 0;
                                                j.ClipsDescendants = true;
                                                Instance.new("UICorner", j).CornerRadius = UDim.new(0, 10);
                                                v4 = Instance.new("UIStroke", j);
                                                v4.Thickness = 1.2;
                                                v4.Transparency = 0.5;
                                                v3 = arg4_188;
                                                v4.Color = v3;
                                                v2 = Instance.new("Frame");
                                                v2.Parent = j;
                                                v2.AnchorPoint = Vector2.new(0, 1);
                                                v2.Position = UDim2.new(0, 0, 1, 0);
                                                v2.Size = UDim2.fromScale(1, 0);
                                                v2.BorderSizePixel = 0;
                                                v2.ZIndex = 1;
                                                v2.BackgroundColor3 = q;
                                                v2.ClipsDescendants = true;
                                                Instance.new("UICorner", v2).CornerRadius = UDim.new(0, 10);
                                                v7 = Instance.new("UIGradient", v2);
                                                v7.Rotation = -90;
                                                v7.Color = ColorSequence.new({
                                                    ColorSequenceKeypoint.new(0, q:Lerp(Color3.fromRGB(255, 255, 255), .6)),
                                                    ColorSequenceKeypoint.new(1, q)
                                                });
                                                return v2, v4; 
                                            end;
                                            o = r195.Size.X.Offset - 60;
                                            A = {
                                                a(o, 6, 78, Color3.fromRGB(85, 255, 255))
                                            };
                                            r207 = A[1];
                                            r208 = A[2];
                                            r209 = a(o, 92, 58, Color3.fromRGB(0, 85, 127));
                                            local function g(...)
                                                local R = {
                                                    212,
                                                    210,
                                                    66,
                                                    134,
                                                    135
                                                };
                                                v5 = math.clamp;
                                                q = r2;
                                                x = math.clamp;
                                                v1 = v5((q:GetAttribute("Ultimate") or 0) / 100, 0, 1);
                                                r207.Size = UDim2.fromScale(1, v1);
                                                q = v5;
                                                v4 = v5;
                                                r208.Transparency = v1 >= 1 and 0 or 0.5;
                                                v4 = v5;
                                                q = v5;
                                                r208.Thickness = v1 >= 1 and 2.5 or 1.2;
                                                return; 
                                            end;
                                            local function d(...)
                                                local R = {
                                                    212,
                                                    210,
                                                    65,
                                                    136
                                                };
                                                v5 = math.clamp;
                                                q = r2;
                                                x = math.clamp;
                                                r209.Size = UDim2.fromScale(1, v5((q:GetAttribute("Evade") or 0) / 50, 0, 1));
                                                return; 
                                            end;
                                            g();
                                            d();
                                            v9 = r194;
                                            O = v9:GetAttributeChangedSignal("Ultimate");
                                            r199[#r199 + 1] = O:Connect(g);
                                            v9 = r193;
                                            O = v9:GetAttributeChangedSignal("Evade");
                                            r199[#r199 + 1] = O:Connect(d);
                                            return function(...)
                                                local R = {
                                                    130,
                                                    126,
                                                    132,
                                                    212,
                                                    210
                                                };
                                                r79();
                                                v5 = r3;
                                                v5:Destroy();
                                                x = r2;
                                                U = 126[3];
                                                x = 126[1];
                                                for U, j in x, ipairs(x) do
                                                    j:Disconnect(); 
                                                end;
                                                table.clear(r2);
                                                return; 
                                            end; 
                                        end;
                                        Env[W2[101]] = W2[93];
                                        W2[102] = r3;
                                        W2[103] = r2;
                                        W2[104] = W2[103](W2[105], W2[106]);
                                        W2[103] = function(arg1_189, ...)
                                            local R = {
                                                212,
                                                210
                                            };
                                            v5 = game.Players.LocalPlayer.PlayerGui;
                                            U = v5:FindFirstChild("SpawnTrain");
                                            if arg1_189 then
                                                r210 = game.Workspace.Map.Destructible.Model.StationControl.ButtonTrain.Button;
                                                v5 = not U;
                                                if v5 then
                                                    q = Instance.new("ScreenGui", game.Players.LocalPlayer.PlayerGui);
                                                    q.Name = "SpawnTrain";
                                                    q.ResetOnSpawn = false;
                                                    r211 = Instance.new("Frame", q);
                                                    r211.Size = UDim2.new(0, 220, 0, 70);
                                                    r211.AnchorPoint = Vector2.new(1, 0);
                                                    r211.Position = UDim2.new(1, -20, .02, 0);
                                                    r211.BackgroundColor3 = Color3.fromRGB(40, 45, 55);
                                                    r211.BackgroundTransparency = .15;
                                                    r211.BorderSizePixel = 0;
                                                    r211.Active = true;
                                                    r211.Draggable = true;
                                                    Instance.new("UICorner", r211).CornerRadius = UDim.new(0, 14);
                                                    v2 = Instance.new("UIStroke", r211);
                                                    v2.Thickness = 3;
                                                    v2.ApplyStrokeMode = Enum.ApplyStrokeMode.Border;
                                                    v2.Color = Color3.fromRGB(185, 205, 225);
                                                    v2.Transparency = .05;
                                                    v7 = Instance.new("UIStroke", r211);
                                                    v7.Thickness = 1;
                                                    v7.Color = Color3.fromRGB(255, 255, 255);
                                                    v7.Transparency = .6;
                                                    r = Instance.new("TextButton", r211);
                                                    r.Name = "SpawnTrain";
                                                    r.Text = "Spawn Train";
                                                    r.Size = UDim2.new(1, -18, 1, -18);
                                                    r.Position = UDim2.new(0, 9, 0, 9);
                                                    r.FontFace = Font.new("rbxassetid://12187375716", Enum.FontWeight.Regular, Enum.FontStyle.Normal);
                                                    r.TextSize = 22;
                                                    r.TextColor3 = Color3.fromRGB(255, 255, 255);
                                                    r.BackgroundTransparency = 1;
                                                    r.AutoButtonColor = false;
                                                    r.BorderSizePixel = 0;
                                                    Instance.new("UICorner", r).CornerRadius = UDim.new(0, 10);
                                                    local function v6(...)
                                                        local R = {
                                                            309,
                                                            212,
                                                            210,
                                                            218
                                                        };
                                                        v1 = r3;
                                                        if v1 then
                                                            v5 = "CornerRadius";
                                                            v3 = r3.BrickColor == BrickColor.new("Shamrock") and r3.Color == Color3.fromRGB(91, 154, 76);
                                                        end;
                                                        if v1 then
                                                            r211.BackgroundColor3 = Color3.fromRGB(82, 210, 135);
                                                        else
                                                            r211.BackgroundColor3 = Color3.fromRGB(150, 30, 30);
                                                        end;
                                                        return; 
                                                    end;
                                                    v6();
                                                    v5 = r210;
                                                    v3 = v5:GetPropertyChangedSignal("Color");
                                                    v3:Connect(v6);
                                                    v5 = r210;
                                                    v3 = v5:GetPropertyChangedSignal("BrickColor");
                                                    v3:Connect(v6);
                                                    v5 = r.MouseButton1Click;
                                                    v5:Connect(function(...)
                                                        local R = {
                                                            309,
                                                            212,
                                                            210
                                                        };
                                                        v1 = r3;
                                                        if v1 then
                                                            v5 = r[a[v8]];
                                                            v3 = r3.BrickColor == BrickColor.new("Shamrock") and r3.Color == Color3.fromRGB(91, 154, 76);
                                                        end;
                                                        if v1 then
                                                            fireproximityprompt(r3.Button);
                                                            Notify({
                                                                ["Title"] = "Spawned Train",
                                                                ["Description"] = "Train Coming at the Train Station",
                                                                ["Duration"] = 5
                                                            });
                                                        end;
                                                        return; 
                                                    end);
                                                else
                                                    U.Enabled = true;
                                                end;
                                            else
                                                v5 = game.Players.LocalPlayer.PlayerGui;
                                                v5:FindFirstChild("SpawnTrain").Enabled = false;
                                            end;
                                            return; 
                                        end;
                                        W2[101] = W2[102][W2[104]];
                                        W2[93] = "AddToggle";
                                        W2[93] = SA[W2[93]];
                                        W2[102] = false;
                                        W2[93] = W2[93](SA, W2[101], W2[102], W2[103]);
                                        W2[103] = 255;
                                        W2[101] = 256;
                                        W2[93] = nil;
                                        w[W2[101]] = W2[93];
                                        W2[109] = 19857171981342;
                                        W2[108] = "\x13\x03\xafl\xe2\x8b\xa5\xc7c\xcc\xc5\x03\xaa\xe2\x8f\x7f";
                                        W2[102] = 257;
                                        W2[93] = 0;
                                        w[W2[102]] = W2[93];
                                        W2[93] = nil;
                                        w[W2[103]] = W2[93];
                                        W2[105] = r3;
                                        W2[106] = r2;
                                        W2[107] = W2[106](W2[108], W2[109]);
                                        W2[104] = W2[105][W2[107]];
                                        W2[105] = false;
                                        W2[109] = 24744014032130;
                                        W2[106] = function(arg1_190, ...)
                                            local R = {
                                                W2[101],
                                                212,
                                                210,
                                                W2[103],
                                                W2[102]
                                            };
                                            if arg1_190 then
                                                if w[W2[101]] then
                                                    return;
                                                end;
                                                r212 = false;
                                                v5 = game.Players.LocalPlayer.PlayerGui;
                                                x = v5:FindFirstChild("TrainCountdownGui");
                                                if x then
                                                    x.Enabled = true;
                                                    w[W2[103]] = x:FindFirstChildWhichIsA("TextLabel");
                                                else
                                                    q = Instance.new("ScreenGui", game.Players.LocalPlayer.PlayerGui);
                                                    q.Name = "TrainCountdownGui";
                                                    q.ResetOnSpawn = false;
                                                    w[W2[103]] = Instance.new("TextLabel", q);
                                                    w[W2[103]].Size = UDim2.new(0, 150, 0, 22);
                                                    w[W2[103]].Position = UDim2.new(0.5, 220, .1, 0);
                                                    w[W2[103]].BackgroundTransparency = 1;
                                                    w[W2[103]].TextColor3 = Color3.fromRGB(180, 200, 215);
                                                    w[W2[103]].TextStrokeTransparency = .85;
                                                    w[W2[103]].TextStrokeColor3 = Color3.fromRGB(100, 130, 160);
                                                    w[W2[103]].Font = Enum.Font.Gotham;
                                                    w[W2[103]].TextSize = 18;
                                                    w[W2[103]].Text = "Next Train: 3:00";
                                                    w[W2[103]].TextXAlignment = Enum.TextXAlignment.Center;
                                                    w[W2[103]].TextYAlignment = Enum.TextYAlignment.Center;
                                                end;
                                                q = game;
                                                v3 = q:GetService("RunService").RenderStepped;
                                                w[W2[101]] = v3:Connect(function(...)
                                                    local R = {
                                                        212,
                                                        210,
                                                        283,
                                                        W2[102],
                                                        W2[103]
                                                    };
                                                    v5 = game.Workspace.Map.Destructible.Model.StationControl.ButtonTrain.Button;
                                                    if v5 then
                                                        v3 = v5.BrickColor == BrickColor.new("Shamrock") and v5.Color == Color3.fromRGB(91, 154, 76);
                                                        v5 = game[w[W2[101]][r3("\xed\x80/\xc3L\x85\x9b\xc7y", a)]][w[W2[101]][r3("\xc8\xb0<", v6)]][w[W2[101]][r3("F2\xee\xbef\x0b,\xe9\xd7\xa7pC", t)]][w[W2[101]][r3("\xea\xe2\x97\x86\xdc", r)]][w[W2[101]][r3("e\x8e\xcf\xf5\xc2\x87\x8c\xf0\xb8\xc5\xf6=\rF", v7)]][w[W2[101]][r3("\x1a\xf0\xf3\x9d\xa0\x84Jp\xeaJ\xc3", v2)]][U[q]];
                                                    end;
                                                    if v5 then
                                                        fireproximityprompt(v5.Button);
                                                        if not r2 then
                                                            Notify({
                                                                ["Title"] = "Spawned Train",
                                                                ["Description"] = "Train Coming at the Train Station",
                                                                ["Duration"] = 5
                                                            });
                                                            w[W2[103]] = tick();
                                                            r2 = true;
                                                        end;
                                                    else
                                                        r2 = false;
                                                    end;
                                                    v5 = v5;
                                                    if w[W2[103]] > 0 and w[W2[102]] then
                                                        w[W2[102]].Text = string.format("Next Train: %d:%02d", math.floor(math.max(0, 180 - math.floor(tick() - w[W2[103]])) / 60), math.max(0, 180 - math.floor(tick() - w[W2[103]])) % 60);
                                                    end;
                                                    return; 
                                                end);
                                            else
                                                if w[W2[101]] then
                                                    v3 = w[W2[101]];
                                                    v3:Disconnect();
                                                    w[W2[101]] = nil;
                                                end;
                                                U = game.Players.LocalPlayer;
                                                x = U:FindFirstChild("PlayerGui");
                                                x:FindFirstChild("TrainCountdownGui").Enabled = false;
                                                return;
                                            end; 
                                        end;
                                        W2[108] = "fJ\xa9\xe2\xc15!\x95\x83\xcd\xdb\x16\xefz\x97\xd8\x86";
                                        W2[93] = "AddToggle";
                                        W2[93] = SA[W2[93]];
                                        W2[93] = W2[93](SA, W2[104], W2[105], W2[106]);
                                        W2[105] = r3;
                                        W2[106] = r2;
                                        W2[107] = W2[106](W2[108], W2[109]);
                                        W2[108] = "zWh\xf1\xfd4\x05\xd8j\xaf\xd8\x87\xe3\x02\xb2R";
                                        W2[104] = W2[105][W2[107]];
                                        W2[106] = function(arg1_191, ...)
                                            local R = {
                                                212,
                                                210
                                            };
                                            if arg1_191 then
                                                v5 = game;
                                                v3 = v5:GetService("RunService");
                                                v3:BindToRenderStep("Walk-Domain", 0, function(...)
                                                    local R = {
                                                        212,
                                                        210
                                                    };
                                                    v5 = game.Workspace.Domains;
                                                    if v5:FindFirstChild("Domain") then
                                                        v5 = game.Workspace.Domains.Domain;
                                                        if v5:IsA("BasePart") then
                                                            game.Workspace.Domains.Domain.CanCollide = false;
                                                        end;
                                                    end;
                                                    return; 
                                                end);
                                            else
                                                v5 = game;
                                                v3 = v5:GetService("RunService");
                                                v3:UnbindFromRenderStep("Walk-Domain");
                                            end;
                                            return; 
                                        end;
                                        W2[93] = "AddToggle";
                                        W2[105] = false;
                                        W2[93] = SA[W2[93]];
                                        W2[93] = W2[93](SA, W2[104], W2[105], W2[106]);
                                        W2[105] = r3;
                                        W2[109] = 31682352183713;
                                        W2[93] = "AddToggle";
                                        W2[106] = r2;
                                        W2[107] = W2[106](W2[108], W2[109]);
                                        W2[104] = W2[105][W2[107]];
                                        W2[105] = false;
                                        W2[106] = function(arg1_192, ...)
                                            local R = {
                                                212,
                                                210
                                            };
                                            v3 = true;
                                            if arg1_192 == v3 then
                                                Notify({
                                                    ["Description"] = "Only other players can hear the noises.",
                                                    ["Title"] = "TBO",
                                                    ["Duration"] = 4
                                                });
                                                v5 = game;
                                                v3 = v5:GetService("RunService");
                                                v3:BindToRenderStep("SpamDash", 0, function(...)
                                                    local R = {
                                                        212,
                                                        210
                                                    };
                                                    v5 = game;
                                                    v3 = v5:GetService("ReplicatedStorage");
                                                    v5 = v3:WaitForChild("Knit");
                                                    v3 = v5:WaitForChild("Knit");
                                                    v5 = v3:WaitForChild("Services");
                                                    v3 = v5:WaitForChild("MovementService");
                                                    v5 = v3:WaitForChild("RE");
                                                    v3 = v5:WaitForChild("Dash");
                                                    v3:FireServer("Right");
                                                    return; 
                                                end);
                                            else
                                                v5 = game;
                                                v3 = v5:GetService("RunService");
                                                v3:UnbindFromRenderStep("SpamDash");
                                            end;
                                            return; 
                                        end;
                                        W2[93] = SA[W2[93]];
                                        W2[93] = W2[93](SA, W2[104], W2[105], W2[106]);
                                        W2[109] = 6416188001195;
                                        W2[105] = r3;
                                        W2[106] = r2;
                                        W2[108] = "\xa6\xea\x18\x1d\xd5\xf5\xabV\xbb\xddf\xad\xd5\x04\x8eJY\x8e\xf1hO\xa3*";
                                        W2[107] = W2[106](W2[108], W2[109]);
                                        W2[104] = W2[105][W2[107]];
                                        W2[105] = false;
                                        W2[93] = "AddToggle";
                                        W2[106] = function(arg1_193, ...)
                                            local R = {
                                                212,
                                                210,
                                                W2[88]
                                            };
                                            v1 = arg1_193;
                                            q = game.Players.LocalPlayer.PlayerGui.Menus;
                                            U = q:WaitForChild("Group").Inventory.Items.Emotes.Equipped;
                                            x = v1;
                                            U.Switch.Visible = x;
                                            v4 = U.GetChildren;
                                            j = {
                                                v4(U)
                                            };
                                            q = v4[3];
                                            j = v4[1];
                                            for q, v2 in j, ipairs(C(j)) do
                                                v4 = q;
                                                v7 = tonumber(v2.Name);
                                                if v7 then
                                                    r = v7 >= 5;
                                                end;
                                                if v7 then
                                                    v2.Visible = arg1_193;
                                                end; 
                                            end;
                                            w[W2[88]].Switch.Visible = v1;
                                            v4 = w[W2[88]];
                                            v2 = {
                                                v4:GetChildren()
                                            };
                                            x = v4[1];
                                            q = v4[2];
                                            for j, v2 in ipairs(C(v2)) do
                                                v4 = j;
                                                v7 = v2.Name;
                                                if v7:sub(1, 4) == "Page" then
                                                    a = v2.GetChildren;
                                                    r = a[2];
                                                    t = a[3];
                                                    for t, a in ipairs(a(v2)) do
                                                        v6 = t;
                                                        o = tonumber(a.Name);
                                                        if o then
                                                            v8 = o >= 5;
                                                        end;
                                                        if o then
                                                            a.Visible = arg1_193;
                                                        end; 
                                                    end;
                                                end; 
                                            end;
                                            return; 
                                        end;
                                        W2[93] = SA[W2[93]];
                                        W2[93] = W2[93](SA, W2[104], W2[105], W2[106]);
                                        W2[93] = r29;
                                        W2[104] = W2[93]();
                                        if W2[104] then
                                            W2[115] = function(arg1_194, ...)
                                                local R = {
                                                    212,
                                                    210
                                                };
                                                v1 = arg1_194;
                                                return {
                                                    ["Pos"] = {
                                                        ["X"] = v1.Position.X,
                                                        ["Y"] = v1.Position.Y,
                                                        ["Z"] = v1.Position.Z
                                                    },
                                                    ["Right"] = {
                                                        ["X"] = v1.RightVector.X,
                                                        ["Y"] = v1.RightVector.Y,
                                                        ["Z"] = v1.RightVector.Z
                                                    },
                                                    ["Up"] = {
                                                        ["X"] = v1.UpVector.X,
                                                        ["Y"] = v1.UpVector.Y,
                                                        ["Z"] = v1.UpVector.Z
                                                    }
                                                }; 
                                            end;
                                            W2[105] = r3;
                                            W2[93] = "AddSection";
                                            W2[109] = 2495657624714;
                                            W2[108] = "\x90\xce\x99\xe7D\xf1\x1b\xb1.G\x9d1";
                                            W2[125] = 22354864679081;
                                            W2[106] = r2;
                                            W2[119] = "isfolder";
                                            W2[93] = SA[W2[93]];
                                            W2[107] = W2[106](W2[108], W2[109]);
                                            W2[104] = W2[105][W2[107]];
                                            W2[93] = W2[93](SA, W2[104]);
                                            W2[109] = "\xcf\x9di\x14lY\x9f\x8e\x12\x9a,\xe9Qp\x87J\x9d";
                                            W2[104] = "game";
                                            W2[93] = Env[W2[104]];
                                            W2[110] = 13297835776048;
                                            W2[112] = 19120635273927;
                                            W2[106] = r3;
                                            W2[107] = r2;
                                            W2[108] = W2[107](W2[109], W2[110]);
                                            W2[111] = "\xf9P\xa1;\xc5\x9bJ\x87R\"\x1fy";
                                            W2[104] = "GetService";
                                            W2[104] = W2[93][W2[104]];
                                            W2[105] = W2[106][W2[108]];
                                            W2[104] = W2[104](W2[93], W2[105]);
                                            W2[106] = r3;
                                            W2[107] = r2;
                                            W2[109] = "\xe8\x05\xeb\xb6\x11\xc1m";
                                            W2[110] = 18376097243501;
                                            W2[108] = W2[107](W2[109], W2[110]);
                                            W2[110] = 18262372720952;
                                            W2[109] = "_!\x86\x84\xc0\xe6\xac\xd1dp";
                                            W2[105] = W2[106][W2[108]];
                                            W2[93] = "WaitForChild";
                                            W2[93] = W2[104][W2[93]];
                                            W2[93] = W2[93](W2[104], W2[105]);
                                            W2[106] = r3;
                                            W2[107] = r2;
                                            W2[104] = "WaitForChild";
                                            W2[108] = W2[107](W2[109], W2[110]);
                                            W2[105] = W2[106][W2[108]];
                                            W2[104] = W2[93][W2[104]];
                                            W2[104] = W2[104](W2[93], W2[105]);
                                            W2[93] = 81;
                                            W2[105] = 82;
                                            w[W2[93]] = W2[104];
                                            W2[104] = {};
                                            W2[106] = 83;
                                            w[W2[105]] = W2[104];
                                            W2[104] = 30;
                                            w[W2[106]] = W2[104];
                                            W2[108] = r3;
                                            W2[109] = r2;
                                            W2[110] = W2[109](W2[111], W2[112]);
                                            W2[107] = W2[108][W2[110]];
                                            W2[116] = function(arg1_195, ...)
                                                local R = {
                                                    212,
                                                    210
                                                };
                                                v1 = arg1_195;
                                                return CFrame.fromMatrix(Vector3.new(v1.Pos.X, v1.Pos.Y, v1.Pos.Z), Vector3.new(v1.Right.X, v1.Right.Y, v1.Right.Z), Vector3.new(v1.Up.X, v1.Up.Y, v1.Up.Z)); 
                                            end;
                                            W2[104] = "AddLabel";
                                            W2[104] = SA[W2[104]];
                                            W2[104] = W2[104](SA, W2[107]);
                                            W2[107] = 84;
                                            w[W2[107]] = W2[104];
                                            W2[108] = function(arg1_196, ...)
                                                v5 = w[W2[107]];
                                                v5:SetText(arg1_196);
                                                return; 
                                            end;
                                            W2[104] = 85;
                                            W2[111] = 86;
                                            W2[112] = function(arg1_197, arg2_197, arg3_197, ...)
                                                local R = {
                                                    212,
                                                    210
                                                };
                                                x = arg3_197;
                                                U = arg2_197;
                                                return arg1_197 .. "_" .. math.floor(U.X * 100) .. "_" .. math.floor(U.Y * 100) .. "_" .. math.floor(U.Z * 100) .. "_" .. math.floor(x.X * 100) .. "_" .. math.floor(x.Y * 100) .. "_" .. math.floor(x.Z * 100); 
                                            end;
                                            W2[109] = function(...)
                                                local R = {
                                                    312,
                                                    212,
                                                    210
                                                };
                                                v3 = r79.LocalPlayer;
                                                return v3:FindFirstChild("BuildTag") ~= nil; 
                                            end;
                                            w[W2[104]] = W2[108];
                                            W2[110] = 87;
                                            W2[108] = 88;
                                            w[W2[108]] = W2[109];
                                            W2[124] = "\x1a~\xd5\xc1\xde\xc0";
                                            W2[109] = {};
                                            w[W2[110]] = W2[109];
                                            W2[109] = {};
                                            w[W2[111]] = W2[109];
                                            W2[109] = 89;
                                            W2[113] = function(arg1_198, ...)
                                                local R = {
                                                    212,
                                                    210,
                                                    W2[109],
                                                    W2[110]
                                                };
                                                v1 = arg1_198;
                                                j = v1.GetChildren;
                                                q = {
                                                    j(v1)
                                                };
                                                x = j[3];
                                                q = j[1];
                                                for x, v4 in q, ipairs(C(q)) do
                                                    j = x;
                                                    if v4:IsA("BasePart") then
                                                        v2 = w[W2[109]](v4.Name, v4.Position, v4.Size);
                                                        w[W2[110]][v2] = w[W2[110]][v2] or ;
                                                        table.insert(w[W2[110]][v2], v4);
                                                    end; 
                                                end;
                                                return; 
                                            end;
                                            w[W2[109]] = W2[112];
                                            W2[112] = 90;
                                            w[W2[112]] = W2[113];
                                            W2[114] = function(arg1_199, arg2_199, arg3_199, arg4_199, ...)
                                                local R = {
                                                    W2[109],
                                                    W2[110],
                                                    W2[111]
                                                };
                                                v1 = arg1_199;
                                                j = w[W2[109]](arg2_199, arg3_199, arg4_199);
                                                v4 = w[W2[110]][j];
                                                if not v4 then
                                                    return;
                                                end;
                                                v5 = w[W2[111]];
                                                v5[j] = w[W2[111]][j] or 1;
                                                v2 = w[W2[111]][j];
                                                v3 = v4[v2];
                                                if v3 then
                                                    v3 = w[W2[111]];
                                                    v3[j] = v3[j] + 1;
                                                    return v4[v2];
                                                end;
                                                return; 
                                            end;
                                            W2[113] = 91;
                                            w[W2[113]] = W2[114];
                                            W2[114] = 92;
                                            W2[117] = function(arg1_200, ...)
                                                local R = {
                                                    212,
                                                    210,
                                                    W2[114]
                                                };
                                                v1 = arg1_200;
                                                v4 = v1.GetChildren;
                                                j = {
                                                    v4(v1)
                                                };
                                                x = v4[2];
                                                j = v4[1];
                                                for q, v2 in ipairs(C(j)) do
                                                    v4 = q;
                                                    if v2:IsA("BasePart") then
                                                        v7 = v2:GetAttributes();
                                                        if v7 then
                                                            if v7.Boost ~= nil then
                                                                v7.Boost = {
                                                                    ["X"] = v7.Boost.X,
                                                                    ["Y"] = v7.Boost.Y,
                                                                    ["Z"] = v7.Boost.Z
                                                                };
                                                            end;
                                                            if v7.Des ~= nil then
                                                                v7.Des = w[W2[114]](v7.Des);
                                                            end;
                                                        end;
                                                        v5 = v2:FindFirstChild("Core");
                                                        if v5 then
                                                            v6 = v5:FindFirstChildWhichIsA("Sound", true);
                                                            if v6 then
                                                                v8 = tostring(v6.SoundId);
                                                                r = {
                                                                    ["SoundId"] = v8:gsub("rbxassetid://", ""),
                                                                    ["Range"] = v6.RollOffMaxDistance,
                                                                    ["Looped"] = v6.Looped,
                                                                    ["Volume"] = v6.Volume
                                                                };
                                                            end;
                                                        end;
                                                        V = tostring(v2.Material);
                                                        cA = v5;
                                                        v5 = v5;
                                                        table.insert({}, {
                                                            ["Name"] = v2.Name,
                                                            ["Position"] = {
                                                                ["X"] = v2.Position.X,
                                                                ["Y"] = v2.Position.Y,
                                                                ["Z"] = v2.Position.Z
                                                            },
                                                            ["CFrame"] = w[W2[114]](v2.CFrame),
                                                            ["Size"] = {
                                                                ["X"] = v2.Size.X,
                                                                ["Y"] = v2.Size.Y,
                                                                ["Z"] = v2.Size.Z
                                                            },
                                                            ["Attributes"] = v7,
                                                            ["Sound"] = nil,
                                                            ["Color"] = {
                                                                v2.Color.R,
                                                                v2.Color.G,
                                                                v2.Color.B
                                                            },
                                                            ["Material"] = V:gsub("Enum.Material.", ""),
                                                            ["CanCollide"] = v2.CanCollide,
                                                            ["CastShadow"] = v2.CastShadow,
                                                            ["Transparency"] = v2.Transparency,
                                                            ["Neutral"] = v2.Name == "SpawnLocation" and v2.Neutral or nil
                                                        });
                                                    end; 
                                                end;
                                                return {}; 
                                            end;
                                            w[W2[114]] = W2[115];
                                            W2[115] = 93;
                                            w[W2[115]] = W2[116];
                                            W2[116] = 94;
                                            w[W2[116]] = W2[117];
                                            W2[118] = Env[W2[119]];
                                            W2[121] = r3;
                                            W2[122] = r2;
                                            W2[123] = W2[122](W2[124], W2[125]);
                                            W2[120] = W2[121][W2[123]];
                                            W2[119] = W2[118](W2[120]);
                                            W2[117] = not W2[119];
                                            if W2[117] then
                                                W2[118] = "makefolder";
                                                W2[123] = "\xadT\xee\x99\xc5\x81";
                                                W2[124] = 1067235377648;
                                                W2[117] = Env[W2[118]];
                                                W2[120] = r3;
                                                W2[121] = r2;
                                                W2[122] = W2[121](W2[123], W2[124]);
                                                W2[119] = W2[120][W2[122]];
                                                W2[118] = W2[117](W2[119]);
                                            end;
                                            W2[123] = 52;
                                            W2[120] = 53;
                                            W2[119] = 54;
                                            W2[117] = function(...)
                                                local R = {
                                                    212,
                                                    210
                                                };
                                                q = listfiles;
                                                U = q[2];
                                                x = q[3];
                                                q = "ipairs";
                                                for x, v4 in ipairs(q("Builds")) do
                                                    j = x;
                                                    if v4:match("%.json$") then
                                                        table.insert({}, v4);
                                                    end; 
                                                end;
                                                return {}; 
                                            end;
                                            W2[118] = false;
                                            W2[126] = 55;
                                            W2[131] = "\x98\x1f\x8b\x19\x1c\x81\xa1\xa1";
                                            W2[132] = 32589907409735;
                                            w[W2[119]] = W2[118];
                                            W2[118] = nil;
                                            w[W2[120]] = W2[118];
                                            W2[121] = 56;
                                            W2[124] = 57;
                                            W2[118] = nil;
                                            W2[122] = 58;
                                            w[W2[121]] = W2[118];
                                            W2[118] = 1;
                                            w[W2[122]] = W2[118];
                                            W2[118] = 1;
                                            W2[135] = "Zv\xf7\x1a\xe6\xee";
                                            w[W2[123]] = W2[118];
                                            W2[118] = 0;
                                            w[W2[124]] = W2[118];
                                            W2[125] = 59;
                                            W2[118] = false;
                                            w[W2[125]] = W2[118];
                                            W2[118] = 0;
                                            w[W2[126]] = W2[118];
                                            W2[128] = r3;
                                            W2[129] = r2;
                                            W2[130] = W2[129](W2[131], W2[132]);
                                            W2[127] = W2[128][W2[130]];
                                            W2[118] = "AddButton";
                                            W2[118] = SA[W2[118]];
                                            W2[132] = 25565972721281;
                                            W2[131] = "\xe15m\xee\xdf\x86\x8b\xac\xd9\x12\x81\xb0\xbbHF";
                                            W2[128] = function(...)
                                                local R = {
                                                    W2[116],
                                                    212,
                                                    210,
                                                    W2[104],
                                                    245,
                                                    W2[121]
                                                };
                                                v1 = w[W2[116]](workspace.Logic);
                                                U = w[W2[116]](workspace.Map.Destructible.Buildable);
                                                x = w[W2[116]](workspace.Map.Core.Buildable);
                                                r213 = {
                                                    ["Logic"] = v1,
                                                    ["Buildable"] = U,
                                                    ["CoreBuildable"] = x
                                                };
                                                r214 = #v1 + #U + #x;
                                                if r214 == 0 then
                                                    w[W2[104]]("No parts found");
                                                    return;
                                                end;
                                                v4 = Instance.new("BindableFunction");
                                                v4.OnInvoke = function(arg1_201, ...)
                                                    local R = {
                                                        212,
                                                        210,
                                                        W2[104],
                                                        245,
                                                        44,
                                                        W2[121],
                                                        45
                                                    };
                                                    if arg1_201 == "Yes" then
                                                        task.spawn(function(...)
                                                            local R = {
                                                                210,
                                                                W2[116],
                                                                212,
                                                                W2[104],
                                                                245,
                                                                W2[121],
                                                                45
                                                            };
                                                            w[W2[116]]("Scanning parts...");
                                                            v1 = "Builds/Build_" .. os.time() .. ".json";
                                                            U = w[W2[104]];
                                                            writefile(v1, U:JSONEncode(r23));
                                                            v5 = w[W2[121]];
                                                            v5:AddOption(v1);
                                                            w[W2[116]]("Save complete \xe2\x9c\x94 (" .. r214 .. " parts) as " .. v1);
                                                            return; 
                                                        end);
                                                    end;
                                                    return; 
                                                end;
                                                v5 = game;
                                                v3 = v5:GetService("StarterGui");
                                                v3:SetCore("SendNotification", {
                                                    ["Title"] = "TBO",
                                                    ["Text"] = "This Map Has " .. r214 .. " Parts Are You Sure you Want to Save it",
                                                    ["Duration"] = 9000000000,
                                                    ["Callback"] = v4,
                                                    ["Button1"] = "Yes",
                                                    ["Button2"] = "No"
                                                });
                                                return; 
                                            end;
                                            W2[118] = W2[118](SA, W2[127], W2[128]);
                                            W2[128] = r3;
                                            W2[129] = r2;
                                            W2[130] = W2[129](W2[131], W2[132]);
                                            W2[129] = function(arg1_202, ...)
                                                local R = {
                                                    W2[125],
                                                    W2[119],
                                                    W2[122],
                                                    W2[123],
                                                    W2[124],
                                                    212,
                                                    210,
                                                    W2[120],
                                                    W2[104]
                                                };
                                                v1 = arg1_202;
                                                w[W2[125]] = true;
                                                w[W2[119]] = false;
                                                w[W2[122]] = 1;
                                                w[W2[123]] = 1;
                                                w[W2[124]] = 0;
                                                task.wait();
                                                w[W2[125]] = false;
                                                w[W2[120]] = v1;
                                                w[W2[104]]("Selected file: " .. v1);
                                                return; 
                                            end;
                                            W2[127] = W2[128][W2[130]];
                                            W2[130] = false;
                                            W2[132] = r3;
                                            W2[118] = "AddDropdown";
                                            W2[133] = r2;
                                            W2[128] = {};
                                            W2[136] = 20325530117368;
                                            W2[134] = W2[133](W2[135], W2[136]);
                                            W2[118] = SA[W2[118]];
                                            W2[131] = W2[132][W2[134]];
                                            W2[118] = W2[118](SA, W2[127], W2[128], W2[129], W2[130], W2[131]);
                                            w[W2[121]] = W2[118];
                                            W2[128] = "ipairs";
                                            W2[127] = Env[W2[128]];
                                            W2[131] = {
                                                W2[117]()
                                            };
                                            W2[132] = {
                                                W2[127](C(W2[131]))
                                            };
                                            W2[128] = W2[132][1];
                                            W2[130] = W2[132][3];
                                            W2[129] = W2[132][2];
                                            W2[130], W2[131] = W2[128](W2[129], W2[130]);
                                            while W2[130] do
                                                W2[132] = w[W2[121]];
                                                W2[133] = "AddOption";
                                                W2[127] = W2[130];
                                                W2[133] = W2[132][W2[133]];
                                                W2[127] = nil;
                                                W2[133] = W2[133](W2[132], W2[131]);
                                                W2[131] = nil; 
                                            end;
                                            W2[129] = r3;
                                            W2[132] = "\x0c \x1d\x06\xc5uYx\x98>\xad\x1d&\xb2";
                                            W2[133] = 15582193425496;
                                            W2[130] = r2;
                                            W2[131] = W2[130](W2[132], W2[133]);
                                            W2[128] = W2[129][W2[131]];
                                            W2[107] = nil;
                                            W2[132] = "G\x8ew\xb32\xfdBf\xb4";
                                            W2[129] = false;
                                            W2[130] = function(arg1_203, ...)
                                                local R = {
                                                    163,
                                                    212,
                                                    210,
                                                    W2[68]
                                                };
                                                if arg1_203 then
                                                    v5 = r38;
                                                    v5:BindToRenderStep("AntiBuildLag", 0, function(...)
                                                        local R = {
                                                            W2[68],
                                                            212,
                                                            210
                                                        };
                                                        v5 = r38.PlayerGui;
                                                        v1 = v5:FindFirstChild("BuildTools");
                                                        if v1 then
                                                            v1:Destroy();
                                                        end;
                                                        return; 
                                                    end);
                                                else
                                                    v5 = r38;
                                                    v5:UnbindFromRenderStep("AntiBuildLag");
                                                end;
                                                return; 
                                            end;
                                            W2[127] = "AddToggle";
                                            W2[127] = SA[W2[127]];
                                            W2[121] = nil;
                                            W2[127] = W2[127](SA, W2[128], W2[129], W2[130]);
                                            W2[127] = "AddToggle";
                                            W2[117] = nil;
                                            W2[129] = r3;
                                            W2[130] = r2;
                                            W2[116] = nil;
                                            W2[114] = nil;
                                            W2[133] = 979864617416;
                                            W2[131] = W2[130](W2[132], W2[133]);
                                            W2[128] = W2[129][W2[131]];
                                            W2[129] = false;
                                            W2[127] = SA[W2[127]];
                                            W2[130] = function(arg1_204, ...)
                                                local R = {
                                                    W2[119],
                                                    W2[125],
                                                    W2[126],
                                                    W2[110],
                                                    W2[111],
                                                    W2[112],
                                                    212,
                                                    210,
                                                    W2[120],
                                                    W2[104],
                                                    W2[108],
                                                    245,
                                                    W2[122],
                                                    W2[123],
                                                    W2[113],
                                                    W2[93],
                                                    W2[109],
                                                    W2[105],
                                                    W2[115],
                                                    W2[106],
                                                    W2[124]
                                                };
                                                v1 = arg1_204;
                                                x = not v1;
                                                w[W2[119]] = v1;
                                                v3 = x;
                                                U = v1;
                                                if x then
                                                    v5 = v5;
                                                    if x then
                                                        return;
                                                    end;
                                                    w[W2[126]] = w[W2[126]] + 1;
                                                    w[W2[110]] = {};
                                                    w[W2[111]] = {};
                                                    w[W2[112]](workspace.Logic);
                                                    w[W2[112]](workspace.Map.Destructible.Buildable);
                                                    w[W2[112]](workspace.Map.Core.Buildable);
                                                    r215 = w[W2[126]];
                                                    task.spawn(function(...)
                                                        local R = {
                                                            W2[120],
                                                            W2[104],
                                                            212,
                                                            210,
                                                            W2[108],
                                                            W2[119],
                                                            245,
                                                            W2[122],
                                                            W2[123],
                                                            154,
                                                            W2[126],
                                                            W2[113],
                                                            W2[93],
                                                            W2[109],
                                                            W2[110],
                                                            W2[105],
                                                            W2[115],
                                                            W2[106],
                                                            W2[124]
                                                        };
                                                        if not w[W2[119]] or not isfile(w[W2[119]]) then
                                                            w[W2[125]]("No file selected");
                                                            return;
                                                        end;
                                                        if not w[W2[111]]() then
                                                            w[W2[112]] = false;
                                                            w[W2[125]]("You don't have a build");
                                                            return;
                                                        end;
                                                        v3 = r3;
                                                        v1 = v3:JSONDecode(readfile(w[W2[119]]));
                                                        x = {
                                                            {
                                                                workspace.Logic,
                                                                v1.Logic
                                                            },
                                                            {
                                                                workspace.Map.Destructible.Buildable,
                                                                v1.Buildable
                                                            },
                                                            {
                                                                workspace.Map.Core.Buildable,
                                                                v1.CoreBuildable,
                                                                true,
                                                                false
                                                            }
                                                        };
                                                        v3 = r2;
                                                        v2 = 1 < 0;
                                                        for q = v3, #x do
                                                            v8 = {
                                                                unpack(x[q])
                                                            };
                                                            v6 = v8[3];
                                                            a = v8[4];
                                                            r = v8[1];
                                                            v3 = w[W2[120]];
                                                            A = 1 < 0;
                                                            for o = v3, #v8[2] do
                                                                g = o;
                                                                if w[W2[104]] ~= w[W2[108]] then
                                                                    return;
                                                                else
                                                                    while not w[W2[112]] do
                                                                        if w[W2[104]] ~= w[W2[108]] then
                                                                            return;
                                                                        else
                                                                            task.wait();
                                                                        end; 
                                                                    end;
                                                                    d = w[W2[111]];
                                                                    if not d() then
                                                                        w[W2[112]] = false;
                                                                        w[W2[125]]("You don't have a build");
                                                                        return;
                                                                    else
                                                                        d = v8[2][o];
                                                                        p = v6;
                                                                        F = v5;
                                                                        if v6 then
                                                                            p = workspace.Map.Destructible.Buildable;
                                                                        end;
                                                                        v5 = v5;
                                                                        if p then
                                                                            v5 = v5;
                                                                            p = r23(p, d.Name, Vector3.new(d.Position.X, d.Position.Y, d.Position.Z), Vector3.new(d.Size.X, d.Size.Y, d.Size.Z));
                                                                            v5 = v5;
                                                                            if not p and d.Name == "SpawnLocation" then
                                                                                r23(p, "Spawn", Vector3.new(d.Position.X, d.Position.Y, d.Position.Z), Vector3.new(d.Size.X, d.Size.Y, S[Z]));
                                                                            end;
                                                                            if not p then
                                                                                F = w[W2[122]];
                                                                                K = d.Name == "SpawnLocation" and "Spawn";
                                                                                v5 = m;
                                                                                v5 = m;
                                                                                F:FireServer("Create", K or d.Name, Vector3.new(d.Position.X, d.Position.Y, d.Position.Z));
                                                                                S = v5;
                                                                                F = p;
                                                                                if p then
                                                                                    v5 = v5;
                                                                                    task.wait();
                                                                                    K = p.GetChildren;
                                                                                    V = {
                                                                                        K(p)
                                                                                    };
                                                                                    CA = K[3];
                                                                                    for CA, V in K[1], ipairs(C(V)) do
                                                                                        F = CA;
                                                                                        v5 = v5;
                                                                                        if V:IsA("BasePart") and (V.Position - Vector3.new(d.Position.X, d.Position.Y, d.Position.Z)).Magnitude < .05 then
                                                                                            p = V;
                                                                                            iA = w[W2[123]](V.Name, V.Position, V.Size);
                                                                                            w[W2[113]][iA] = w[W2[113]][iA] or ;
                                                                                            v5 = v5;
                                                                                            table.insert(w[W2[113]][iA], V);
                                                                                        else
                                                                                            
                                                                                        end; 
                                                                                    end;
                                                                                    S = v5;
                                                                                    if p then
                                                                                        v5 = S;
                                                                                        if p then
                                                                                            v5 = v5;
                                                                                            if not r23(v9, d[Z[V]], O, B) or w[W2[104]] ~= w[W2[108]] then
                                                                                                return;
                                                                                            else
                                                                                                table.insert(w[W2[93]], {
                                                                                                    r23(v9, d[Z[V]], O, B),
                                                                                                    w[W2[109]](d.CFrame),
                                                                                                    Vector3.new(d.Size.X, d.Size.Y, S[Z])
                                                                                                });
                                                                                                if #w[W2[93]] >= w[W2[105]] then
                                                                                                    F = w[W2[122]];
                                                                                                    F:FireServer("Move", w[W2[93]]);
                                                                                                    table.clear(w[W2[93]]);
                                                                                                end;
                                                                                                TA = 25722715025098;
                                                                                                F = d.Name == w[W2[126]][w[W2[110]]("\xca\x9eA\x7f\xa2\x1f\xfcS\xfc\x0b\rk\x1a", TA)];
                                                                                                if F then
                                                                                                    F = w[W2[122]];
                                                                                                    F:FireServer("Neutral", {
                                                                                                        r23(v9, d[Z[V]], O, B)
                                                                                                    }, t[g].Neutral);
                                                                                                end;
                                                                                                S = "Attributes";
                                                                                                F = d[S];
                                                                                                if F then
                                                                                                    F = d.Attributes.I;
                                                                                                    S = d.Attributes.O;
                                                                                                    vA = w[W2[110]];
                                                                                                    TA = "Attributes";
                                                                                                    iA = d[TA];
                                                                                                    G = TA[3];
                                                                                                    for G, iA in TA[1], pairs(iA) do
                                                                                                        hA = S;
                                                                                                        vA = G == "DMG" and "Damage";
                                                                                                        v5 = S;
                                                                                                        if vA then
                                                                                                            v5 = S;
                                                                                                            hA = vA == "Des";
                                                                                                            if hA then
                                                                                                                hA = w[W2[122]];
                                                                                                                hA:FireServer("LogicProp", {
                                                                                                                    r23(v9, d[Z[V]], O, B)
                                                                                                                }, "Destination", {
                                                                                                                    w[W2[109]](iA)
                                                                                                                });
                                                                                                            else
                                                                                                                hA = vA == "Boost";
                                                                                                                if hA then
                                                                                                                    hA = w[W2[122]];
                                                                                                                    hA:FireServer("LogicProp", {
                                                                                                                        r23(v9, d[Z[V]], O, B)
                                                                                                                    }, "Boost", Vector3.new(iA.X, iA.Y, iA.Z));
                                                                                                                else
                                                                                                                    hA = vA == "CD";
                                                                                                                    if hA then
                                                                                                                        hA = w[W2[122]];
                                                                                                                        hA:FireServer("LogicProp", {
                                                                                                                            r23(v9, d[Z[V]], O, B)
                                                                                                                        }, "Cooldown", tonumber(iA));
                                                                                                                    else
                                                                                                                        hA = vA == "IMG";
                                                                                                                        if hA then
                                                                                                                            hA = w[W2[122]];
                                                                                                                            hA:FireServer("LogicProp", {
                                                                                                                                r23(v9, d[Z[V]], O, B)
                                                                                                                            }, "Image", tostring(t[g].Attributes.IMG));
                                                                                                                        else
                                                                                                                            hA = vA == "Time";
                                                                                                                            if hA then
                                                                                                                                hA = w[W2[122]];
                                                                                                                                hA:FireServer("LogicProp", {
                                                                                                                                    r23(v9, d[Z[V]], O, B)
                                                                                                                                }, "Delay", tostring(iA));
                                                                                                                            else
                                                                                                                                hA = TA ~= "I" and TA ~= "O";
                                                                                                                                v5 = S;
                                                                                                                                if hA then
                                                                                                                                    hA = w[W2[122]];
                                                                                                                                    hA:FireServer("LogicProp", {
                                                                                                                                        r23(v9, d[Z[V]], O, B)
                                                                                                                                    }, vA, iA);
                                                                                                                                end;
                                                                                                                            end;
                                                                                                                        end;
                                                                                                                    end;
                                                                                                                end;
                                                                                                            end;
                                                                                                        else
                                                                                                            TA = G;
                                                                                                        end; 
                                                                                                    end;
                                                                                                    if F then
                                                                                                        v5 = S;
                                                                                                        if F then
                                                                                                            Z = w[W2[122]];
                                                                                                            V = "Inputs";
                                                                                                            iA = F;
                                                                                                            TA = v5;
                                                                                                            G = {
                                                                                                                r23(v9, d[Z[V]], O, B)
                                                                                                            };
                                                                                                            if F then
                                                                                                                v5 = v5;
                                                                                                                TA = S;
                                                                                                                hA = v5;
                                                                                                                if S then
                                                                                                                    v5 = v5;
                                                                                                                    Z:FireServer(w[W2[126]][w[W2[110]](hA, vA)], {
                                                                                                                        p
                                                                                                                    }, F, TA);
                                                                                                                    if d.Sound then
                                                                                                                        F = d.Sound.SoundId and d.Sound.SoundId ~= "";
                                                                                                                        v5 = v5;
                                                                                                                        if F then
                                                                                                                            F = w[W2[122]];
                                                                                                                            F:FireServer("LogicProp", {
                                                                                                                                r23(v9, d[Z[V]], O, B)
                                                                                                                            }, "SoundId", t[g].Sound.SoundId);
                                                                                                                        end;
                                                                                                                        F = d.Sound.Range;
                                                                                                                        if F then
                                                                                                                            F = w[W2[122]];
                                                                                                                            F:FireServer("LogicProp", {
                                                                                                                                r23(v9, d[Z[V]], O, B)
                                                                                                                            }, "SoundRange", tonumber(t[g].Sound.Range));
                                                                                                                        end;
                                                                                                                        F = d.Sound.Looped ~= nil;
                                                                                                                        if F then
                                                                                                                            F = w[W2[122]];
                                                                                                                            F:FireServer("LogicProp", {
                                                                                                                                r23(v9, d[Z[V]], O, B)
                                                                                                                            }, "SoundLoop", t[g].Sound.Looped);
                                                                                                                        end;
                                                                                                                        F = d.Sound.Volume ~= nil;
                                                                                                                        if F then
                                                                                                                            F = w[W2[122]];
                                                                                                                            F:FireServer("LogicProp", {
                                                                                                                                r23(v9, d[Z[V]], O, B)
                                                                                                                            }, "SoundVol", tostring(t[g].Sound.Volume));
                                                                                                                        end;
                                                                                                                    end;
                                                                                                                    F = w[W2[122]];
                                                                                                                    F:FireServer("Color", {
                                                                                                                        p
                                                                                                                    }, Color3.new(d.Color[1], d.Color[2], d.Color[3]));
                                                                                                                    F = w[W2[122]];
                                                                                                                    F:FireServer("Material", {
                                                                                                                        p
                                                                                                                    }, d.Material);
                                                                                                                    F = w[W2[122]];
                                                                                                                    F:FireServer("Transparency", {
                                                                                                                        p
                                                                                                                    }, d.Transparency);
                                                                                                                    F = w[W2[122]];
                                                                                                                    F:FireServer("Collide", {
                                                                                                                        p
                                                                                                                    }, d.CastShadow, d.CanCollide);
                                                                                                                    F = v8[4] ~= nil;
                                                                                                                    if F then
                                                                                                                        F = w[W2[122]];
                                                                                                                        F:FireServer("Breakable", {
                                                                                                                            r23(v9, d[Z[V]], O, B)
                                                                                                                        }, v8[4]);
                                                                                                                    end;
                                                                                                                    w[W2[115]] = w[W2[115]] + 1;
                                                                                                                    w[W2[120]] = o + 1;
                                                                                                                    r2 = q;
                                                                                                                    w[W2[125]]("Building: " .. w[W2[115]] .. " / " .. #v1.Logic + #v1.Buildable + #v1.CoreBuildable);
                                                                                                                else
                                                                                                                    TA = "";
                                                                                                                end;
                                                                                                            else
                                                                                                                iA = "";
                                                                                                            end;
                                                                                                        end;
                                                                                                    else
                                                                                                        Z = d.Attributes.O;
                                                                                                    end;
                                                                                                end;
                                                                                            end;
                                                                                        end;
                                                                                    else
                                                                                        F = w[W2[104]] ~= w[W2[108]];
                                                                                    end;
                                                                                else
                                                                                    F = w[W2[104]] ~= w[W2[108]];
                                                                                end;
                                                                            end;
                                                                        else
                                                                            v9 = v8[1];
                                                                        end;
                                                                    end;
                                                                end; 
                                                            end;
                                                            w[W2[120]] = 1; 
                                                        end;
                                                        if #w[W2[93]] > 0 then
                                                            q = w[W2[122]];
                                                            q:FireServer("Move", w[W2[93]]);
                                                            table.clear(w[W2[93]]);
                                                        end;
                                                        w[W2[125]]("Build complete \xe2\x9c\x94 (" .. #v1.Logic + #v1.Buildable + #v1.CoreBuildable .. " parts)");
                                                        r2 = 1;
                                                        w[W2[120]] = 1;
                                                        w[W2[115]] = 0;
                                                        return; 
                                                    end);
                                                    return;
                                                else
                                                    v3 = w[W2[125]];
                                                end; 
                                            end;
                                            W2[125] = nil;
                                            W2[113] = nil;
                                            W2[109] = nil;
                                            W2[111] = nil;
                                            W2[127] = W2[127](SA, W2[128], W2[129], W2[130]);
                                            W2[123] = nil;
                                            W2[119] = nil;
                                            W2[120] = nil;
                                            W2[93] = nil;
                                            W2[126] = nil;
                                            W2[106] = nil;
                                            W2[110] = nil;
                                            W2[124] = nil;
                                            W2[115] = nil;
                                            W2[104] = nil;
                                            W2[105] = nil;
                                            W2[122] = nil;
                                            W2[112] = nil;
                                            W2[108] = nil;
                                        end;
                                        W2[105] = r3;
                                        W2[37] = nil;
                                        W2[16] = nil;
                                        W2[34] = nil;
                                        W2[102] = nil;
                                        W2[109] = 22761014733158;
                                        W2[70] = nil;
                                        W2[60] = nil;
                                        W2[47] = nil;
                                        W2[108] = "!\x06'\xf3J=\x14\x99XN\"\x10\x84\x8c\x07\x1f\xf6\xebJ";
                                        W2[31] = nil;
                                        W2[65] = nil;
                                        W2[106] = r2;
                                        W2[107] = W2[106](W2[108], W2[109]);
                                        W2[90] = nil;
                                        W2[69] = nil;
                                        W2[104] = W2[105][W2[107]];
                                        W2[99] = nil;
                                        W2[93] = "AddButton";
                                        W2[30] = nil;
                                        W2[79] = nil;
                                        W2[75] = nil;
                                        W2[87] = nil;
                                        W2[12] = nil;
                                        W2[73] = nil;
                                        W2[111] = 2556084683942;
                                        W2[108] = "a.\xc8\xe6\x9d\x05~\x88";
                                        W2[93] = VA[W2[93]];
                                        W2[32] = nil;
                                        W2[20] = nil;
                                        W2[109] = 9118367600790;
                                        W2[3] = nil;
                                        W2[105] = function(...)
                                            local R = {
                                                212,
                                                210
                                            };
                                            if setclipboard then
                                                setclipboard("https://discord.gg/jwYqu66bqm");
                                            else
                                                if toclipboard then
                                                    toclipboard("https://discord.gg/jwYqu66bqm");
                                                end;
                                                Notify({
                                                    ["Title"] = "TBO Discord",
                                                    ["Description"] = "https://discord.gg/TBO",
                                                    ["Duration"] = 5
                                                });
                                                return;
                                            end; 
                                        end;
                                        W2[89] = nil;
                                        W2[23] = nil;
                                        W2[93] = W2[93](VA, W2[104], W2[105]);
                                        W2[85] = nil;
                                        W2[105] = r3;
                                        W2[25] = nil;
                                        W2[86] = nil;
                                        W2[10] = nil;
                                        W2[106] = r2;
                                        W2[107] = W2[106](W2[108], W2[109]);
                                        W2[44] = nil;
                                        W2[108] = 27300981273001;
                                        W2[53] = nil;
                                        W2[17] = nil;
                                        W2[93] = "AddSection";
                                        W2[74] = nil;
                                        W2[24] = nil;
                                        W2[38] = nil;
                                        W2[104] = W2[105][W2[107]];
                                        W2[50] = nil;
                                        W2[62] = nil;
                                        W2[21] = nil;
                                        W2[42] = nil;
                                        W2[93] = VA[W2[93]];
                                        W2[93] = W2[93](VA, W2[104]);
                                        W2[28] = nil;
                                        W2[64] = nil;
                                        W2[84] = nil;
                                        W2[82] = nil;
                                        W2[104] = r3;
                                        W2[76] = nil;
                                        W2[68] = nil;
                                        W2[48] = nil;
                                        W2[107] = "";
                                        W2[51] = nil;
                                        W2[105] = r2;
                                        W2[40] = nil;
                                        W2[109] = "\xc0!0\xc4\x8c\xfe(";
                                        W2[7] = nil;
                                        W2[26] = nil;
                                        W2[67] = nil;
                                        W2[103] = nil;
                                        W2[46] = nil;
                                        W2[45] = nil;
                                        W2[106] = W2[105](W2[107], W2[108]);
                                        W2[43] = nil;
                                        W2[93] = W2[104][W2[106]];
                                        W2[104] = 60;
                                        w[W2[104]] = W2[93];
                                        W2[106] = r3;
                                        W2[110] = 12624913471222;
                                        W2[72] = nil;
                                        W2[107] = r2;
                                        W2[83] = nil;
                                        W2[112] = 19140231013072;
                                        W2[108] = W2[107](W2[109], W2[110]);
                                        W2[33] = nil;
                                        W2[80] = nil;
                                        W2[110] = "\x83\xfc\x8fd\x06\xf1\x1f\xf5\xf5\x1bz\xdfw1\xd1\xe0\x0c \xf4\xfa\x15\x83\xa9\xc2m+\x91\x82sK";
                                        W2[78] = nil;
                                        W2[93] = "AddTextBox";
                                        W2[6] = nil;
                                        W2[61] = nil;
                                        W2[105] = W2[106][W2[108]];
                                        W2[93] = VA[W2[93]];
                                        W2[107] = r3;
                                        W2[39] = nil;
                                        W2[15] = nil;
                                        W2[108] = r2;
                                        W2[109] = W2[108](W2[110], W2[111]);
                                        W2[27] = nil;
                                        W2[41] = nil;
                                        W2[108] = true;
                                        W2[106] = W2[107][W2[109]];
                                        W2[57] = nil;
                                        W2[107] = function(arg1_205, ...)
                                            w[W2[104]] = arg1_205;
                                            return; 
                                        end;
                                        W2[93] = W2[93](VA, W2[105], W2[106], W2[107], W2[108]);
                                        W2[111] = "\xa5\xb9X\xa4E`\xa6\x0b\x1f\xd7\xbb\xae\xe9{\x90\x98\x85\xfd\x89R%\x13J'\xd4\xc9,g\xcek";
                                        W2[105] = "commentTextbox";
                                        Env[W2[105]] = W2[93];
                                        W2[54] = nil;
                                        W2[1] = nil;
                                        W2[77] = nil;
                                        W2[96] = nil;
                                        W2[29] = nil;
                                        W2[106] = function(arg1_206, arg2_206, ...)
                                            local R = {
                                                212,
                                                210,
                                                277,
                                                W2[104]
                                            };
                                            U = arg2_206;
                                            if U == "" then
                                                warn("No comment to send!");
                                                return;
                                            end;
                                            a = game;
                                            o = a:GetService("HttpService");
                                            r22({
                                                ["Url"] = "https://peeky.pythonanywhere.com/webhook/XFiNLGnfhC8M",
                                                ["Method"] = "POST",
                                                ["Headers"] = {
                                                    ["Content-Type"] = "application/json"
                                                },
                                                ["Body"] = o:JSONEncode({
                                                    ["content"] = arg1_206 .. U
                                                })
                                            });
                                            w[W2[104]] = "";
                                            return; 
                                        end;
                                        W2[105] = 61;
                                        W2[81] = nil;
                                        W2[92] = nil;
                                        w[W2[105]] = W2[106];
                                        W2[98] = nil;
                                        W2[108] = r3;
                                        W2[55] = nil;
                                        W2[66] = nil;
                                        W2[109] = r2;
                                        W2[106] = "AddButton";
                                        W2[9] = nil;
                                        W2[110] = W2[109](W2[111], W2[112]);
                                        W2[5] = nil;
                                        W2[94] = nil;
                                        W2[101] = nil;
                                        W2[8] = nil;
                                        W2[2] = nil;
                                        W2[14] = nil;
                                        W2[52] = nil;
                                        W2[13] = nil;
                                        W2[88] = nil;
                                        W2[106] = VA[W2[106]];
                                        W2[18] = nil;
                                        W2[107] = W2[108][W2[110]];
                                        W2[112] = 5415377078745;
                                        W2[97] = nil;
                                        W2[19] = nil;
                                        W2[4] = nil;
                                        W2[111] = "\xb0\xb1\xd8\\\xb5\xf6\x99_\xf8(\xed\xc7\xc8X\x99\x9a\xaf5\xad[\xd3\xa3}?\x11\x020\xa1\xc6\xcaS\x93AIt\xdd\xb3\x8e'";
                                        W2[91] = nil;
                                        W2[108] = function(...)
                                            local R = {
                                                W2[105],
                                                212,
                                                210,
                                                W2[104]
                                            };
                                            w[W2[105]]("**Comment/Rate:** ", w[W2[104]]);
                                            return; 
                                        end;
                                        W2[106] = W2[106](VA, W2[107], W2[108]);
                                        W2[108] = r3;
                                        W2[109] = r2;
                                        W2[63] = nil;
                                        W2[110] = W2[109](W2[111], W2[112]);
                                        W2[106] = "AddButton";
                                        W2[22] = nil;
                                        W2[11] = nil;
                                        W2[71] = nil;
                                        W2[107] = W2[108][W2[110]];
                                        W2[100] = nil;
                                        W2[108] = function(...)
                                            local R = {
                                                W2[105],
                                                212,
                                                210,
                                                W2[104]
                                            };
                                            w[W2[105]]("**Suggestion/Bug Report:** ", w[W2[104]]);
                                            return; 
                                        end;
                                        W2[59] = nil;
                                        W2[105] = nil;
                                        W2[58] = nil;
                                        W2[106] = VA[W2[106]];
                                        W2[106] = W2[106](VA, W2[107], W2[108]);
                                        W2[95] = nil;
                                        W2[49] = nil;
                                        W2[104] = nil;
                                    end;
                                end;
                            end;
                        end;
                    end;
                    return;
                end;
            end;
        end;
    end;
end;
return (function(...)
    while true do
        l1 = l2;
        l2 = l1;
        r1(); 
    end;
    return; 
end)();