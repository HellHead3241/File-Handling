file = open("bucket-list.txt", "w")
file.write("1.Visit the Eiffel Tower\n")
file.write("2 Learn to play the drums\n")
file.write("3 Code my own game\n")
file.close()
print("Bucket list saved to bucketlist.txt!")


file = open("bucket-list.txt", "r")
content = file.read()
print("\n=== My Bucket List ===")
print(content)
file.close()



file = open("bucket-list.txt", "r")
lines = file.readlines()
print(f"You have {len(lines)} Items on your bucket list")
file.close()


file = open("bucket-list.txt", "a")
file.write("4 Travel to Japan\n")
file.write("5 Run a 10km marathon\n")
file.close()
print("\n2 more lines added!")


file = open("bucket-list.txt", "r")
print("\n=== Updated Bucket List ===")
print(file.read())
file.close