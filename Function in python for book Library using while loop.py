def run():
    print("Welcome User! How Can I Help You")

    
    while True:
        print("\n1. Continue")
        print("2. Exit")
        choice = input("Enter your choice (1 or 2): ")
        if choice == "1":
            book()
        elif choice == "2":
            print("Thanks for visiting us: ")
            break
        else:
            print("Invalid Input given")
def book():
    while True:
        print("\n SELECT A BOOK: ")
        print("Enter 1 for To Kill a Mockingbird by Harper Lee ")
        print("Enter 2 for 1984 by George Orwell")
        print("Enter 3 for The Alchemist by Paulo Coelho")
        print("Enter 4 for The Great Gatsby by F. Scott Fitzgerald")
        print("Enter 5 for Harry Potter and the Sorcerer’s Stone by J.K. Rowling")
    
        b = input("Enter a number (1 to 5): ")
        if b == "1":
            print("\nTo Kill a Mockingbird by Harper Lee -> \n-------- Description -------- \n A timeless classic exploring racial injustice and moral growth in the Deep South. Told through the eyes of young Scout Finch, it teaches empathy, courage, and integrity.")
        elif b == "2":
            print("\n1984 by George Orwell -> \n-------- Description -------- \n A dystopian novel about a totalitarian regime that controls truth, history, and thought. It’s a powerful warning about surveillance, propaganda, and loss of freedom.")
        elif b == "3":
            print("\nThe Alchemist by Paulo Coelho -> \n-------- Description -------- \n A philosophical tale about following one’s dreams and listening to the heart. It follows Santiago, a shepherd, on his journey to find his personal legend")
        elif b == "4":
            print("\nThe Great Gatsby by F. Scott Fitzgerald -> \n-------- Description -------- \n Set in the roaring 1920s, it depicts love, wealth, and the illusion of the American Dream. Jay Gatsby’s tragic pursuit of Daisy Buchanan reflects the emptiness of materialism.")
        elif b == "5":
            print("\nHarry Potter and the Sorcerer’s Stone by J.K. Rowling -> \n-------- Description -------- \n The first book in the magical Harry Potter series. It introduces a boy wizard discovering friendship, courage, and destiny at Hogwarts. ")
        else:
            print("Invalid Input \n ---------- No Book Found ----------")
            continue
        more = input("\n Do you want to read more books? (yes/no): ").strip().lower()
        if more != "Yes":
            print("Retuning to main menu")
            break
run()
        

