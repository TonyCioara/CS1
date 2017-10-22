from simulation import Simulation
from virus import Virus


def create_simulation():
    virus_name = "Ebola"
    mortality_rate = 0.4
    infection_rate = 0.8
    pop_size = 3000
    vacc_percentage = 0.4
    initial_infected = 6
    virus = Virus(virus_name, infection_rate, mortality_rate)
    return Simulation(pop_size, vacc_percentage, virus, initial_infected)


def test_create_population():
    simulation_instance = create_simulation()
    simulation_instance.population = simulation_instance._create_population(6)
    infected_count = 0
    total_count = 0
    assert len(simulation_instance.population) == 3000
    for index in range(0, len(simulation_instance.population)):
        if simulation_instance.population[index].infected is True:
            infected_count += 1
        total_count += 1
    assert total_count == 3000
    assert infected_count == 6


def test_simulation_should_continue():
    simulation_instance = create_simulation()
    simulation_instance.population = simulation_instance._create_population(6)

    should_continue = simulation_instance._simulation_should_continue()
    assert should_continue is True
    for index in range(0, len(simulation_instance.population)):
        simulation_instance.population[index].is_alive = False
    should_continue = simulation_instance._simulation_should_continue()
    assert should_continue is False


def test_interaction():
    person = Person(1, False, True)
