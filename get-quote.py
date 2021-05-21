def main():
  print("Keep it logically awesome.")
  
   f = open("quotes.txt", "a")
   f.write("Have a good day!")

  f = open("quotes.txt")
  quotes = f.read()
  f.close()

  #last = 13
  #rnd = random.randint(0, last)
  print(quotes[3:])
  
if __name__ == "__main__":
 main()  
