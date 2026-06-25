# Voting Logic System

class VotingSystem:
    def __init__(self):
        self.voters = {}
        self.candidates = {}
        self.votes = {}
    
    def register_candidate(self, candidate_name):
        """Register a candidate for voting"""
        if candidate_name not in self.candidates:
            self.candidates[candidate_name] = True
            self.votes[candidate_name] = 0
            print(f"✓ {candidate_name} registered as a candidate")
        else:
            print(f"✗ {candidate_name} is already registered")
    
    def check_voter_eligibility(self, voter_name, age):
        """Check if voter is eligible (age >= 18)"""
        if age >= 18:
            print(f"✓ {voter_name} (Age: {age}) is eligible to vote")
            return True
        else:
            print(f"✗ {voter_name} (Age: {age}) is NOT eligible to vote. Minimum age required: 18")
            return False
    
    def register_voter(self, voter_name, age):
        """Register a voter if eligible"""
        if self.check_voter_eligibility(voter_name, age):
            if voter_name not in self.voters:
                self.voters[voter_name] = {"age": age, "has_voted": False}
                print(f"✓ {voter_name} registered as a voter\n")
                return True
        print()
        return False
    
    def cast_vote(self, voter_name, candidate_name):
        """Cast a vote for a candidate"""
        if voter_name not in self.voters:
            print(f"✗ {voter_name} is not registered as a voter\n")
            return False
        
        if self.voters[voter_name]["has_voted"]:
            print(f"✗ {voter_name} has already voted\n")
            return False
        
        if candidate_name not in self.candidates:
            print(f"✗ {candidate_name} is not a registered candidate\n")
            return False
        
        self.voters[voter_name]["has_voted"] = True
        self.votes[candidate_name] += 1
        print(f"✓ {voter_name} voted for {candidate_name}\n")
        return True
    
    def get_results(self):
        """Display voting results"""
        print("\n" + "="*40)
        print("VOTING RESULTS")
        print("="*40)
        
        if not self.votes:
            print("No votes cast yet!")
            return
        
        sorted_votes = sorted(self.votes.items(), key=lambda x: x[1], reverse=True)
        
        for candidate, vote_count in sorted_votes:
            percentage = (vote_count / sum(self.votes.values())) * 100 if sum(self.votes.values()) > 0 else 0
            print(f"{candidate}: {vote_count} votes ({percentage:.1f}%)")
        
        winner = sorted_votes[0][0]
        print("\n" + "-"*40)
        print(f"🏆 WINNER: {winner} with {sorted_votes[0][1]} votes")
        print("="*40 + "\n")


# Demo: Using the Voting System
if __name__ == "__main__":
    # Create voting system
    voting = VotingSystem()
    
    # Register candidates
    voting.register_candidate("Alice")
    voting.register_candidate("Bob")
    voting.register_candidate("Charlie")
    print()
    
    # Register voters
    voting.register_voter("Voter1", 25)
    voting.register_voter("Voter2", 17)  # Too young
    voting.register_voter("Voter3", 30)
    voting.register_voter("Voter4", 22)
    
    # Cast votes
    voting.cast_vote("Voter1", "Alice")
    voting.cast_vote("Voter3", "Bob")
    voting.cast_vote("Voter4", "Alice")
    voting.cast_vote("Voter2", "Charlie")  # Will fail - not registered
    
    # Display results
    voting.get_results()
