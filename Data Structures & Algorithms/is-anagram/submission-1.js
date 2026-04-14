class Solution {
    /**
     * @param {string} s
     * @param {string} t
     * @return {boolean}
     */
    isAnagram(s, t) {
        
        
        if (s.length !== t.length){ return false; }

                const sorted_s = s.split('').sort()
                const sorted_t = t.split('').sort()
                                
                    if (sorted_s.toString() === sorted_t.toString()){ return true; }

                  return false

    }
}
