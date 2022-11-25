#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Q1:-Create an assert statement that throws an AssertionError if the variable spam is a negative integer.
#Ans:-
spam = -55
assert spam > 0, 'The spam variable is is a negative integer.'


# <b>------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# In[13]:


#Q2:- Write an assert statement that triggers an AssertionError if the variables eggs and bacon contain
strings that are the same as each other, even if their cases are different (that is, &#39;hello&#39; and &#39;hello&#39; are
considered the same, and &#39;goodbye&#39; and &#39;GOODbye&#39; are also considered the same).

#Ans:-
                                                                            
eggs = 'hello'
bacon = 'Hello'

assert eggs.lower() != bacon.lower(), 'The eggs and bacon variables are the same!' 
assert eggs.upper() != bacon.upper(), 'The eggs and bacon variables are the same!'


# In[ ]:


#Q3:-Create an assert statement that throws an AssertionError every time.

#Ans:-assert False, 'This assertion always triggers.'


# In[ ]:





# In[ ]:


#Q4:-What are the two lines that must be present in your software in order to call logging.debug()?

#Ans:-To be able to call logging.debug(), you must have these two lines at the start of your program:


# In[2]:


import logging
logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s -%(levelname)s - %(message)s')


# In[ ]:





# In[ ]:


#Q5:-What are the two lines that your program must have in order to have logging.debug() send a logging message to a file named programLog.txt?

#Ans:-To be able to send logging messages to a file named programLog.txt with logging.debug(), you must have these two lines at the start of your program:


# In[3]:


import logging
logging.basicConfig(filename='programLog.txt', level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')


# In[ ]:





# In[ ]:


#Q6:-What are the five levels of logging?

#Ans:-DEBUG, INFO, WARNING, ERROR, and CRITICAL


# In[ ]:





# In[ ]:


#Q7:-What line of code would you add to your software to disable all logging messages?

#Ans:-logging.disable(logging.CRITICAL)


# In[ ]:





# In[ ]:


#Q8:-Why is using logging messages better than using print() to display the same message?

#Ans:-You can disable logging messages without removing the logging function calls. You can selectively disable lower-level logging messages. 
#     You can create logging messages. Logging messages provides a timestamp.


# In[ ]:





# In[ ]:


#Q9:-What are the differences between the Step Over, Step In, and Step Out buttons in the debugger?

#Ans:-The Step button will move the debugger into a function call. The Over button will quickly execute the function call without stepping into it. 
#     The Out button will quickly execute the rest of the code until it steps out of the function it currently is in.


# In[ ]:





# In[ ]:


#Q10:-After you click Continue, when will the debugger stop ?

#Ans:-After you click Continue, the debugger will stop when it has reached the end of the program or a line with a breakpoint.


# In[ ]:





# In[ ]:


#Q11:-What is the concept of a breakpoint?

#Ans:-Breakpoint is a setting on a line of code that causes the debugger to pause when the program execution reaches the line

