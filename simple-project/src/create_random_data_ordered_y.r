# Stolen from https://stats.stackexchange.com/a/321792.

{% include 'save_data.r' %}

set.seed(123)

n     <- 100
x1    <- rnorm(n, 175, 7)
x2    <- rnorm(n,  30, 8)
y_continuous <- 0.5 * x1 - 0.3 * x2 + 10 + rnorm(n, 0, 6)
y_ordinal  <- cut(y_continuous, breaks=quantile(y_continuous), include.lowest=TRUE,
             labels=c("--", "-", "+", "++"), ordered=TRUE)

df <- data.frame(x1 = x1, x2 = x2, y = factor(y_ordinal))

save_data(df, "{{ produces }}")
