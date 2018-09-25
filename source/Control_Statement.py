

logger.info("=============== ATM Application ============== #")
logger.info("Insert your card")
logger.info("Enter your password:")
pass_word = input()
# Get Card password from db
# To validate the entered password
# Get card account details and balance
balance = 20000

while True:  # while True/Falsee
    logger.info("Enter option to continue")
    logger.info("1.Withdraw\t2.Balance Check")
    option = int(input())
    if option == 1:
        logger.info("Enter amount to Withdraw:")
        withdraw_amount = int(input())
        if withdraw_amount <= balance:
            balance = balance - withdraw_amount
            logger.info("Collect Amount: %s", withdraw_amount)

            else:
            logger.warning("You entered amount more than available balance")
            continue

    elif option == 2:
        logger.info(balance)

        else:
        logger.info("You have selected wrong option, Try again")
        continue
        logger.info("Do you want to continuew y/n")
        continue_option = input()
        if continue_option == "n":
            break

