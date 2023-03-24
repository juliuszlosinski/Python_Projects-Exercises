"""
Juliusz Łosiński ~ 24.03.2023
"""


def try_convert(label: str):
    """
    Trying convert string to some other format.
    :param label: Label that contains string
    :return: Proper format of string.
    """
    if label.lower().count("true") or label.lower().count("false"):
        return bool(label)
    try:
        value = float(label)
        return value
    except ValueError:
        return label


def read_file_ini(path_to_file: str) -> dict:
    """
    Read file .init from file, and convert it to the dictionary date type.
    :param path_to_file: File's path.
    :return: Dictionary that represents readed data.
    """
    file = open(path_to_file)
    config: dict = {"LOGIN": {}, "SERVER": {}, "INFO": {}}
    reading_login_section: bool = False
    reading_info_section: bool = False
    reading_server_section: bool = False
    for line in file:
        if line.count("LOGIN"):
            reading_login_section = True
            reading_server_section = False
            reading_info_section = False
        elif line.count("SERVER"):
            reading_login_section = False
            reading_server_section = True
            reading_info_section = False
        elif line.count("INFO"):
            reading_login_section = False
            reading_server_section = False
            reading_info_section = True
        line = line.replace(" ", "")
        line = line.replace("\n", "")
        data = line.split("=")
        if len(data) >= 2:
            if reading_login_section:
                config["LOGIN"][f"{data[0]}"] = try_convert(str(data[1]))
            elif reading_info_section:
                config["INFO"][f"{data[0]}"] = try_convert(str(data[1]))
            elif reading_server_section:
                config["SERVER"][f"{data[0]}"] = try_convert(str(data[1]))
    return config


# Testing.
config_dict = read_file_ini("config.ini")
print(config_dict)
