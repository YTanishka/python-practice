registered = input()
fee_paid = input()
verified = input()
system_checker = input()

if registered == "yes":
    if fee_paid == "yes" and verified == "yes":
        if system_checker == "pass":
            print("Access Granted")
        else:
            print("Access Denied: system checker failed")
    else:
        print("Access Denied: Not  Verified")
else:
    print("Access Denied: Not Registered")
