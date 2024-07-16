impl Solution {
    pub fn length_of_last_word(s: String) -> i32 {
        let mut length = 0;
        for i in s.chars().rev() {
            if i == ' ' && length < 1{
                continue
            }
            else if i == ' ' && length >= 1{
                return length;
            }
            else if i != ' '{
                length+=1;
            }
        }
        length
    }
}

//Kinda correct. Needed lots of help from internet and a little help from chatgpt for syntax and rev function