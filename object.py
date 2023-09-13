from vector import vector

class emptyval:
    pass

class object:
    mass = emptyval()
    position = emptyval()
    velocity = emptyval()

    def __init__(self, mass, initial_position, initial_velocity):
        self.mass = mass
        self.position = vector(initial_position[0], initial_position[1])
        self.velocity = vector(initial_velocity[0], initial_velocity[1])

    def gravity_to(self, other):
        return 6.674*10**(-11)*self.mass*other.mass/(self.position-other.position).lengthsq()

    def step(self, dt):
        self.position += self.velocity*dt

