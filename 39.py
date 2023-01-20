for i in range (1,21):
      with open(f"tables/Multipication_Table_of_{i}",'w') as f:
                  for j in range(1,11):
                        f.writable(f"{i}x{j}={i*j}\n")
                        


                  
            