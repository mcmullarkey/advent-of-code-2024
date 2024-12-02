from collections import Counter

def main():
    
    location_list_one, location_list_two = read_in_data()
    
    part_one_answer = sort_get_diff([location_list_one, location_list_two])
    
    print(f"I found my answer to part one! The answer is {part_one_answer}")
    
    part_two_answer = calculate_similarity_score([location_list_one, location_list_two])
    
    print(f"I found my answer to part two! The answer is {part_two_answer}")
    
    return 0

def read_in_data():
    
    # Read the txt file and extract columns into two lists
    location_list_one, location_list_two = [], []

    with open('01/input/input.txt', 'r') as file:
        for line in file:
            columns = line.strip().split()
            if len(columns) >= 2:  # Ensure there are at least two columns
                location_list_one.append(int(columns[0]))
                location_list_two.append(int(columns[1]))

    return location_list_one, location_list_two

def sort_get_diff(location_lists):
    
    sorted_lists = [sorted(location_list) for location_list in location_lists]
    
    diff_list = [abs(list_two_value - list_one_value) 
                 for list_one_value, list_two_value 
                 in zip(sorted_lists[0], sorted_lists[1])]
    
    answer = sum(diff_list)
    
    return answer

def calculate_similarity_score(location_lists):
    
    # Get unique values in left list
    
    unique_values = list(set(location_lists[0]))
    
    # Count the number of times each unique value in left list appears in right list
    
    # Count occurrences of all items in the list
    counts = Counter(location_lists[1])

    # Filter counts to include only items in the set
    filtered_counts = {key: counts[key] for key in unique_values}
    
    # Sum up similarity scores while using original left list with duplicate values
    
    similarity_score_list = [location_id * filtered_counts.get(location_id, 0)
                             for location_id 
                             in location_lists[0]]
    
    part_two_answer = sum(similarity_score_list)
    
    return part_two_answer

if __name__ == '__main__':
    main()