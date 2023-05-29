liste = []

def add_list(name,bid):
      hight_bid = 0
      new_people = {}
      new_people["Name"] = name
      new_people["Bid"] = bid
      liste.append(new_people)
      print(liste)

      desicion = input("Are there any other bidders ? Type 'yes' or 'no' ")
      if desicion == "yes":
            add_list(input("What is your name?: "), input("Whats is your bid?: "))
      else:
            for i in range(len(liste)):
                  if int(liste[i]["Bid"]) > hight_bid:
                        hight_bid= int(liste[i]["Bid"])
                        print("The winner is "+ liste[i]["Name"] +" with a bid of " + str(hight_bid))

            

add_list(input("What is your name?: "), int(input("Whats is your bid?: ")))
