car=""
while(car!='quit'):
    car = input(">").lower()
    # car_quit = car
    if car=='start':
        print("To start the car")
    elif car=='stop':
        print("To stop the car")
    elif car=='quit':
        break
    else:
        print("I don't understand that...")