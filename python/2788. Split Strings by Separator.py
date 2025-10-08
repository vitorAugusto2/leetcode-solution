class Solution:
    def splitWordsBySeparator(self, words: List[str], separator: str) -> List[str]:
        list_split = []
        
        for word in words:
            aux_list = word.split(separator)
            for word in aux_list:
                if word != "":
                    list_split.append(word) 
        
        return list_split

