print("\n\n\t\t\t\t Hello, Welcome to the University of Lagos Navigation system\n\n\n");
import numpy
from collections import defaultdict

class NavigationSystem():
    def __init__(self):
        
        self.routes = defaultdict(list)
        self.weights = {}
    
    def add_route(self, source, your_destination, weight):
        self.routes[source].append(your_destination)
        self.routes[your_destination].append(source)
        self.weights[(source, your_destination)] = weight
        self.weights[(your_destination, source)] = weight

NavSystem = NavigationSystem()

routes = [
	('Unilag_gate', 'Uba_park', 2),
	('Unilag_gate', 'Education', 3),
	('Unilag_gate', 'Sport_center', 6),
	('Uba_park', 'Environmental_science', 2),
	('Environmental_science', 'New_hall', 4),
	('Education', 'Amina', 3),
	('Education', 'Kofo', 5),
	('Amina', 'Kofo', 2),
	('Kofo', 'Biobaku', 2),
	('Biobaku', 'Dli', 7),
	('Dli', 'Second_gate', 4),
	('Dli', 'First_bank', 1),
	('Dli', 'Fss', 7),
	('Dli', 'Health_center', 7),
	('Sport_center', 'Fss', 2),
	('Sport_center', 'New_hall', 2),
	('New_hall', 'Campus_shuttle', 2),
	('Fss', 'New_hall', 1),
	('Fss', 'Campus_shuttle', 4),
	('Campus_shuttle', 'Cits', 1),
	('Campus_shuttle', 'Masscom_roundout', 4),
	('Masscom_roundout', 'Moremi', 3),
	('Masscom_roundout', 'Art', 2),
	('Masscom_roundout', 'Main_aud', 4),
	('Moremi', 'Jaja', 2),
	('Moremi', 'Jaja_complex', 2),
	('Jaja_complex', 'Petrochemical_Engineering', 3),
	('Petrochemical_Engineering', 'Science', 2),
	('Science', 'Engeering', 5),
	('Science', 'Health_center', 5),
	('Engeering', 'Main_aud', 3),
	('Art', 'Business_admin', 3),
	('Art', 'Law', 1),
	('Art', 'Main_aud', 3),
	('Law', 'Main_library', 1),
	('Business_admin', 'Main_library', 1),
	('Main_library', 'Lagoon_front', 3),
	('Main_aud', 'Main_library', 2),
	('Main_aud', 'Lagoon_front', 5),

]


for route in routes:
    NavSystem.add_route(*route)

def navigate(graph, beginning, dest):
    shortest_routes = {beginning: (None, 0)}
    current_vertex = beginning
    visited_vertex = set()
    
    while current_vertex != dest:
        visited_vertex.add(current_vertex)
        destinations = graph.routes[current_vertex]
        weight_to_current_vertex = shortest_routes[current_vertex][1]

        for next_vertex in destinations:
            weight = graph.weights[(current_vertex, next_vertex)] + weight_to_current_vertex
            if next_vertex not in shortest_routes:
                shortest_routes[next_vertex] = (current_vertex, weight)
            else:
                current_shortest_weight = shortest_routes[next_vertex][1]
                if current_shortest_weight > weight:
                    shortest_routes[next_vertex] = (current_vertex, weight)
        
        next_destinations = {vertex: shortest_routes[vertex] for vertex in shortest_routes if vertex not in visited_vertex}
        if not next_destinations:
            return "Sorry, Route Not Possible Within Unilag Or Please Check Your Spellings"
     
        current_vertex = min(next_destinations, key=lambda k: next_destinations[k][1])
    
    shortest_path = []
    while current_vertex is not None:
        shortest_path.append(current_vertex)
        next_vertex = shortest_routes[current_vertex][0]
        current_vertex = next_vertex
    shortest_path = shortest_path[::-1]
    return shortest_path
    
CurrentLocation = input("Input your current location: ")
print("\n\t\t\t\tYour source is " + CurrentLocation)
Destination = input("\nInput your destination: ")
print("\n\t\t\t\tYour destination is " + Destination)
print("\n The best route from "+ CurrentLocation + " to "+ Destination + " is \n\t\t\t\t")
print(navigate(NavSystem, CurrentLocation, Destination))