# Academic Integrity Statement
# filename: "first_prac.py"
# author: Prabhav BHAGAT
# student id: 524555
# email: 524555@learning.eynesbury.edu.au
# date: 28/10/2026
#
# This is all my own work as per the Eynesbury College Academic Integrity Policy 


#TASK_01
days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
total_letter = 0 
for day in days: 
    total_letter = total_letter + len(day)

average = total_letter / len(day) 

print("Total_letters:",total_letter)
print("Average word length:",average)   

#TASK_02
def distance(speed,time): 
    result = speed*time
    return result
answer = distance(60,100)
print("Distance travelled:", float(answer),"meters.")


#TASK_03
def kinetic_energy(velocity,mass): 
    result = 0.5*mass*velocity**2
    return result
answer = kinetic_energy(60,10)
print("Kinetic Energy:",answer,"joules.")

#TASK_04
class MovingObject: 
    def __init__(self, velocity, mass): 
        self.velocity = velocity
        self.mass = mass 

    def distance(self,duration): 
        result = self.velocity * duration 
        return result

    def kinetic_energy(self): 
        result = 0.5 * self.mass * self.velocity ** 2
        return result

    #TASK_05
myMovingObject = MovingObject(6,20) #
print("Distance travelled:", myMovingObject.distance(60))
print("Kinetic Energy:", myMovingObject.kinetic_energy())