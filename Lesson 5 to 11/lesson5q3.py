#qns3

def main():
    date = input('Enter date,dd/mm/yyyy:')
    months = "JanFebMarAprMayJunJulAugSepOctNovDec"
    dd = date[0:2]
    mm = int(date[3:5])
    yyyy = date[6:]

    mm_abb = months[mm*3-3:mm*3]
    print(dd,mm_abb,yyyy)

main()
            
