import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.List;
import java.util.stream.Collectors;
import java.util.stream.IntStream;

public class Day9 {

    public static long part1(long[] in){
        final int PREAMBLE_LEN = 25;
        for (int i = PREAMBLE_LEN; i < in.length; ++i) {
            boolean valid = false;
            long curr = in[i];
            for (int j=i-PREAMBLE_LEN;j<i-1;++j) {
                for (int k=j+1;k<i;++k) {
                    if (curr == in[k]+in[j]) {
                        valid = true;
                    }
                }
            }
            if (!valid) return curr;
        }
        return 0;
    }

    public static long part2(long[] in, long n) {
        for (int i=0;i<in.length-1;++i) {
            long sum = in[i];
            for (int j=i+1;j<in.length;++j) {
                sum += in[j];
                if (sum==n) {
                    List<Long> range = IntStream.range(i, j + 1).mapToObj(k -> in[k]).sorted().collect(Collectors.toList());
                    return range.get(0) + range.get(range.size()-1);
                }
            }
        }
        return 0;
    }
 
    public static void main(String[] args) throws IOException {
        long[] input = Files.lines(Paths.get("c:/temp/p9")).mapToLong(x->Long.parseLong(x)).toArray();
        long n = part1(input);
        // Part 1
        System.out.println(n);
        // Part 2
        System.out.println(part2(input, n));
        
    }

}