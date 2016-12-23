"""
    Create a hierarchical class system, using the skeletion in assignment2.
    It should produce the outputs below and store them in a file
    Do it in as few lines as possible.
"""

from assignment2_answer import LogFile, DelimFile

log = LogFile("log.txt")
c = DelimFile("text.csv", ",")

log.write("This is a log message") #YYYY-MM-DD HH:MM this is a log message
log.write("This is another log message") #YYYY-MM-DD this is another log message

c.write(['a', 'b', 'c', 'd']) #a,b,c,d
c.write(['1', '2', '3', '4']) #1,2,3,4
