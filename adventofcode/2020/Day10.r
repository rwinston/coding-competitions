# Day 10 
# Part 1
p10 <- read_csv(clipboard(), column_names=c('data'))
adapters <- sort(c(p10$data, c(0, max(p10$data)+3)))
prod(table(diff(sort(data$data))))

# Part 2
prod(c(2,4,7)^(table(rle(diff(adapters))))[-1,1])

