from MarsRover.CoordinateToSquare import CoordinateToSquare
from MarsRover.Mars import Mars
from MarsRover.Pilot import Pilot
from MarsRover.Location import Location
from MarsRover.Rover import Rover


def main():
    # Requests the pilots name and save it as a variable
    pilot_name = Pilot(input("What is your name?\n"))
    print("Hello " + pilot_name.pilot_name + ", welcome to the Mars Rover")

    # Creates mars with default size of 0 by 0
    mars = Mars()

    # Sets the width of the the grid mars (x)
    print("Please specify the width of Mars, this would be the max possible value for the x co-ordinate.")
    while True:
        try:
            mars.width = int(input())
            break
        except ValueError:
            # if the user enters anything other then a number the program will not proceed
            print("That is not a number. Please enter a number")

    # Sets the height of the the grid mars (y)
    print("Please specify the height of Mars, this would be the max possible value for the x co-ordinate.")
    while True:
        try:
            mars.height = int(input())
            break
        except ValueError:
            # if the user enters anything other then a number the program will not proceed
            print("That is not a number. Please enter a number")

    # Test print out to confirm that grid is size set by user
    print("Mars has been initialised as a grid of ", mars.width, " by ", mars.height)

    # Sets the start x coordinate of the rover
    print("Please specify the x start co-ordinate of the rover")
    while True:
        try:
            rover_start_x = int(input())
            break
        except ValueError:
            # if the user enters anything other then a number the program will not proceed
            print("That is not a number. Please enter a number")

    # Sets the start y coordinate of the rover
    print("Please specify the y start co-ordinate of the rover")
    while True:
        try:
            rover_start_y = int(input())
            break
        except ValueError:
            # if the user enters anything other then a number the program will not proceed
            print("That is not a number. Please enter a number")

    # Test print out to confirm that the start location of the rover is location set by user
    print("The rover will begin at: (", rover_start_x, ",", rover_start_y, ")")

    # Sets the start location of that will be used by the rover
    location = Location(rover_start_x, rover_start_y)

    # Get the start bearing of the rover
    print("Please specify the start bearing of the rover,\nN = 1,\nE = 2\nS = 3,\nW = 4")
    while True:
        try:
            rover_start_bearing = int((input()))
            break
        except ValueError:
            # if the user enters anything other then a number the program will not proceed
            print("That is not a number. Please enter a number")

    # Initialises the Rover
    rover = Rover(mars, location, rover_start_bearing)

    # Variable to exit moving rover loop
    end = 0
    start_square = CoordinateToSquare(rover.location.x, rover.location.y, rover.mars.width)
    # Converts rover bearing number to N, E, S, or W
    if rover.bearing == 1:
        direction = 'N'
    elif rover.bearing == 2:
        direction = 'E'
    elif rover.bearing == 3:
        direction = 'S'
    else:
        direction = 'W'

    # While loop for moving rover
    while end != 2:
        print("The rover is in square ", start_square.square, " with a current bearing of ", direction)
        print("Please enter how you would like to move the rover\n"
              "-1 to turn left\n"
              "-2 to turn right\n"
              "Enter a positive number to move forward that number of squares\n"
              "-3 to exit the rover:")

        # While loop for taking 5 inputs
        i = 0
        while i < 5:
            while True:
                try:
                    control = int((input()))
                    break
                except ValueError:
                    # if the user enters anything other then a number the program will not proceed
                    print("That is not a number. Please enter a number")

            if control == -1:
                rover.turn_left()
            elif control == -2:
                rover.turn_left()
            elif control == -3:
                i = 5
            else:
                rover.move(control)
            i = i + 1

        # Converts rover bearing number to N, E, S, or W
        if rover.bearing == 1:
            direction = 'N'
        elif rover.bearing == 2:
            direction = 'E'
        elif rover.bearing == 3:
            direction = 'S'
        else:
            direction = 'W'

        # Converts finish location coordinate to Square number in grid
        finish_square = CoordinateToSquare(rover.location.x, rover.location.y, rover.mars.width)
        print("The rover is in square ", finish_square.square, " with a current bearing of ", direction)

        start_square = finish_square

        # Takes input from user and stores it as variable done
        print("Would you like to move the rover again? 1 for yes, 2 for no")
        while True:
            try:
                done = int(input())
                break
            except ValueError:
                # if the user enters anything other then a number the program will not proceed
                print("That is not a number. Please enter a number")

        # If done is equal to 2 then the variable end will be set to 2, movement loop will close and program end
        if done == 2:
            end = 2


if __name__ == '__main__':
    main()
