"""
1. Database Connection (DONE)
1.1 Connect to your existing database.
1.2 Fetch airport data.
1.3 (Optional) Update player location or score in the database.

2. Game Initialization (done)
2.1 Initialize player position (starting airport).
2.2 Initialize any resources (e.g., fuel, points).

3. Main Game Loop
3.1 Show available airports to the player.
3.2 Get player input (keyboard).
3.3 Validate input (check if selected airport exists and is reachable).
3.4 Move player to the selected airport.
3.5 Update game state (current airport, resources, score).

4. Functional Actions
4.1 select_airport(): choose the next airport.
4.2 display_airport_info(): show airport details.
4.3 update_player_state(): save changes in memory and database.

5. Non-functional Considerations
5.1 Ensure fast database queries.
5.2 Provide immediate feedback after each action.
5.3 Handle errors (invalid input, database errors).

6. Game End Conditions
6.1 Check if objective is reached (e.g., visited all airports or reached goal).
6.2 Display final score or message.
"""



# python main.py
  