import pandas as pd
from path import Path
from users import get_users
from investors import get_investors
from usersLoanBook import get_usersLoanBook
from userLoanApproval import userLoanApproval
 
user_df = get_users()
investor_df = get_investors()
usersLoanBook_df = get_usersLoanBook()
 
userID = 'U10001'
loanRequest = 200000
investor_selected = userLoanApproval(userID,loanRequest,investor_df,user_df,usersLoanBook_df)