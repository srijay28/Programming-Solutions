class Solution {
    public int canCompleteCircuit(int[] gas, int[] cost) {
        int gs = 0, cs = 0;
        for(int i = 0;i<gas.length;i++){
            gs = gs + gas[i];
            cs = cs + cost[i];
        }
        if (gs < cs){
            return -1;
        }
        int start = 0, curr = 0;
        for(int j = 0; j<gas.length; j++){
            curr += gas[j] - cost[j];
            if (curr < 0){
                curr = 0;
                start = j + 1;
            }
        }
        return start;
    }
}