import sys
import os
import attacks
import subprocess


def get_model_name():

    while True:
        print("\n\nChoose your LLM [1,2,3]:\n"
              "1 - gpt-3.5-turbo\n"
              "2 - gpt-4-1106-preview\n"
              "3 - text-davinci-003\n"
              "0 - exit")
        user_input = int(input("> "))
        if user_input >=0 and user_input <= 3:
            break
        else:
            print("Model incorrect! Please choose wisely!")

    if user_input == 0:
        exit_program("Thank you! Come again!")

    if user_input == 1:
        return "gpt-3.5-turbo"
    if user_input == 2:
        return "gpt-4-1106-preview"
    if user_input == 3:
        return "text-davinci-003"
        

def check_openai_version(model):
    # detect openai version
    version = subprocess.run(["openai", "--version"], capture_output=True).stdout.split()[1]
    # install the correct version for the selected model
    if version == b'0.28.1' and model != "text-davinci-003":
        os.system("pip install openai --upgrade")
        exit_program("Please restart the application to make the changes effective!")
    elif version != b'0.28.1' and model == "text-davinci-003":
        os.system("pip install openai==0.28.1")
        exit_program("Please restart the application to make the changes effective!")
    else:
        return


def get_attack():

    while True:
        print("\nChoose your attack [0 to exit]:\n"
              "---------BASIC ATTACKS----------\n"
              "1 - encode attack\n"
              "2 - fill in the blank attack\n"
              "3 - frag. & conc. attack\n"
              "4 - task deflection attack\n"
              "5 - virtualization attack\n"
              "6 - indirect injection attack\n"
              "7 - text completion as instruct attack\n"
              "8 - instruction repetition attack\n"
              "9 - prefix injection attack\n"
              "10- refusal suppression attack\n"
              "11- distractor instructions attack\n"
              "---------FAMOUS ATTACKS---------\n"
              "12- DAN 6.0 attack\n"
              "13- Dev. mode attack\n"
              "14- DUDE attack\n"
              "15- Jailbreak mode attack\n"
              "16- MONGO Tom attack\n"
              "17- STAN attack\n"
              "18- Evil confidant attack\n"
              "--------------------------------\n"
              "999 - Launch All\n"
              "0 - exit")

        # getting and controlling user input
        user_input = int(input("> "))
        if user_input < 0 and user_input > 18 and user_input < 999:
            print("Wrong attack selected, please select a right one!")
        else:
            break

    if user_input == 0:
        exit_program("Thank you! Come again!")

    if user_input == 1:
        while True:
            print("Select the encoding type: [1,2]:\n"
                  "1 - base64\n"
                  "2 - morse\n"
                  "3 - back")
            user_input = input("> ")
            if user_input == "1":
                return "base64_encode_attack"
            elif user_input == "2":
                return "morse_encode_attack"
            elif user_input == "3":
                break
            else:
                print("invalid encoding type. Please select a right one!")
    elif user_input == 2:
        return "fill_in_the_blank_attack"
    elif user_input == 3:
        return "fragmentation_concatenation_attack"
    elif user_input == 4:
        return "task_deflection_attack"
    elif user_input == 5:
        return "virtualization_attack"
    elif user_input == 6:
        return "indirect_injection_attack"
    elif user_input == 7:
        return "text_completion_as_instruct_attack"
    elif user_input == 8:
        return "instruction_repetition_attack"
    elif user_input == 9:
        return "prefix_injection_attack"
    elif user_input == 10:
        return "refusal_suppression_attack"
    elif user_input == 11:
        return "distractor_instructions_attack"
    elif user_input == 12:
        return "dan6_attack"
    elif user_input == 13:
        return "developer_mode_attack"
    elif user_input == 14:
        return "dude_attack"
    elif user_input == 15:
        return "jailbreak_mode_attack"
    elif user_input == 16:
        return "mongo_tom_attack"
    elif user_input == 17:
        return "stan_attack"
    elif user_input == 18:
        return "evil_confidant"
    elif user_input == 999:
        return "all_the_attacks"


def main():

    try:
        # get the LLM model
        model = get_model_name()
        # check openai version
        check_openai_version(model)

        while True:
            # choose the attack
            attack = get_attack()
            # launch the attack selected to the LLM model chosen
            if attack == "all_the_attacks":
                attacks.launch_all_attacks(model)
            else:
                attacks.launch_attack(attack, model)

    except Exception as e:
        exit_program(f"An error occurred: {e}")


def exit_program(message):
    print(f"{message}")
    sys.exit(0)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
