def growingPlant(upSpeed, downSpeed, desiredHeight):
    height = upSpeed
    day = 1
    while (height < desiredHeight):
        height -= downSpeed
        day += 1
        height += upSpeed
    return day
