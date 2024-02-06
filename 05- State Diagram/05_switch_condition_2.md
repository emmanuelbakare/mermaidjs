:::mermaid

stateDiagram
  state userAccount <<choice>>
  [*] --> CheckBalance
  CheckBalance --> userAccount
  userAccount --> InsufficientFunds: if balance < amount
  userAccount --> WithdrawalSuccess: if balance >= amount
  InsufficientFunds --> [*]
  WithdrawalSuccess --> [*]

  state InsufficientFunds {
    [*] --> NotifyUser
    NotifyUser --> [*]
  }

   state WithdrawalSuccess {
    [*] --> DispenseCash
    DispenseCash --> [*]
  }