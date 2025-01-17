import json

def split_line(line: str, char: str):
    sliced_array = line.split(char)
    result_array = []
    for sentence in sliced_array:
        sentence = str(sentence) + str(char)
        if len(sentence) > 1 and str(sentence[-1]) != str(char) and str(sentence[-1]) not in [".", "!", "?"]:
            sentence = sentence.replace("\n", "")
            if len(sentence) > 1:
                result_array.append(sentence)
    return result_array

def split_inner_list(array_of_arrays: list[list[str]], char: str):
    result_array = []
    for array in array_of_arrays:
        for sub_array in array:
            slice_array = sub_array.split(str(char))
            for slice_str in slice_array:
                slice_str = slice_str + str(char)
                slice_str = slice_str.replace(f"{str(char)}{str(char)}", str(char))
            for slice_str in slice_array:
                charEndingSlice = slice_str + str(char)
                charEndingSlice = charEndingSlice.replace(f"{str(char)}{str(char)}", str(char))
                if len(charEndingSlice) > 1:
                    result_array.append(charEndingSlice)

            
            # for slice_str in slice_array:
            #     slice_str = slice_str + str(char)
            #     slice_str = slice_str.replace(f"{str(char)}{str(char)}", str(char))
            #     if len(slice_str) > 1:
            #         result_array.append(slice_str)

    return result_array

lorem_ipsum1 = """
Lorem ipsum dolor sit amet. Est dolorem recusandae qui asperiores laboriosam et maiores omnis eum molestiae quia sed veritatis beatae et voluptas consectetur! Aut repellendus quia non placeat dolorem sed provident inventore aut galisum animi? Rem fuga tempora non quod nobis vel impedit eveniet qui velit quibusdam vel culpa sint. Aut autem totam sed cupiditate iste et doloribus quia aut reiciendis eligendi est Quis magnam ad similique deleniti! Sit tempora ullam non voluptatem animi et ipsam nisi ut quae mollitia et esse quae aut repellendus saepe est eius error. Et error unde a porro sequi eum galisum aperiam et exercitationem voluptatum. In reiciendis exercitationem et libero magnam ea omnis accusantium. Ut culpa repellendus ut mollitia facere aut adipisci iste in culpa repudiandae non recusandae libero.
"""
lorem_ipsum2 = """
Et error voluptate nam necessitatibus quaerat in distinctio voluptatem aut aspernatur optio. Aut neque sequi sit error fugiat et internos praesentium eum harum voluptas eos dolorem cumque At perferendis labore ut velit repudiandae! Est voluptatum omnis rem adipisci fuga 33 sapiente provident ut sequi omnis ad aliquid incidunt non deleniti amet. Eos Quis esse aut itaque repellat sed unde quisquam est nihil cumque. In voluptatum asperiores et nobis dolorem est illo molestiae cum numquam ipsum aut officiis nisi non dolorem fuga est molestias molestiae? Et aperiam asperiores ad impedit ipsam a possimus nulla sit dignissimos nulla et voluptate magni sit ipsa esse? Et doloremque rerum At illo laudantium est fugiat tenetur et voluptas placeat. Sit natus autem qui voluptatem internos ut sequi quidem et ducimus repellat quo facilis aliquam et sint eveniet.
"""
import os
os.system("clear")
# print("\n\\===================================================================")
# lorem_ipsum1_2 = lorem_ipsum1 + " " + lorem_ipsum2
# print(f"\n\nlorem_ipsum1+2\n-------------------\n{lorem_ipsum1_2}\n-------------------\n\n")

lorem_ipsum1and2_list = [lorem_ipsum1, lorem_ipsum2]
print(f"lorem_ipsum1and2_list\n-------------------\n{json.dumps(lorem_ipsum1and2_list)}\n-------------------\n")

dotLists = list(map(lambda x: x.split("."), lorem_ipsum1and2_list))
print(f"\n• dotLists\n-------------------\n{json.dumps(obj=dotLists, indent=4)}\n-------------------\n")

all_lists = split_inner_list(array_of_arrays=dotLists, char="!")
print(f"\n• all_lists dot\n-------------------\n{json.dumps(obj=all_lists, indent=4)}\n-------------------\n")

# print("\n\\===================================================================")
# all_lists = list(map(lambda x: x.split("!"), all_lists))
# print(f"\n• all_lists bang\n-------------------\n{json.dumps(obj=all_lists, indent=4)}\n-------------------\n")

# all_lists = split_inner_list(array_of_arrays=all_lists, char="?")
# print(f"\n• all_lists question\n-------------------\n{json.dumps(obj=all_lists, indent=4)}\n-------------------\n")