balance = 10  # ანას ბალანსი

apple = 5
pear = 2

# მომხმარებლისგან ვკითხოთ რისი ყიდვა უნდა
choice = input("რას იყიდი? (ვაშლი ან მსხალი): ")

if choice == "ვაშლი":
    if balance >= apple:
        balance = balance - apple
        print("ვაშლი იყიდე. დარჩენილი ბალანსი:", balance, "ლარი")
    else:
        print("არ გაქვს საკმარისი თანხა ბალანსზე!")
elif choice == "მსხალი":
    if balance >= pear:
        balance = balance - pear
        print("მსხალი იყიდე. დარჩენილი ბალანსი:", balance, "ლარი")
    else:
        print("არ გაქვს საკმარისი თანხა ბალანსზე!")
else:
    print("არჩევანი არასწორია.")



