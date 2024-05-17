function onClickedcreditpredictor(){
    console.log("Estimated Credit Score button clicked")
    var age = document.getElementById("age").value;
    var annualIncome = document.getElementById("annual_income").value;
    var monthlyInhandSalary = document.getElementById("monthly_inhand_salary").value;
    var numBankAccounts = document.getElementById("num_bank_accounts").value;
    var numCreditCard = document.getElementById("num_credit_card").value;
    var interestRate = document.getElementById("interest_rate").value;
    var delayFromDueDate = document.getElementById("delay_from_due_date").value;
    var numOfDelayedPayment = document.getElementById("num_of_delayed_payment").value;
    var changedCreditLimit = document.getElementById("changed_credit_limit").value;
    var numCreditInquiries = document.getElementById("num_credit_inquiries").value;
    var outstandingDebt = document.getElementById("outstanding_debt").value;
    var creditUtilizationRatio = document.getElementById("credit_utilization_ratio").value;
    var totalEMIPerMonth = document.getElementById("total_emi_per_month").value;
    var amountInvestedMonthly = document.getElementById("amount_invested_monthly").value;
    var monthlyBalance = document.getElementById("monthly_balance").value;
    var creditHistoryAgeMonths = document.getElementById("credit_history_age_months").value;
    var occupation = document.getElementById("uiOccupation").value;
    var creditMix = document.getElementById("uiCredit_mix").value;
    var estcrd =document.getElementById("uiEstimatedCreditScore");

    var url = "http://127.0.0.1:5000/predict_credit_score";
    $.post(url,{
        age: age,
        annual_income: annualIncome,
        monthly_inhand_salary: monthlyInhandSalary,
        num_bank_accounts: numBankAccounts,
        num_credit_card: numCreditCard,
        interest_rate: interestRate,
        delay_from_due_date: delayFromDueDate,
        num_of_delayed_payment: numOfDelayedPayment,
        changed_credit_limit: changedCreditLimit,
        num_credit_inquiries: numCreditInquiries,
        outstanding_debt: outstandingDebt,
        credit_utilization_ratio: creditUtilizationRatio,
        total_emi_per_month: totalEMIPerMonth,
        amount_invested_monthly: amountInvestedMonthly,
        monthly_balance: monthlyBalance,
        credit_history_age_months: creditHistoryAgeMonths,
        occupation: occupation,
        credit_mix: creditMix
    },function(data,status){
        console.log(data.estimated_credit_score);
        estcrd.innerHTML = "<h2>" + data.estimated_credit_score.toString() + " </h2>";
        console.log(status);
    });


}






function onPageLoad() {
    console.log( "document loaded" );
    var url = "http://127.0.0.1:5000/get_credit_score"; // Use this if you are NOT using nginx which is first 7 tutorials
    //var url = "/api/get_location_names"; // Use this if  you are using nginx. i.e tutorial 8 and onwards
    $.get(url,function(data, status) {
        console.log("got response for get_credit_mix & get_occupation_names request");
        if(data) {
            var credit_mix = data['credit-mix'];
            var uiCredit_mix = document.getElementById("uiCredit_mix");
            $('#uiCredit_mix').empty();
            for(var i in credit_mix) {
                var opt = new Option(credit_mix[i]);
                $('#uiCredit_mix').append(opt);
            }
            var occupation = data.occupation;
            var uiOccupation = document.getElementById("uiOccupation");
            $('#uiOccupation').empty();
            for(var i in occupation) {
                var opt = new Option(occupation[i]);
                $('#uiOccupation').append(opt);
            }
            
        }
    });
  }
  window.onload =onPageLoad;