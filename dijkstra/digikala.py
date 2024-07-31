import numpy as np
import pandas as pd
import heapq

# Load the Excel file and create the distance matrix
df = pd.read_excel("distances.xlsx", index_col=0)
df = df.fillna(float("inf"))
cities_list = df.values.tolist()


def dijkstra(start: str, end: str) -> int:
    # Dictionary to map city names to indices
    cities_dict = {
        "zahedan": 0,
        "bandar": 1,
        "shiraz": 2,
        "yazd": 3,
        "kerman": 4,
        "mashhad": 5,
        "sari": 6,
        "tehran": 7,
        "esfahan": 8,
        "ahvaz": 9,
        "khoram": 10,
        "kermanshah": 11,
        "tabriz": 12,
    }

    # Get the indices of the start and end cities
    start_index = cities_dict[start]
    end_index = cities_dict[end]

    # Number of cities
    num_cities = len(cities_list)

    # Initialize distances with infinity and set the distance to the start city to 0
    distances = [float("inf")] * num_cities
    distances[start_index] = 0

    # Priority queue to store (distance, city_index) tuples
    priority_queue = [(0, start_index)]

    # Boolean list to check if a city has been visited
    visited = [False] * num_cities

    while priority_queue:
        # Pop the city with the smallest distance
        current_distance, current_city = heapq.heappop(priority_queue)

        # If we have reached the end city, return the distance
        if current_city == end_index:
            return current_distance

        # If the city is already visited, skip it
        if visited[current_city]:
            continue

        # Mark the current city as visited
        visited[current_city] = True

        # Update the distances to the neighboring cities
        for neighbor_index, distance in enumerate(cities_list[current_city]):
            if not visited[neighbor_index] and distance < float("inf"):
                new_distance = current_distance + distance
                if new_distance < distances[neighbor_index]:
                    distances[neighbor_index] = new_distance
                    heapq.heappush(priority_queue, (new_distance, neighbor_index))

    return float("inf")  # Return infinity if there is no path from start to end


print(dijkstra("kerman", "kerman"))
