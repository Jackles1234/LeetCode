impl Solution {
    pub fn lucky_numbers(matrix: Vec<Vec<i32>>) -> Vec<i32> {
        let mut max = i32::MIN;
        let mut max_row = 0;
        let mut min = i32::MAX;
        let mut min_col = 0;

        // Find the maximum value in the matrix and its row
        for i in 0..matrix.len() {
            for j in 0..matrix[i].len() {
                if matrix[i][j] > max {
                    max = matrix[i][j];
                    max_row = i;
                }
            }
        }

        // Find the minimum value in the row containing the maximum value
        for j in 0..matrix[max_row].len() {
            if matrix[max_row][j] < min {
                min = matrix[max_row][j];
                min_col = j;
            }
        }

        return vec![matrix[max_row][min_col]]
    }
}

// Incorrect
//Had to use Chat and look at answer and still got it incorrect. :(