import os
from currency_converter import CurrencyConverter
from crypto_converter import CryptoConverter

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def main():
    cc = CurrencyConverter()
    cc_crypto = CryptoConverter()

    while True:
        clear_screen()
        #Logo
        print("\n" + "="*40)
        print("CONVERSOR DE MOEDAS".center(40))
        print("="*40 + "\n")

        print("Escolha uma opção:")
        print("1. Converter moeda")
        print("2. Converter criptomoeda")
        print("3. Ver preço do câmbio atual")
        print("4. Ver preço de criptomoeda")
        print("5. Mostrar abreviações de moedas mais usadas")
        print("6. Sair")

        opcao = input("\nDigite o número da opção desejada: ")

        if opcao == '1':
            #Logo
            clear_screen()
            print("\n" + "="*40)
            print("CONVERSOR DE MOEDAS".center(40))
            print("="*40 + "\n")

            base_currency = input("Converter de: ")
            target_currency = input("Para: ")
            amount = float(input("Digite o valor: "))

            result = cc.convert(base_currency, target_currency, amount)

            #Logo
            clear_screen()
            print("\n" + "="*40)
            print("CONVERSOR DE MOEDAS".center(40))
            print("="*40 + "\n")
            
            print(f"{amount} {base_currency} equivale a {round(result, 2)} {target_currency}\n")
            input("Pressione ENTER para continuar...")
        
        elif opcao == '2':
            #Logo
            clear_screen()
            print("\n" + "="*40)
            print("CONVERSOR DE MOEDAS".center(40))
            print("="*40 + "\n")

            amount = float(input("Digite a quantidade de dinheiro que você tem: "))
            base_currency = input("Digite a moeda que você tem: ").lower()
            crypto_currency = input("Digite a criptomoeda que você deseja comprar (utilize o nome e não a abreviação): ").lower()

            try:
                #Logo
                clear_screen()
                print("\n" + "="*40)
                print("CONVERSOR DE MOEDAS".center(40))
                print("="*40 + "\n")

                result = cc_crypto.convert(amount, base_currency, crypto_currency)
                print(f"Com {amount:.2f} {base_currency}, você pode comprar {result:.8f} {crypto_currency}")
            
            except Exception as e:
                #Logo
                clear_screen()
                print("\n" + "="*40)
                print("CONVERSOR DE MOEDAS".center(40))
                print("="*40 + "\n")

                print(f"Erro: {str(e)}")

            input("\nPressione ENTER para continuar...")

        elif opcao == '3':
            #Logo
            clear_screen()
            print("\n" + "="*40)
            print("CONVERSOR DE MOEDAS".center(40))
            print("="*40 + "\n")

            base_currency = input("Digite a moeda base: ")
            target_currency = input("Digite a moeda alvo: ")

            rate = cc.convert(base_currency, target_currency, 1)

            #Logo
            clear_screen()
            print("\n" + "="*40)
            print("CONVERSOR DE MOEDAS".center(40))
            print("="*40 + "\n")

            print(f"A taxa de câmbio atual de 1 {base_currency} é {round(rate, 2)} {target_currency}\n")
            input("Pressione ENTER para continuar...")
        
        elif opcao == '4':
            #Logo
            clear_screen()
            print("\n" + "="*40)
            print("CONVERSOR DE MOEDAS".center(40))
            print("="*40 + "\n")

            crypto_currency = input("Digite a criptomoeda (utilize o nome e não a abreviação): ").lower()
            target_currency = input("Digite a moeda alvo: ").lower()

            price = cc_crypto.get_price(crypto_currency, target_currency)

            #Logo
            clear_screen()
            print("\n" + "="*40)
            print("CONVERSOR DE MOEDAS".center(40))
            print("="*40 + "\n")

            print(f"O preço atual de 1 {crypto_currency} é {price} {target_currency}\n")
            input("Pressione ENTER para continuar...")

        elif opcao == '5':
            #Logo
            clear_screen()
            print("\n" + "="*40)
            print("CONVERSOR DE MOEDAS".center(40))
            print("="*40 + "\n")

            print("Abreviações de moedas mais usadas:")
            print("USD - Dólar Americano")
            print("EUR - Euro")
            print("BRL - Real")
            print("JPY - Yen Japonês")
            print("GBP - Libra Esterlina")
            print("AUD - Dólar Australiano")
            print("CAD - Dólar Canadense")
            print("CHF - Franco Suíço")
            print("CNY - Yuan Chinês")
            print("SEK - Coroa Sueca")
            input("\nPressione ENTER para continuar...")
        
        elif opcao == '6':
            #Logo
            clear_screen()
            print("\n" + "="*40)
            print("CONVERSOR DE MOEDAS".center(40))
            print("="*40 + "\n")

            print("Obrigado por usar o conversor de moedas. Desenvolvido por: Luan\n")
            input("Pressione ENTER para sair...")
            clear_screen()
            break
        else:
            #Logo
            clear_screen()
            print("\n" + "="*40)
            print("CONVERSOR DE MOEDAS".center(40))
            print("="*40 + "\n")

            print("Opção inválida. Por favor, tente novamente.\n")
            input("Pressione ENTER para continuar...")

if __name__ == "__main__":
    main()
