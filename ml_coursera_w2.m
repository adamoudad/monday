% Coursera - Machine Learning
% Linear Regression With Multiple Variables (Quizz notes)

X = [89 7921 ;72 5184 ;94 8836 ;69 4761];
y = [96; 74 ; 87 ; 78];
i = 2 % feature #
j = 2 % sample #
xi_max = max(X(:,i));
xi_min = min(X(:,i));
range = xi_max - xi_min;
disp((X(2,i) - mean(X(:,i))) / range);

