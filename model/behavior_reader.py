def read_behavior_info(file_path):
    try:
        with open(file_path, "r") as f:
            data = f.read().strip()
            return data
    except FileNotFoundError:
        return "No behavior data"
