def ir_calculator(salary):
    salary = salary*12
    if salary < 22847.76:
        print("Parabéns! Você está isento do pagamento do IRPF!")
        
    elif salary < 33919.80:
        deduction = 1713.58
        ir = (salary*(7.5)/100) - deduction
        print(f"Boa notícia! Você só vai pagar R$ {ir:.2f} de imposto!")
        
    elif salary < 45012.60:
        deduction = 4257.57
        ir = (salary*(15)/100) - deduction
        print(f"Você terá de pagar R$ {ir:.2f} de imposto.")
    
    elif salary < 55976.16:
        deduction = 7633.51
        ir = (salary*(22.5)/100) - deduction
        print(f"Lamento, mas você terá de pagar R$ {ir:.2f} de imposto.")
    
    else:
        deduction = 10432.32
        ir = (salary*(27.5)/100) - deduction
        print(f"Um dia triste na vida do jovem, você terá de pagar R$ {ir:.2f} de imposto.")
        
salary = int(input("Digite aqui o seu salário em R$: "))
ir_calculator(salary)
