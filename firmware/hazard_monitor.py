water_level = 72
rain_intensity = 80
hazard_indicator = 65

print("SMART MONSOON ELECTRICAL SAFETY SYSTEM")
print("--------------------------------------")

print(f"Water Level      : {water_level}%")
print(f"Rain Intensity   : {rain_intensity}%")
print(f"Hazard Indicator : {hazard_indicator}%")

if hazard_indicator >= 70 and water_level >= 60:
    print("STATUS: DANGER")
    print("ALERT: ELECTRICAL HAZARD DETECTED")
elif water_level >= 60:
    print("STATUS: CAUTION")
    print("WARNING: WATERLOGGING DETECTED")
else:
    print("STATUS: SAFE")
