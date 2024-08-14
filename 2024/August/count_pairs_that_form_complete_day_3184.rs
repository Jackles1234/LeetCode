impl Solution {
    pub fn count_complete_day_pairs(hours: Vec<i32>) -> i32 {
        let mut count: i32 = 0;
        for i in 0..hours.len(){
            for j in (i+1)..hours.len(){
                if (hours[i] + hours[j]) % 24 == 0{
                    count+=1;
                }
                    
            }
        }
        return count
    }
}