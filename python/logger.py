import datetime


def log_attack_model(attack: str, model: str):
    # get the wright filename
    file_name = get_filename(attack, model)

    # open log file
    file = open(file_name, "a")

    # write attack description
    file.write("---------------------------\n")
    file.write(f"{attack.upper()} - {model.upper()} - {datetime.datetime.now()}\n\n")

    # close log file
    file.close()


def log(message, attack: str, model: str):
    # get the wright filename
    file_name = get_filename(attack, model)

    # open log file
    file = open(file_name, "a")

    # write messages
    file.write(f"{message}\n")

    # close log file
    file.close()


def get_filename(attack, model):
    dir_log = "log"
    dir_model = f"{dir_log}/log-{model.replace('.', '-')}"
    return f"{dir_model}/{attack}_log.txt"
