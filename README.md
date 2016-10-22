# mato
Matopeli GitHubiin
1. Basic logic
    - 3 types of space: available, snake, apple
    - Coordinate list for each
    - Drawing room by coordinate lists
2. Movement
    - Direction NWSE
    - Get next space = requested_space
    - If available: move snake by adding requested_space to snake and putting last item in snake list to be available again
3. Eating apple
    - Move snake, revert removing tail
    - Game loop checks apple state, spawns new if no apple but available space
4. Scoring, Winning conditions, Losing Conditions, Statistics, Decorations