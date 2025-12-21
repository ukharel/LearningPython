# Format specifier - (value: flags) format the value based on what flags is inserted


'''
.(number)f - round to that many decimals places
:(number) - allocate that many spaces
:0(number) - allocate and zero pad that many spaces
:< - left justify
:> - right justify
:^ - centre justify
:+ - add plus sign to indicate positive number
:= - place sign to leftmost position
: - enter a space before postive number
:, - add comma seperator

'''

amount1 = 2341.122334
amount2 = -13423.23
amount3 = 12343.1111


print(f'Amount1 is ${amount1:.3f}')
print(f'Amount2 is ${amount2:10}')
print(f'Amount3 is ${amount3:015}')
print(f'Amount1 is ${amount1:<15}')
print(f'Amount2 is ${amount2:>15}')
print(f'Amount3 is ${amount3:^15}')
print(f'Amount2 is ${amount3:+}')
print(f'Amount3 is ${amount3:=}')
print(f'Amount2 is ${amount2:,}')
print(f'Amount3 is ${amount3:>+,.2f}')
