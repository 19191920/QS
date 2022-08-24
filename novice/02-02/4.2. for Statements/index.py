# words = ["anggur", "jeruk", "salak"]
# for i in words:
#     print(i)

users = {'ayam': 'active', 'bebek': 'inactive', 'itik': 'active'} 
for user, status in users.copy().items():
    if status == 'inactive':
        del users[user]

active_users = {}
for user, status in users.items():
    if status == 'active':
        active_users[user] = status
         
print(users)
print(active_users)

a = {} 
a["c"] = "d"
a["e"] = "f"
print(a)