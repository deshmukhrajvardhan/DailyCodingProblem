#Given a list of strings, find the length of the longest chain formed by adding a single letter to the end of each word in the chain but the last, where every word in the chain must exist in the list. 

#words = [“sfg”, “sfgas”, “as”, “add, ”awa”, “sfga”,"ad", “asad”]
#chain1 (length 3): sfg->sfga->sfgas
#chain2 (length 2): ad->add
#the answer is 3
#{S:{f:{G:{}}},a:{d:{d:{}}}}

class Chain:
    def __init__(self):
        self.word_dict=dict()
        self.string=None
        self.string_list=None
    
    def add_word(self,string):
        self.string=string
        self.string_list=list(self.string)
        self.len_word=len(self.string_list)
        dict_level=self.word_dict
        self.flag=0
        #[‘s’,’f’.’g’]=> {s:{f:{g:}}}
        self._add_word(0,dict_level)

    def _add_word(self,current_index,dict_level):
        print(dict_level.keys())
        if current_index<self.len_word-1:
            try: 
                dict_level[self.string_list[current_index]][0]
                self._add_word(current_index+1,dict_level[self.string_list[current_index]][0])
            except KeyError: ###”abc” “abcde”
                    dict_level[self.string_list[current_index]]=[dict()]
                    self._add_word(current_index+1,dict_level[self.string_list[current_index]][0])
        else:
            print(self.string_list[current_index],dict_level.keys())
            try:
                dict_level[self.string_list[current_index]]
                if len(dict_level[self.string_list[current_index]])==2: 
                    dict_level[self.string_list[current_index]][1]=0
                else:
                    dict_level[self.string_list[current_index]].append(0)
            except:
                dict_level[self.string_list[current_index]]=[dict(),0]
            return
            
#    {g:[{},#times referenced]
#    words = [“abc”, ”abcde”] 2
#    abc->abcd->abcde
    def find_longest_chain(self):
        level_dict=self.word_dict
        level_len=0
        self.chain_length=0 #[]
        self.max_chain_l=0
        prev_c=0
        self._find_longest_chain(level_dict,prev_c)
        print(level_dict.keys(),self.max_chain_l+1)
        
    def _find_longest_chain(self,level_dict,prev_c):
        if level_dict and type(level_dict)is not list:
            for key in level_dict.keys():
                k=key
                if type(key) is list:
                    k=key[0]
                print("key:{},value:{}".format(k,level_dict[k]))
                li=level_dict[k]
                if len(li)==2:
                    if prev_c==1:
                        self.chain_length+=1
                
                try:
                    if self.chain_length> self.max_chain_l:
                        self.max_chain_l=self.chain_length
                except IndexError:
                    print("li:{},level_dict[key]:{}".format(li,level_dict[key]))
                #level_len+=1
                self._find_longest_chain(li,prev_c)
        elif type(level_dict) is list:
            if len(level_dict)==2:
                prev_c=1
            else:
                prev_c=0
                
            self._find_longest_chain(level_dict[0],prev_c)
            
        else:
            print("l_dict:{},chain_len:{}".format(level_dict,self.chain_length))
            self.chain_length=0
            #level_len=0
            return
        
# abc
#a{b:{c:[1]}}}
#words <= N
#word <= k
#{}
if __name__=='__main__':
    ch=Chain()
    words=["sfg", "sfgas", "as", "add","sfga", "awa","ad", "asada","addd","add"]
    for word in words:
        print(word)
        ch.add_word(word)
    ch.find_longest_chain()
    print(ch)
