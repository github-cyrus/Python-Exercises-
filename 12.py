
# customize letter

letter = '''
  
  Javed

Read More Book Store

24, Crosby Lane

Bangalore 600045

<|Date|>

The Manager

<|Name|>

Mumbai 400012

Subject: Requirement of new books for the store – reg.

Dear Sir,

I have received the books that you had sent last week. The books are in perfect condition, and they were delivered on time. Owing to the great service rendered, I would like to order more books that would be a great addition to the wide range of books available at my store. Given below is a list of books that I would like to purchase:
  
  
  
  
  
  '''

a = input("Enter Yoour Name :")
b = input("Enter Yoour Date :")

letter = letter.replace("<|Name|>",a)
letter = letter.replace("<|Date|>",b)

print(letter)