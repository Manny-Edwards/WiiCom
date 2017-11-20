'''
'''
'''
On API
It sends information to the PI's wiimote writer using a thread. 
'''

'''
On Big Brother
Has an automated cycle that makes a get and post request to the API every 3 seconds. 
get- It gets information from Big brother.
post- it posts to the API when it does have a message in the database.
Log- It keeps a time stamped log of information
'''

'''
On pi
WIID function- function to integrate wii controls into commands sent from the API

wiimote reader- It collects information  given from the wiimote and then sends it to the database and makes a post request
to BigBrother. 
wiimote writer- It takes information from the API and sends the command to the Wiimote to do the commands.

Implement a Lock to handle simultaneous posting and receiving. A wiimote can only make a post when it has the lock. 
'''

'''
In database
stores all posts from the wiimote reader.
'''