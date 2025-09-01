guest = ['Messi','Pele', 'Ronaldo']

guest.insert(0,'Ozil')
guest.insert(4,'Saka')
guest.insert(5,'Neymar')   

guest.append('Kroos')
guest.append('Yaya')
guest.append('Drogba')

# Pop guests until only 2 remain
print(f"{guest.pop()}, can't make the dinner.")
print(f"{guest.pop()}, can't make the dinner.")
print(f"{guest.pop()}, can't make the dinner.")
print(f"{guest.pop()}, can't make the dinner.")
print(f"{guest.pop()}, can't make the dinner.")
print(f"{guest.pop()}, can't make the dinner.")
print(f"{guest.pop()}, can't make the dinner.")

guestMsg = f"\n{guest}, can still make the event."
print(guestMsg)

# Delete the final 2 guests
del guest[0]
del guest[0]

# Show final list
print("\nFinal guest list:", guest)
