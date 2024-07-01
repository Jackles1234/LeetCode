class Solution(object):
    def findRepeatedDnaSequences(self, s):
        string_map = {}
        output = []
        i = 0
        while i+9 < len(s):
            try:
                string_map[s[i:i+10]] +=1
                if string_map[s[i:i+10]] > 1:
                    i+=1
                else:
                    output.append(s[i:i+10])
                    i+=1
            except:
                string_map[s[i:i+10]] = 0
                i+=1

        return output
    

### CORRECT ###

#Jake's smarter way of doing it:

# class Solution {
# public:
#     vector<string> findRepeatedDnaSequences(string s) {
#         std::vector<std::string> multipleSequences;
#         std::unordered_map<std::string, bool> allSequences;

#         for (auto i = 0; i + 10 <= s.length(); ++i) {
#             std::string currentSequence = s.substr(i, 10);
#             if (!allSequences.contains(currentSequence)) {
#                 allSequences[currentSequence] = false;
#             } else {
#                 if (allSequences[currentSequence] == false) {
#                     allSequences[currentSequence] = true;
#                     multipleSequences.push_back(currentSequence);
#                 }
#             }
#         }
#         return multipleSequences;
#     }
# };