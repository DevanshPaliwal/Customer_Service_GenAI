# Update the issue column to "UPI" for all sentences
import pandas as pd


data = {
    "Sentence": [
    "Hi, I'm trying to make a payment, but it's saying my UPI PIN is incorrect. Can you help me with this?",
    "I keep getting an error that my UPI PIN is wrong. What should I do?",
    "I'm having trouble with my UPI transaction because it says my PIN is incorrect. Can you assist?",
    "Every time I try to make a payment, it says my UPI PIN is invalid. What's going on?",
    "I've entered my UPI PIN correctly, but it's still showing as incorrect. Please help!",
    "I’m unable to complete my UPI transaction because the bank server is down. Can you help?",
    "My UPI payment keeps failing due to a bank server issue. What should I do?",
    "I’ve been trying to make a UPI payment, but it says the bank server is down. Can you assist?",
    "The bank server seems to be down, and my UPI transaction isn’t going through. Can you check?",
    "Every time I try a UPI transaction, it fails due to the bank server being down. Please help.",
    "I need to reset my UPI PIN. Can you guide me through the process?",
    "How can I reset my UPI PIN? I forgot my current one.",
    "Can you help me with resetting my UPI PIN? I can't remember it.",
    "What steps do I need to follow to reset my UPI PIN?",
    "I’m having issues with my UPI PIN and need to reset it. Can you assist?" ,       
# deposit 
 	"I'm having trouble depositing money into my account.",
    	"My deposit isn't going through for some reason.",
    	"Why is my deposit being rejected?",
    	"I'm trying to deposit money, but it keeps failing.",
    	"Can you help me? My deposit won't process.",
    	"I'm getting an error every time I try to make a deposit.",
    	"My deposit attempt just resulted in an error message.",
    	"I've tried several times, but my deposit isn't being accepted.",
    	"I need assistance with a failed deposit.",
    	"The system isn't letting me deposit funds.",
    	"There's a problem with my deposit transaction.",
    	"My deposit isn't showing up in my account.",
    	"Why am I getting an error when I try to deposit?",
    	"My money isn't being deposited, even though I've tried multiple times.",
    	"Every time I deposit money, I get an error notice. What should I do?",
    # withdrawal
	"I'm unable to withdraw funds from my account.",
    	"My withdrawal request keeps failing.",
    	"Can you tell me why my withdrawal is being denied?",
    	"I'm experiencing problems when trying to withdraw money.",
    	"Each time I attempt a withdrawal, I encounter an error.",
    	"I'm facing issues with the withdrawal process.",
    	"My withdrawal keeps getting declined.",
    	"I've tried withdrawing money, but it's not working.",
    	"I need help with a withdrawal that didn't go through.",
    	"The system isn't processing my withdrawal request.",
    	"There seems to be an issue with my withdrawal.",
    	"My account won't let me withdraw money.",
    	"Why is my withdrawal not being processed?",
    	"I'm not able to take money out of my account.",
    	"Every time I try to withdraw money, it gets blocked.",
        # Loan
    "I can't find the information on my remaining loan amount. Can you assist?",
    "Where can I check the balance of my remaining loan?",
    "The app isn’t showing my remaining loan amount. What should I do?",
    "I’m unable to see the details of my outstanding loan balance.",
    "Could you help me locate the remaining balance on my loan?",
    "How can I find out the current interest I need to pay on my loan?",
    "I want to check the interest due on my loan. Where can I see it?",
    "The interest amount on my loan isn’t visible. Can you help me find it?",
    "Can you tell me how much interest I owe on my current loan?",
    "I need assistance in viewing the current interest charges on my loan.",
    "Can you guide me on how to apply for a new loan?",
    "What is the process for taking out a loan with your bank?",
    "I need information on how to get a loan. Can you help?",
    "How can I start the application process for a loan?",
    "Could you explain the steps involved in obtaining a loan?",
    #Open Account
    "How do I open an account in your bank?",
    "Can you guide me through the process of opening a bank account?",
    "What are the steps to open a new account with your bank?",
    "What documents do I need to provide to open a bank account?",
    "Is it possible to open a bank account online, and if so, how?",
    "What is the minimum deposit required to open a new account?",
    "How long does it take to open a bank account with your bank?",
    "Can I open an account with your bank if I am not a resident of the country?",
    "What are the eligibility criteria for opening a bank account?",
    "Can you explain the process for opening a joint account at your bank?",
    "What types of accounts can I open with your bank?",
    "Can you provide information on the different types of accounts your bank offers?",
    "What is the difference between a savings account and a checking account at your bank?",
    "Does your bank offer business accounts, and how do I open one?",
    "Are there any special accounts available for students or minors at your bank?"

    	],
    "Issue": [
        "UPI",
        "UPI",
        "UPI",
        "UPI",
        "UPI",
        "UPI",
        "UPI",
        "UPI",
        "UPI",
        "UPI",
        "UPI",
        "UPI",
        "UPI",
        "UPI",
        "UPI",
	"DEPOSIT",
	"DEPOSIT",
	"DEPOSIT",
	"DEPOSIT",
	"DEPOSIT",
	"DEPOSIT",
	"DEPOSIT",
	"DEPOSIT",
	"DEPOSIT",
	"DEPOSIT",
	"DEPOSIT",
	"DEPOSIT",
	"DEPOSIT",
	"DEPOSIT",
	"DEPOSIT",
	"WITHDRAWAL",
	"WITHDRAWAL",
	"WITHDRAWAL",
	"WITHDRAWAL",
	"WITHDRAWAL",
	"WITHDRAWAL",
	"WITHDRAWAL",
	"WITHDRAWAL",
	"WITHDRAWAL",
	"WITHDRAWAL",
	"WITHDRAWAL",
	"WITHDRAWAL",
	"WITHDRAWAL",
	"WITHDRAWAL",
	"WITHDRAWAL",
    "LOAN",
    "LOAN",
    "LOAN",
    "LOAN",
    "LOAN",
    "LOAN",
    "LOAN",
    "LOAN",
    "LOAN",
    "LOAN",
    "LOAN",
    "LOAN",
    "LOAN",
    "LOAN",
    "LOAN",
    "OPEN ACCOUNT",
	"OPEN ACCOUNT",
	"OPEN ACCOUNT",
	"OPEN ACCOUNT",
	"OPEN ACCOUNT",
	"OPEN ACCOUNT",
	"OPEN ACCOUNT",
	"OPEN ACCOUNT",
	"OPEN ACCOUNT",
	"OPEN ACCOUNT",
	"OPEN ACCOUNT",
	"OPEN ACCOUNT",
	"OPEN ACCOUNT",
	"OPEN ACCOUNT",
	"OPEN ACCOUNT",
    ]
}

# Create the DataFrame
df = pd.DataFrame(data)

# Save to CSV
file_path = "SentenceToIssues.csv"
df.to_csv(file_path, index=False)