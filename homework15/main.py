class Player:
    _id_counter = 1

    def __init__(self, name, position, number, age, nationality):
        self.id = Player._id_counter
        Player._id_counter += 1
        self.name = name
        self.position = position
        self.__number = number
        self.__age = age
        self.nationality = nationality
        self.matches_played = 0
        self.goals_scored = 0

    def update_stat(self, matches=None, goals=None):
        if matches is not None:
            self.matches_played = matches
        if goals is not None:
            self.goals_scored = goals

    def show_info(self):
        print(f"ID: {self.id}")
        print(f"სახელი: {self.name}")
        print(f"პოზიცია: {self.position}")
        print(f"ნომერი: {self.__number}")
        print(f"ასაკი: {self.__age}")
        print(f"ეროვნება: {self.nationality}")
        print(f"მატჩები: {self.matches_played}, გოლები: {self.goals_scored}")

    def __str__(self):
        return f"{self.name} ({self.position}, #{self.__number})"


class Coach:
    def __init__(self, name, experience_years):
        self.name = name
        self.__experience_years = experience_years

    def show_info(self):
        print(f"მწვრთნელი: {self.name}")
        print(f"გამოცდილება: {self.__experience_years} წელი")

    def __str__(self):
        return f"{self.name}, გამოცდილება: {self.__experience_years} წელი"


class Team:
    def __init__(self, name, coach):
        self.name = name
        self.coach = coach
        self.players = []

    def add_player(self, player):
        if len(self.players) >= 25:
            print("გუნდში ვერ დაემატება 25-ზე მეტი მოთამაშე.")
        else:
            self.players.append(player)
            print(f"{player.name} დაემატა გუნდში {self.name}.")

    def find_player(self, player_id):
        for player in self.players:
            if player.id == player_id:
                player.show_info()
                return
        print(f"მოთამაშე აიდით {player_id} ვერ მოიძებნა.")

    def update_player(self, player_id, key, value):
        for player in self.players:
            if player.id == player_id:
                if hasattr(player, key):
                    setattr(player, key, value)
                    print(f"{player.name}-ის {key} განახლდა: {value}")
                elif key == "matches":
                    player.update_stat(matches=value)
                elif key == "goals":
                    player.update_stat(goals=value)
                else:
                    print("არასწორი ველი.")
                return
        print(f"მოთამაშე აიდით {player_id} ვერ მოიძებნა.")

    def remove_player(self, player_id):
        for player in self.players:
            if player.id == player_id:
                self.players.remove(player)
                print(f"{player.name} წაიშალა გუნდიდან.")
                return
        print(f"მოთამაშე აიდით {player_id} ვერ მოიძებნა.")

    def show_team_info(self):
        print(f"კლუბი: {self.name}")
        print(f"მწვრთნელი: {self.coach}")
        if not self.players:
            print("მოთამაშეები: გუნდი ცარიელია.")
        else:
            print("მოთამაშეები:")
            for player in self.players:
                print(f"- {player}")

    def __str__(self):
        return f"{self.name} | {self.coach}"
coach = Coach("John Doe", 10)
team = Team("FC Example", coach)

p1 = Player("Leo Messi", "Forward", 10, 36, "Argentinian")
p2 = Player("Cristiano Ronaldo", "Forward", 7, 39, "Portuguese")

team.add_player(p1)
team.add_player(p2)

team.show_team_info()
team.find_player(1)
team.update_player(1, "goals", 10)
team.update_player(1, "matches", 5)
team.find_player(1)
team.remove_player(2)
team.show_team_info()