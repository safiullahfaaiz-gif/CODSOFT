

import random
import time
from datetime import datetime

# Game choices dictionary
CHOICES = {
    '1': 'Rock',
    '2': 'Paper',
    '3': 'Scissors'
}

# Rules for winning
WINNING_RULES = {
    'Rock': 'Scissors',
    'Paper': 'Rock',
    'Scissors': 'Paper'
}

class RockPaperScissorsGame:
    """Advanced Rock Paper Scissors Game with statistics and difficulty levels"""
    
    def __init__(self):
        """Initialize game with player statistics"""
        self.player_score = 0
        self.computer_score = 0
        self.rounds_played = 0
        self.game_history = []
        self.difficulty = 'normal'
        self.start_time = None
        
    def display_welcome_banner(self):
        """Display beautiful welcome banner"""
        print("\n" + "="*50)
        print("WELCOME TO ROCK PAPER SCISSORS GAME".center(50))
        print("="*50)
        print("\nDeveloped for CodSoft Internship Program")
        print("Author: N.Mohammed Safiullah Faaiz")
        print("="*50 + "\n")
    
    def select_difficulty(self):
        """Let player choose game difficulty level"""
        print("SELECT DIFFICULTY LEVEL:\n")
        print("1. Easy (Computer plays randomly)")
        print("2. Normal (Computer plays smart)")
        print("3. Hard (Computer predicts your move)\n")
        
        choice = input("Enter difficulty (1/2/3): ").strip()
        
        if choice == '1':
            self.difficulty = 'easy'
            print("Difficulty set to: EASY\n")
        elif choice == '2':
            self.difficulty = 'normal'
            print("Difficulty set to: NORMAL\n")
        elif choice == '3':
            self.difficulty = 'hard'
            print("Difficulty set to: HARD\n")
        else:
            print("Invalid choice! Setting to NORMAL\n")
            self.difficulty = 'normal'
    
    def get_computer_move(self, player_move=None):
        """Get computer's move based on difficulty level"""
        random_choice = random.choice(list(CHOICES.values()))
        
        if self.difficulty == 'easy':
            return random_choice
        
        elif self.difficulty == 'normal':
            # 70% random, 30% smart
            if random.random() < 0.3 and player_move:
                return WINNING_RULES.get(player_move, random_choice)
            return random_choice
        
        elif self.difficulty == 'hard':
            # 60% smart, 40% random
            if random.random() < 0.6 and player_move:
                # Try to beat player's last move
                counter_move = WINNING_RULES.get(player_move, random_choice)
                return counter_move
            return random_choice
        
        return random_choice
    
    def get_player_move(self):
        """Get and validate player's move"""
        while True:
            try:
                print("\nYOUR TURN:")
                print("1. Rock")
                print("2. Paper")
                print("3. Scissors")
                print("4. Show Statistics")
                print("5. Quit Game\n")
                
                choice = input("Enter your choice (1/2/3/4/5): ").strip()
                
                if choice in ['1', '2', '3']:
                    return CHOICES[choice]
                elif choice == '4':
                    self.display_statistics()
                    continue
                elif choice == '5':
                    return 'quit'
                else:
                    print("Invalid input! Please enter 1, 2, 3, 4, or 5")
                    continue
            
            except Exception as e:
                print("Error: {}. Please try again.".format(e))
    
    def determine_winner(self, player_move, computer_move):
        """Determine winner of current round"""
        if player_move == computer_move:
            return 'tie'
        
        if WINNING_RULES[player_move] == computer_move:
            return 'player'
        
        return 'computer'
    
    def play_round(self):
        """Play a single round of the game"""
        player_move = self.get_player_move()
        
        if player_move == 'quit':
            return 'quit'
        
        # Add small delay for better UX
        time.sleep(0.5)
        computer_move = self.get_computer_move(player_move)
        
        # Display moves
        print("\n" + "-"*50)
        print("Your Choice:      {}".format(player_move))
        print("Computer Choice:  {}".format(computer_move))
        print("-"*50)
        
        # Determine and display result
        result = self.determine_winner(player_move, computer_move)
        
        if result == 'tie':
            print("RESULT: TIE! Both played the same move!\n")
        elif result == 'player':
            print("RESULT: YOU WIN THIS ROUND!\n")
            self.player_score += 1
        else:
            print("RESULT: COMPUTER WINS THIS ROUND!\n")
            self.computer_score += 1
        
        # Record in history
        self.rounds_played += 1
        self.game_history.append({
            'round': self.rounds_played,
            'player': player_move,
            'computer': computer_move,
            'result': result,
            'timestamp': datetime.now()
        })
        
        # Display current score
        self.display_current_score()
        return 'continue'
    
    def display_current_score(self):
        """Display current score after each round"""
        ties = self.rounds_played - self.player_score - self.computer_score
        print("CURRENT SCORE:")
        print("   You: {} | Computer: {} | Ties: {}".format(
            self.player_score, self.computer_score, ties))
        print()
    
    def display_statistics(self):
        """Display detailed game statistics"""
        print("\n" + "="*50)
        print("GAME STATISTICS".center(50))
        print("="*50)
        
        if self.rounds_played == 0:
            print("\nNo rounds played yet!")
            print("="*50 + "\n")
            return
        
        ties = self.rounds_played - self.player_score - self.computer_score
        win_percentage = (self.player_score / self.rounds_played) * 100
        
        print("\nTotal Rounds:        {}".format(self.rounds_played))
        print("Your Wins:           {}".format(self.player_score))
        print("Computer Wins:       {}".format(self.computer_score))
        print("Ties:                {}".format(ties))
        print("Your Win Rate:       {:.1f}%".format(win_percentage))
        print("Difficulty Level:    {}".format(self.difficulty.upper()))
        
        print("\nLAST 5 MOVES:")
        if len(self.game_history) > 0:
            for game in self.game_history[-5:]:
                result_text = "WIN" if game['result'] == 'player' else "LOSS" if game['result'] == 'computer' else "TIE"
                print("   Round {}: You({}) vs Computer({}) {}".format(
                    game['round'], game['player'], game['computer'], result_text))
        
        print("\n" + "="*50 + "\n")
    
    def display_final_results(self):
        """Display final game results"""
        print("\n" + "="*50)
        print("FINAL RESULTS".center(50))
        print("="*50)
        
        ties = self.rounds_played - self.player_score - self.computer_score
        
        print("\nTotal Rounds Played:     {}".format(self.rounds_played))
        print("Your Wins:               {}".format(self.player_score))
        print("Computer Wins:           {}".format(self.computer_score))
        print("Ties:                    {}".format(ties))
        print("Difficulty Level:        {}".format(self.difficulty.upper()))
        
        print("\n" + "-"*50)
        
        # Determine overall winner
        if self.player_score > self.computer_score:
            print("CONGRATULATIONS! YOU WON THE GAME!".center(50))
        elif self.computer_score > self.player_score:
            print("COMPUTER WON THE GAME!".center(50))
        else:
            print("THE GAME IS TIED!".center(50))
        
        print("-"*50 + "\n")
        
        # Performance analysis
        if self.rounds_played > 0:
            win_percentage = (self.player_score / self.rounds_played) * 100
            print("Your Win Percentage: {:.1f}%".format(win_percentage))
            
            if win_percentage > 60:
                print("Outstanding performance!")
            elif win_percentage > 50:
                print("Good job! You're on the winning side!")
            elif win_percentage == 50:
                print("Evenly matched!")
            else:
                print("Keep practicing, you'll get better!")
        
        print("\n" + "="*50 + "\n")
    
    def play_game(self):
        """Main game loop"""
        self.display_welcome_banner()
        self.select_difficulty()
        self.start_time = time.time()
        
        print("Let's start playing! Type 'quit' during a round to end the game.\n")
        
        while True:
            result = self.play_round()
            
            if result == 'quit':
                break
            
            # Ask if player wants to continue
            continue_choice = input("Play another round? (yes/no): ").strip().lower()
            if continue_choice not in ['yes', 'y']:
                break
        
        # Display final results
        self.display_final_results()


# ==========================================
# MAIN PROGRAM EXECUTION
# ==========================================

if __name__ == "__main__":
    try:
        # Create game instance and start playing
        game = RockPaperScissorsGame()
        game.play_game()
        
        print("Thanks for playing Rock Paper Scissors!")
        print("Made for CodSoft Internship Program\n")
    
    except KeyboardInterrupt:
        print("\n\nGame interrupted by user.")
        print("Goodbye!\n")
    
    except Exception as e:
        print("\nAn error occurred: {}".format(e))
        print("Please try running the program again.\n")
