class Team:
    def __init__(self, id, name, LeagueId):
        self.id = id
        self.name = name
        self.LeagueId = LeagueId


    def __str__(self):
        return f"{self.id}-{self.name}-{self.LeagueId}"
    
    def __eq__(self, other):
        if isinstance(other, Team):
            return self.name == other.name
        return False
    
    def get_name(self):
        return self.name
        