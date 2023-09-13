from vector import vector

class planetsystem:
    objects = 0

    def __init__(self):
        self.objects = []

    def step(self, dt):
        for object1 in self.objects:
            for object2 in self.objects:
                if object2 != object1:
                    object2.velocity += (object1.position - object2.position).normalized()*(object2.gravity_to(object1))/object2.mass*dt
        for object in self.objects:
            object.step(dt)

    def drawData(self):
        data = []
        for object in self.objects:
            data.append([object.position.getX(), object.position.getY(), object.mass])
        return data
