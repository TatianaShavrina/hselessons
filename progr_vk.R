library(tidyverse)

posts <- read.csv(file="C:\\Users\\USER\\Documents\\hse\\r\\bc_wall_posts.csv", header=TRUE, sep="\t", encoding = "UTF-8")
posts

posts %>%
  ggplot(aes(text.length))+
  geom_histogram(fill="lightblue",bins = nclass.FD(posts$text.length)) +
  labs(title = "Distribution of post length") +
  xlab("text length") +
  xlim(0,1500)

posts %>%
  ggplot(aes(likes)) +
  geom_histogram(bins = nclass.FD(posts$likes), fill='blue') +
  labs(title = "Distribution of likes") +
  xlab("post likes") +
  xlim(0,20000)

posts %>%
  ggplot(aes(text.length, likes)) +
  geom_point(fill='blue') +
  labs(title = "Correlation of text length and likes") +
  xlab("text length") +
  ylab("likes")

posts %>%
  ggplot(aes(comments, likes)) +
  geom_point(aes(colour='pink')) +
  labs(title = "Correlation of comments and likes") +
  xlab("comments") +
  ylab("likes")

posts %>%
  ggplot(aes(age, text.length)) +
  geom_point(colour = "red") +
  facet_wrap(~age)  +
  labs(title = "Correlation of author age and mean post length ") +
  xlab("author age") +
  ylab("text.length")

posts %>%
  ggplot(aes(age, text.length)) +
  geom_point(colour = "red", aes(size = likes)) +
  scale_colour_gradient(low = "red") +
  labs(title = "Correlation of author age and post length (with likes)") +
  xlab("author age") +
  ylab("text.length")

comms <- read.csv(file="C:\\Users\\USER\\Documents\\hse\\progr\\vk\\bc_wall_comments.csv", header=TRUE, sep="\t", encoding = "UTF-8")
comms

comms %>%
  ggplot(aes(text.length))+
  geom_histogram(fill="lightblue",bins = nclass.FD(comms$text.length)) +
  labs(title = "Distribution of comment length") +
  xlab("text length") +
  xlim(0,200)


comms %>%
  ggplot(aes(age, text.length)) +
  geom_point(colour = "red", size = 1) +
  scale_colour_gradient(low = "red") +
  labs(title = "Correlation of author age and comment length") +
  xlab("author age") +
  ylab("text.length")

