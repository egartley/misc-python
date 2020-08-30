# Codeword Solver

Solver for the codeword puzzles in the [_World's Biggest Crossword_](https://apps.apple.com/us/app/crossword-worlds-biggest/id859866568) app.

These puzzles are similar to normal crosswords, however instead of being given clues, you are given only two or three letters to start with. The goal is the fill in the rest of the board, making sure real words are spelled in every direction. Each spot on the board has a number between 1 and 26 which corresponds to a letter, meaning each letter in the alphabet is included at least once somewhere on the board.

Given a board file (included are `board1.txt` and `board2.txt`) with already known letters and their corresponding number on the board, the remaining letters are inserted. After being filled in, the script checks to see if there is an actual word (present in `words.txt`, almost every word in the English language) in the board. If there are the set number of words or more present, the generated board is then printed out.   
   
Here is an example solution:   
`■ c ■ z ■ p ■ p ■ g ■`   
`w h o o s h ■ a j a r`   
`■ u ■ o ■ l ■ r ■ v ■`   
`i n n ■ c o n q u e r`   
`■ k ■ b ■ x ■ u ■ ■ ■`   
`m y r r h ■ b e s e t`   
`■ ■ ■ i ■ p ■ t ■ n ■`   
`a r s e n a l ■ o f f`   
`■ o ■ f ■ r ■ a ■ o ■`   
`l u l l ■ t i d i l y`   
`■ x ■ y ■ y ■ o ■ d ■`   

## Inefficiencies and Limitations

While it's obviously not the best way to look for a solution by going through every possible combination of the unknown letters, it was the simplest to implement. Due to this approach, the time it takes to look at each solution exponentially increases with every additional unknown letter. By default, the app only gives two or three known letters, which essentially requires at least a few more letters to be either guessed or inferred based on their position and frequency in the board. For example, a number that appears often is likely a vowel, while a number that only appears once is likely an uncommon letter such as Q or Z. The more known letters that are provided, the quicker a viable solution will be found.

A much better approach would be to "intelligently" guess where letters are placed. For example, S is often followed by H, while S is usually not followed by V. LY and ING are common suffixes, while AGZ and LW are not. This would require a lot of predefined commonalities and exclusions, and would take awhile to get working.
   
Another flaw is that the script only looks for words horizontally, not both directions. Again, it was easier to only check for words in this way, however it may change in the future such that both rows and columns are checked.

## Board File Format

The first line is all of the known letters. First, the letter itself, a comma, and finally the number which represents that letter in the board.   
   
Example: `h,12`, or for more than one `k,13,w,22`   
   
The remaining lines represent that board itself, with each line being a single row. Each spot has a number representing a specific letter. Single digit numbers have a zero in front, while blank spots are designated with two zeros.   
   
Example:   
■ 6 ■ 17 ■ 7 ■ 3 ■ 8 ■ would be `0006001700070003000800`
