with open('result.txt', 'r', encoding='utf-8') as f:
    user_set = set()
    for line in f:
        id, email, nickname = line.split(',')
        user_set.add((id, email, nickname))
print(len(user_set))
with open('ids.txt', 'w', encoding='utf-8') as f:
    for user,_,name in user_set:
        name = name.replace('\n', '')
        f.write(f'{user},{name}\n')
#
# with open('mail-nickname-checklist.txt', 'a+', encoding='utf-8') as f:
#     for id_, email_, nickname_ in user_set:
#         nickname_ = nickname_.replace('\n', '')
#         if email_ != 'None':
#             f.write(f'{email_},{nickname_}\n')
