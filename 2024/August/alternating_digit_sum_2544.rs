impl Solution {
    pub fn alternate_digit_sum(n: i32) -> i32 {
        let mut count = 0;
        let mut total = 0;
        for i in n.to_string().chars() {
            let mut num = i.to_digit(10).unwrap();
            if count % 2 == 0 {
                total+= num;
                count +=1;
            }
            else{
                total -= num;
                count +=1;
            }

        }
        return total as i32;
    }
}

/// CORRECT!