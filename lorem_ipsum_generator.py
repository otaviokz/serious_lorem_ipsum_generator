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
            quit()
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


# 141 '.', 19 '!'. 19 '?' = 179 // QUASE lá
def paragraphs(completion): 
    os.system('cls' if os.name == 'nt' else 'clear')
    print("========================================================")
    print("Generating Lorem Ipsum gibberish by number of paragraphs.\n")
    option = input("Enter a number (1 to 20) or 'q' to go back: ")
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
    option = input("Enter the number of phrases you want to generate (1 to 209), or 'q' to go back.\n: ")
    if re.match(r'^[1-9]$|^1[0-9]$|^2[0-9]$|^1[0-9]{2}$|^20[0-8]$|^209$', option):
        if option == "q":
            completion()
        
        print("Generating " + option + " phrases of Lorem Ipsum gibberish.\n")
        number_of_phrases = int(option)
        single_phrases = []
        
        def check_number_of_phrases_reached():
            return len(single_phrases) >= number_of_phrases
        
        lines = []
        with open("documents/lorem_ipsum.txt") as file:
            while new_line := file.readline():
                lines = lines + [new_line.rstrip()]
                        
        for line in lines:            
            # Split on '.'
            point_slices = line.split(".")            
            for point_slice in point_slices:
                 
                 # Stop if the number of phrases is reached
                 if check_number_of_phrases_reached():
                     break
                 
                 # If the '.' sliced string is not empty and the last character is not a punctuation 
                 if len(point_slice) > 0 and point_slice[-1] not in [".", "!", "?"]:        
                    # # Add back the '.' at the end
                    point_slice = point_slice + "."

                    # If there is no more punctuation in the slice, then it's a single phrase.
                    if "!" not in point_slice and "?" not in point_slices:
                        # Add it to the single_phrases list.
                        single_phrases = single_phrases + [point_slice]
                       
                    # Split on '!'
                    bang_slices = point_slice.split("!")
                    for bang_slice in bang_slices:

                        # Stop if the number of phrases is reached
                        if check_number_of_phrases_reached():                            
                            break
                        
                        # If the '!' sliced string is not empty and the last character is not a punctuation
                        if len(bang_slice) > 1 and bang_slice[-1] not in [".", "!", "?"]:
                            # Add back the '!' at the end
                            bang_slice = bang_slice + "!"

                            # If there is no more punctuation in the slice, then it's a single phrase.
                            if "?" not in bang_slice:
                                # Add it to the single_phrases list.
                                single_phrases = single_phrases + [bang_slice]

                            # Split on '?'
                            question_slices = bang_slice.split("?")
                            for question_slice in question_slices:

                                # Stop if the number of phrases is reached
                                if check_number_of_phrases_reached():                            
                                    break

                                # If the '?' sliced string is not empty and the last character is not a punctuation
                                if len(question_slice) > 1 and question_slice[-1] not in [".", "!", "?"]:
                                    # Add back the '?' at the end
                                    question_slice = question_slice + "?"

                                    # There's no more punctuation, given '?' is the last punctuation to be tested
                                    single_phrases = single_phrases + [question_slice]
                                    
        print_phrases_list(single_phrases, completion)        
    else:
        input("Invalid input. Press any button to try again\n========================================================")
        phrases(completion)


def print_phrases_list(phrases_list, completion):
    os.system('cls' if os.name == 'nt' else 'clear')
    print("=== Your Result (Type any key to open the main menu) ===")
    print()
    for phrase in phrases_list:
        print(f"{phrase[1:] if phrase[0] == str(' ') else phrase[0:]}", end=" ")
    print()
    print()
    input_placeholder = input("========================================================")    
    completion()


def print_result(result: str):
    os.system('cls' if os.name == 'nt' else 'clear')
    print("=== Your Result (Type any key to open the main menu) ===")
    print(f"{result}")    
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