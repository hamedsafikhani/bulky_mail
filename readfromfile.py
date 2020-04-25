f = open('./mail-send-list.txt','r')
a = f.readlines()

all_mail = []
for i in a :
    all_mail.append(i.strip())
# print(all_mail)

toList = []
bcc_list = []
def send_email(x):
    for i in all_mail:
        # print(a.index(i))
        if all_mail.index(i) % x == 0:
            # print(all_mail.index(i))
            toList.append(i)
            bcc_list.append(all_mail[all_mail.index(i)+1 :all_mail.index(i) + x])
    return (toList,bcc_list)

# print(len(toList), " : " , toList)
# print(len(bcc_list), " : " ,bcc_list)

