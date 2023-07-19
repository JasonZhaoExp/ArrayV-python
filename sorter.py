import os
import time
import subprocess
import arraygen
import csv
from consolemenu import SelectionMenu

def clear(self):
    if os.name == "posix": 
        subprocess.run(["clear"])
    else: 
        subprocess.run(["cls"], shell=True)

def load_sorting_algorithms():
    sorting_algorithms = []
    sorts_dir = "sorts"
    for filename in os.listdir(sorts_dir):
        if filename.endswith(".py"):
            filepath = os.path.join(sorts_dir, filename)
            algorithm = {}
            with open(filepath, "r") as file:
                exec(file.read(), algorithm)
            if "name" in algorithm and "sort" in algorithm:
                sorting_algorithms.append(algorithm)
            else:
                print(f"Invalid format in {filename}. Skipping this algorithm.")
    return sorting_algorithms

def time_sorting_algorithm(sort_func, array, repetitions):
    total_time = 0
    for _ in range(repetitions):
        start_time = time.perf_counter()
        try:
            sorted_array = sort_func(array.copy())
        except Exception as e:
            print(f"Error occurred during sorting with algorithm '{sort_func.__name__}': {e}")
            return None
        end_time = time.perf_counter()
        if sorted_array is None or sorted_array != sorted(array):
            print(f"Warning: Sorting algorithm '{sort_func.__name__}' did not return a sorted array.")
            return None
        total_time += end_time - start_time
    return total_time / repetitions

def generate_random_id():
    import Crypto.Random.random as random
    import string
    return ''.join(random.sample(string.ascii_letters + string.digits, k=15))

def main():
    sorting_algorithms = load_sorting_algorithms()
    if not sorting_algorithms:
        print("No valid sorting algorithms found in the 'sorts' folder.")
        return
    try:
        repetitions = int(input("Enter the number of times to repeat each sorting algorithm: "))
        if repetitions <= 0:
            print("Please enter a positive integer for repetitions.")
            return
    except ValueError:
        print("Invalid input. Please enter a positive integer.")
        return
    
    types_of_random_array = ["Random sequential array", "Random array", "Randomize custom array", "Custom array"]
    array_type_index = SelectionMenu.get_selection(types_of_random_array)
    
    match array_type_index:
        case 0:
            bottom_number = int(input("Input bottom number (default 0): "))
            top_number = int(input("Input top number (default 2048): "))
            array_to_sort = arraygen.generate_random_sequenced_array(bottom_number, top_number)
        case 1:
            array_size = int(input("Input array size (default 2048): "))
            bottom_limit = int(input("Input bottom limit (default 0): "))
            top_limit = int(input("Input top limit (default 2048): "))
            array_to_sort = arraygen.generate_random_array(array_size, bottom_limit, top_limit)
        case 2:
            custom_array = eval(input("""Enter custom array 
                                      (format: [1, 2, 3, 4, 2])
                                      (default random [0...1024]: """))
            array_to_sort = arraygen.array_randomizer(custom_array)
        case 3:
            array_to_sort = [a for a in range(0, 1024)]
            array_to_sort = arraygen.array_randomizer(array_to_sort)
            array_to_sort = eval(input("""Enter custom array
                                       (format: [1, 2, 3, 4, 2])
                                       (default random [0...1024]: """))
    
    algorithm_times = []
    error_algorithms = []
    for algorithm in sorting_algorithms:
        algorithm_name = algorithm["name"]()
        sort_func = algorithm["sort"]
        average_time = time_sorting_algorithm(sort_func, array_to_sort, repetitions)
        if average_time is not None:
            algorithm_times.append((algorithm_name, average_time))
        else:
            print(f"{algorithm_name}: Error occurred during sorting.")
            error_algorithms.append(algorithm_name)
    
    sorted_algorithms = sorted(algorithm_times, key=lambda x: x[1])

    # Generate a random ID and get the current date and time
    random_id = generate_random_id()
    current_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

    results_folder = "results"
    if not os.path.exists(results_folder):
        os.makedirs(results_folder)

    # Save the current date and time along with the random ID to a CSV file
    csv_filename = os.path.join(results_folder, "results.csv")
    csv_exists = os.path.isfile(csv_filename)

    with open(csv_filename, "a", newline="") as csvfile:
        csv_writer = csv.writer(csvfile)
        if not csv_exists:
            csv_writer.writerow(["RandomID", "DateTime"])
        csv_writer.writerow([random_id, current_time])

    existing_files = [filename for filename in os.listdir(results_folder) if filename.startswith("results-")]
    next_number = len(existing_files) + 1
    results_filename = os.path.join(results_folder, f"results-{next_number}-{random_id}.txt")

    with open(results_filename, "w") as results_file:
        for algorithm_name, average_time in sorted_algorithms:
            results_file.write(f"{algorithm_name}\n{average_time:.9f} seconds\n\n")
        if error_algorithms:
            results_file.write(f"Errors: ")
            results_file.write(", ".join(error_algorithms))

    print(f"Results saved to {results_filename}")

if __name__ == "__main__":
    main()
