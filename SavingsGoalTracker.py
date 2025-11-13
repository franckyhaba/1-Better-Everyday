print  ('\n=== Welcome to the saving goal tracker! ===\n')


savingTotals = (
    
    200 #emergency       
    ,300# mutual 
    ,500 #travel 
    ,1000 #device
    ) #emergency fund, mutual, travel fund, device fund

emergencySaving= []
mutualSaving= []
travelSaving =  []
deviceSaving= []

print("Please enter the saving for the month: \n")
emergencySaving.append (float(input("Emergency savings for this month(£):  ")))
mutualSaving.append (float(input("Mutual savings for this month(£):  ")))
travelSaving.append (float(input("Travel savings for this month(£):  ")))
deviceSaving.append (float(input("Device savings for this month(£):  ")))

#calc so now i want to calc and show the total and the limit.

totalEmergencySavings = sum (emergencySaving)
totalMutualSavings = sum (mutualSaving)
totalTravelSavings = sum (travelSaving)
totalDeviceSavings = sum (deviceSaving)

print ("==== Monthly budget====")
print (f"Emergency: £{totalEmergencySavings}/{savingTotals[0]}")
print (f"Mutual: £{totalMutualSavings}/{savingTotals[1]}")
print (f"Travel: £{totalTravelSavings}/{savingTotals[2]}")
print (f"Device: £{totalDeviceSavings}/{savingTotals[3]}")





