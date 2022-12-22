g_income=int(input('enter your gross income(in dollars)'))
no_dependent=int(input('enter total number of dependents'))
taxable_income=g_income-10000-(3000*no_dependent)

tax=taxable_income*0.20

print('total payable tax=',tax)