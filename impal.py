def process_user_input():
    user_input = input("1.Transfer pulsa\n2.Minta pusa\n3.Auto TP\n4.Delete auto TP\n5.List auto TP\n6.Cek kupon Undian TP\nmasukkan pilahan anda :")
    # we only process the first input for the input option, because we are asked to choose only one to do until the final execution
    if user_input == '1':
        transfer_credit()
    else:
        print('Pilihan tidak valid. Silakan coba lagi.')
    
    return True 

 # Continue the loop

def transfer_credit():
    recipient = input("Masukkan nomor tujuan: ")
    
    try:
        amount = int(input("Masukkan jumlah pulsa: "))
    except ValueError:
        print('Jumlah pulsa tidak valid. Harap masukkan angka.')
        return
    
    user_balance = 100000  # Example balance in rupiah

    if is_valid_phone_number(recipient):
        if amount > 0:
            if amount <= user_balance:
                user_balance -= amount
                print(f'Transfer berhasil! Anda telah mengirim pulsa senilai Rp{amount} ke nomor {recipient}.')
                print(f'Sisa saldo Anda adalah Rp{user_balance}.')
            else:
                print('Saldo tidak mencukupi.')
        else:
            print('Jumlah pulsa tidak valid.')
    else:
        print('Nomor tujuan tidak valid.')

def is_valid_phone_number(phone_number):
    # Check if the phone number is numeric and has a length of 10 or 12
    return (phone_number.isdigit() and
            (len(phone_number) == 11 or 12 and phone_number.startswith('08') or
             len(phone_number) == 12 or 13 and phone_number.startswith('62')))

if __name__ == "__main__":
    continue_program = True
    while continue_program:
        continue_program = process_user_input()
