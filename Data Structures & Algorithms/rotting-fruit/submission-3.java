class Solution {
    public int orangesRotting(int[][] grid) {
        
        int min = 0;

        List<Queue<Pair<Integer, Integer>>> rotten = new ArrayList<>();

        //List<Pair<Integer, Integer>> initRot = new ArrayList<>();
        if (grid.length == 0){
            return 0;
        }

        for (int i = 0; i < grid.length; i++){
            for (int j = 0; j < grid[0].length; j++){
                if (grid[i][j] == 2){
                    Queue<Pair<Integer, Integer>> tmp = new LinkedList<>();
                    tmp.add(new Pair(Integer.valueOf(i), Integer.valueOf(j)));
                    rotten.add(tmp);
                }
            }
        }

        System.out.println("Rotten: " + rotten.toString());

        int emptyQs = 0;

        // while all queues are not empty 
        while (emptyQs < rotten.size()){
            // iterate through queues
            for (int i = 0; i < rotten.size(); i++){
                Queue<Pair<Integer, Integer>> currq = rotten.get(i);
                // iterate through queue values
                int iterate = currq.size();
                for (int j = 0; j < iterate; j++){
                    Pair<Integer, Integer> currN = currq.poll();
                    System.out.println("Rot: " + currN.toString());
                    int y = currN.getKey().intValue();
                    int x = currN.getValue().intValue();
                    // Pair<Integer, Integer> currT = new Pair(Integer.valueOf(y+1), Integer.valueOf(x));
                    // Pair<Integer, Integer> currR = new Pair(Integer.valueOf(y), Integer.valueOf(x+1));
                    // Pair<Integer, Integer> currD = new Pair(Integer.valueOf(y-1), Integer.valueOf());
                    // Pair<Integer, Integer> currL = new Pair(Integer.valueOf(y), Integer.valueOf(y-1));

                    // if top fresh 
                    int maxY = grid.length;
                    int maxX = grid[0].length;
                    System.out.println("Max Y: " + String.valueOf(maxY));
                    System.out.println("Max X: " + String.valueOf(maxX));
                    if (y+1 < maxY && y+1 >= 0){
                        if (grid[y+1][x] == 1){
                            // make rotten, add to queue
                            grid[y+1][x] = 2;
                            Pair<Integer, Integer> currT = new Pair(Integer.valueOf(y+1), Integer.valueOf(x));
                            currq.add(currT);
                        }
                    }
                    // if bottom fresh
                    if (y-1 < maxY && y-1 >= 0){
                        if (grid[y-1][x] == 1){
                            // make rotten, add to queue
                            grid[y-1][x] = 2;
                            Pair<Integer, Integer> currT = new Pair(Integer.valueOf(y-1), Integer.valueOf(x));
                            currq.add(currT);
                        }
                    }
                    // if right fresh
                    if (x+1 < maxX && x+1 >= 0){
                        if (grid[y][x+1] == 1){
                            // make rotten, add to queue
                            grid[y][x+1] = 2;
                            Pair<Integer, Integer> currR = new Pair(Integer.valueOf(y), Integer.valueOf(x+1));
                            currq.add(currR);
                        }
                    }
                    // if left fresh
                    if (x-1 < maxX && x-1 >= 0){
                        if (grid[y][x-1] == 1){
                            // make rotten, add to queue
                            grid[y][x-1] = 2;
                            Pair<Integer, Integer> currL = new Pair(Integer.valueOf(y), Integer.valueOf(x-1));
                            currq.add(currL);
                        }
                    }

                    if (currq.isEmpty()){
                        emptyQs++;
                    }
                }
            }
            min++;
            System.out.println("min: " + String.valueOf(min));
            for (int i = 0; i < grid.length; i++){
                System.out.println("");
                for (int j = 0; j < grid[0].length; j++){
                    System.out.print(String.valueOf(grid[i][j]) + ", ");
                }
                System.out.println("");
            }
            
        }

        // return true if no more fresh fruit
        for (int i = 0; i < grid.length; i++){
            for (int j = 0; j < grid[0].length; j++){
                if (grid[i][j] == 1){
                    return -1;
                }
            }
        }

        return Math.max(min-1, 0);

    }

}
