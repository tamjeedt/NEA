#Mechanics Simulator
#Author: Tamjeed Tawsif 13D
#Date started: 15/08/22
#Date finished: TBD


#Imported modules
import sys
#Maths module imported for all calculations involving trigonometry and square roots
import math
#Tabulate is used to make the tables in each topic more presentable
from tabulate import tabulate




#2D Array containing any trigonometric values needed for calculations
trig_values = [["angle in degrees", "sin", "cos", "tan"],
               [30, 0.5, 0.8660254038, 0.5773502692],
               [45, 0.7071067812, 0.7071067812, 1],
               [60, 0.8660254038, 0.5, 1.732050808],
               [90, 1, 0, -1], #-1 is used to represent a math error
               ["sin (theta)", "cos (theta)", "tan (theta)"], #When the angle is theta or alpha
               [0.6, 0.8, 0.75], #When tan theta is 3/4
               [0.5144957554, 0.8574929257, 0.6], #When tan theta is 3/5
               [0.6246950476, 0.7808688094, 0.8] #When tan theta is 4/5
               ]




#Class for the stack
class Stack:
    def __init__(self):
        #Stack has a maximum capacity of 20 elements
        self.stack = ["x", "x", "x", "x", "x", "x", "x", "x", "x", "x", "x", "x", "x", "x", "x", "x", "x", "x", "x", "x"]
        self.header = 0
        self.tail = -1
        self.max = 19

    #Method for pushing items into the stack
    def push(self, value):
        #Checks if the stack is full or not before pushing values into the stack
        if self.tail == self.max:
            print("Cannot push values into a full stack")
        else:
            #Pushes the item into the stack and the tail pointer goes up one position
            self.stack[self.tail + 1] = str(value)
            self.tail += 1

    #Method for popping items from the stack
    def pop(self):
        #Checks if the stack is empty or not
        if self.tail == -1:
            print("Cannot pop values from an empty stack")
        else:
            #Sets the item as the value in the tail position and the tail pointer goes down one position
            item = self.stack[self.tail]
            self.stack[self.tail] = "x"
            self.tail -= 1
            return item





#Class for a linear queue
class Queue:
    def __init__(self):
        #Queue has a max capacity of 20 elements
        self.queue = ["x", "x", "x", "x", "x", "x", "x", "x", "x", "x", "x", "x", "x", "x", "x", "x", "x", "x", "x", "x"]
        self.header = 0
        self.tail = -1
        self.max = 19

    #Method for enqueing items into a queue
    def enqueue(self, node):
        #Checks if the queue is full or not before enqueing items into the queue
        if self.tail == self.max:
            print("Cannot enqueue to a full queue")
        else:
            #Tail position increases by one before enqueing the item into that position
            self.tail = self.tail + 1
            self.queue[self.tail] = node
        return self.tail

    #Method for dequeing items from the queue
    def dequeue(self):
        #Checks if the queue is empty by checking if the head pointer is greater than the tail
        if self.header > self.tail:
            print("Cannot dequeue from an empty queue")
        else:
            #Dequeued node is taken from the queue's header pointer and the header pointer moves up one position
            dequeued_node = self.queue[self.header]
            self.queue[self.header] = "x"
            self.header = self.header + 1
        return dequeued_node

               


#SUVAT class
class SUVAT:
    def __init__(self):
        #2D Array holding the variable names and their current values
        self.SUVAT_table = [["Variable [Units]", "Value"],
                            ["Displacement [m]", "0.0"],
                            ["Initial Velocity [m/s]", "0.0"],
                            ["Final Velocity [m/s]", "0.0"],
                            ["Acceleration [m/s^2]", "0.0"],
                            ["Time [s]", "0.0"]]
        self.displacement = 0
        self.initial_v = 0
        self.final_v = 0
        self.acceleration = 0
        self.time = 0
        self.value = 0

    #Each variable has 4 different equations of calculating it
    #Hence why alphabets are used to define temporary variables during the calculations
      
    #If self.final_v and self.time and self.acceleration != 0
    def find_s_1(self):
        a = self.final_v * self.time
        b = 0.5 * self.acceleration * self.time * self.time
        c = a - b
        return c

    #If self.initial_v and self.time and self.acceleration != 0
    def find_s_2(self):
        d = self.initial_v * self.time
        e = 0.5 * self.acceleration * self.time * self.time
        f = d + e
        return f

    #If self.initial_v and self.final_v and self.time != 0
    def find_s_3(self):
        g = self.time / 2
        h = self.initial_v + self.final_v
        i = g * h
        return i
    
    #If self.initial_v and self.final_v and self.acceleration != 0
    def find_s_4(self):
        j = self.initial_v * self.initial_v
        k = self.final_v * self.final_v
        l = 2 * self.acceleration
        m = j + k
        n = m / l
        return n

    #Determines which method to use to calculate displacement
    def find_s(self):
        if self.final_v and self.time and self.acceleration != 0:
            value = self.find_s_1()
            return value
        elif self.initial_v and self.time and self.acceleration != 0:
            value = self.find_s_2()
            return value
        elif self.initial_v and self.final_v and self.time != 0:
            value = self.find_s_3()
            return value
        elif self.initial_v and self.final_v and self.acceleration != 0:
            value = self.find_s_4()
            return value


    #If self.final_v and self.acceleration and self.time != 0
    def find_u_1(self):
        a = self.acceleration + self.time
        b = self.final_v - a
        return b
    
    #If self.displacement and self.acceleration and self.time != 0
    def find_u_2(self):
        c = self.acceleration * self.time * self.time
        d = 2 * self.time
        e = self.displacement - c
        f = e / d
        return f
        
    #If self.final_v and self.displacement and self.time != 0
    def find_u_3(self):
        g = 2 * self.displacement
        h = g / self.time
        i = h + self.final_v
        return i
    
    #If self.final_v and self.acceleration and self.displacement != 0
    def find_u_4(self):
        j = 2 * self.acceleration * self.displacement
        k = self.final_v * self.final_v
        l = j - k
        m = math.sqrt(l)
        return m

    #Determines which method to use to calculate initial velocity
    def find_u(self):
        if self.final_v and self.acceleration and self.time != 0:
            value = self.find_u_1()
            return value
        elif self.displacement and self.acceleration and self.time != 0:
            value = self.find_u_2()
            return value
        elif self.final_v and self.displacement and self.time != 0:
            value = self.find_u_3()
            return value
        elif self.final_v and self.acceleration and self.displacement != 0:
            value = self.find_u_4()
            return value


    #If self.initial_v and self.acceleration and self.time != 0
    def find_v_1(self):
        a = self.acceleration * self.time#
        b = self.initial_v + a
        return b
    
    #If self.displacement and self.acceleration and self.time != 0
    def find_v_2(self):
        c = self.acceleration * self.time * self.time
        d = 2 * self.time
        e = self.displacement + c
        f = e / d
        return f
    
    #If self.initial_v and self.displacement and self.time != 0
    def find_v_3(self):
        g = 2 * self.displacement
        h = g / self.time
        i = h - self.initial_v
        return i
    
    #if self.initial_v and self.acceleration and self.displacement != 0
    def find_v_4(self):
        j = 2 * self.acceleration * self.displacement
        k = self.initial_v * self.initial_v
        l = j + k
        m = math.sqrt(l)
        return m

    #Determines which method to use to calculate final velocity
    def find_v(self):
        if self.initial_v and self.acceleration and self.time != 0:
            value = self.find_v_1()
            return value
        elif self.displacement and self.acceleration and self.time != 0:
            value = self.find_v_2()
            return value
        elif self.initial_v and self.displacement and self.time != 0:
            value = self.find_v_3()
            return value
        elif self.initial_v and self.acceleration and self.displacement != 0:
            value = self.find_v_4()
            return value


    #If self.initial_v and self.final_v and self.time != 0
    def find_a_1(self):
        a = self.final_v - self.initial_v
        b = a / self.time
        return b
    
    #If self.final_v and self.time and self.displacement != 0
    def find_a_2(self):
        c = self.final_v * self.time
        d = c - self.displacement
        e = 2 * d
        f = self.time * self.time
        g = e / f
        return g
    
    #If self.initial_v and self.time and self.displacement != 0
    def find_a_3(self):
        h = self.initial_v * self.time
        i = self.displacement - h
        j = 2 * i
        k = self.time * self.time
        l = j / k
        return l
    
    #If self.initial_v and self.final_v and self.displacement != 0
    def find_a_4(self):
        m = self.final_v * self.final_v
        n = self.initial_v * self.initial_v
        o = m - n
        p = 2 * self.displacement
        q = o / p
        return q
      
    #Determines which method to use to calculate acceleration
    def find_a(self):
        if self.initial_v and self.final_v and self.time != 0:
            value = self.find_a_1()
            return value
        elif self.final_v and self.time and self.displacement != 0:
            value = self.find_a_2()
            return value
        elif self.initial_v and self.time and self.displacement != 0:
            value = self.find_a_3()
            return value
        elif self.initial_v and self.final_v and self.displacement != 0:
            value = self.find_a_4()
            return value


    #If self.initial_v and self.final_v and self.acceleration != 0
    def find_t_1(self):
        a = self.final_v - self.initial_v
        b = a / self.acceleration
        return b
    
    #If self.final_v and self.acceleration and self.displacement != 0
    def find_t_2(self):
        c = self.final_v * self.final_v
        d = 2 * self.acceleration * self.displacement
        e = c - d
        f = math.sqrt(e)
        g = self.final_v - f
        h = g / self.acceleration
        return h
        
    #If self.initial_v and self.acceleration and self.displacement != 0
    def find_t_3(self):
        i = 2 * self.acceleration * self.displacement
        j = self.initial_v * self.initial_v
        k = i + j
        l = math.sqrt(k)
        m = l - self.initial_v
        n = m / self.acceleration
        return n
    
    #If self.displacement and self.initial_v and self.final_v != 0
    def find_t_4(self):
        o = 2 * self.displacement
        p = self.initial_v + self.final_v
        q = o / p
        return q

    #Determines which method to use to calculate time
    def find_t(self):
        if self.initial_v and self.final_v and self.acceleration != 0:
            value = self.find_t_1()
            return value
        elif self.final_v and self.acceleration and self.displacement != 0:
            value = self.find_t_2()
            return value
        elif self.initial_v and self.acceleration and self.displacement != 0:
            value = self.find_t_3()
            return value
        elif self.displacement and self.initial_v and self.final_v != 0:
            value = self.find_t_4()
            return value


    #Simulation method for the SUVAT class
    def simulation(self):
        while True:
            #Table is created using the tabulate module and the 2D array of variables and their values
            print(tabulate(self.SUVAT_table, headers="firstrow", tablefmt="fancy_grid"))
            print("These are the current values of each variable")
            #Option is automatically set to lower case
            self.action_choice = input("""What would you like to do: 

m - Modify the variable values
c - Calculate a value
i - Import values from a text file
e - Export the table to a text file
r - Return to menu to navigate to another topic
q - Quit 

""").lower()
            #While loop used if the user chooses to modify values to make error checking easier
            while self.action_choice == "m":
                #User chooses from the SUVAT variables to modify
                self.variable_choice = input("""Which variable would you like to modify:

s - Displacement
u - Initial Velocity
v - Final Velocity
a - Acceleration
t - Time

r - Return to the SUVAT menu

""").lower()
                if self.variable_choice == "s":
                    #Validation to make sure the value is an integer or real type
                    try:
                        #User enters the value
                        self.value = float(input("Enter the value you would like to assign to the 'displacement' variable: "))
                        #Variable value is updated
                        self.displacement = self.value
                        #Variable is updated in the table too
                        self.SUVAT_table[1][1] = self.displacement
                    except:
                        print("Invalid input for a value [Please enter integer or real values only]")
                elif self.variable_choice == "u":
                    #Validation to make sure the value is an integer or real type
                    try:
                        #User enters the value
                        self.value = float(input("Enter the value you would like to assign to the 'initial velocity' variable: "))
                        #Variable value is updated
                        self.initial_v = self.value
                        #Variable value is updated in the table too
                        self.SUVAT_table[2][1] = self.initial_v
                    except:
                        print("Invalid input for a value [Please enter integer or real values only]")
                elif self.variable_choice == "v":
                    #Validation to make sure the value is an integer or real type
                    try:
                        #User enters the value
                        self.value = float(input("Enter the value you would like to assign to the 'final velocity' variable: "))
                        #Variable value is updated
                        self.final_v = self.value
                        #Variable value is updated in the table too
                        self.SUVAT_table[3][1] = self.final_v
                    except:
                        print("Invalid input for a value [Please enter integer or real values only]")
                elif self.variable_choice == "a":
                    #Validation to make sure the value is an integer or real type
                    try:
                        #User enters the value
                        self.value = float(input("Enter the value you would like to assign to the 'acceleration' variable: "))
                        #Variable value is updated
                        self.acceleration = self.value
                        #Variable value is updated in the table too
                        self.SUVAT_table[4][1] = self.acceleration
                    except:
                        print("Invalid input for a value [Please enter integer or real values only]")
                elif self.variable_choice == "t":
                    #Validation to make sure the value is an integer or real type
                    try:
                        #User enters the value
                        self.value = float(input("Enter the value you would like to assign to the 'time' variable: "))
                        #Variable value is updated
                        self.time = self.value
                        #Variable value is updated in the table too
                        self.SUVAT_table[5][1] = self.time
                    except:
                        print("Invalid input for a value [Please enter integer or real values only]")
                #Breaks the while loop for modifying values and returns to the SUVAT menu
                #If the user chooses to return to the SUVAT menu the loop is broken
                elif self.variable_choice == "r":
                    break
                else:
                    #If any incorrect choices are made then they while loop resets
                    print("Invalid choice")
                    self.action_choice == "m"
            #While loop used if the user chooses to calculate values to make error checking easier
            while self.action_choice == "c":
                #User chooses which variable to calculate a value for
                self.calculation_choice = input("""Which variable would you like to calculate:

s - Displacement
u - Initial Velocity
v - Final Velocity
a - Acceleration
t - Time

r - Return to the SUVAT menu

""").lower()
                #For displacement
                if self.calculation_choice == "s":
                    #Variable value is calculated and updated
                    self.displacement = self.find_s()
                    #Variable value is updated in the table too
                    self.SUVAT_table[1][1] = self.displacement
                #For initial velocity
                elif self.calculation_choice == "u":
                    #Variable value is calculated and updated
                    self.initial_v = self.find_u()
                    #Variable value is updated in the table too
                    self.SUVAT_table[2][1] = self.initial_v
                #For final velocity
                elif self.calculation_choice == "v":
                    #Variable value is calculated and updated
                    self.final_v = self.find_v()
                    #Variable value is updated
                    self.SUVAT_table[3][1] = self.final_v
                #For acceleration
                elif self.calculation_choice == "a":
                    #Variable value is calculated and updated
                    self.acceleration = self.find_a()
                    #Variable value is updated in the table too
                    self.SUVAT_table[4][1] = self.acceleration
                #For time
                elif self.calculation_choice == "t":
                    #Variable value is calculated and updated
                    self.time = self.find_t()
                    #Variable value is updated in the table too
                    self.SUVAT_table[5][1] = self.time
                #If the user chooses to return to the SUVAT menu the loop is broken
                elif self.calculation_choice == "r":
                    break
                #If any incorrect choices are made then they while loop resets
                else:
                    print("Invalid choice")
                    self.action_choice == "c"
            #For importing data from a text file
            if self.action_choice == "i":
                #Validation for making the text file
                try:
                    name = input("What is the name of the file: ")
                    #To add the .txt to the file name if the user hasn't
                    if ".txt" not in name:
                        name += ".txt"
                    #File is opened
                    f = open(name, "r")
                    #The data in the text file is read into an empty array
                    table = f.readlines()
                    #File is closed
                    f.close()
                    #Empty queue is created to store the data
                    values = Queue()
                    #The data from the table are added to the queue
                    for i in range(len(table)):
                        values.enqueue(table[i])
                    #The data is then dequeued from the queue in the correct order
                    #Variable is updated
                    self.displacement = float(values.dequeue())
                    #Variable is updated in the table too
                    self.SUVAT_table[1][1] = self.displacement
                    #Variable is updated
                    self.initial_v = float(values.dequeue())
                    #Variable is updated in the table too
                    self.SUVAT_table[2][1] = self.initial_v
                    #Variable is updated
                    self.final_v = float(values.dequeue())
                    #Variable is updated in the table too
                    self.SUVAT_table[3][1] = self.final_v
                    #Variable is updated
                    self.acceleration = float(values.dequeue())
                    #Variable is updated in the table too
                    self.SUVAT_table[4][1] = self.acceleration
                    #Variable is updated
                    self.time = float(values.dequeue())
                    #Variable is updated in the table too
                    self.SUVAT_table[5][1] = self.time
                except Exception as e:
                    print(e)
                    print("A file with that name does not exist")
            #For exporting the current data to a text file
            elif self.action_choice == "e":
                #User chooses the name of the file
                name = input("What would you like to name the file: ")
                #To add the .txt to the file name if the user hasn't
                if ".txt" not in name:
                    name += ".txt"
                #File of that name is created
                f = open(name, "w")
                #An empty array is created to store the table's data
                table = []
                #Each item in the table is added to the array
                for i in range(1, len(self.SUVAT_table)):
                    add = str(self.SUVAT_table[i][1]) + "\n"
                    table.append(add)
                #The items in the array are then written into the file
                for j in range(0, len(table)):
                    f.writelines(table[j])
                #File is closed
                f.close()
            elif self.action_choice == "r":
                #Validation to ensure the user is sure about returning to the main menu
                try:
                    choice = input("Are you sure you want to return to the menu [Type YES in all caps to confirm]: ")
                    #Only returns to the main menu if yes is typed in all caps
                    if choice == "YES":
                        print("You have confirmed you want to return to the menu")
                        #Table's contents are entered into the stack to allow an undo option (not expanded/implemented)
                        for k in range(1, len(self.SUVAT_table)):
                            saved_list.push(str(self.SUVAT_table[k][1]))
                        #Returns to the main menu
                        return
                    #Otherwise the SUVAT simulation continues
                    else:
                        print("Incorrect input so the simulator will continue")
                except Exception as e:
                    print(e)
                    print("Incorrect input so the simulator will continue")
            elif self.action_choice == "q":
                #Validation to ensure the user is sure about quitting the simulator altogether
                try:
                    choice = input("Are you sure you want to quit [Type YES in all caps to confirm]: ")
                    #Only quits if yes is typed in all caps
                    if choice == "YES":
                        print("You have confirmed you want to quit")
                        sys.exit()
                    #Otherwise the SUVAT simulation continues
                    else:
                        print("Incorrect input so the simulator will continue")
                except Exception as e:
                    print(e)
                    print("Incorrect input so the simulator will continue")
            #The loop is reset if the input is invalid
            elif self.action_choice != "m" and self.action_choice != "c":
                print("Invalid choice") 

            


#Inclined Planes class
class Inclined_Planes():
    def __init__(self):
        ##2D Array holding the variable names and their current values
        self.inclined_planes_table = [["Variable [Units]","Value"],
                                      ["Angle [Degrees]", "0"],
                                      ["Angle fraction [tan theta as a fraction]", ""],
                                      ["Mass [kg]", "0"],
                                      ["Coefficient [No unit]", "0"],
                                      ["Friction [N]", "0"],
                                      ["Weight [N]", "0"],
                                      ["Normal Reaction [N]", "0"]]
        self.gravity = 9.8
        self.angle_degrees = 0
        self.angle_type = "tan theta"
        self.angle_fraction = 0.0
        self.mass = 0
        self.coefficient = 0
        self.friction = 0
        self.weight = 0
        self.normal_reaction = 0

    #Normal reaction force has 2 different equations of calculating it
    #Hence why alphabets are used to define temporary variables during the calculations

    #Method for calculating weight
    def find_w(self):
        a = self.mass * self.gravity
        return a

    #Method 1 for calculating the normal reaction force
    def find_R_1(self):
        if self.angle_degrees != 0:
            if self.angle_degrees == 30:
                r = trig_values[1][2]
            elif self.angle_degrees == 45:
                r = trig_values[2][2]
            elif self.angle_degrees == 60:
                r = trig_values[3][2]
        elif self.angle_fraction != 0.0:
            if self.angle_fraction == 0.75:
                r = trig_values[6][1] 
            elif self.angle_fraction == 0.6:
                r = trig_values[7][1]
            elif self.angle_fraction == 0.8:
                r = trig_values[8][1]
        b = self.weight * r
        return b

    #Method 2 for calculating the normal reaction force
    def find_R_2(self):
        c = self.friction / self.coefficient
        return c

    #Method for determining which method to use to calculate the normal reaction force
    def find_R(self):
        if self.weight != 0:
            value = self.find_R_1()
            return value
        elif self.friction and self.coefficient != 0:
            value = self.find_R_2()
            return value

    #Method for calculating the coefficient of friction
    def find_coefficient(self):
        d = self.friction / self.normal_reaction
        return d

    #Method for calculating the frictional force
    def find_Fr(self):
        e = self.coefficient * self.normal_reaction
        return e
    

    #Simulation method for the inclined planes class
    def simulation(self):
        while True:
            #Table is created using the tabulate module and the 2D array of variables and their values
            print(tabulate(self.inclined_planes_table, headers="firstrow", tablefmt="fancy_grid"))
            print("These are the current values of each variable")
            #Note for the set value of g
            print("NOTE: The acceleration due to gravity (g) is set to 9.8 m/s^2 by default to meet the A-Level Maths criteria")
            #Option is automatically set to lower case
            self.action_choice = input("""What would you like to do: 

m - Modify the variable values
c - Calculate a value
i - Import values from a text file
e - Export the table to a text file
r - Return to menu to navigate to another topic
q - Quit 

""").lower()
            #While loop used if the user chooses to modify values to make error checking easier
            while self.action_choice == "m":
                #User chooses from the Inclined Planes variables to modify
                self.variable_choice = input("""Which variable would you like to modify:

a - Angle
m - Mass
c - Coefficient of Friction
f - Frictional Force
w - Weight
n - Normal Reaction Force

r - Return to the Inclined Planes menu
                                                                                  

""").lower()
                if self.variable_choice == "a":
                    #Validation to make sure the user's angle type is correct
                    try:
                        self.choice = input("Is the angle in degrees [Type YES in all caps]: ")
                        #If in degrees the angle is an integer value
                        if self.choice == "YES":
                            self.value = int(input("Enter the value you would like to assign to the 'angle' variable: "))
                            #Variable value is updated
                            self.angle_degrees = self.value
                            #Variable value is updated in the table too
                            self.inclined_planes_table[1][1] = self.angle_degrees
                        #Otherwise the angle in terms of tan theta is in decimal form (real type)
                        else:
                            self.value = float(input("Enter the decimal equivalent of the fraction for tan theta for the 'angle' variable: "))
                            #Variable value is updated
                            self.angle_fraction = self.value
                            #Variable value is updated in the table too
                            self.inclined_planes_table[2][1] = self.angle_fraction
                    except:
                        print("Invalid input for a value [Please enter the correct data type]")
                elif self.variable_choice == "m":
                    #Validation to make sure the value is an integer or real type
                    try:
                        self.value = float(input("Enter the value you would like to assign to the 'mass' variable: "))
                        #Variable value is updated
                        self.mass = self.value
                        #Variable value is updated in the table too
                        self.inclined_planes_table[3][1] = self.mass
                    except:
                        print("Invalid input for a value [Please enter integer or real values only]")
                elif self.variable_choice == "c":
                    #Validation to make sure the value is a real type
                    try:
                        self.value = float(input("Enter the value you would like to assign to the 'coefficient' variable: "))
                        #Variable value is updated
                        self.coefficient = self.value
                        #Variable value is updated in the table too
                        self.inclined_planes_table[4][1] = self.coefficient
                    except:
                        print("Invalid input for a value [Please enter integer or real values only]")
                elif self.variable_choice == "f":
                    #Validation to make sure the value is an integer or real type
                    try:
                        self.value = float(input("Enter the value you would like to assign to the 'frictional force' variable: "))
                        #Variable value is updated
                        self.friction = self.value
                        #Variable value is updated in the table too
                        self.inclined_planes_table[5][1] = self.friction
                    except:
                        print("Invalid input for a value [Please enter integer or real values only]")
                elif self.variable_choice == "w":
                    #Validation to make sure the value is an integer or real type
                    try:
                        self.value = float(input("Enter the value you would like to assign to the 'weight' variable: "))
                        #Variable value is updated
                        self.weight = self.value
                        #Variable value is updated in the table too
                        self.inclined_planes_table[6][1] = self.weight
                    except:
                        print("Invalid input for a value [Please enter integer or real values only]")
                elif self.variable_choice == "n":
                    #Validation to make sure the value is an integer or real type
                    try:
                        self.value = float(input("Enter the value you would like to assign to the 'normal reaction force' variable: "))
                        #Variable value is updated
                        self.normal_reaction = self.value
                        #Variable value is updated in the table too
                        self.inclined_planes_table[7][1] = self.normal_reaction
                    except:
                        print("Invalid input for a value [Please enter integer or real values only]")
                #If the user chooses to return to the SUVAT menu the loop is broken
                elif self.variable_choice == "r":
                    break
                #If any incorrect choices are made then they while loop resets
                else:
                    print("Invalid choice")
                    self.action_choice = "m"
            #While loop used if the user chooses to calculate values to make error checking easier
            while self.action_choice == "c":
                #User chooses which variable to calculate a value for
                #Note included for set value of g
                print("NOTE: The acceleration due to gravity (g) is set to 9.8 m/s^2 by default to meet the A-Level Maths criteria")
                self.calculation_choice = input("""Which variable would you like to calculate:

w - Weight
n - Normal Reaction Force
c - Coefficient of Friction
f - Frictional Force 

r - Return to the Inclined Planes menu

""").lower()
                #For weight
                if self.calculation_choice == "w":
                    #Variable value is calculated and updated
                    self.weight = self.find_w()
                    #Variable value is updated in the table too
                    self.inclined_planes_table[6][1] = self.weight
                #For normal reaction force
                elif self.calculation_choice == "n":
                    #Variable value is calculated and updated
                    self.normal_reaction = self.find_R()
                    #Variable value is updated in the table too
                    self.inclined_planes_table[7][1] = self.normal_reaction
                #For coefficient of friction
                elif self.calculation_choice == "c":
                    #Variable value is calculated and updated
                    self.coefficient = self.find_coefficient()
                    #Variable value is updated in the table too
                    self.inclined_planes_table[4][1] = self.coefficient
                #For frictional force
                elif self.calculation_choice == "f":
                    #Variable value is calculated and updated
                    self.friction = self.find_Fr()
                    #Variable value is updated in the table too
                    self.inclined_planes_table[5][1] = self.friction
                #If the user chooses to return to the Inclined Planes menu the loop is broken
                elif self.calculation_choice == "r":
                    break
                #If any incorrect choices are made then they while loop resets
                else:
                    print("Invalid choice")
                    self.action_choice == "c"
            #For importing data from a text file
            if self.action_choice == "i":
                #Validation for making the text file
                try:
                    name = input("What is the name of the file: ")
                    #To add the .txt to the file name if the user hasn't
                    if ".txt" not in name:
                        name += ".txt"
                    #File is opened
                    f = open(name, "r")
                    #The data in the text file is read into an empty array
                    table = f.readlines()
                    #File is closed
                    f.close()
                    #Empty queue is created to store the data
                    values = Queue()
                    #The data from the table are added to the queue
                    for i in range(len(table)):
                        values.enqueue(table[i])
                    #The data is then dequeued from the queue in the correct order
                    #Variable is updated
                    self.angle_degrees = int(values.dequeue())
                    #Variable is updated in the table too
                    self.inclined_planes_table[1][1] = self.angle_degrees
                    #Variable is updated
                    self.angle_fraction = float(values.dequeue())
                    #Variable is updated in the table too
                    self.inclined_planes_table[2][1] = self.angle_fraction
                    #Variable is updated
                    self.mass = float(values.dequeue())
                    #Variable is updated in the table too
                    self.inclined_planes_table[3][1] = self.mass
                    #Variable is updated
                    self.coefficient = float(values.dequeue())
                    #Variable is updated in the table too
                    self.inclined_planes_table[4][1] = self.coefficient
                    #Variable is updated
                    self.friction = float(values.dequeue())
                    #Variable is updated in the table too
                    self.inclined_planes_table[5][1] = self.friction
                    #Variable is updated
                    self.weight = float(values.dequeue())
                    #Variable is updated in the table too
                    self.inclined_planes_table[6][1] = self.weight
                    #Variable is updated
                    self.normal_reaction = float(values.dequeue())
                    #Variable is updated in the table too
                    self.inclined_planes_table[7][1] = self.normal_reaction
                except Exception as e:
                    print(e)
                    print("A file with that name does not exist")
            #For exporting the current data to a text file
            elif self.action_choice == "e":
                #User chooses the name of the file
                name = input("What would you like to name the file: ")
                #To add the .txt to the file name if the user hasn't
                if ".txt" not in name:
                    name += ".txt"
                #File of that name is created
                f = open(name, "w")
                #An empty array is created to store the table's data
                table = []
                #Each item in the table is added to the array
                for i in range(1, len(self.inclined_planes_table)):
                    add = str(self.inclined_planes_table[i][1]) + "\n"
                    table.append(add)
                #The items in the array are then written into the file
                for j in range(0, len(table)):
                    f.writelines(table[j])
                #File is closed
                f.close()
            elif self.action_choice == "r":
                #Validation to ensure the user is sure about returning to the main menu
                try:
                    choice = input("Are you sure you want to return to the menu [Type YES in all caps to confirm]: ")
                    #Only returns to the main menu if yes is typed in all caps
                    if choice == "YES":
                        print("You have confirmed you want to return to the menu")
                        #Table's contents are entered into the stack to allow an undo option (not expanded/implemented)
                        for k in range(1, len(self.inclined_planes_table)):
                            saved_list.push(str(self.inclined_planes_table[k][1]))
                        #Returns to the main menu
                        return
                    #Otherwise the Inclined Planes simulation continues
                    else:
                        print("Incorrect input so the simulator will continue")
                except Exception as e:
                    print(e)
                    print("Incorrect input so the simulator will continue")
            elif self.action_choice == "q":
                #Validation to ensure the user is sure about quitting the simulator altogether
                try:
                    choice = input("Are you sure you want to quit [Type YES in all caps to confirm]: ")
                    #Only quits if yes is typed in all caps
                    if choice == "YES":
                        print("You have confirmed you want to quit")
                        sys.exit()
                    #Otherwise the Inclined Planes simulation continues
                    else:
                        print("Incorrect input so the simulator will continue")
                except Exception as e:
                    print("Incorrect input so the simulator will continue")
            #The loop is reset if the input is invalid
            elif self.action_choice != "m" and self.action_choice != "c":
                print("Invalid choice")




#Pulleys class
class Pulleys():
    def __init__(self):
        #2D Array holding the variable names and their current values
        self.pulleys_table = [["Variable [Units]", "Value"],
                              ["Object 1 Mass [kg]", "0"],
                              ["Object 2 Mass [kg]", "0"],
                              ["Object 1 Weight [N]", "0"],
                              ["Object 2 Weight [N]", "0"],
                              ["Tension [N]", "0"],
                              ["Acceleration [m/s^2]", "0"]]
        self.gravity = 9.8
        self.mass_1 = 0
        self.mass_2 = 0
        self.weight_1 = 0
        self.weight_2 = 0
        self.tension = 0
        self.acceleration = 0

    #Weight has 2 different equations for calculating it
    #Hence why alphabets are used to define temporary variables during the calculations


    #Method for calculating the weight of object 1
    def find_w_1(self):
        a = self.mass_1 * self.gravity
        return a

    #Method for calculating the weight of object 2
    def find_w_2(self):
        b = self.mass_2 * self.gravity
        return b

    #Method to calculate the tension within the string holding both objects
    def find_t(self):
        if self.mass_1 != 0:
            c = self.mass_1 * self.acceleration
            d = self.weight_1 - c
            return d
        elif self.mass_2 != 0:
            e = self.mass_2 * self.acceleration
            f = self.weight_2 + e
            return f

    #Method to calculate the acceleration of the dropping object
    def find_a(self):
        if self.mass_1 != 0:
            g = self.weight_1 - self.tension
            h = g / self.mass_1
            return h
        elif self.mass_2 != 0:
            i = self.tension - self.weight_2
            j = i / self.mass_2
            return j


    #Simulation method for the pulleys class
    def simulation(self):
        while True:
            #Table is created using the tabulate module and the 2D array of variables and their values
            print(tabulate(self.pulleys_table, headers="firstrow", tablefmt="fancy_grid"))
            print("These are the current values of each variable")
            #Note for the default pulley type
            print("NOTE: The pulley is smooth by default")
            #Note for the user to use the Pulleys section correctly
            print("NOTE: Assign the heavier mass to object 1 for correct use of the equations")
            #Note for the set value of g
            print("NOTE: The acceleration due to gravity (g) is set to 9.8 m/s^2 by default to meet the A-Level Maths criteria")
            #Option is automatically set to lower case
            self.action_choice = input("""What would you like to do: 

m - Modify the variable values
c - Calculate a value
i - Import values from a text file
e - Export the table to a text file
r - Return to menu to navigate to another topic
q - Quit

""").lower()
            #While loop used if the user chooses to modify values to make error checking easier
            while self.action_choice == "m":
                #User chooses from the Inclined Planes variables to modify
                self.variable_choice = input("""Which variable would you like to modify:

m1 - Mass of object 1
m2 - Mass of object 2
w1 - Weight of object 1
w2 - Weight of object 2
t - Tension between pulley and objects
a - Acceleration of object 1

r - Return to the Pulleys menu
                                                                                  

""").lower()
                if self.variable_choice == "m1":
                    #Validation to make sure the value is an integer or real type
                    try:
                        self.value = float(input("Enter the value you would like to assign to the 'mass of object 1' variable: "))
                        #Variable value is updated
                        self.mass_1 = self.value
                        #Variable value is updated in the table too
                        self.pulleys_table[1][1] = self.mass_1
                    except:
                        print("Invalid input for a value [Please enter integer or real values only]")
                elif self.variable_choice == "m2":
                    #Validation to make sure the value is an integer or real type
                    try:
                        self.value = float(input("Enter the value you would like to assign to the 'mass of object 2' variable: "))
                        #Variable value is updated
                        self.mass_2 = self.value
                        #Variable value is updated in the table too
                        self.pulleys_table[2][1] = self.mass_2
                    except:
                        print("Invalid input for a value [Please enter integer or real values only]")
                elif self.variable_choice == "w1":
                    #Validation to make sure the value is an integer or real type
                    try:
                        self.value = float(input("Enter the value you would like to assign to the 'weight of object 1' variable: "))
                        #Variable value is updated
                        self.weight_1 = self.value
                        #Variable value is updated in the table too
                        self.pulleys_table[3][1] = self.weight_1
                    except:
                        print("Invalid input for a value [Please enter integer or real values only]")
                elif self.variable_choice == "w2":
                    #Validation to make sure the value is an integer or real type
                    try:
                        self.value = float(input("Enter the value you would like to assign to the 'weight of object 2' variable: "))
                        #Variable value is updated
                        self.weight_2 = self.value
                        #Variable value is updated in the table too
                        self.pulleys_table[4][1] = self.weight_2
                    except:
                        print("Invalid input for a value [Please enter integer or real values only]")
                elif self.variable_choice == "t":
                    #Validation to make sure the value is an integer or real type
                    try:
                        self.value = float(input("Enter the value you would like to assign to the 'tension between pulley and objects' variable: "))
                        #Variable value is updated
                        self.tension = self.value
                        #Variable value is updated in the table too
                        self.pulleys_table[5][1] = self.tension
                    except:
                        print("Invalid input for a value [Please enter integer or real values only]")
                elif self.variable_choice == "a":
                    #Validation to make sure the value is an integer or real type
                    try:
                        self.value = float(input("Enter the value you would like to assign to the 'accleration of objects' variable: "))
                        #Variable value is updated
                        self.acceleration = self.value
                        #Variable value is updated in the table too
                        self.pulleys_table[6][1] = self.acceleration
                    except:
                        print("Invalid input for a value [Please enter integer or real values only]")
                #If the user chooses to return to the SUVAT menu the loop is broken
                elif self.variable_choice == "r":
                    break
                #If any incorrect choices are made then they while loop resets
                else:
                    print("Invalid choice")
                    self.action_choice = "m"
            #While loop used if the user chooses to calculate values to make error checking easier
            while self.action_choice == "c":
                #Note for the default pulley type
                print("NOTE: The pulley is smooth by default")
                #Note for the user to use the Pulleys section correctly
                print("NOTE: Assign the heavier mass to object 1 for correct use of the equations")
                #Note for the set value of g
                print("NOTE: The acceleration due to gravity (g) is set to 9.8 m/s^2 by default to meet the A-Level Maths criteria")
                #User chooses which variable to calculate a value for
                self.calculation_choice = input("""Which variable would you like to calculate:

w1 - Weight of object 1
w2 - Weight of object 2
t - Tension between pulley and objects
a - Acceleration of objects

r - Return to the pulleys menu

""").lower()
                #For weight of object 1
                if self.calculation_choice == "w1":
                    #Variable value is calculated and updated
                    self.weight_1 = self.find_w_1()
                    #Variable value is updated in the table too
                    self.pulleys_table[3][1] = self.weight_1
                #For weight of object 2
                elif self.calculation_choice == "w2":
                    #Variable value is calculated and updated
                    self.weight_2 = self.find_w_2()
                    #Variable value is updated in the table too
                    self.pulleys_table[4][1] = self.weight_2
                #For tension
                elif self.calculation_choice == "t":
                    #Variable value is calculated and updated
                    self.tension = self.find_t()
                    #Variable value is updated in the table too
                    self.pulleys_table[5][1] = self.tension
                #For acceleration
                elif self.calculation_choice == "a":
                    #Variable value is calculated and updated
                    self.acceleration = self.find_a()
                    #Variable value is updated in the table too
                    self.pulleys_table[6][1] = self.acceleration
                #If the user chooses to return to the SUVAT menu the loop is broken
                elif self.calculation_choice == "r":
                    break
                #If any incorrect choices are made then they while loop resets
                else:
                    print("Invalid choice")
                    self.action_choice = "c"
            #For importing data from a text file
            if self.action_choice == "i":
                #Validation for making the text file
                try:
                    name = input("What is the name of the file: ")
                    #To add the .txt to the file name if the user hasn't
                    if ".txt" not in name:
                        name += ".txt"
                    #File is opened
                    f = open(name, "r")
                    #The data in the text file is read into an empty array
                    table = f.readlines()
                    f.close()
                    #Empty queue is created to store the data
                    values = Queue()
                    #The data from the table are added to the queue
                    for i in range(len(table)):
                        values.enqueue(table[i])
                    #The data is then dequeued from the queue in the correct order
                    #Variable is updated
                    self.mass_1 = float(values.dequeue())
                    #Variable is updated in the table too
                    self.pulleys_table[1][1] = self.mass_1
                    #Variable is updated
                    self.mass_2 = float(values.dequeue())
                    #Variable is updated in the table too
                    self.pulleys_table[2][1] = self.mass_2
                    #Variable is updated
                    self.weight_1 = float(values.dequeue())
                    #Variable is updated in the table too
                    self.pulleys_table[3][1] = self.weight_1
                    #Variable is updated
                    self.weight_2 = float(values.dequeue())
                    #Variable is updated in the table too
                    self.pulleys_table[4][1] = self.weight_2
                    #Variable is updated
                    self.tension = float(values.dequeue())
                    #Variable is updated in the table too
                    self.pulleys_table[5][1] = self.tension
                    #Variable is updated
                    self.acceleration = float(values.dequeue())
                    #Variable is updated in the table too
                    self.pulleys_table[6][1] = self.acceleration
                except Exception as e:
                    print(e)
                    print("A file with that name does not exist")
            #For exporting the current data to a text file
            elif self.action_choice == "e":
                #User chooses the name of the file
                name = input("What would you like to name the file: ")
                #To add the .txt to the file name if the user hasn't
                if ".txt" not in name:
                    name += ".txt"
                #File of that name is created
                f = open(name, "w")
                #An empty array is created to store the table's data
                table = []
                #Each item in the table is added to the array
                for i in range(1, len(self.pulleys_table)):
                    add = str(self.pulleys_table[i][1]) + "\n"
                    table.append(add)
                #The items in the array are then written into the file
                for j in range(0, len(table)):
                    f.writelines(table[j])
                #File is closed
                f.close()
            elif self.action_choice == "r":
                #Validation to ensure the user is sure about returning to the main menu
                try:
                    choice = input("Are you sure you want to return to the menu [Type YES in all caps to confirm]: ")
                    #Only returns to the main menu if yes is typed in all caps
                    if choice == "YES":
                        print("You have confirmed you want to return to the menu")
                        #Table's contents are entered into the stack to allow an undo option (not expanded/implemented)
                        for k in range(1, len(self.pulleys_table)):
                            saved_list.push(str(self.pulleys_table[k][1]))
                        #Returns to the main menu
                        return
                    #Otherwise the Pulleys simulation continues
                    else:
                        print("Incorrect input so the simulator will continue")
                except Exception as e:
                    print(e)
                    print("Incorrect input so the simulator will continue")
            elif self.action_choice == "q":
                #Validation to ensure the user is sure about quitting the simulator altogether
                try:
                    choice = input("Are you sure you want to quit [Type YES in all caps to confirm]: ")
                    #Only quits if yes is typed in all caps
                    if choice == "YES":
                        print("You have confirmed you want to quit")
                        sys.exit()
                    #Otherwise the Pulleys simulation continues
                    else:
                        print("Incorrect input so the simulator will continue")
                except Exception as e:
                    print("Incorrect input so the simulator will continue")
            #The loop is reset if the input is invalid
            elif self.action_choice != "m" and self.action_choice != "c":
                print("Invalid choice")




#Inclined Pulleys class
class Inclined_Pulleys(Inclined_Planes, Pulleys):
    def __init__(self):
        #2D Array holding the variable names and their current values
        self.inclined_pulleys_table = [["Variable [Units]", "Value"],
                                       ["Angle [Degrees]", "0"],
                                       ["Angle fraction [tan theta as a fraction]", "0.0"],
                                       ["Smooth Pulley? [T/F]","T"],
                                       ["Object 1 Mass [kg]", "0"],
                                       ["Object 2 Mass [kg]", "0"],
                                       ["Object 1 Weight [N]", "0"],
                                       ["Object 2 Weight [N]", "0"],
                                       ["Tension 1 [N]", "0"],
                                       ["Tension 2 [N]", "0"],
                                       ["Coefficient [No unit]", "0"],
                                       ["Friction [N]", "0"],
                                       ["Normal Reaction [N]", "0"]]
        #To inherit the methods from its parent classes
        super().__init__()
        self.gravity = 9.8
        self.angle_degrees = 0
        self.angle_type = "tan theta"
        self.angle_fraction = 0.0
        self.is_pulley_smooth = True
        self.mass_1 = 0
        self.mass_2 = 0
        self.weight_1 = 0
        self.weight_2 = 0
        self.tension_1 = 0
        self.tension_2 = 0
        self.coefficient = 0
        self.friction = 0
        self.normal_reaction = 0

    #Tension has 2 different equations of calculating it
    #Hence why alphabets are used to define temporary variables during the calculations

    #Method for calculating tension between object 1 and the pulley
    def find_t_1(self):
        if self.angle_degrees != 0:
            if self.angle_degrees == 30:
                r = trig_values[1][1]
            elif self.angle_degrees == 45:
                r = trig_values[2][1]
            elif self.angle_degrees == 60:
                r = trig_values[3][1]
        elif self.angle_fraction != 0.0:
            if self.angle_fraction == 0.75:
                r = trig_values[6][0] 
            elif self.angle_fraction == 0.6:
                r = trig_values[7][0]
            elif self.angle_fraction == 0.8:
                r = trig_values[8][0]
        c = self.weight_1 * r
        return c

    #Method for calculating the tension between object 2 and the pulley
    def find_t_2(self):
        if self.is_pulley_smooth == True:
            return self.tension_1
        else:
            if self.angle_degrees != 0:
                if self.angle_degrees == 30:
                    r = trig_values[1][1]
                elif self.angle_degrees == 45:
                    r = trig_values[2][1]
                elif self.angle_degrees == 60:
                    r = trig_values[3][1]
            elif self.angle_fraction != 0.0:
                if self.angle_fraction == 0.75:
                    r = trig_values[6][0] 
                elif self.angle_fraction == 0.6:
                    r = trig_values[7][0]
                elif self.angle_fraction == 0.8:
                    r = trig_values[8][0]
            d = self.weight_1 * r
            e = d + self.weight_2
            return e
        
    #The other methods used are from its two parent classes
    
    #Simulation class for the inclined pulleys class
    def simulation(self):
        while True:
            #Table is created using the tabulate module and the 2D array of variables and their values
            print(tabulate(self.inclined_pulleys_table, headers="firstrow", tablefmt="fancy_grid"))
            print("These are the current values of each variable")
            #Note for the default pulley type
            print("NOTE: The pulley is smooth by default")
            #Note for the set value of g
            print("NOTE: The acceleration due to gravity (g) is set to 9.8 m/s^2 by default to meet the A-Level Maths criteria")
            #Option is automatically set to lower case
            self.action_choice = input("""What would you like to do: 

m - Modify the variable values
c - Calculate a value
i - Import values from a text file
e - Export the table to a text file
r - Return to menu to navigate to another topic
q - Quit 

""").lower()
            #While loop used if the user chooses to modify values to make error checking easier
            while self.action_choice == "m":
                #User chooses from the Inclined Planes variables to modify
                self.variable_choice = input("""Which variable would you like to modify:

a - Angle
s - Smooth or not smooth
m1 - Mass of object 1
m2 - Mass of object 2
w1 - Weight of object 1
w2 - Weight of object 2
t1 - Tension between pulley and object 1
t2 - Tension between pulley and object 2
c - Coefficient of Friction
f - Frictional Force
n - Normal Reaction Force

r - Return to the Inclined Planes menu
                                                                                  

""").lower()
                if self.variable_choice == "a":
                    #Validation to make sure the user's angle type is correct
                    try:
                        self.choice = input("Is the angle in degrees [Type YES in all caps]: ")
                        #If in degrees the angle is an integer value
                        if self.choice == "YES":
                            self.value = int(input("Enter the value you would like to assign to the 'angle' variable: "))
                            #Variable value is updated
                            self.angle_degrees = self.value
                            #Variable value is updated in the table too
                            self.inclined_pulleys_table[1][1] = self.angle_degrees
                        #Otherwise the angle in terms of tan theta is in decimal form (real type)
                        else:
                            self.value = float(input("Enter the decimal equivalent of the fraction for tan theta for the 'angle' variable: "))
                            #Variable value is updated
                            self.angle_fraction = self.value
                            #Variable value is updated in the table too
                            self.inclined_pulleys_table[2][1] = self.angle_fraction
                    except:
                        print("Invalid input for a value [Please enter the correct data type]")
                elif self.variable_choice == "s":
                    #Validation to make sure the value matches the boolean equivalent
                    try:
                        self.choice = input("Is the pulley smooth [Type YES or NO in all caps]: ")
                        #For a smooth pulley
                        if self.choice == "YES":
                            #Variable value is updated
                            self.is_pulley_smooth == True
                            #Variable value is updated in the table too
                            self.inclined_pulleys_table[3][1] = str(True)
                        #For a pulley which isn't smooth
                        elif self.choice == "NO":
                            #Variable value is updated
                            self.is_pulley_smooth = False
                            #Variable value is updated in the table too
                            self.inclined_pulleys_table[3][1] = str(False)
                    except:
                        print("Invalid input for a value [Please enter the correct data type]")
                elif self.variable_choice == "m1":
                    #Validation to make sure the value is an integer or real type
                    try:
                        self.value = float(input("Enter the value you would like to assign to the 'mass of object 1' variable: "))
                        #Variable value is updated
                        self.mass_1 = self.value
                        #Variable value is updated in the table too
                        self.inclined_pulleys_table[4][1] = self.mass_1
                    except:
                        print("Invalid input for a value [Please enter integer or real values only]")
                elif self.variable_choice == "m2":
                    #Validation to make sure the value is an integer or real type
                    try:
                        self.value = float(input("Enter the value you would like to assign to the 'mass of object 2' variable: "))
                        #Variable value is updated
                        self.mass_2 = self.value
                        #Variable value is updated in the table too
                        self.inclined_pulleys_table[5][1] = self.mass_2
                    except:
                        print("Invalid input for a value [Please enter integer or real values only]")
                elif self.variable_choice == "w1":
                    #Validation to make sure the value is an integer or real type
                    try:
                        self.value = float(input("Enter the value you would like to assign to the 'weight of object 1' variable: "))
                        #Variable value is updated
                        self.weight_1 = self.value
                        #Variable value is updated in the table too
                        self.inclined_pulleys_table[6][1] = self.weight_1
                    except:
                        print("Invalid input for a value [Please enter integer or real values only]")
                elif self.variable_choice == "w2":
                    #Validation to make sure the value is an integer or real type
                    try:
                        self.value = float(input("Enter the value you would like to assign to the 'weight of object 2' variable: "))
                        #Variable value is updated
                        self.weight_2 = self.value
                        #Variable value is updated in the table too
                        self.inclined_pulleys_table[7][1] = self.weight_2
                    except:
                        print("Invalid input for a value [Please enter integer or real values only]")
                elif self.variable_choice == "t1":
                    #Validation to make sure the value is an integer or real type
                    try:
                        self.value = float(input("Enter the value you would like to assign to the 'tension between pulley and object 1' variable: "))
                        #Variable value is updated
                        self.tension_1 = self.value
                        #Variable value is updated in the table too
                        self.inclined_pulleys_table[8][1] = self.tension_1
                    except:
                        print("Invalid input for a value [Please enter integer or real values only]")
                elif self.variable_choice == "t2":
                    #Validation to make sure the value is an integer or real type
                    try:
                        self.value = float(input("Enter the value you would like to assign to the 'tension between pulley and object 2' variable: "))
                        #Variable value is updated
                        self.tension_2 = self.value
                        #Variable value is updated in the table too
                        self.inclined_pulleys_table[9][1] = self.tension_2
                    except:
                        print("Invalid input for a value [Please enter integer or real values only]")
                elif self.variable_choice == "c":
                    #Validation to make sure the value is an integer or real type
                    try:
                        self.value = float(input("Enter the value you would like to assign to the 'coefficient' variable: "))
                        #Variable value is updated
                        self.coefficient = self.value
                        #Variable value is updated in the table too
                        self.inclined_pulleys_table[10][1] = self.coefficient
                    except:
                        print("Invalid input for a value [Please enter integer or real values only]")
                elif self.variable_choice == "f":
                    #Validation to make sure the value is an integer or real type
                    try:
                        self.value = float(input("Enter the value you would like to assign to the 'frictional force' variable: "))
                        #Variable value is updated
                        self.friction = self.value
                        #Variable value is updated in the table too
                        self.inclined_pulleys_table[11][1] = self.friction
                    except:
                        print("Invalid input for a value [Please enter integer or real values only]")
                elif self.variable_choice == "n":
                    #Validation to make sure the value is an integer or real type
                    try:
                        self.value = float(input("Enter the value you would like to assign to the 'normal reaction force' variable: "))
                        #Variable value is updated
                        self.normal_reaction = self.value
                        #Variable value is updated in the table too
                        self.inclined_pulleys_table[12][1] = self.normal_reaction
                    except:
                        print("Invalid input for a value [Please enter integer or real values only]")
                #If the user chooses to return to the SUVAT menu the loop is broken
                elif self.variable_choice == "r":
                    break
                #If any incorrect choices are made then they while loop resets
                else:
                    print("Invalid choice")
                    self.action_choice = "m"
            #While loop used if the user chooses to calculate values to make error checking easier
            while self.action_choice == "c":
                #Note for default pulley type
                print("NOTE: The pulley is smooth by default")
                #Note included for set value of g
                print("NOTE: The acceleration due to gravity (g) is set to 9.8 m/s^2 by default to meet the A-Level Maths criteria")
                #User chooses which variable to calculate a value for
                self.calculation_choice = input("""Which variable would you like to calculate:

w1 - Weight of object 1
w2 - Weight of object 2
t1 - Tension between pulley and object 1
t2 - Tension between pulley and object 2
n - Normal Reaction Force
c - Coefficient of Friction
f - Frictional Force

r - Return to the Inclined Pulleys menu

""").lower()
                #For weight of object 1
                if self.calculation_choice == "w1":
                    #Variable value is calculated and updated
                    self.weight_1 = self.find_w_1()
                    #Variable value is updated in the table too
                    self.inclined_pulleys_table[6][1] = self.weight_1
                #For weight of object 2
                elif self.calculation_choice == "w2":
                    #Variable value is calculated and updated
                    self.weight_2 = self.find_w_2()
                    #Variable value is updated in the table too
                    self.inclined_pulleys_table[7][1] = self.weight_2
                #For tension between object 1 and the pulley
                elif self.calculation_choice == "t1":
                    #Variable value is calculated and updated
                    self.tension_1 = self.find_t_1()
                    #Variable value is updated in the table too
                    self.inclined_pulleys_table[8][1] = self.tension_1
                #For tension between the pulley and object 2
                elif self.calculation_choice == "t2":
                    #Variable value is calculated and updated
                    self.tension_2 = self.find_t_2()
                    #Variable value is updated in the table too
                    self.inclined_pulleys_table[9][1] = self.tension_2
                #For normal reaction force
                elif self.calculation_choice == "n":
                    #Variable value is calculated and updated
                    self.normal_reaction = self.find_R()
                    #Variable value is updated in the table too
                    self.inclined_pulleys_table[12][1] = self.normal_reaction
                #For coefficient of friction
                elif self.calculation_choice == "c":
                    #Variable value is calculated and updated
                    self.coefficient = self.find_coefficient()
                    #Variable value is updated in the table too
                    self.inclined_pulleys_table[10][1] = self.coefficient
                #For frictional force
                elif self.calculation_choice == "f":
                    #Variable value is calculated and updated
                    self.friction = self.find_Fr()
                    #Variable value is updated in the table too
                    self.inclined_pulleys_table[11][1] = self.friction
                #If the user chooses to return to the Inclined Planes menu the loop is broken
                elif self.calculation_choice == "r":
                    break
                #If any incorrect choices are made then they while loop resets
                else:
                    print("Invalid choice")
                    self.action_choice = "c"
            #For importing data from a text file
            if self.action_choice == "i":
                #Validation for making the text file
                try:
                    name = input("What is the name of the file: ")
                    #To add the .txt to the file name if the user hasn't
                    if ".txt" not in name:
                        name += ".txt"
                    #File is opened
                    f = open(name, "r")
                    #The data in the text file is read into an empty array
                    table = f.readlines()
                    #File is closed
                    f.close()
                    #Empty queue is created to store the data
                    values = Queue()
                    #The data from the table are added to the queue
                    for i in range(len(table)):
                        values.enqueue(table[i])
                    #The data is then dequeued from the queue in the correct order
                    #Variable is updated
                    self.angle_degrees = int(values.dequeue())
                    #Variable is updated in the table too
                    self.inclined_pulleys_table[1][1] = self.angle_degrees
                    #Variable is updated
                    self.angle_fraction = float(values.dequeue())
                    #Variable is updated in the table too
                    self.inclined_pulleys_table[2][1] = self.angle_fraction
                    #Variable is updated
                    self.is_pulley_smooth = bool(values.dequeue())
                    #Variable is updated in the table too
                    self.inclined_pulleys_table[3][1] = self.is_pulley_smooth
                    #Variable is updated
                    self.mass_1 = float(values.dequeue())
                    #Variable is updated in the table too
                    self.inclined_pulleys_table[4][1] = self.mass_1
                    #Variable is updated
                    self.mass_2 = float(values.dequeue())
                    #Variable is updated in the table too
                    self.inclined_pulleys_table[5][1] = self.mass_2
                    #Variable is updated
                    self.weight_1 = float(values.dequeue())
                    #Variable is updated in the table too
                    self.inclined_pulleys_table[6][1] = self.weight_1
                    #Variable is updated
                    self.weight_2 = float(values.dequeue())
                    #Variable is updated in the table too
                    self.inclined_pulleys_table[7][1] = self.weight_2
                    #Variable is updated
                    self.tension_1 = float(values.dequeue())
                    #Variable is updated in the table too
                    self.inclined_pulleys_table[8][1] = self.tension_1
                    #Variable is updated
                    self.tension_2 = float(values.dequeue())
                    #Variable is updated in the table too
                    self.inclined_pulleys_table[9][1] = self.tension_2
                    #Variable is updated
                    self.coefficient = float(values.dequeue())
                    #Variable is updated in the table too
                    self.inclined_pulleys_table[10][1] = self.coefficient
                    #Variable is updated
                    self.friction = float(values.dequeue())
                    #Variable is updated in the table too
                    self.inclined_pulleys_table[11][1] = self.friction
                    #Variable is updated
                    self.normal_reaction = float(values.dequeue())
                    #Variable is updated in the table too
                    self.inclined_pulleys_table[12][1] = self.normal_reaction
                except Exception as e:
                    print(e)
                    print("A file with that name does not exist")
            #For exporting the current data to a text file
            elif self.action_choice == "e":
                #User chooses the name of the file
                name = input("What would you like to name the file: ")
                #To add the .txt to the file name if the user hasn't
                if ".txt" not in name:
                    name += ".txt"
                #File of that name is created
                f = open(name, "w")
                #An empty array is created to store the table's data
                table = []
                #Each item in the table is added to the array
                for i in range(1, len(self.inclined_pulleys_table)):
                    add = str(self.inclined_pulleys_table[i][1]) + "\n"
                    table.append(add)
                #The items in the array are then written into the file
                for j in range(0, len(table)):
                    f.writelines(table[j])
                #File is closed
                f.close()
            elif self.action_choice == "r":
                #Validation to ensure the user is sure about returning to the main menu
                try:
                    choice = input("Are you sure you want to return to the menu [Type YES in all caps to confirm]: ")
                    #Only returns to the main menu if yes is typed in all caps
                    if choice == "YES":
                        print("You have confirmed you want to return to the menu")
                        #Table's contents are entered into the stack to allow an undo option (not expanded/implemented)
                        for k in range(1, len(self.inclined_pulleys_table)):
                            saved_list.push(str(self.inclined_pulleys_table[k][1]))
                        #Returns to the main menu
                        return
                    #Otherwise the Inclined Pulleys simulation continues
                    else:
                        print("Incorrect input so the simulator will continue")
                except Exception as e:
                    print(e)
                    print("Incorrect input so the simulator will continue")
            elif self.action_choice == "q":
                #Validation to ensure the user is sure about quitting the simulator altogether
                try:
                    choice = input("Are you sure you want to quit [Type YES in all caps to confirm]: ")
                    #Only quits if yes is typed in all caps
                    if choice == "YES":
                        print("You have confirmed you want to quit")
                        sys.exit()
                    #Otherwise the Inclined Pulleys simulation continues
                    else:
                        print("Incorrect input so the simulator will continue")
                except Exception as e:
                    print("Incorrect input so the simulator will continue")
            #The loop is reset if the input is invalid
            elif self.action_choice != "m" and self.action_choice != "c":
                print("Invalid choice")
    
    


#Class to generate the nodes for a linked list
class Node:
    def __init__(self, data = None):
        #Data value of the element
        self.data = data
        #Pointer next to the node
        self.next = None


#Linked list class for the menu
#The linked list implemented is a circular doubly linked list
class Linked_List:
    def __init__(self):
        #Head pointer of the linked list is defined
        self.header = Node()

    #Method for adding nodes to the linked list
    def add_node_to_list(self, data):
        #New node to be added is defined
        add = Node(data)
        #Head pointer points to the new node
        current = self.header
        while current.next is not None:
            current = current.next
        #New node added to the linked list
        current.next = add

    #Method for displaying the menu using an array to store the options
    def output_list(self):
        #The options are stored as a 1D array
        options = []
        #Starts from the head node
        current_node = self.header
        #If there is no none value it is added to the linked list
        while current_node.next is not None:
            current_node = current_node.next
            #Option added to the array
            options.append(current_node.data)
        for i in range(0, len(options)):
            #f-string used to display the options from the array
            print(f"{i + 1} - {options[i]}")


#Class for creating the menu using the linked list
class Menu:
    def __init__(self):
        #The menu options are written in a 1D array
        self.menu_items = ["SUVAT", "Inclined Planes", "Pulleys", "Inclined Pulleys", "Quit"]
        #The menu linked list is generated
        self.menu_list = Linked_List()
        #The menu options are added to the linked list as nodes
        for item in self.menu_items:
            self.menu_list.add_node_to_list(item)

    #Method for generating the menu using the options provided
    def generate_menu(self):
        while True:
            print("Mechanics Simulator Menu:")
            self.menu_list.output_list()
            choice = input("Enter your choice: ")
            #Calls the SUVAT class
            if choice == "1":
                suvat = SUVAT()
                #Simulation for the SUVAT class
                suvat.simulation()
            #Calls the Inclined Planes class
            elif choice == "2":
                inclined_planes = Inclined_Planes()
                #Simulation for the Inclined Planes class
                inclined_planes.simulation()
            #Calls the Pulleys class
            elif choice == "3":
                pulleys = Pulleys()
                #Simulation for the Pulleys class
                pulleys.simulation()
            #Calls the Inclined Pulleys class
            elif choice == "4":
                inclined_pulleys = Inclined_Pulleys()
                #Simulation for the Inclined Pulleys class
                inclined_pulleys.simulation()
            #Choice for quitting the simulator
            elif choice == "5":
                #Validation to ensure that the user wants to quit
                try:
                    choose = input("Are you sure you want to quit [Type YES in all caps to confirm]: ")
                    #Will only quit if yes is typed in all caps
                    if choose == "YES":
                        print("You have confirmed you want to quit")
                        sys.exit()
                    #Otherwise the simulator continues running
                    else:
                        print("Incorrect input so the simulator will continue")
                except Exception as e:
                    print(e)
                    print("Incorrect input so the simulator will continue")
            else:
                print("Invalid choice.")


#Stack created for the undo feature
saved_list = Stack()

#Main code generated using the menu class
main = Menu()
main.generate_menu()