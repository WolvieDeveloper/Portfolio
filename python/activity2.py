def showlugar():
    print("1. Roosevelt   | 2. Balintawak        | 3. Yamaha Mou      | 4. 5th Avenue | 5. R. Rapa")
    print("6. Abad Santos | 7. Bluementrtitt     | 8. Tayuman         | 9. Bambang    | 10. Doroteo Jose")
    print("11. Carriedo   | 12. Central Terminal | 13. United Nations | 14. Pedro Gil | 15. Quirino")
    print("16. Vito Cruz  | 17. Gil Puyat        | 18. Libertad       | 19. EDSA      | 20. Baclaran")


while True:
    print("FARE PRICING SYSTEM")
    showlugar()
    opt = input("Enter the number corresponding to your current station: ")
    opt = int(opt)
    

    places = {
        "Roosevelt" :  0,
        "Balintawak" : 1573,
        "Monumento": 1816,
        "5th Avenue": 892,
        
            }