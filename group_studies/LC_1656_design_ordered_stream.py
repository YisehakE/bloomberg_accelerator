
'''

Reflection


'''




'''
Solution 1: My own solution worked out in 30 mins

T: O(n)
S: O(n)

'''
class OrderedStream(object):

    def __init__(self, n):
        """
        :type n: int
        """
        self.n = n
    
        self.DEFAULT_STR = "######"
        self.stream_list = ["######"]*n
        self.curr_ptr = 0
        

    def insert(self, idKey, value):
        """
        :type idKey: int
        :type value: str
        :rtype: List[str]
        """

        id_index = idKey - 1 # Zero index the idkey
        self.stream_list[id_index] = value # Put 5 letter value at idKey <-> index eqv spot

        ordered_stream = []
        while self.curr_ptr != self.n and self.stream_list[self.curr_ptr] != self.DEFAULT_STR:
            ordered_stream.append(self.stream_list[self.curr_ptr])
            self.curr_ptr += 1 
        
        return ordered_stream
        



'''
TESTS

'''

