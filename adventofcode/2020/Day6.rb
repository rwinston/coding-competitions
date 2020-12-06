
lines = []
File.open("c:/temp/p6").each_line do |line|
   lines.push(line.chomp)
 end


# Part 1
qns = []
qn = []
total = 0

lines.each do |line|
   if line == ""
     qns.push(qn)
     qn=[]
   else
     qn.push(line)
   end
 end

qns.each do |ans|
  total += ans.join("").each_char.tally.size
 end

puts(total)

# Part 2
total = 0
qns.each do |ans|
  r = ans.length()
  h = ans.join("").each_char.tally.each_value {|v| 
  if v == r
	total+=1
  end}
end

puts(total)


