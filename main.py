"""Josephus problem
People are standing in a circle waiting to be executed. Counting begins at a specified point in the circle and proceeds around the circle in a specified direction. After a specified number of people are skipped, the next person is executed. The procedure is repeated with the remaining people, starting with the next person, going in the same direction and skipping the same number of people, until only one person remains, and is freed.
"""

from Circle_linked_list import Circle_linked_list
from faker import Faker
from time import sleep
fake = Faker('zh_CN')


class Person:
    def __init__(self, i):
        self.i = i
        self.name = fake.name()

    def __repr__(self):
        return f'Person: id -> {self.i}, name -> {self.name}'


def gen_to_be_executed(n):
    l = Circle_linked_list()
    for i in range(n):
        l.push(Person(i))
    return l


def main():
    n = 0
    skip = 5
    people = gen_to_be_executed(10)

    for p in people:
        if n == skip:
            r = people.pop()
            print(f'Execute! {r}')
            n = 0
        else:
            print(p)
            n += 1
        sleep(0.5)


if __name__ == "__main__":
    main()
