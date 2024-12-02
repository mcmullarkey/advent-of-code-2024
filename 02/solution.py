def main():
    solve_part_one()
    solve_part_two()
    return 0

def parse_file(file_path):
    with open(file_path, 'r') as file:
        return [list(map(int, line.strip().split())) for line in file]

def check_increasing_decreasing(report):
    all_increasing = all(report[i] < report[i + 1] for i in range(len(report) - 1))
    all_decreasing = all(report[i] > report[i + 1] for i in range(len(report) - 1))
    return all_increasing or all_decreasing

def check_level_change(report):
    return all(1 <= abs(report[i] - report[i + 1]) <= 3 for i in range(len(report) - 1))

def is_safe_report(report):
    return check_increasing_decreasing(report) and check_level_change(report)

def is_tolerable_report(report):
    return is_safe_report(report) or removal_create_safe(report)

def removal_create_safe(input_list):
    for i in range(len(input_list)):
        modified_list = input_list[:i] + input_list[i+1:]
        if is_safe_report(modified_list):
            return True  # Return True if removing one element results in a safe report
    return False  # Return False if no single removal results in a safe report

def solve_part_one():
    reports = parse_file('02/input/input.txt')
    safe_reports = sum(is_safe_report(report) for report in reports)
    print(safe_reports)
    return safe_reports

def solve_part_two():
    reports = parse_file('02/input/input.txt')
    tolerable_reports = sum(is_tolerable_report(report) for report in reports)
    print(tolerable_reports)
    return tolerable_reports

if __name__ == '__main__':
    main()