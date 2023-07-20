import os
import time
import subprocess
import arraygen
import csv
from consolemenu import SelectionMenu

def clear():
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

def time_sorting_algorithm(sort_func, sort_name, arrays_to_sort):
    times = []
    for idx, array in enumerate(arrays_to_sort, start=1):
        print(f"Testing {sort_name} on array #{idx}")
        start_time = time.perf_counter()
        try:
            sorted_array = sort_func(array)
        except Exception as e:
            print(f"Error occurred during sorting with algorithm '{sort_name}': {e}")
            return None
        end_time = time.perf_counter()
        if sorted_array is None or sorted_array != sorted(array):
            print(f"Warning: Sorting algorithm '{sort_name}' did not return a sorted array.")
            return None
        times.append(end_time - start_time)
    return times

def generate_random_id():
    import Crypto.Random.random as random
    import string
    return ''.join(random.sample(string.ascii_letters + string.digits, k=15))

def time_now():
    t = time.localtime()
    current_time = time.strftime("%Y-%m-%d %H:%M:%S", t)
    return current_time

def perf_counter():
    t = time.perf_counter()
    return t

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
    
    types_of_random_array = ["Random sequential array", "Random array", "Randomize custom array", "Custom array", "Mutiple test cases"]
    array_type_index = SelectionMenu.get_selection(types_of_random_array)
    arrays_to_test = []
    
    match array_type_index:
        case 0:
            try:
                bottom_number = int(input("Input bottom number (default 0): "))
            except ValueError:
                bottom_number = 0
            try:
                top_number = int(input("Input top number (default 2048): "))
            except ValueError:
                top_number = 2048
            for _ in range(repetitions):
                arrays_to_test.append(arraygen.generate_random_sequenced_array(bottom_number, top_number))
        case 1:
            try:
                array_size = int(input("Input array size (default 2048): "))
            except ValueError:
                array_size = 2048
            try:
                bottom_limit = int(input("Input bottom limit (default 0): "))
            except ValueError:
                bottom_limit = 0
            try:
                top_limit = int(input("Input top limit (default 2048): "))
            except ValueError:
                top_limit = 2048
            for _ in range(repetitions):
                arrays_to_test.append(arraygen.generate_random_array(array_size, bottom_limit, top_limit))
        case 2:
            try:
                custom_array = eval(input("""Enter custom array 
                                            (format: [1, 2, 3, 4, 2])
                                            (default random [0...1024])
                                          
                                          Input: """))
                if not isinstance(custom_array, list):
                    raise ValueError("Input must be a list. Using default list.")
                for _ in range(repetitions):
                    arrays_to_test.append(arraygen.array_randomizer(custom_array))
            except (ValueError, SyntaxError):
                for _ in range(repetitions):
                    arrays_to_test.append(arraygen.generate_random_sequenced_array(bottom_limit=0, top_limit=1024))
        case 3:
            try:
                array_to_sort = eval(input("""Enter custom array
                                            (format: [1, 2, 3, 4, 2])
                                            (default random [0...1024])
                                           
                                           Input: """))
                for _ in range(repetitions):
                    arrays_to_test.append(array_to_sort)
                if not isinstance(array_to_sort, list):
                    raise ValueError("Input must be a list. Using default list.")

            except (ValueError, SyntaxError):
                for _ in range(repetitions):
                    arrays_to_test.append(arraygen.generate_random_sequenced_array(bottom_limit=0, top_limit=1024))
        case 4:
            del types_of_random_array[4]
            types_of_random_array.append("Same limit random sequential")
            array_type_index = SelectionMenu.get_selection(types_of_random_array)
            
            max_value = 8192
            defaults = [256 * (2 ** i) if 256 * (2 ** i) < max_value else max_value for i in range(repetitions)]
            match array_type_index:
                case 0:
                    for i in range(repetitions):
                        try:
                            lower_limit = int(input("Input bottom limit (default: 0): "))
                        except ValueError:
                            print("Invalid input for the lower limit. Using default value 0.")
                            lower_limit = 0
                        try:
                            upper_limit = int(input(f"Input upper limit (default: {defaults[i]}): "))
                        except (ValueError, IndexError):
                            print(f"Invalid input for the upper limit or default index. Using default value {defaults[i]}.")
                            upper_limit = defaults[i]
                        arrays_to_test.append(arraygen.generate_random_sequenced_array(lower_limit, upper_limit))
                case 1:
                    for i in range(repetitions):
                        try:
                            array_size = int(input(f"Input array size (default: {defaults[i]}): "))
                        except ValueError:
                            print(f"Invalid input for the lower limit. Using default value {defaults[i]}.")
                            array_size  = defaults[i]
                        try:
                            lower_limit = int(input("Input bottom limit (default: 0): "))
                        except ValueError:
                            print("Invalid input for the lower limit. Using default value 0.")
                            lower_limit = 0
                        try:
                            upper_limit = int(input(f"Input upper limit (default: {defaults[i]}): "))
                        except (ValueError, IndexError):
                            print(f"Invalid input for the upper limit or default index. Using default value {defaults[i]}.")
                            upper_limit = defaults[i]
                        arrays_to_test.append(arraygen.generate_random_array(array_size, lower_limit, upper_limit))
                case 2:
                    for i in range(repetitions):
                        try:
                            custom_array = eval(input(f"""Enter custom array 
                                                        (format: [1, 2, 3, 4, 2])
                                                        (default random [0...{defaults[i]}])
                                                        
                                                        Input: """))
                            if not isinstance(custom_array, list):
                                raise ValueError("Input must be a list. Using default list.")
                            arrays_to_test.append(arraygen.array_randomizer(custom_array))
                        except (ValueError, SyntaxError):
                                arrays_to_test.append(arraygen.generate_random_sequenced_array(0, defaults[i]))
                case 3:
                    for i in range(repetitions):
                        try:
                            array_to_sort = eval(input(f"""Enter custom array
                                    (format: [1, 2, 3, 4, 2])
                                    (default random [0...{defaults[i]}])
                                    
                                    Input: """))
                            if not isinstance(array_to_sort, list):
                                raise ValueError("Input must be a list. Using default list.")

                        except (ValueError, SyntaxError):
                            arrays_to_test.append(arraygen.generate_random_sequenced_array(bottom_limit=0, top_limit=1024))
                case 4:
                    try:
                        lower_limit = int(input("Input lower limit (default 0): "))
                    except ValueError:
                        lower_limit = 0
                    try:
                        upper_limit = int(input("Input upper limit (default 2048): "))
                    except ValueError:
                        upper_limit = 2048
                    for _ in range(repetitions):
                        arrays_to_test.append(arraygen.generate_random_sequenced_array(lower_limit, upper_limit))

    clear()
    program_runtime_start = perf_counter()
    print(f"Arrays:")
    for idx, array in enumerate(arrays_to_test, start=1):
        print(f"{idx})\n{array}\n\n")

    algorithm_times = []
    error_algorithms = []
    for algorithm in sorting_algorithms:
        algorithm_name = algorithm["name"]()
        sort_func = algorithm["sort"]
        print(f"Testing {algorithm_name}")
        times = time_sorting_algorithm(sort_func, algorithm_name, arrays_to_test)
        if times is not None:
            algorithm_times.append((algorithm_name, times))
        else:
            print(f"{algorithm_name}: Error occurred during sorting.")
            error_algorithms.append(algorithm_name)
        print("\n")

    for idx, (algorithm_name, times) in enumerate(algorithm_times):
        average_time = sum(times) / len(times)
        algorithm_times[idx] = (algorithm_name, times, average_time)

    sorted_algorithms = sorted(algorithm_times, key=lambda x: x[2])

    random_id = generate_random_id()
    current_time = time_now()
    results_folder = "results"
    if not os.path.exists(results_folder):
        os.makedirs(results_folder)

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
    average_filename = os.path.join(f"{results_filename[:-4]}-averages.txt")

    with open(results_filename, "w") as results_file:
        with open(average_filename, "w") as average_file:
            for algorithm_name, times, average_time in sorted_algorithms:
                results_file.write(f"{algorithm_name}\n\n")
                average_file.write(f"{algorithm_name}\n")
                for count, time in enumerate(times):
                    results_file.write(f"Array #{count+1}: {time:.9f} seconds\n")
                average_file.write(f"Average time: {average_time:.9f} seconds\n\n")
            if error_algorithms:
                results_file.write(f"Errors: ")
                results_file.write(", ".join(error_algorithms))
                average_file.write(f"Errors: ")
                average_file.write(", ".join(error_algorithms))
            for count, array in enumerate(arrays_to_test):
                results_file.write(f"Array #{count+1}:\n\nLength: {len(array)}\n\n{array}\n\n\n\n\n")
                average_file.write(f"Array #{count+1}:{len(array)} items\n\n")

    print(f"Results saved to {results_filename}")
    program_runtime_end = perf_counter()
    program_runtime = program_runtime_end - program_runtime_start
    print(f"Program runtime: {program_runtime}")


if __name__ == "__main__":
    main()
