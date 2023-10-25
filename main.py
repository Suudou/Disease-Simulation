import random
import matplotlib.pyplot as plt
import matplotlib.animation as animation

class Person:
    def __init__(self, x, y, proximity_limit):
        self.x = x
        self.y = y
        self.proximity_limit = proximity_limit

def spawn_people(num_people, square_size, proximity_limit):
    people = []
    for _ in range(num_people):
        # Ensure initial spawn within the proximity limit
        x = random.uniform(proximity_limit, square_size - proximity_limit)
        y = random.uniform(proximity_limit, square_size - proximity_limit)
        people.append(Person(x, y, proximity_limit))
    return people


def move_people(people, square_size):
    for person in people:
        dx = random.uniform(-1, 1)
        dy = random.uniform(-1, 1)

        # Ensure the person stays within the boundaries
        person.x = max(0, min(person.x + dx, square_size))
        person.y = max(0, min(person.y + dy, square_size))

        # Limit proximity to the boundary
        person.x = max(person.x, person.proximity_limit)
        person.x = min(person.x, square_size - person.proximity_limit)
        person.y = max(person.y, person.proximity_limit)
        person.y = min(person.y, square_size - person.proximity_limit)


def update(frame, people, sc, square_size):
    move_people(people, square_size)
    check_collisions(people)
    sc.set_offsets([(person.x, person.y) for person in people])
    return sc,


def check_collisions(people):
    coordinates_set = set()
    for person in people:
        coordinates = (round(person.x, 2), round(person.y, 2))
        if coordinates in coordinates_set:
            print("Collision detected at coordinates:", coordinates)
        else:
            coordinates_set.add(coordinates)

def simulate(num_people, square_size, num_ticks, proximity_limit):
    people = spawn_people(num_people, square_size, proximity_limit)

    fig, ax = plt.subplots()
    ax.set_xlim(0, square_size)
    ax.set_ylim(0, square_size)
    sc = ax.scatter([person.x for person in people], [person.y for person in people])

    ani = animation.FuncAnimation(fig, update, fargs=(people, sc, square_size), frames=num_ticks, interval=100,repeat=False)
    plt.show()


if __name__ == "__main__":
    num_people = 15 # Ilosc ludzi
    square_size = 10 # Rozmiar mapy
    num_ticks = 100 # Ilosc iteracji
    proximity_limit = 0.2 # Odleglosc od granic

    simulate(num_people, square_size, num_ticks, proximity_limit)