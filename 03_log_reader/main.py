def read_last_errors(log_path, keyword="ERROR", lines=50):
    with open(log_path, "r") as file:
        lines_list = file.readlines()[-lines:]
        for line in lines_list:
            if keyword in line:
                print(line.strip())
