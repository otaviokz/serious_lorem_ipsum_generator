import os
import re

def main():
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("========================================================")        
        print("                ***Lorem Ipsum generator***")
        print()
        print("Choose an option:")
        print()
        print("1. Generate by number of paragraphs")
        print("2. Generate by number of sentences")
        print("'q' for Exit")
        option = input("Enter your choice: ")
        if option == "q":
            break
        elif option == "1":
            paragraphs(main)
        elif option == "2":
            phrases(main)
        else:
            invalid_option(main)
        print("\n========================================================")


def invalid_option(completion):
        os.system('cls' if os.name == 'nt' else 'clear')
        f = (open("documents/lorem_ipsum.txt", "r"))
        print("========================================================\n")
        option = input("Invalid input. Press any button to go back.\n========================================================")        
        completion()


def paragraphs(completion):
    os.system('cls' if os.name == 'nt' else 'clear')
    print("========================================================")
    option = input("Enter the number of paragraphs you want to generate (1 to 20), or 'q' to go back.")
    if option == "q":
        completion()
    if re.match(r'^[1-9]$|^1[0-9]$|^20$', option):
        print("Generating " + option + " paragraphs of Lorem Ipsum gibberish.\n")
        number_of_paragrphs = int(option)
        f = (open("documents/lorem_ipsum.txt", "r"))
        lines = f.readlines()

        result = ""
        for i in range(number_of_paragrphs):
            result += f"\n{lines[i]}"
        print_result(result)
        f.close()
    else:
        input("Invalid input. Press any button to try again\n========================================================")
        paragraphs(completion)
        print("")


def phrases(completion):
    os.system('cls' if os.name == 'nt' else 'clear')
    print("========================================================")
    option = input("Enter the number of fhrases you want to generate (1 to 209), or 'q' to go back.")
    if re.match(r'^[1-9]$|^1[0-9]$|^20[0-9]$|^209$', option):
        if option == "q":
            completion()
        
        print("Generating " + option + " phrases of Lorem Ipsum gibberish.\n")
        number_of_phrases = int(option)
        
        f = (open("documents/lorem_ipsum.txt", "r"))
        lines = f.read()
        
        puncgtuated_phrases = []
        phrase_count = 0
        should_continue = True
        
        for line in lines:            
            point_frases = line
            bang_phrases = []
            for point_phrase in point_phrases:
                 point_phrase += "."
                 bang_phrases += point_phrase.split("!")
                 for phrase in bang_phrases:
                    phrase += "!"
                    question_frases = []
                    for bang_phrase in bang_phrases:                     
                        question_frases += bang_phrase.split("?")
                        for phrase in question_frases:
                            phrase += "?"
                            line_phrases = question_frases

            print(f"line_frases: {line_phrases}")
            while phrase_count < number_of_phrases:
                for phrase in line_phrases:                    
                    result_phrases = result_phrases + phrase + "."
                    phrase_count += 1
                    if phrase_count >= number_of_phrases:
                        should_continue = False
                        break              
                if not should_continue:
                    break
            if not should_continue:
                    break
        f.close()
        print_result(result_phrases)        
    else:
        input("Invalid input. Press any button to try again\n========================================================")
        phrases(completion)
        
    
def print_result(result: str):
    print("=== Your Result (Type any key to open the main menu) ===")
    print()
    print("\"" + result + "\"")
    print()
    input_placeholder = input("========================================================")    
    main()
    

# def words(completion: function):
#     os.system('cls' if os.name == 'nt' else 'clear')
#     print("========================================================")
#     input = input("Enter the number of words you want to generate (1 to 3089), or 'q' to go back.")
#     if input == "q":
#         completion()
#     if input.match(r'^[1-2].{1}\d\d\d|^3[0-9].{2}$|^30[0-7].{1}\d]|^308[0-9]$'):
#         print("Generating " + input + " words of Lorem Ipsum gibberish.")
#         number_of_words = int(input)
#         f = (open("documents/lorem_ipsum.txt", "r"))
#         text = f.read()
#         text.split(r"\n.!?[ ],")
#         result = ""
#         for i in range(number_of_words):
#             result += lines[i]
#         print_result(result)
#         f.close()
#     input = input("Enter the number of words you want to generate (1 to 3089), or 'q' to go back.")
    
#     if result == "q":
#         completion()
#         re.match("\w+\b")
#     f = (open("documents/lorem_ipsum.txt", "r"))
#     all_text = f.read()
#     match_result = re.match("\w+\b", all_text)    
#     if match_result:
#         word_count = match_result.count()
#         all_words = all_text.replace("\n", " ") .split(" ")
#         rsult = ""
#         print("Generating " + input + " words of Lorem Ipsum gibberish.")
#         number_of_words = int(input)
#         f = (open("documents/lorem_ipsum.txt", "r"))
#         lines = f.read_lines()

#         result = ""
#         for i in range(number_of_words):
#             result += lines[i]        
#     else:
#         print()
#     print("========================================================")

if __name__ == "__main__":
    main()