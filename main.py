from person import Person
from personService import PersonService


class App():
    def menuApp(self):
        print("1. Agregar persona")
        print("2. Listar persona")
        print("3. Modificar persona")
        print("4. Borrar persona")
        print("5. Ejercicio")
        return int(input("Elija una opción: "))


if __name__ == '__main__':
    app = App()
    personService = PersonService()

    while True:
        opcionElegida = app.menuApp()
        if opcionElegida == 1:
            personService.add_person()

        if opcionElegida == 2:
            print(personService.get_personList())

        if opcionElegida == 3:
            personService.update_person()

        if opcionElegida == 4:
            personService.delete_person()

        if opcionElegida == 5:
            p1 = Person()
            p1.name = 'Federico'
            p1.surname = 'Gonzalez'
            p1.age = '20'
            personService.add_person(p1)

            p1 = Person()
            p1.name = 'Claudio'
            p1.surname = 'Pico'
            p1.age = '33'
            personService.add_person(p1)

            p1 = Person()
            p1.name = 'Nicolas'
            p1.surname = 'Pico'
            p1.age = '40'
            personService.add_person(p1)

            print(personService.get_personList())

            p1 = Person()
            p1.name = 'Federico'
            p1.surname = 'Gonzalez'
            p1.age = '12'
            personService.update_person(0, p1)
            print(personService.get_personList())
            personService.delete_person(2)
            print(personService.get_personList())
