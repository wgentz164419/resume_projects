/*
Name: Walker Gentz 
Explaination: Code works through the Knight's Tour problem, taking a user-inputed starting position
and making valid moves until all 64 spaces are visited or no valid moves are available. Valid moves are
defined as moving to a space that has not been visited yet and within the 8x8 chest board. The output for
the code is a chest board showing how the knight moved around the board with each location marked
 */

import java.util.Scanner;
public class KnightsTour {
    final static int[][] board = new int[8][8];
    final static int[] horizontal = { 2, 1, -1, -2, -2, -1, 1, 2 };
    final static int[] vertical = { -1, -2, -2, -1, 1, 2, 2, 1 };

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter starting row (0-7): ");
        int currentRow = sc.nextInt();
        System.out.print("Enter starting column (0-7): ");
        int currentColumn = sc.nextInt();
        sc.close();

        // Initialize board to 0
        for (int i = 0; i < 8; i++) {
            for (int j = 0; j < 8; j++) {
                board[i][j] = 0;
            }
        }

        // Initialize starting point and number of moves to 1 
        board[currentRow][currentColumn] = 1;
        int numMoves = 1; 

        while (numMoves <= 64) {
            int nextColumn = -1;
            int nextRow = -1;

            for (int i = 0; i < 8; i++) {
                int checkColumn = currentColumn + horizontal[i];
                int checkRow = currentRow + vertical[i];

                if (validMove(checkColumn, checkRow) && board[checkColumn][checkRow] == 0) {
                    nextColumn = checkColumn;
                    nextRow = checkRow;
                    break;
                }
            }

            if (nextColumn == -1 || nextRow == -1) {
                break;
            }

            board[nextColumn][nextRow] = ++numMoves;
            currentColumn = nextColumn;
            currentRow = nextRow;
        }

        printBoard();
        System.out.println("Number of squares visited: " + numMoves);
    }

    private static boolean validMove(int column, int row) {
        return (column >= 0 && column < 8 && row >= 0 && row < 8);
    }

    private static void printBoard() {
        for (int i = 0; i < 8; i++) {
            for (int j = 0; j < 8; j++) {
                System.out.print(board[i][j] + "\t");
            }
            System.out.println();
        }
    }
}
