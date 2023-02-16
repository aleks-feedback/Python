supported = ["Lights off", "Lock the door", 
    "Open the door", "Make coffee", "Shut down"]
command=str(input())
if command in supported:
    print("OK")
else:
     print("Unknown")
