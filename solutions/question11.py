class AutoComplete:
    def __init__(self,string=None):   
        self.auto_complete_dict={}
        self.string_list = None
        self.string = None
        if string is not None:
            self.make_entry(string)
    
    def make_entry(self, string):
        self.string_list = list(string)
        self.string = string
        self.str_end_index = len(self.string_list)-1
        curr_level_dict = self.auto_complete_dict
        current_index = 0
        self._make_entry(current_index,curr_level_dict)
#         print(self.auto_complete_dict)
        
    def _make_entry(self,current_index,curr_level_dict):
        if current_index <= self.str_end_index:
            try:
#                 print(self.string)
                curr_level_dict[self.string_list[current_index]].append(self.string)
                self._make_entry(current_index+1,curr_level_dict[self.string_list[current_index]][0])
            except KeyError: # takes care of exceptions and keeps O(1)
#                 print(self.string)
                curr_level_dict[self.string_list[current_index]]=[dict(),self.string]
                self._make_entry(current_index+1,curr_level_dict[self.string_list[current_index]][0])

        else:
            return
        
    def fetch_auto_complete(self,incomplete_string):
        self.incomplete_string_list = list(incomplete_string)
        self.str_end_index = len(self.incomplete_string_list)-1
        current_index = 0
        curr_level_dict = self.auto_complete_dict
        self._fetch_auto_complete(current_index,curr_level_dict)
        
    def _fetch_auto_complete(self,current_index,curr_level_dict):
        if current_index <= self.str_end_index:
            try:
#                 print(self.string)
                if current_index == self.str_end_index:
                    print("words:{}".format(curr_level_dict[self.incomplete_string_list[current_index]][1:]))
                else:
                    self._fetch_auto_complete(current_index+1,curr_level_dict[self.incomplete_string_list[current_index]][0])
            except KeyError:
                print("No such Word")
        else:
            return

        
if __name__ == '__main__':
    a1 = AutoComplete("hid")
    a1.make_entry("hide")
    a1.make_entry("hideous")
    a1.make_entry("lo")
    a1.make_entry("loop")
    a1.make_entry("behold")
    a1.fetch_auto_complete("hik")
