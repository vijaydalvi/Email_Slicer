email=input("Enter Your Email Id:").strip()
username=email[: email.index("@")]
domin=email[email.index("@")+1:]
print("Your  User Name is",username)
print("Domin Name is:",domin)