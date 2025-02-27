# Football Team Managmenet System

# შექმენით კლასი FootballTeam შემდეგი ატრიბუტებით:
# team_name (string) - კლუბის სახელი
# coach (string) - მწვრთნელი
# players - მოთამაშეების სია(შექმნისას ცარიელი უნდა იყოს)

# კლასს უნდა გააჩნდეს შემდეგი მეთოდები:
# 1. მოთამაშის დამატება - მოთამაშის სახელი, პოზიცია, სათამაშო ნომერი, 
#    ასაკი და ეროვნება(დიქტის სახით უნდა დაემატოს მოთამაშეების სიაში)

# 2. მოთამაშის წაშლა - მოთამაშე უნდა წაიშალოს სიიდან სათამაშო ნომრის მიხედვით

# 3. მოთამაშის ინფორმაციის განახლება - მოთამაშე უნდა მონახოთ სათამაშო ნომრის მიხედვით
#    და უნდა დაუსეტოთ ისეთი ინფორმაცია, რომელსაც გადასცემთ ამ მეთოდს, მაგ: "goal": 1 
#    ანუ key და value უნდა იყოს გადაცემული ამავე მეთოდის გამოძახებისას!

# 4. კლუბის ინფორმაციის ჩვენება - გამოიტანეთ კლუბის სახელი, მწვრთნელის სახელი და მოთამაშეების სია

# 5. მოთამაშის ინფორმაციის ჩვენება - უნდა გამოიტანოთ ინფორმაცია მოთამაშის ნომრის მიხედვით

class FootballTeam:
    def __init__(self,team_name,coach):
        self.team_name = team_name
        self.coach =coach
        self.players =[]
    def add_player(self,name,position,number,age, nationality):
        player = {
            "name" : name,
            "position" : position,
            "number" : number,
            "age" : age,
            "nationality" : nationality,
        }
        self.players.append(player)
        print(f"მოთამაშე {name} წარმატებით დაემატა გუნდში {self.team_name}.")
    def remove_player(self,number):
         for player in self.players:
             if player["number"] == number:
                self.players.remove(player)
                print(f"მოთამაშე {number} წაიშალა გუნდიდან.")
    def show_players(self):
        if not self.players:
            print("გუნდი ცარიელია.")
        else:
            print(f"{self.team_name} - მოთამაშეები:")
            for player in self.players:
                print(f"{player['name']} - {player['position']} ({player['number']})")

    def update_player(self, number, key, value):
        for player in self.players:
            if player["number"] == number:
                player[key] = value
                print(f"მოთამაშე {player['name']}-ის '{key}' განახლდა: {value}")
                return
        print(f"მოთამაშე ნომრით {number} ვერ მოიძებნა გუნდში.")

        def show_team_info(self):
            print(f"კლუბი: {self.team_name}")
            print(f"მწვრთნელი: {self.coach}")
        if not self.players:
            print("მოთამაშეები: გუნდი ცარიელია.")
        else:
            print("მოთამაშეები:")
            for player in self.players:
                print(f"- {player['name']} ({player['position']}, ნომერი {player['number']})")

                team = FootballTeam("FC Example", "John Doe")

                team.add_player("Leo Messi", "Forward", 10, 36, "Argentinian")
                team.add_player("Cristiano Ronaldo", "Forward", 7, 39, "Portuguese")
                team.show_team_info()  # კლუბის ინფორმაციის გამოყვანა
                team.update_player(10, "goals", 5)  # განახლება
                team.show_team_info()  
        def show_player_info(self, number):
        
         for player in self.players:
            if player["number"] == number:
                print(f"მოთამაშის ინფორმაცია (ნომერი {number}):")
                print(f"სახელი: {player['name']}")
                print(f"პოზიცია: {player['position']}")
                print(f"ასაკი: {player['age']}")
                print(f"ეროვნება: {player['nationality']}")
                return
        print(f"მოთამაშე ნომრით {number} ვერ მოიძებნა გუნდში.")

        team = FootballTeam("FC Example", "John Doe")
        team.add_player("Leo Messi", "Forward", 10, 36, "Argentinian")
        team.add_player("Cristiano Ronaldo", "Forward", 7, 39, "Portuguese")
        team.show_team_info()  
        team.update_player(10, "goals", 5)  
        team.show_team_info()  
        team.show_player_info(10)  
        team.show_player_info(7)    
        team.show_player_info(9)


