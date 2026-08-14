class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        word_dict = {}
        return_list = []

        for wrd in strs:
            sorted_word = "".join(sorted(wrd))
            word_dict[sorted_word] = []

        for wrd in strs:
            sorted_word = "".join(sorted(wrd))

            if sorted_word in word_dict:
                word_dict[sorted_word].append(wrd)


        for key,value in word_dict.items():
            return_list.append(value)

        
        return return_list


            

        