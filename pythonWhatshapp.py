import pywhatkit

#Put the phone to send mensage
numberPhone = "+34xxxxxxxx"

#Search your GroupID
groupId = "https://chat.whatsapp.com/example"

#Example 1
#Number fone with prefix, mensage, time to deliver
pywhatkit.sendwhatmsg(numberPhone, "Test" , 9,30)

#Example 2
#Number fone with prefix, mensage, time to deliver, Close tap in 2 seconds
pywhatkit.sendwhatmsg(numberPhone, "Test" , 9, 30, 15, True, 2)

#Example 3 For Groups
#Number fone with prefix, mensage, time to deliver, Close tap in 2 seconds
pywhatkit.sendwhatmsg_to_group(groupId, "Test 2" , 9,30)