def maxDistance(colors):
    l, r = 0, len(colors) - 1
        
    ans = 0
        
    for i in range(len(colors) - 1):
        if colors[i] != colors[l]:
            ans = max(ans, abs(l - i))
        if colors[i] != colors[r]:
            ans = max(ans, abs(r - i))
                
    return ans