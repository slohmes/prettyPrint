class StopwatchRecord:
    def __init__(self, key, start_time, end_time):
        self.key=key
        self.start_time=start_time
        self.end_time=end_time
    
    
def print_record(R,indent): #function to print each StopwatchRecord
    print R.start_time,indent*"    ","[",R.end_time-R.start_time,"]",R.key
      
def prettyPrint(A): #function to print a StopwatchRecord array
    # I'm assuming that the actual nesting of the function calls is based on their location in the array,
    # so this prettyPrint function bases the indentation level on record location in the array.
    indent = -1
    for i in range(0, (len(A)/2)+1): #left half of array
            indent+=1
            print_record(A[i],indent)
            
    for i in range((len(A)/2)+1, len(A)): #right half of array
            indent-=1
            print_record(A[i],indent)


myInput =[StopwatchRecord('render_module', 101.0, 105.0), StopwatchRecord('get_data', 101.1, 101.2), StopwatchRecord('get_data', 101.5, 103.0), StopwatchRecord('cache_get_data', 101.6, 101.7), StopwatchRecord('db_get_data', 101.8, 102.9), StopwatchRecord('render_module', 103.1, 104.9), StopwatchRecord('render_module', 105.1, 106.0)]
prettyPrint(myInput)




